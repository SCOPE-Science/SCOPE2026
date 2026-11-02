"""GF(2) polynomial certificates for recurrent 3x7 and 3x31 grids."""

def modulus(a,p):
    while a and a.bit_length() >= p.bit_length():
        a ^= p << (a.bit_length() - p.bit_length())
    return a

def product(a,b,p):
    out=0
    while b:
        if b&1:out ^= a
        a<<=1;b>>=1
    return modulus(out,p)

def gcd(a,b):
    while b:a,b=b,modulus(a,b)
    return a

def irreducible_prime_degree(p,d):
    assert p.bit_length()==d+1
    assert d in (7,31)  # both prime degrees
    a=2
    for j in range(d):a=product(a,a,p)
    return a==2 and gcd(p,0b110)==1 # x^2 - x = x^2 + x -> 0b110

def is_prime(n):
    if n<2:return False
    d=2
    while d*d<=n:
        if n%d==0:return False
        d += 1 if d==2 else 2
    return True

for b in (3,5):
    n=(1<<b)-1
    p=(1<<n)|(1<<(n-1))
    for j in range(3,b+1):p|=1<<((1<<b)-(1<<j))
    assert irreducible_prime_degree(p,n)
    assert is_prime((1<<n)-1)
    x=2
    for _ in range(n):x=product(x,x,p)
    assert x==2
    print(f'b={b}: P=0x{p:x}, irreducible_degree={n}, period={2**n-1} prime, one nonzero primitive orbit over GF(2)')
print('VERIFY_POLYNOMIAL_OK')
