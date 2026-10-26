from math import isqrt

def primes_upto(n):
    is_prime = bytearray(b'\x01')*(n+1)
    is_prime[:2] = b'\x00\x00'
    for a in range(2,isqrt(n)+1):
        if is_prime[a]:
            is_prime[a*a:n+1:a] = b'\x00'*(((n-a*a)//a)+1)
    return [i for i in range(n+1) if is_prime[i]]

def residue_support_criterion(p,q):
    # Prime-support restriction is necessary for superharmonicity.
    z=(p*p+p+1)*(q*q+q+1)
    for r in (3,p,q):
        while z%r==0:
            z//=r
    return z==1

ps=primes_upto(2000)
checked=0
for i,p in enumerate(ps):
    for q in ps[i+1:]:
        checked += 1
        assert not residue_support_criterion(p,q),(p,q)
assert 7 == 2*2+2+1
assert 57==7*7+7+1 and 57==3*19
assert 13==3*3+3+1
assert 183==13*13+13+1 and 183==3*61
assert (13*13+13+1)//3==61
assert 61*61+61+1==3*13*97
assert 97==97 and 97 in ps
for p in ps:
    if p<7 or p%3!=1:continue
    q=(p*p+p+1)//3
    if (p*p+p+1)%3==0 and q>p and (q*q+q+1)%p==0:
        assert p==13 and q==61
print(f'VERIFY_OK: {checked} distinct prime pairs <=2000; forced pairs (2,7), (3,13), (13,61) eliminated; congruence witness 13 checked')
