#!/usr/bin/env python3
"""Independent finite-arithmetic checks of binary PLRS legal words and gap-pair counts.
No statistical sample is presented as an infinite proof.
"""
from collections import Counter
from fractions import Fraction

def coeffs(p,q):
    c=[0]*(p+q+1)
    for i in (0,p,p+q): c[i]=1
    return tuple(c)

def plrs(p,q,n):
    c=coeffs(p,q); L=len(c)
    H=[0,1]
    for j in range(1,n+1):
        H.append(sum(c[i-1]*H[j+1-i] for i in range(1,min(j,L)+1))+(j<L))
    return H

def legal(w,c):
    if not w: return True
    if w[0]!='1':return False
    L=len(c); cw=''.join(map(str,c))
    if len(w)<L and w==cw[:len(w)]:return True
    for j in range(1,min(L,len(w))):
        if c[j]==1 and w[:j]==cw[:j] and w[j]=='0':
            k=j+1
            while k<len(w) and w[k]=='0':k+=1
            return legal(w[k:],c)
    return False

def blocks(p,q,upto):
    c=coeffs(p,q);L=len(c);prefix=''.join(map(str,c))
    sets=[set() for _ in range(upto+1)]
    for j in range(min(upto,L-1)+1): sets[j].add(prefix[:j])
    for n in range(1,upto+1):
        for k in range(n-p):
            b='1'+'0'*(p+k)
            if len(b)<=n: sets[n].update(b+w for w in sets[n-len(b)])
        for k in range(n-p-q):
            b='1'+'0'*(p-1)+'1'+'0'*(q+k)
            if len(b)<=n: sets[n].update(b+w for w in sets[n-len(b)])
    return sets

def gaps(w):
    ones=[i for i,x in enumerate(w) if x=='1']
    return [y-x for x,y in zip(ones,ones[1:])]

def finite(p,q,n):
    c=coeffs(p,q)
    strings={format(x,'0%db'%n) for x in range(1<<(n-1),1<<n) if legal(format(x,'0%db'%n),c)}
    H=plrs(p,q,n)
    vals={sum(int(x)*H[n-i] for i,x in enumerate(w)) for w in strings}
    assert vals==set(range(H[n],H[n+1])), (p,q,n,len(vals),H[n+1]-H[n], sorted(vals)[:3])
    assert strings==blocks(p,q,n)[n], (p,q,n,'blocks differ')
    counts=Counter()
    for w in strings:
        gs=gaps(w)
        counts.update(zip(gs,gs[1:]))
    return len(strings), sum(counts.values()), counts

def bracketing(p,q,low,high):
    def f(z):return 1-z-z**(p+1)-z**(p+q+1)
    assert f(low)>0 and f(high)<0, (p,q,f(low),f(high))

def sign_certificate():
    # Cov = -b(d-bH)(bd-H)/(1+b)^2,
    # b=z/(1+z), H=1/(1-z), d=p-1 for q=1.
    # For (3,1), root <7/10, hence 2>bH and 2b<H => positive.
    bracketing(3,1,Fraction(2,3),Fraction(7,10))
    z=Fraction(7,10); assert 2>z/(1-z*z)
    assert 2*z*(1-z)<1+z
    # For (20,1), root in (87/100,88/100), giving d=19>bH,
    # and 19b>H. Check endpoint monotonic bounds exactly.
    lo,hi=Fraction(87,100),Fraction(88,100)
    bracketing(20,1,lo,hi)
    assert 19>hi/(1-hi*hi)
    assert 19*hi*(1-hi)>1+hi
    # At (2,1), golden-root identity 1-z=z^2 implies bH=1.
    return 'rational root intervals and covariance signs verified'

if __name__=='__main__':
    tests=[(1,2,8),(1,3,12),(2,1,13),(3,1,14),(3,2,14),(4,1,14)]
    for p,q,n in tests:
        words,pairs,c=finite(p,q,n)
        print('p,q,n',p,q,n,'words',words,'gap_pairs',pairs,'first_counts',c.most_common(5))
        if (p,q,n)==(1,2,8):
            # paper Appendix C states 33 gaps of length 1 and 34 of length 2
            cc=Counter()
            for w in blocks(p,q,n)[n]:cc.update(gaps(w))
            assert (cc[1],cc[2])==(33,34),(cc[1],cc[2])
    print(sign_certificate())
    print('VERIFY_OK')
