"""Exact finite checks for coincidence-count conditional regression in uniform words."""
from itertools import product
from fractions import Fraction as F
from collections import Counter,defaultdict
from math import comb

def test(q,n):
    L=n-1;p=F(1,q)
    joint=Counter()
    for word in product(range(q),repeat=n):
        a=sum(word[i]==word[i+1] for i in range(n-1))
        b=sum(word[i]==word[i+2] for i in range(n-2))
        joint[a,b]+=1
    count=q**n
    pa=Counter(); pb=Counter(); cross=F(0); second=F(0)
    for (a,b),c in joint.items():
        pa[a]+=c; pb[b]+=c; cross+=F(a*b*c,count)
    assert len(pa)==L+1
    assert len(pb)==L
    assert all(F(pa[k],count)==F(comb(L,k))*p**k*(1-p)**(L-k) for k in range(L+1))
    assert all(F(pb[k],count)==F(comb(L-1,k))*p**k*(1-p)**(L-1-k) for k in range(L))
    assert cross==L*(L-1)*p**2
    for k in range(L+1):
        observed=F(sum(b*c for (a,b),c in joint.items() if a==k),pa[k])
        predicted=F(k*(k-1),L)+F((L-k)*(L-k-1),L*(q-1))
        Q=F(k*(k-1))-2*(L-1)*p*k+L*(L-1)*p*p
        assert observed==predicted
        assert observed-(L-1)*p==Q/(L*(1-p))
        second+=F(pa[k],count)*(observed-(L-1)*p)**2
    var_b=(L-1)*p*(1-p)
    assert second/var_b==F(2,(q-1)*L)
    cumulant=F(0)
    for (a,b),c in joint.items():
        cumulant+=F(c,count)*(a-L*p)**2*(b-(L-1)*p)
    assert cumulant==2*(L-1)*p*p*(1-p)
    return len(joint)+2*(L+1)+L+6

def main():
    t=0; cases=0
    for q in range(2,6):
        for n in range(3,9 if q==2 else 8 if q==3 else 7 if q==4 else 6):
            t+=test(q,n);cases+=1
    print(f'PASS: {cases} complete word-censuses; all exact-rational assertions succeeded')
if __name__=='__main__':main()
