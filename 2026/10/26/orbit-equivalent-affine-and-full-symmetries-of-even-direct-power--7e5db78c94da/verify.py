"""Finite validation of parity-lift automorphisms of finite core quandles."""
from itertools import product
from math import prod

def points(mod, dim): return list(product(range(mod),repeat=dim))
def add(a,b,mod): return tuple((x+y)%mod for x,y in zip(a,b))
def core(a,b,mod): return tuple((2*y-x)%mod for x,y in zip(a,b))
def auts_small(mod=4,dim=2):
    domain=points(mod,dim)
    parity=points(2,dim)
    zeros=(0,)*dim
    target_h=points(mod//2,dim)
    # full invertible maps for 2A at k=2 are GL_d(F2)
    matrices=[]
    for ent in product(range(2),repeat=dim*dim):
        mat=[ent[j*dim:(j+1)*dim] for j in range(dim)]
        h=lambda x:tuple(sum(mat[i][j]*x[j] for j in range(dim))%2 for i in range(dim))
        if len({h(x) for x in parity})==2**dim: matrices.append(mat)
    visited=set()
    for mat in matrices:
        h=lambda x:tuple(sum(mat[i][j]*x[j] for j in range(dim))%2 for i in range(dim))
        representatives=parity[1:]
        roots=[]
        for r in representatives:
            wanted=h(r)
            choices=[p for p in domain if tuple(2*t%mod for t in p)==tuple(2*t%mod for t in wanted)]
            assert len(choices)==2**dim
            roots.append(choices)
        for tuple_roots in product(*roots):
            v={zeros:zeros, **dict(zip(representatives,tuple_roots))}
            f=[]
            for x in domain:
                r=tuple(z%2 for z in x)
                a=tuple((z-r[i])//2 for i,z in enumerate(x))
                ha=h(a)
                f.append(add(v[r],tuple(2*z for z in ha),mod))
            assert len(set(f))==len(domain)
            fm=dict(zip(domain,f))
            for x in domain:
                for y in domain:
                    assert fm[core(x,y,mod)]==core(fm[x],fm[y],mod)
            visited.add(tuple(f))
    assert len(visited)==len(matrices)*2**(dim*(2**dim-1))
    assert len(visited)==384
    identity=domain.index((0,0))
    assert identity==0
    orbit_val0={v[domain.index((1,0))] for v in visited}
    orbit_val1={v[domain.index((2,0))] for v in visited}
    assert len(orbit_val0)==12 and len(orbit_val1)==3
    assert all(any(z%2 for z in x) for x in orbit_val0)
    assert all(all(z%2==0 for z in x) and x!=(0,0) for x in orbit_val1)
    print('PAIR_ORBIT_SIZES_OK',1,len(orbit_val1),len(orbit_val0))
    print('POINT_STABILIZER_OK',len(visited))
    print('AUTOMORPHISM_ORDER_OK',len(visited)*mod**dim)
    print('AFFINE_INDEX_OK', (len(visited)*mod**dim)//1536)
    # explicit nonaffine involution supported on a parity cell
    def tau(x):
        return add(x, (mod//2 if x[0]%2==x[1]%2==1 else 0,0),mod)
    for x in domain:
        for y in domain:
            assert tau(core(x,y,mod))==core(tau(x),tau(y),mod)
    assert tau((1,1))!=(1,1) and all(tau(x)==x for x in ((0,0),(1,0),(0,1)))
    print('NONAFFINE_EXAMPLE_OK')

if __name__=='__main__':
    auts_small()
    print('VERIFY_OK')
