"""Exact finite checks for a squarefree base-digit collision theorem.
No third-party packages required. Finite checks supplement, not replace, the proof.
"""
from math import gcd, isqrt

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * ((n-p*p)//p+1)
    return [j for j in range(2,n+1) if sieve[j]]

PS=primes_upto(70000)
def squarefree(n):
    for p in PS:
        if p*p>n: break
        if n%(p*p)==0: return False
    return True

def digit_sum(n,b):
    ans=0
    while n:
        n,r=divmod(n,b);ans+=r
    return ans

successful=[]
for b in range(12,1001,2):
    q=b*b-2;u=2*b-1;v=2*b-3
    n=q*u; m=q*v
    assert n!=m and n>0 and m>0
    assert n == b**3+(b-2)*b*b+(b-4)*b+2
    assert m == b**3+(b-4)*b*b+(b-4)*b+6
    assert digit_sum(n,b)==v
    assert digit_sum(m,b)==u
    assert n*digit_sum(n,b)==m*digit_sum(m,b)
    condition=(b%7!=4 and squarefree(q) and squarefree(u) and squarefree(v))
    if condition: successful.append(b)
    if b<=400:
        assert (squarefree(n) and squarefree(m))==condition
    else:
        if condition:
            assert gcd(q,u)==gcd(q,v)==gcd(u,v)==1
assert successful[0]==12

for p in PS:
    if p>101:break
    mod=p*p
    good=0
    for b in range(mod):
        if p==2:
            qualifies=b%2==0
        else:
            qualifies=(b%7!=4 if p==7 else True) and all(v%mod!=0 for v in (b*b-2,2*b-1,2*b-3))
        good+=qualifies
    if p==2: expected=2
    elif p==3: expected=7
    elif p==7: expected=40
    else: expected=mod-(4 if pow(2,(p-1)//2,p)==1 else 2)
    assert good==expected,(p,good,expected)

delta=(1/2)*(7/9)*(40/49)
for p in PS:
    if p<5 or p==7:continue
    delta*=1-(4 if pow(2,(p-1)//2,p)==1 else 2)/p**2
print('VERIFY_OK')
print('even_bases_tested=12..1000')
print('exact_collision_digit_expansions=PASS')
print('complete_n_m_squarefree_equivalence_even_bases_12..400=PASS')
print('positive_witness_bases_12..1000=',len(successful))
print('positive_witness_first_20=',successful[:20])
print('local_residue_counts_primes_to_101=PASS')
print('Euler_product_truncated_to_primes_70000=',format(delta,'.12f'))
print('finite_tests_supplement_unrestricted_symbolic_proof_and_density_sieve')
