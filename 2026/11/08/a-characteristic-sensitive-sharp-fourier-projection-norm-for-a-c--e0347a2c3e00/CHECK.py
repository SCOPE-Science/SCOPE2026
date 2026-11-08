"""Direct Fourier-sum checks for cubic-fold frequency surfaces over small finite fields."""
import cmath
import math
from collections import Counter


def run_case(p, ext2=False):
    if ext2:
        # F_{p^2}=F_p[t]/(t^2-d), with a chosen nonsquare d.
        nonsquares = {v*v % p for v in range(p)}
        d = next(v for v in range(2, p) if v not in nonsquares)
        elems = [(a,b) for a in range(p) for b in range(p)]
        add = lambda z,w: ((z[0]+w[0])%p,(z[1]+w[1])%p)
        mul = lambda z,w: ((z[0]*w[0]+d*z[1]*w[1])%p,(z[0]*w[1]+z[1]*w[0])%p)
        tr = lambda z: (2*z[0])%p
        zero = (0,0)
    else:
        elems=list(range(p))
        add=lambda z,w:(z+w)%p
        mul=lambda z,w:(z*w)%p
        tr=lambda z:z
        zero=0
    q=len(elems)
    chars=[cmath.exp(2j*math.pi*i/p) for i in range(p)]
    norm=0.0
    nonzero=0
    hist=Counter()
    for a in elems:
        for b in elems:
            for c in elems:
                direct = sum(chars[tr(add(add(mul(a,x),mul(b,y)),mul(c,mul(x,mul(y,y)))))]
                             for x in elems for y in elems)
                fibers=[y for y in elems if add(a,mul(c,mul(y,y)))==zero]
                predicted=q*sum(chars[tr(mul(b,y))] for y in fibers)
                assert abs(direct-predicted)<2e-8, (p,ext2,a,b,c,direct,predicted)
                assert len(fibers) in (0,1,2,q)
                hist[len(fibers)]+=1
                norm+=abs(direct)
                nonzero += abs(direct) > 1e-8
    expected=1+(q-1)**2/(p*q*math.sin(math.pi/(2*p)))
    assert abs(norm/q**3-expected)<2e-8,(p,q,norm/q**3,expected)
    assert hist[0]==q*(q-1)+(q-1)**2*q//2
    assert hist[1]==q*(q-1)
    assert hist[2]==(q-1)**2*q//2
    assert hist[q] == q
    assert nonzero == 1+(q**3-q)//2
    # There are q formal q-root fibers at c=a=0; only b=0 survives cancellation.
    return p,q,norm/q**3,expected,hist

if __name__=='__main__':
    for p,ext in [(3,False),(5,False),(7,False),(11,False),(3,True),(5,True)]:
        print('CHECK',run_case(p,ext))
    print('CHECK_OK cubic_fold_prime_and_quadratic_extension_fields')
