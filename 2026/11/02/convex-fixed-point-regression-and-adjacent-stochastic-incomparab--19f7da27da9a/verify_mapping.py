from math import comb, factorial
from collections import Counter
from itertools import product
from fractions import Fraction

def derangements(n):
    d=[1,0]+[0]*max(0,n-1)
    for j in range(2,n+1): d[j]=(j-1)*(d[j-1]+d[j-2])
    return d

def law(n,k):
    q=n-1;m=n-k;D=derangements(n)
    return {k+j:Fraction(comb(m,j)*D[j]*(j+k)*n**(m-j),n*q**m) for j in range(m+1)}

def cyclic_count(f):
    n=len(f); cy=set()
    for start in range(n):
        seen={};v=start
        while v not in seen:
            seen[v]=len(seen);v=f[v]
        cyc=list(seen)[seen[v]:]
        cy.update(cyc)
    return len(cy)

checks=0
for n in range(3,8):
    cnt=[Counter() for _ in range(n+1)]
    for f in product(range(n),repeat=n):
        k=sum(f[i]==i for i in range(n));c=cyclic_count(f)
        cnt[k][c]+=1
    for k in range(n+1):
        observed={c:Fraction(v,sum(cnt[k].values())) for c,v in cnt[k].items()}
        predicted={c:v for c,v in law(n,k).items() if v}
        assert observed==predicted,('law',n,k,observed,predicted)
        checks+=1
        mean=sum(c*v for c,v in predicted.items())
        q=n-1;m=n-k
        expect=Fraction(k)+sum((Fraction(factorial(m),factorial(m-j)*q**j) for j in range(2,m+1)),Fraction(0))
        assert mean==expect,(n,k,mean,expect)
        checks+=1
    means=[sum(c*v for c,v in law(n,k).items()) for k in range(n+1)]
    assert means[1]<means[0] and means[1]<means[2];checks+=1
    delta=[means[k+1]-means[k] for k in range(n)]
    assert all(delta[k+1]>delta[k] for k in range(n-1));checks+=1
    for k in range(1,n-1):
        L=law(n,k);R=law(n,k+1)
        def tail(d,h):return sum((v for c,v in d.items() if c>=h),Fraction(0))
        assert tail(R,k+1)>tail(L,k+1) and tail(R,k+2)<tail(L,k+2)
        checks+=2
    total=n**n
    E_K=Fraction(sum(k*sum(v for v in cnt[k].values()) for k in range(n+1)),total)
    E_C=Fraction(sum(c*v for k in range(n+1) for c,v in cnt[k].items()),total)
    E_KC=Fraction(sum(k*c*v for k in range(n+1) for c,v in cnt[k].items()),total)
    assert E_K==1 and E_KC-E_K*E_C==0; checks+=1
# Non-exhaustive but exact all-integer formula consistency and sharp inequalities.
for n in range(8,71):
    q=n-1
    means=[]
    for k in range(n+1):
        m=n-k
        distribution=law(n,k)
        assert sum(distribution.values())==1;checks+=1
        mean=sum(c*v for c,v in distribution.items())
        series=Fraction(k)+sum((Fraction(factorial(m),factorial(m-j)*q**j) for j in range(2,m+1)),Fraction(0))
        assert mean==series;checks+=1
        means.append(mean)
    assert means[1]<means[0] and means[1]<means[2];checks+=1
    assert means[2]-means[1]==Fraction(1,q);checks+=1
    assert all(means[k+2]-means[k+1]>means[k+1]-means[k] for k in range(n-1));checks+=1
    gap=sum((Fraction(factorial(q),factorial(q-t)*q**t) for t in range(1,q+1)),Fraction(0))/q
    assert means[0]-means[1]==gap;checks+=1
    for k in range(1,n-1):
        L,R=law(n,k),law(n,k+1)
        def tail(d,h):return sum((v for c,v in d.items() if c>=h),Fraction(0))
        assert tail(R,k+1)>tail(L,k+1);checks+=1
        assert tail(R,k+2)<tail(L,k+2);checks+=1
print('PASS',checks,'exact checks; exhaustive mappings n=3..7 and formula tests n=8..70')
