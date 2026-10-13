from math import gcd, log

def divisors_box(b,t):
    a=b+t*(b+1)
    q=2**(b+1)-1
    p=2**(a+1)-(2**b+1)
    n=2**a*p*q
    F={2**i*(p if e else 1)*(q if d else 1)
       for i in range(a+1) for e in (0,1) for d in (0,1)}
    omit={2**b,n//2**b,q*2**b,n//(q*2**b)}
    S=F-omit
    assert gcd(p,q)==1
    assert len(F)==4*(a+1)
    assert all(n%d==0 for d in F)
    assert all((n//d) in S for d in S)
    assert sum(S)==2*n
    return a,p,q,n

# Exhaustive symbolic-shape regression over a rectangle of parameters.
for b in range(1,10):
    for t in range(1,10):
        divisors_box(b,t)

# The b=1 strengthening works for every a>=2.
for a in range(2,40):
    b=1; q=3; p=2**(a+1)-3; n=2**a*p*q
    assert gcd(p,q)==1
    F={2**i*(p if e else 1)*(q if d else 1)
       for i in range(a+1) for e in (0,1) for d in (0,1)}
    omit={2,n//2,6,n//6}
    S=F-omit
    assert len(F)==4*(a+1)
    assert all((n//d) in S for d in S)
    assert sum(S)==2*n
    assert n%3==0 and (n//3)%3!=0

examples=[divisors_box(b,1) for b in range(1,6)]
print('VERIFY_OK grid=9x9 b1_a=2..39 examples=' + ';'.join(f'b={b}:a={a},p={p},q={q},n={n}' for b,(a,p,q,n) in zip(range(1,6),examples)))
