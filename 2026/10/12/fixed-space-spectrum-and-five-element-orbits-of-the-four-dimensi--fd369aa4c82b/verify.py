from collections import Counter
from itertools import product

def rank_mod(M,p):
    A=[row[:] for row in M]; r=0; m=len(A); n=len(A[0])
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=pow(A[r][c]%p,-1,p)
        A[r]=[(x*z)%p for x in A[r]]
        for i in range(r+1,m):
            if A[i][c]%p:
                z=A[i][c]%p
                A[i]=[(A[i][j]-z*A[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

def auts(p):
    nz=range(1,p)
    for a in nz:
      for h in nz:
       for b,c,d,r,s in product(range(p), repeat=5):
        # columns of phi in basis e1,e2,e3,e4
        yield ((a,b,c,d),(0,h,r,s),(0,0,a*h,a*r),(0,0,0,a*a*h))

def spectrum(p):
    C=Counter(); count=0
    for cols in auts(p):
        M=[[cols[j][i]-(1 if i==j else 0) for j in range(4)] for i in range(4)]
        M=[[x%p for x in row] for row in M]
        C[4-rank_mod(M,p)]+=1; count+=1
    return C,count

def formula(q):
    return {
      0:(q-3)**2*q**5,
      1:q**3*(4*q**3-8*q**2-3*q+1),
      2:3*q**4-2*q**3-q**2+q,
      3:q**3+q**2-q-1,
      4:1,
    }

def act(cols,v,p):
    return tuple(sum(cols[j][i]*v[j] for j in range(4))%p for i in range(4))

for q in (3,5,7):
    C,total=spectrum(q); F=formula(q)
    assert {i:C.get(i,0) for i in range(5)}==F,(q,C,F)
    assert total==(q-1)**2*q**5
    burn=sum(F[i]*q**i for i in range(5))//total
    assert burn==5
    print(f'q={q} total={total} spectrum={dict(sorted(C.items()))} burnside={burn}')

q=3
A=list(auts(q))
unseen=set(product(range(q), repeat=4)); orbits=[]
while unseen:
    v=next(iter(unseen))
    orb={act(g,v,q) for g in A}
    unseen-=orb; orbits.append(orb)
assert len(orbits)==5
# intrinsic strata: 0; Z\0; gamma2\Z; C(gamma2)\gamma2; L\C(gamma2)
def typ(v):
    x1,x2,x3,x4=v
    if v==(0,0,0,0): return 0
    if x1==x2==x3==0: return 1
    if x1==x2==0: return 2
    if x1==0: return 3
    return 4
assert {frozenset(typ(v) for v in o) for o in orbits}=={frozenset([i]) for i in range(5)}
print('q=3 orbit_sizes', sorted(len(o) for o in orbits))
print('VERIFY_OK')
