"""Direct exact enumeration of two-term equations in groups with adjoined zero."""
from fractions import Fraction
from itertools import product
from math import gcd,lcm

def direct(moduli,k,e,f):
    group=list(product(*(range(x) for x in moduli)))
    alphabet=[None]+group
    n=0
    for values in product(alphabet,repeat=k):
        def ev(coeff):
            if any(values[j] is None for j,c in enumerate(coeff) if c!=-1):
                return None
            return tuple(sum(c*values[j][t] for j,c in enumerate(coeff) if c!=-1)%moduli[t] for t in range(len(moduli)))
        n+=(ev(e)==ev(f))
    return Fraction(n,len(alphabet)**k)

def predicted(moduli,e,f):
    q=1
    for a in moduli:q*=a
    s=Fraction(q,q+1)
    I={j for j,c in enumerate(e) if c!=-1}
    J={j for j,c in enumerate(f) if c!=-1}
    expo=lcm(*moduli)
    d=expo
    for j in range(len(e)):
        a=e[j] if e[j]!=-1 else 0
        b=f[j] if f[j]!=-1 else 0
        d=gcd(d,a-b)
    image_size=1
    for a in moduli:image_size*=a//gcd(d,a)
    c=Fraction(1,image_size)
    return 1-s**len(I)-s**len(J)+(1+c)*s**len(I|J)

def run():
    cases=[([4],3),([2,2],3),([3],3),([6],2),([4,2],2),([2,2,2],2),([2,3],2)]
    checks=0
    for moduli,k in cases:
        expo=lcm(*moduli)
        # -1 absent, 0 represents exponent 'expo' (present, trivial group exponent).
        words=[e for e in product([-1]+list(range(expo)),repeat=k) if any(c!=-1 for c in e)]
        for e in words:
            for f in words:
                a=direct(moduli,k,e,f)
                b=predicted(moduli,e,f)
                assert a==b,(moduli,k,e,f,a,b)
                checks+=1
        print(f'PASS moduli={moduli} arity={k} equations={len(words)**2}')
    print('VERIFY_OK',checks)

if __name__=='__main__':run()
