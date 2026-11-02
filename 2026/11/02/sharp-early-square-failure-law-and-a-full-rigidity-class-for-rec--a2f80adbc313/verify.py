"""Exact finite checks for the early square-defect law in reciprocal-sum recurrences.

Only Python's standard library is required.  This checks local root formulas,
CRT probabilities, and representative rational square identities.  The general
statements follow from the accompanying proof, not from finite enumeration.
"""
from fractions import Fraction
from math import gcd, isqrt, prod


def primes_below(n):
    return [p for p in range(2, n) if all(p % d for d in range(2, isqrt(p) + 1))]


def factor(n):
    f = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            f[d] = f.get(d,0)+1
            n //= d
        d = 3 if d == 2 else d+2
    if n > 1: f[n] = f.get(n,0)+1
    return f


def kappa(p):
    if p == 2: return 1, 0
    if p % 4 == 3: return 0, 0
    if p == 5: return 2, 2
    if p % 20 in (1, 9): return 2, 4
    return 2, 0


def local_flags(p, x):
    # First and second numerator polynomials with v_0=1 and u_0=x.
    return ((x*x+1)%p==0, (x**4+3*x*x+1)%p==0)


def exact_flags(h, initial):
    g=gcd(h, initial)
    u,v=initial//g,h//g
    u,v=u*u+v*v,u*v
    first = gcd(u,h)>1
    u,v=u*u+v*v,u*v
    second = gcd(u,h)>1
    return (first, second)


def integer_square(q):
    if q < 0 or q.denominator != 1: return False
    u = isqrt(q.numerator)
    return u*u == q.numerator


def direct_flags(h, initial):
    x=Fraction(initial)
    S=x
    bits=[]
    for n in range(1,4):
        x=Fraction(h*h,1)/S
        S+=x
        if n>=2:
            y=Fraction(x.denominator)+Fraction(2*x.numerator,h)
            bits.append(not integer_square(y))
    return tuple(bits)


def predicted_counts(h):
    fs=factor(h)
    mod=prod(p**(a+1) for p,a in fs.items())
    A=B=C=Fraction(1)
    for p,a in fs.items():
        k1,k2=kappa(p)
        r=Fraction(1,p**(a+1))
        A*=1-k1*r
        B*=1-k2*r
        C*=1-(k1+k2)*r
    probs={(False,False):C,(True,False):B-C,
           (False,True):A-C,(True,True):1-A-B+C}
    counts={key:pr*mod for key,pr in probs.items()}
    assert all(q.denominator==1 for q in counts.values())
    return mod, {key:int(n) for key,n in counts.items()}


def run():
    ps=primes_below(300)
    for p in ps:
        observed=tuple(sum(local_flags(p,x)[j] for x in range(1,p)) for j in (0,1))
        expected=kappa(p)
        assert observed==expected,(p,observed,expected)
        assert not any(all(local_flags(p,x)) for x in range(1,p))
        # For the excluded classes there is a depth-2 witness.
        if expected[1]: assert any(local_flags(p,x)[1] for x in range(1,p))
    examples=(1,2,3,4,5,8,10,13,17,26,29,37,41,65,85,104,169,221,289)
    total=0
    for h in examples:
        mod,predicted=predicted_counts(h)
        observed={key:0 for key in predicted}
        for x in range(1,mod+1):
            flags=exact_flags(h,x)
            observed[flags]+=1
            total+=1
        assert observed==predicted,(h,mod,observed,predicted)
        if h in (1,2,5,13,17,26,29,41,65,104,221):
            for x in list(range(1,min(mod,40)+1)) + [mod,mod+1,mod+2]:
                assert direct_flags(h,x)==exact_flags(h,x),(h,x)
        if all(p not in (5,) and p%20 not in (1,9) for p in factor(h)):
            # A longer finite check corroborates the no-later-defect proof.
            for x in range(1,min(mod,1000)+1):
                g=gcd(h,x); u,v=x//g,h//g
                for depth in range(1,12):
                    u,v=u*u+v*v,u*v
                    if depth>=2: assert gcd(h,u)==1,(h,x,depth)
                    # Avoid unbounded exact exponent growth in this check.
                    if depth==4: break
        else:
            # Some starting value must give a failure at the third term.
            found=any(exact_flags(h,x)[1] for x in range(1,min(mod,100000)+1))
            assert found,h
    print('VERIFY_OK local_primes=%d crt_examples=%d starting_residues=%d direct_rational_checks=yes classification_checks=yes' %
          (len(ps),len(examples),total))
    for h in (13,17,26,65,221,5,29):
        mod,counts=predicted_counts(h)
        print('h=%d period=%d N00=%d N10=%d N01=%d N11=%d' %
              (h,mod,counts[(False,False)],counts[(True,False)],counts[(False,True)],counts[(True,True)]))

if __name__=='__main__': run()
