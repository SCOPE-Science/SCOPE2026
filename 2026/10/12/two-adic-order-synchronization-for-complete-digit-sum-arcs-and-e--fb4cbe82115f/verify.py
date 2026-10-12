"""Finite checks for a digit-sum-two modular criterion and base-class count."""
from math import gcd


def factor(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            out.append((p,a))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n,1))
    return out


def valuation2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def multiplicative_order(b, mod):
    assert mod >= 2 and gcd(b,mod) == 1
    t, v = 0, 1
    while True:
        t += 1
        v = v*b % mod
        if v == 1:
            return t
        assert t <= mod


def odd_prime_power_parts(n):
    return [(p,p**a,(p-1)*p**(a-1)) for p,a in factor(n) if p != 2]


def criterion(b,n):
    assert b % 2 and gcd(b-1,n)==2
    n0 = 1
    n1 = n
    for p,a in factor(n):
        if b % p == 0:
            n0 *= p**a
            n1 //= p**a
    if n1 == 1:
        return True
    e=valuation2(n1)
    if e>=2 and b%(2**e) != (2**e)-1:
        return False
    vs=[]
    for p,mod,phi in odd_prime_power_parts(n1):
        o=multiplicative_order(b,mod)
        if o%2: return False
        vs.append(valuation2(o))
    if len(set(vs))>1:
        return False
    if e>=2 and any(v!=1 for v in vs):
        return False
    return True


def raw_two_digit_reachable(b,n):
    # Independent finite-state search: enumerate all residues represented
    # by 2b^i or b^i+b^j modulo n after the powers enter a cycle.
    seen=set()
    powers=[]
    r=1
    while r not in seen:
        seen.add(r)
        powers.append(r)
        r=r*b%n
    for i,a in enumerate(powers):
        if 2*a%n == 0:
            return True
        for c in powers[i+1:]:
            if (a+c)%n == 0:
                return True
    return False


def predicted_count(n):
    assert n%2==0
    e=valuation2(n)
    fac=odd_prime_power_parts(n)
    if not fac:
        return 1
    s=[valuation2(phi) for _,_,phi in fac]
    u=1
    for (_,_,phi),s_i in zip(fac,s):
        u*=phi//(2**s_i)
    if e>=2:
        return u
    r=len(fac)
    m=min(s)
    return u*((2**(r*m)-1)//(2**r-1))


def predicted_count_all(n):
    assert n % 2 == 0
    e=valuation2(n)
    fac=odd_prime_power_parts(n)
    if not fac:
        return 1
    a=[valuation2(phi) for _,_,phi in fac]
    u=[phi//(2**t) for (_,_,phi),t in zip(fac,a)]
    d=[mod//p for p,mod,phi in fac]
    if e>=2:
        value=1
        for di,ui in zip(d,u):
            value*=di+ui
        return value
    # At e=1 each nonunit odd-primary coordinate is unrestricted.
    # The empty set of unit coordinates contributes exactly once.
    total=1
    for di in d:
        total*=di
    for mask in range(1,1<<len(fac)):
        r=mask.bit_count()
        m=min(a[i] for i in range(len(fac)) if (mask>>i)&1)
        ways=(2**(r*m)-1)//(2**r-1)
        for i in range(len(fac)):
            ways*=u[i] if (mask>>i)&1 else d[i]
        total+=ways
    return total


def run():
    two_cases=0
    good_cases=0
    for b in range(3,84,2):
        for n in range(2,182,2):
            if gcd(b-1,n)!=2:
                continue
            pred=criterion(b,n)
            actual=raw_two_digit_reachable(b,n)
            assert pred==actual,(b,n,pred,actual)
            two_cases+=1
            good_cases+=bool(pred)
    count_cases=0
    for n in range(2,502,2):
        expected=predicted_count(n)
        direct=sum(criterion(b,n) for b in range(3,n+3,2) if gcd(b,n)==1 and gcd(b-1,n)==2)
        # odd b from 3 to n+1 represents all odd residue classes modulo n
        assert direct==expected,(n,direct,expected)
        count_cases+=1
    all_count_cases=0
    for n in range(2,502,2):
        expected=predicted_count_all(n)
        direct=sum(criterion(b,n) for b in range(3,n+3,2) if gcd(b-1,n)==2)
        assert expected==direct,(n,expected,direct)
        all_count_cases+=1
    examples={}
    for b,n in [(3,10),(3,14),(3,70),(3,8),(19,70),(59,70),(69,70)]:
        examples[f'{b},{n}']=criterion(b,n)
    assert examples == {'3,10':True,'3,14':True,'3,70':False,'3,8':False,'19,70':True,'59,70':True,'69,70':True}, examples
    print('VERIFY_OK')
    print(f'digit_sum_two_finite_state_vs_local_criterion={two_cases}_PASS')
    print(f'positive_finite_state_cases={good_cases}')
    print(f'coprime_base_residue_count_formulas_even_moduli_2_to_500={count_cases}_PASS')
    print(f'all_base_residue_count_formulas_even_moduli_2_to_500={all_count_cases}_PASS')
    print(f'CRT_phase_mismatch_and_success_examples={examples}')
    print('Finite tests support but do not prove the universal statements.')


if __name__=='__main__':
    run()
