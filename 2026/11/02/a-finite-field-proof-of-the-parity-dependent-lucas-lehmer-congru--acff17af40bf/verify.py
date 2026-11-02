"""Independent exact modular checks of the stated prime-case Lucas congruences."""
from sympy import isprime, primerange

def mul(a, b, p):
    return ((a[0]*b[0]+3*a[1]*b[1])%p, (a[0]*b[1]+a[1]*b[0])%p)

def qpow(a, e, p):
    v=(1,0)
    while e:
        if e & 1: v=mul(v,a,p)
        a=mul(a,a,p)
        e//=2
    return v

prime_cases=0
for n in range(3,401):
    p=(1<<(n-1))+3
    if not isprime(p): continue
    s=4%p
    for _ in range(n-2): s=(s*s-2)%p
    assert (s*pow(2,-1,p)-(7 if n%2 else -2))%p==0,(n,p)
    prime_cases+=1
trace_cases=0
for p in primerange(11,20000):
    if p%8!=3 or p%12 not in (7,11): continue
    trace=(2*qpow((2,1),(p-3)//2,p)[0])%p
    assert trace==(14 if p%12==7 else -4)%p,(p,trace)
    trace_cases+=1
assert prime_cases>5 and trace_cases>500
print(f'VERIFY_OK prime_cases={prime_cases} trace_cases={trace_cases}')
