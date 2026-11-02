"""Independent finite exact-arithmetic checks for cyclic differences in symmetric Lorentz norms.
Runs with Python standard library. Checks a finite family; the theorem uses a separate proof.
"""
from fractions import Fraction as F
from itertools import product

def norm(v,w):
    return sum(a*b for a,b in zip(sorted((abs(x) for x in v),reverse=True),w))

def rhs(w):
    n=len(w)
    W=[F(0)]
    for a in w: W.append(W[-1]+a)
    if n%2==0: return F(2)
    return max([ (W[k-1]+W[k+1])/W[k] for k in range(1,n)] + [2*W[n-1]/W[n]])

def trial(n,w):
    pred=rhs(w)
    best=F(0);bestvector=None
    for v in product((-1,0,1),repeat=n):
        if not any(v):continue
        d=[v[j]-v[(j-1)%n] for j in range(n)]
        rat=norm(d,w)/norm(v,w)
        if rat>best:best, bestvector=rat,v
    assert best==pred,(n,w,best,pred,bestvector)
    return best,bestvector

if __name__=='__main__':
    cases=0
    for n in (2,3,4,5,6,7,8,9):
        families=[
            [F(1) for _ in range(n)],
            [F(n-i,n) for i in range(n)],
            [F(1,2**i) for i in range(n)],
            [F(n-i+1,n+1) for i in range(n)],
        ]
        if n>=3:families.append([F(1),F(1)]+[F(1,i) for i in range(3,n+1)])
        for w in families:
            ans,ex=trial(n,w);cases+=1
            print('n=',n,'weights=',','.join(map(str,w)), 'norm=',ans,'extremizer=',ex)
    print('PASS',cases,'full ternary extremal checks; no float arithmetic')
