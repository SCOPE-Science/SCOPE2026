"""Independent finite checks for sharp genus at square multiplicity, embedding dimension three."""
from math import gcd

def frobenius(gens):
    m=min(gens)
    seen={0}
    for n in range(1,100000):
        if any(n-g in seen for g in gens): seen.add(n)
        if len(seen.intersection(range(n-m+1,n+1)))==m:
            return n-m
    raise ValueError('conductor bound exceeded')

def membership(n,a,b):
    return any((n-j*a)%b==0 for j in range(n//a+1))

def enumerate_ci(s):
    m=s*s
    bound=2*m*(s-1)-1
    best=[]
    # Finite search restricted to F <= construction's known bound.
    # F=q(ab-a-b)+(q-1)p, so q,p and a,b are bounded here.
    for a in range(2,m+1):
      for b in range(a+1,m+2):
       if gcd(a,b)!=1: continue
       fu=a*b-a-b
       for q in range(2,m+2):
        if q*a>m and not membership(m,a,b): continue
        p_values=[m] if q*a>m else range(m+1,bound+2)
        for p in p_values:
         if gcd(q,p)!=1 or (p==a or p==b) or not membership(p,a,b): continue
         if min(q*a,p)!=m: continue
         F=q*fu+(q-1)*p
         if F>bound: continue
         if not best or F<best[0][0]: best=[(F,a,b,q,p)]
         elif F==best[0][0]: best.append((F,a,b,q,p))
    assert best and all(t[0]==bound for t in best), (s,best[:5],bound)
    gens=(m,m+s,m+1)
    assert frobenius(gens)==bound, (s,gens,bound)
    return s,len(best),best[:3]

if __name__=='__main__':
    # Small exhaustive bounded parameter search (not a proof for arbitrary s).
    for s in range(2,7):
        print('CASE_OK',enumerate_ci(s))
    print('VERIFY_OK')
