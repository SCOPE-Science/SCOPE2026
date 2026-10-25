#!/usr/bin/env python3
"""Independent characteristic-two extension-field checks (GF(4)), no dependencies."""
from itertools import product
from collections import Counter
Q = tuple(range(4))

def mul_s(a,b):
    c=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1): c^=(1<<(i+j))
    if c&8: raise ValueError('not degree four')
    if c&4:c^=7 # x^2 = x+1, hence xor x^2+x+1
    return c

def scalar_inv(a):
    assert a
    return next(b for b in (1,2,3) if mul_s(a,b)==1)

def vadd(a,b): return tuple(x^y for x,y in zip(a,b))
def scmul(c,a): return tuple(mul_s(c,x) for x in a)
def dot(a,b):
    z=0
    for x,y in zip(a,b):z^=mul_s(x,y)
    return z

def vmul(a,b):
    return (mul_s(a[0],b[0]),
            mul_s(a[0],b[1])^mul_s(a[1],b[0]),
            mul_s(a[0],b[2])^mul_s(a[2],b[0]),
            mul_s(a[0],b[3])^mul_s(a[1],b[2])^mul_s(a[2],b[1])^mul_s(a[3],b[0]))
BASIS=tuple(tuple(int(i==j) for i in range(4)) for j in range(4))

def valid(v,f):
    v2=vmul(v,v)
    for i,a in enumerate(BASIS):
        for j,b in enumerate(BASIS):
            lhs=scmul(mul_s(f[i],f[j]),v2)
            rhs=scmul(mul_s(f[i],dot(f,vmul(v,b)))^mul_s(f[j],dot(f,vmul(a,v))),v)
            if lhs!=rhs:return False
    return True

def norm_lines():
    for v in product(Q,repeat=4):
        if any(v):
            a=next(x for x in v if x)
            if a==1:yield v

def classification(v,f):
    assert v[0]==0
    return ('socle' if v[1]==v[2]==0 else 'nonsocle',
            'one' if f[0] else 'no_one',
            'rad' if f[1] or f[2] or f[3] else 'no_rad')

def group():
    for a,b,c,d,u,v in product(Q,repeat=6):
        det=mul_s(a,d)^mul_s(b,c)
        if not det:continue
        g=(BASIS[0],(0,a,c,u),(0,b,d,v),(0,0,0,det))
        yield g

def apply_g(g,v):
    z=(0,0,0,0)
    for a,c in zip(v,g):z=vadd(z,scmul(a,c))
    return z

def inverse_g(g):
    # finite permutation inverse as 4x4 GF4 matrix elimination
    rows=[[g[j][i] for j in range(4)]+[int(i==j) for j in range(4)] for i in range(4)]
    for i in range(4):
        j=next(j for j in range(i,4) if rows[j][i])
        rows[i],rows[j]=rows[j],rows[i]
        rows[i]=[mul_s(scalar_inv(rows[i][i]),x) for x in rows[i]]
        for j in range(4):
            if j!=i:
                r=rows[j][i]
                rows[j]=[x^mul_s(r,y) for x,y in zip(rows[j],rows[i])]
    return tuple(tuple(rows[j][i+4] for j in range(4)) for i in range(4))

def transform(g,gin,v,f):
    w=apply_g(g,v)
    nf=tuple(dot(f,apply_g(gin,e)) for e in BASIS)
    return tuple(scmul(k,w) for k in nf)

def matrix(v,f): return tuple(scmul(k,v) for k in f)

def main():
    solutions={}
    for v in norm_lines():
        for f in product(Q,repeat=4):
            if any(f) and valid(v,f):
                key=classification(v,f)
                solutions.setdefault(key,set()).add(matrix(v,f))
    counts={k:len(v) for k,v in solutions.items()}
    assert sum(counts.values())==363,counts
    expected={('socle','one','no_rad'):3,('socle','no_one','rad'):15,('socle','one','rad'):45,
              ('nonsocle','one','no_rad'):60,('nonsocle','no_one','rad'):60,
              ('nonsocle','one','rad'):180}
    assert counts==expected,(counts,expected)
    gg=[(g,inverse_g(g)) for g in group()]
    assert len(gg)==2880
    for k,v in solutions.items():
        rep=next(iter(v))
        # recover rank-one decomposition from image line and first nonzero basis vector
        j=next(j for j in range(4) if any(rep[j]))
        w=rep[j]
        f=tuple(next((u for u in Q if scmul(u,w)==col),None) for col in rep)
        assert all(x is not None for x in f)
        orbit={transform(g,gin,w,f) for g,gin in gg}
        assert orbit==v,(k,len(orbit),len(v))
    print('q= 4 rank1= 363 orbit_sizes= [3, 15, 45, 60, 60, 180] automorphisms= 2880')
    print('VERIFY_F4_OK')
if __name__=='__main__':main()
