"""Standalone exact-rational checks of the naive XTrace / XNysTrace formulas."""
from itertools import product
from fractions import Fraction as F
from collections import Counter

SIGNS=list(product((-1,1),repeat=2))

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def basic(probes,scale=F(1)):
    out=[]
    for i,w in enumerate(probes):
        others=probes[:i]+probes[i+1:]
        assert others
        # A pair of orthogonal sign vectors spans the plane.
        full=any(dot(others[0],o)==0 for o in others[1:])
        if full:
            out.append(scale*2)
        else:
            q=others[0]
            remain=F(dot(w,w))-F(dot(w,q)**2,dot(q,q))
            out.append(scale*(1+remain))
    return out

def output(probes,scale=F(1)):
    b=basic(probes,scale)
    k=len(b)
    mean=sum(b)/k
    proxy2=sum((v-mean)**2 for v in b)/F(k*(k-1))
    return mean,proxy2

def expected(probes,scale=F(1)):
    k=len(probes)
    cats=[w[0]*w[1] for w in probes]
    n=sum(x==1 for x in cats)
    if n==0 or n==k:
        return scale,F(0)
    if n==1 or n==k-1:
        return scale*(2+F(1,k)),(scale/F(k))**2
    return 2*scale,F(0)

# Independently evaluate the actual Moore-Penrose Nyström matrix product
# W(W^T W)^dagger W^T on both rank-one and rank-two sign sketches.
def mul(A,B):
    assert len(A[0])==len(B)
    return [[sum(A[i][h]*B[h][j] for h in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def trans(A):
    return [list(row) for row in zip(*A)]

for p in SIGNS:
    for q in SIGNS:
        W=[[F(p[0]),F(q[0])],[F(p[1]),F(q[1])]]
        G=mul(trans(W),W)
        if dot(p,q)==0:
            Gpinv=[[F(1,2),F(0)],[F(0),F(1,2)]]
            target=[[F(1),F(0)],[F(0),F(1)]]
        else:
            s=F(dot(p,q),2)
            Gpinv=[[F(1,8),F(s,8)],[F(s,8),F(1,8)]]
            target=[[F(p[i]*p[j],2) for j in range(2)] for i in range(2)]
        assert mul(mul(G,Gpinv),G)==G
        assert mul(mul(Gpinv,G),Gpinv)==Gpinv
        assert mul(mul(W,Gpinv),trans(W))==target

# Directly enumerate each ordered source probe family, including rank-deficient cases.
for k in range(3,9):
    count=Counter();mse=F(0);proxy=F(0);corr_b=F(0);corr_cross=F(0)
    bad={d:0 for d in [F(1,100),F(1,2*k+1),F(1,2*k),F(1,4),F(49,100)]}
    for probes in product(SIGNS,repeat=k):
        est,err2=output(probes)
        assert (est,err2)==expected(probes)
        count[(est,err2)]+=1
        mse+=(est-2)**2
        proxy+=err2
        bs=basic(probes)
        corr_b+=(bs[0]-2)**2
        corr_cross+=(bs[0]-2)*(bs[1]-2)
        for delta in bad:
            # Avoid irrational sqrt: e <= delta * estimate iff e2 <= delta^2 * estimate^2.
            stopping=err2<=delta*delta*est*est
            inaccurate=abs(est-2)>2*delta
            bad[delta]+=int(stopping and inaccurate)
    total=4**k
    assert count[(F(1),F(0))]==2**(k+1)
    assert count[(F(2)+F(1,k),F(1,k*k))]==k*2**(k+1)
    assert count[(F(2),F(0))]==total-(k+1)*2**(k+1)
    assert mse/F(total)==F(2,2**k)*(1+F(1,k))
    assert proxy/F(total)==F(2,2**k*k)
    assert mse/proxy==k+1
    assert corr_cross/F(total)==corr_b/F(total)/2
    for delta,n in bad.items():
        theory=F(2,2**k)*(1+k*int(F(1,2*k+1)<=delta<F(1,2*k)))
        assert F(n,total)==theory,(k,delta,F(n,total),theory)

print('verification passed')
