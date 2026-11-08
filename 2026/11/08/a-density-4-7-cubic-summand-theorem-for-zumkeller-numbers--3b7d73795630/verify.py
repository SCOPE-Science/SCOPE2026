"""Exact modular and finite Zumkeller checks for a cubic-summand density theorem."""
from math import gcd

def subset_test(n):
    div=[d for d in range(1,n+1) if n%d==0]
    sigma=sum(div)
    if sigma%2:return False
    target=sigma//2
    reachable=1
    for d in div:
        reachable |= reachable<<d
    return bool((reachable>>target)&1)

def verify(p,k,a):
    assert p%3==2 and k>a and a%3==0 and p<=2**(k+1)-1
    z=(2**k)*p
    mod=(2**(k+1))*(p**2)
    assert subset_test(z)
    cubes={pow(x,3,mod) for x in range(mod)}
    valid=[n for n in range(mod) if (n%(2**a)==0 and n%(2**(a+1))==2**a and n%p!=0)]
    assert all((n-z)%mod in cubes for n in valid)
    # independently check that the elementary partition construction balances sigma
    t=2**(k+1)-1;A=(t-p)//2;B=(t+1)//2
    assert A+p*B==(p+1)*t//2
    print('PASS p=%s k=%s a=%s z=%s modulus=%s admissible_residues=%s'%(p,k,a,z,mod,len(valid)))

for p,k,a in [(5,2,0),(11,3,0),(17,4,0),(23,4,0),(5,4,3),(11,4,3),(5,7,6)]:
    verify(p,k,a)
print('ALL_CHECKS_PASSED')
