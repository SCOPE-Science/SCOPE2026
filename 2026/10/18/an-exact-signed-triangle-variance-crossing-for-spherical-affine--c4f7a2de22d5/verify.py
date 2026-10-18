from fractions import Fraction as F
from itertools import product, combinations
from math import comb
p=F(3,4); delta=F(1,8); dim=2
s=p*(1-p); c=1-2*p
vectors=[(1,0),(-1,0),(0,1),(0,-1)]
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def exact_latent(n):
    triangles=list(combinations(range(n),3)); edges=list(combinations(range(n),2))
    E=F(0); E2=F(0)
    for xyz in product(vectors,repeat=n):
        U={(i,j):F(dot(xyz[i],xyz[j])) for i,j in edges}
        Q={tr:{(tr[0],tr[1]),(tr[0],tr[2]),(tr[1],tr[2])} for tr in triangles}
        M={tr:delta**3*__import__('math').prod(U[e] for e in Q[tr]) for tr in triangles}
        E+=sum(M.values())
        for a in triangles:
            for b in triangles:
                common=Q[a]&Q[b]
                prod=F(1)
                for e in common: prod*=s+c*delta*U[e]
                for e in Q[a]^Q[b]: prod*=delta*U[e]
                E2+=prod
    E/=len(vectors)**n; E2/=len(vectors)**n
    return E,E2-E*E
for n in (3,4):
    mean=comb(n,3)*delta**3/dim**2
    var=comb(n,3)*(s**3+c**3*delta**3/dim**2-delta**6/dim**4)+12*comb(n,4)*(s*delta**4/dim**3-delta**6/dim**4)
    assert exact_latent(n)==(mean,var)
    print('Exact independent latent-model check:',n,'PASS')
def phi(n):return c**3*dim**2+3*(n-3)*s*delta*dim-(3*n-8)*delta**3
slope=3*delta*(s*dim-delta**2)
assert slope>0
for n in range(3,20): assert phi(n+1)-phi(n)==slope
assert phi(6)==F(-25,256) and phi(7)==F(19,512)
assert all(phi(n)<0 for n in range(3,7))
assert all(phi(n)>0 for n in range(7,100))
print('Variance-sign threshold and linearity: PASS')
