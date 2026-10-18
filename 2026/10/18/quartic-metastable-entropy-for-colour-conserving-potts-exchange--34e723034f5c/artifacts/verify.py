"""Independent finite checks for energy-lowering exchange blocking on Potts rings.
Only Python standard library is needed. Analytic all-size proof is in RESULT.md.
"""
from itertools import product
from math import factorial

def allowed(u,a,b,v):
    if a==b: return True
    return int(u==a)+int(b==v)>=int(u==b)+int(a==v)

def stable(w):
    N=len(w)
    return all(allowed(w[(i-1)%N],w[i],w[(i+1)%N],w[(i+2)%N]) for i in range(N))

def actual_descent_free(w):
    N=len(w)
    before=sum(w[i]!=w[(i+1)%N] for i in range(N))
    for i in range(N):
        w2=list(w); j=(i+1)%N
        w2[i],w2[j]=w2[j],w2[i]
        if sum(w2[k]!=w2[(k+1)%N] for k in range(N))<before:
            return False
    return True

def full_matrix(q):
    states=list(product(range(q),repeat=3))
    ids={s:i for i,s in enumerate(states)}
    rows=[{} for _ in states]
    for i,(u,a,b) in enumerate(states):
        for v in range(q):
            if allowed(u,a,b,v):
                j=ids[(a,b,v)]
                rows[i][j]=rows[i].get(j,0)+1
    return rows

def trace_power_sparse(rows,N):
    total=0
    for source in range(len(rows)):
        state={source:1}
        for _ in range(N):
            nxt={}
            for i,count in state.items():
                for j,mul in rows[i].items():
                    nxt[j]=nxt.get(j,0)+count*mul
            state=nxt
        total+=state.get(source,0)
    return total

def pattern(t):
    lookup={}
    return tuple(lookup.setdefault(x,len(lookup)) for x in t)

def quotient_from_labeled(q):
    reps=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2)]
    labels={r:i for i,r in enumerate(reps)}
    out=[[0]*5 for _ in range(5)]
    for i,(u,a,b) in enumerate(reps):
        m=len(set((u,a,b)))
        if m>q:continue
        for v in range(q):
            if allowed(u,a,b,v):
                w = v if v<m else m # representative third-party new color
                out[i][labels[pattern((a,b,w))]]+=1
    return out

def expected_quotient(q):
    return [[1,q-1,0,0,0],
            [0,0,1,1,q-2],
            [0,0,0,1,0],
            [1,q-1,0,0,0],
            [0,0,0,1,q-2]]

def determinant_integer(A):
    # Exact determinant by the Bareiss elimination algorithm.
    a=[list(map(int,row)) for row in A];n=len(a);sgn=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[j],a[k]=a[k],a[j];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=a[i][j]*pivot-a[i][k]*a[k][j]
                assert val%prev==0
                a[i][j]=val//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sgn*a[-1][-1]

checks=0
for q in [2,3,4,5,7,10]:
    # For q=2, the ABC orbit is omitted; compare first 4 by deleting last row/column.
    Q=quotient_from_labeled(q); E=expected_quotient(q)
    if q==2:
        assert [row[:4] for row in Q[:4]] == [row[:4] for row in E[:4]]
    else:assert Q==E
    checks+=1
    for x in [-3,-1,0,1,2,3,5,q,q+2]:
        char=x*(x**4+(1-q)*x**3-x**2+(1-q)*x+(q-1)*(q-2))
        assert determinant_integer([[x*int(i==j)-Q[i][j] for j in range(5)] for i in range(5)])==char
        checks+=1

for q,Nmax in [(2,9),(3,8),(4,6)]:
    A=full_matrix(q)
    for N in range(4,Nmax+1):
        enumerated=0
        for w in product(range(q),repeat=N):
            a=stable(w);b=actual_descent_free(w)
            assert a==b,(q,N,w)
            enumerated+=a
        assert enumerated==trace_power_sparse(A,N),(q,N,enumerated)
        checks+=1

for q in [2,3,4,5]:
    A=full_matrix(q)
    # Strong connectivity (all states can reach all-equal) plus self loops is proved symbolically.
    states=list(product(range(q),repeat=3))
    for s in states:
        assert allowed(s[0],s[1],s[2],s[2])
        assert allowed(s[1],s[2],s[2],s[2])
        checks+=1

assert stable((0,1,2,0,1,2))
assert not stable((0,1,0,1))
checks+=2
print(f"PASS: {checks} checks (quotient, characteristic, exhaustive ring energies, irreducibility steps)")
