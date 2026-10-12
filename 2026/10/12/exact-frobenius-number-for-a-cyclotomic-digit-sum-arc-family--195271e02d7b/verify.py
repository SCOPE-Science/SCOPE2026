from math import gcd

def sb(n,b):
    s=0
    while n:
        s += n%b; n//=b
    return s

def reachable_lengths(b,U):
    n=b*b+b+1
    R=set()
    # Because b^3 is 1 modulo n, the distinct-power criterion reduces
    # lengths up to U to counts in the three exponent classes modulo 3.
    for x in range(U+1):
        for y in range(U-x+1):
            for z in range(U-x-y+1):
                t=x+y+z
                if t and (x+b*y+b*b*z)%n==0:
                    R.add(t)
    return R

bases=0; checks=0; witness_checks=0
for b in range(2,101):
    if b%3==1:
        continue
    n=b*b+b+1
    assert gcd(b-1,n)==1
    assert gcd(b,n)==1
    U=2*b+12
    R=reachable_lengths(b,U)
    assert 2*b-2 not in R
    for t in range(2*b-1,U+1):
        assert t in R, (b,t)
        checks+=1
    A=1+b+b*b
    B=1+sum(b**(3*j+1) for j in range(b+1))
    C=sum(b**(3*j) for j in range(b+1))+sum(b**(3*j+1) for j in range(b))
    assert A%n==0 and sb(A,b)==3
    assert B%n==0 and sb(B,b)==b+2
    assert C%n==0 and sb(C,b)==2*b+1
    witness_checks += 3
    bases += 1
print(f'VERIFY_OK bases={bases} post_frobenius_checks={checks} generator_witnesses={witness_checks}')
