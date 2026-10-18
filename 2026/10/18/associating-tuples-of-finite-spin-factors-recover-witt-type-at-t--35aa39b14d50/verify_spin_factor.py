"""Independent finite-prime-field tests for Jordan spin-factor associating tuples.
The formulas are proved in RESULT.md; these finite tests are corroboration.
"""
from itertools import product
from math import prod

def gaussian(n,r,q):
    if r<0 or r>n: return 0
    num=prod(q**(n-i)-1 for i in range(r))
    den=prod(q**(r-i)-1 for i in range(r))
    return num//den

def num_iso(r,m,q,sgn):
    if r==0: return 1
    if sgn==1:
        return gaussian(m,r,q)*prod(q**(m-1-i)+1 for i in range(r))
    return gaussian(m-1,r,q)*prod(q**(m-i)+1 for i in range(r))

def count(m,s,q,sgn):
    index=m if sgn==1 else m-1
    zero=sum(num_iso(r,m,q,sgn)*prod(q**s-q**i for i in range(r)) for r in range(min(index,s)+1))
    lines=(q**(2*m)-1)//(q-1)
    extra=(lines-num_iso(1,m,q,sgn))*(q**s-1)
    return zero+extra

def matrix(m,q,sgn):
    d=2*m
    b=[[0]*d for _ in range(d)]
    for i in range(m if sgn==1 else m-1):
        b[2*i][2*i+1]=1
        b[2*i+1][2*i]=1
    if sgn==-1:
        # 2 is nonsquare modulo 3, 3 modulo 5.
        nonsquare=next(d for d in range(2,q) if pow(d,(q-1)//2,q)==q-1)
        b[-2][-2]=1
        b[-1][-1]=-nonsquare%q
    return b

def brute_pairs(m,q,sgn):
    b=matrix(m,q,sgn)
    d=2*m
    vec=list(product(range(q),repeat=d))
    # Independently test the two nonredundant ordered associator equations.
    n=0
    gram=lambda u,v: sum(u[i]*b[i][j]*v[j] for i in range(d) for j in range(d))%q
    selfgram=[gram(v,v) for v in vec]
    for i,u in enumerate(vec):
        au=selfgram[i]
        for j,v in enumerate(vec):
            av=gram(u,v)
            vv=selfgram[j]
            # (u*u)*v=u*(u*v) and (u*v)*v=u*(v*v)
            if all((au*v[k]-av*u[k])%q==0 and
                   (av*v[k]-vv*u[k])%q==0 for k in range(d)):
                n+=1
    return n

def audit():
    for m,q in [(2,3),(2,5),(3,3)]:
        for sg in (1,-1):
            got=brute_pairs(m,q,sg)
            want=count(m,2,q,sg)
            print('case',m,q,sg,'brute',got,'formula',want)
            assert got==want
    assert (count(2,2,3,1),count(2,2,3,-1))==(705,321)
    for m in range(2,5):
        for q in (3,5,7):
            for sg in (1,-1):
                w=m if sg==1 else m-1
                assert num_iso(w+1,m,q,sg)==0
                for s in (2,3,4):
                    assert sum(num_iso(r,m,q,sg)*prod(q**s-q**i for i in range(r)) for r in range(min(w,s)+1))<=q**(2*m*s)
    print('VERIFY_OK')

if __name__=='__main__':audit()
