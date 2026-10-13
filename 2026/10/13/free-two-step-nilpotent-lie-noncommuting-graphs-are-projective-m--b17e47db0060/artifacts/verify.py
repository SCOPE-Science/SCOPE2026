from itertools import product, combinations
from math import comb

def wedge_basis(r):
    return [(i,j) for i in range(r) for j in range(i+1,r)]

def wedge(v,w,p):
    B=wedge_basis(len(v))
    return tuple((v[i]*w[j]-v[j]*w[i])%p for i,j in B)

def addv(a,b,p):
    return tuple((x+y)%p for x,y in zip(a,b))

def bracket(x,y,p,r):
    v=x[:r]; w=y[:r]
    return wedge(v,w,p)

def normalize(v,p):
    j=next(i for i,x in enumerate(v) if x%p)
    z=pow(v[j],-1,p)
    return tuple((z*x)%p for x in v)

def verify_case(p,r):
    c=comb(r,2)
    V=list(product(range(p),repeat=r))
    Z=list(product(range(p),repeat=c))
    zeroV=(0,)*r
    vertices=[v+z for v in V if v!=zeroV for z in Z]
    s=(p**c)*(p-1)
    k=(p**r-1)//(p-1)
    assert len(vertices)==k*s

    keys={x:normalize(x[:r],p) for x in vertices}
    counts={}
    for x in vertices:
        counts[keys[x]]=counts.get(keys[x],0)+1
    assert len(counts)==k
    assert set(counts.values())=={s}

    deg={x:0 for x in vertices}
    for x,y in combinations(vertices,2):
        actual=any(bracket(x,y,p,r))
        predicted=keys[x]!=keys[y]
        assert actual==predicted,(p,r,x,y)
        if actual:
            deg[x]+=1; deg[y]+=1
    D=s*(k-1)
    assert set(deg.values())=={D}

    # Spectrum consistency for {D^1, (-s)^(k-1), 0^(k(s-1))}.
    N=k*s
    assert 1+(k-1)+k*(s-1)==N
    assert D-(k-1)*s==0
    assert D*D+(k-1)*s*s==N*D

    print({'q':p,'r':r,'center_dimension':c,'parts':k,
           'part_size':s,'vertices':N,'degree':D})

for p,r in [(2,2),(2,3),(3,2),(3,3),(5,2)]:
    verify_case(p,r)

print('VERIFY_OK')
