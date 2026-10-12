from math import gcd


def s_b(n,b):
    s=0
    while n:
        s += n % b
        n //= b
    return s


def core_p(n,p):
    while n % p == 0:
        n //= p
    return n

coprime_pair_tests=0
coprime_value_tests=0
for b in range(2,13):
    vals=[a for a in range(1,41) if gcd(a,b)==1]
    for i,a in enumerate(vals):
        for c in vals[i+1:]:
            coprime_pair_tests += 1
            same=True
            for n in range(1,301):
                coprime_value_tests += 1
                if s_b(a*n,b) != s_b(c*n,b):
                    same=False
                    break
            assert not same, (b,a,c)

prime_pair_tests=0
prime_value_tests=0
for p in (2,3,5,7,11):
    for a in range(1,61):
        for c in range(1,61):
            expected=(core_p(a,p)==core_p(c,p))
            observed=True
            for n in range(1,201):
                prime_value_tests += 1
                if s_b(a*n,p) != s_b(c*n,p):
                    observed=False
                    break
            assert observed == expected, (p,a,c,expected,observed)
            prime_pair_tests += 1

# Exact block identity used in the proof, over a deterministic range.
block_tests=0
for b in range(2,11):
    for q in range(2,21):
        if gcd(q,b)!=1:
            continue
        # multiplicative order of b modulo q
        x=1
        ell=None
        for e in range(1,200):
            x=(x*b)%q
            if x==1:
                ell=e
                break
        assert ell is not None
        B=b**ell
        for r in range(1,q):
            if gcd(r,q)!=1:
                continue
            A=r*(B-1)//q
            assert r*(B-1)%q==0
            assert 1 <= A <= B-2
            for K in (2,3,5,8):
                lhs=r*(b**(K*ell)-1)//q
                rhs=A*sum(B**j for j in range(K))
                assert lhs==rhs
                assert s_b(rhs,b)==K*s_b(A,b)
                block_tests += 1

print('VERIFY_OK')
print(f'coprime_pair_tests={coprime_pair_tests}')
print(f'coprime_value_tests={coprime_value_tests}')
print(f'prime_pair_tests={prime_pair_tests}')
print(f'prime_value_tests={prime_value_tests}')
print(f'block_identity_tests={block_tests}')
