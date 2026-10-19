"""Exact finite-field certificates for two-by-two cyclic sine minors.

The test at each prime is exact modulo that prime. A complex cyclotomic
zero must reduce to zero at every one of these primes. Thus one modular
nonzero value suffices to prove the complex minor is nonzero.
"""
from itertools import combinations

MODULI = {5:(11,31), 9:(19,37), 25:(101,151,251),
          49:(197,491), 121:(727,1453), 125:(251,751)}

def factors(n):
    return [d for d in range(2,n+1) if n%d==0 and all(d%e for e in range(2,int(d**.5)+1))]

def primitive_root(p):
    qs=factors(p-1)
    return next(g for g in range(2,p) if all(pow(g,(p-1)//q,p)!=1 for q in qs))

def table(n,p):
    g=pow(primitive_root(p),(p-1)//n,p)
    assert pow(g,n,p)==1
    assert all(pow(g,n//d,p)!=1 for d in factors(n))
    m=(n-1)//2
    powers=[pow(g,j,p) for j in range(n)]
    mat=[[ (powers[r*c%n]-powers[(-r*c)%n])%p for c in range(1,m+1)] for r in range(1,m+1)]
    return g,mat

def condition(n,r,s,x,y):
    C=((r*x)%n==0 or (s*y)%n==0) and ((r*y)%n==0 or (s*x)%n==0)
    A=any((r*(x+t*y))%n==0 and (s*(x+t*y))%n==0 for t in [-1,1])
    B=any(((r+t*s)*x)%n==0 and ((r+t*s)*y)%n==0 for t in [-1,1])
    return C or A or B

def verify(n,p,k):
    matrices=[(prime,*table(n,prime)) for prime in MODULI[n]]
    m=(n-1)//2
    pairs=list(combinations(range(m),2))
    predicted=0
    verified_zeros=0
    ambiguous=0
    invalid=0
    for i,j in pairs:
        for a,b in pairs:
            r,s,x,y=i+1,j+1,a+1,b+1
            assumed=condition(n,r,s,x,y) if p>=5 else False
            modular_zeros=[]
            for prime,g,M in matrices:
                modular_zeros.append((M[i][a]*M[j][b]-M[i][b]*M[j][a])%prime==0)
            if p>=5:
                predicted+=assumed
                invalid+=assumed and not all(modular_zeros)
                ambiguous+=not assumed and all(modular_zeros)
            elif n==9:
                ambiguous+=all(modular_zeros)
            verified_zeros+=all(modular_zeros)
    assert invalid==ambiguous==0,(n,invalid,ambiguous)
    if p>=5:assert predicted==verified_zeros
    if n==9:assert verified_zeros==0
    if k==2:
        d=(p-1)//2
        formula=((p-1)**2*(p-3)*(8*p*p-7*p-3))//64
        assert verified_zeros==formula,(n,verified_zeros,formula)
    print(f'N={n}: {len(pairs)**2} minors; {verified_zeros} singular; '+
          f'primes={[(q,g) for q,g,_ in matrices]}; exact certificate PASS')

if __name__=='__main__':
    for p,k in ((3,2),(5,1),(5,2),(7,2),(11,2),(5,3)):
        verify(p**k,p,k)
