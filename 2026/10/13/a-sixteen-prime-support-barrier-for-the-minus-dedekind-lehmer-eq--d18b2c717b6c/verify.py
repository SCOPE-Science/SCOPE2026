from fractions import Fraction

LIMIT = 10**6

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,int(n**0.5)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if sieve[i]]

odd_primes=primes_upto(60)[1:16]
assert odd_primes == [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

Q=1
A=1
vals=[]
prev=None
for r,p in enumerate(odd_primes,1):
    Q*=p
    A*=p+1
    bound=Fraction(A+1,Q)
    vals.append(bound)
    if prev is not None:
        assert bound >= prev
    prev=bound
    assert bound < 3
assert vals[-1] == Fraction(3746042448844705477,1253429172199617105)

# Coordinatewise monotonicity: with C,D positive,
# (C(p+1)+1)/(Dp) = C/D + (C+1/D)/p decreases with p.
for C in [1,2,10,12345]:
    for D in [1,3,17]:
        for p in [3,5,11,53]:
            for q in [x for x in [5,7,13,59] if x>p]:
                assert Fraction(C*(p+1)+1,D*p) > Fraction(C*(q+1)+1,D*q)

# Smallest-prime-factor sieve for a regression scan.
spf=list(range(LIMIT+1))
for i in range(2,int(LIMIT**0.5)+1):
    if spf[i]==i:
        for j in range(i*i,LIMIT+1,i):
            if spf[j]==j:
                spf[j]=i

def factor(n):
    out={}
    while n>1:
        p=spf[n]
        out[p]=out.get(p,0)+1
        n//=p
    return out

def psi(n):
    f=factor(n)
    v=1
    for p,a in f.items():
        v*=p**(a-1)*(p+1)
    return v

hits=[]
for n in range(2,LIMIT+1):
    ps=psi(n)
    if (ps+1)%n==0:
        m=(ps+1)//n
        if m>=1:
            hits.append((n,m,len(factor(n))))
assert [h for h in hits if h[2] <= 15] == [(2,2,1)]
print('VERIFY_OK max_support=15 bound=%s/%s scan_limit=%d low_support_hits=%s' % (
    vals[-1].numerator, vals[-1].denominator, LIMIT, [(2,2)]))
