"""Independent finite-size checks for cooperative stability on an ANNNI ring.
Pure Python 3 standard library; run: python verify.py
Finite enumeration is supplementary, not an infinite-family proof.
"""
from fractions import Fraction
from itertools import combinations
from math import isclose


def wall_signature(spin_bits, n):
    mask=(1<<n)-1
    walls = spin_bits ^ ((spin_bits >> 1) | ((spin_bits & 1) << (n-1)))
    assert walls & ~mask == 0
    paired = walls & (((walls << 1) | (walls >> (n-1))) & mask)
    return walls, walls.bit_count(), paired.bit_count()


def reduced_energy(spin_bits,n,kappa):
    _, wall_count, adjacent_pairs=wall_signature(spin_bits,n)
    return (2-4*kappa)*wall_count+4*kappa*adjacent_pairs


def original_energy(spin_bits,n,kappa):
    signs=[1 if (spin_bits>>i)&1 else -1 for i in range(n)]
    return -sum(signs[i]*signs[(i+1)%n] for i in range(n)) + kappa*sum(signs[i]*signs[(i+2)%n] for i in range(n))


def run_lengths(spin_bits,n):
    wall_bits=wall_signature(spin_bits,n)[0]
    positions=[i for i in range(n) if wall_bits & (1<<i)]
    if not positions:
        return []
    assert len(positions)%2==0
    return [(positions[(j+1)%len(positions)]-positions[j])%n
            for j in range(len(positions))]


def predicted(spin_bits,n,kappa,order):
    domain_lengths=run_lengths(spin_bits,n)
    if order==1:
        return all(d>=2 for d in domain_lengths)
    if kappa < Fraction(1,2):
        return all(d>=3 for d in domain_lengths)
    if kappa==Fraction(1,2):
        return all(d>=2 for d in domain_lengths)
    return bool(domain_lengths) and all(2<=d<=5 for d in domain_lengths)


def exact_count(n,allowed,include_uniform):
    # Root a cyclic word at a domain boundary. Each configuration having
    # 2r domains has exactly 2r eligible root boundaries among n sites.
    dp=[[0]*(n+1) for _ in range(n+1)]
    dp[0][0]=1
    for m in range(1,n+1):
        for t in range(n+1):
            dp[m][t]=sum(dp[m-1][t-j] for j in allowed
                         if j<=t)
    return int((2 if include_uniform else 0)+
               sum(Fraction(n*dp[2*r][n],r)
                   for r in range(1,n//2+1)))


def direct_check(n,kappa):
    flips=[1<<i for i in range(n)]
    pairs=[(1<<i)|(1<<j) for i,j in combinations(range(n),2)]
    counts=[0,0]
    for spins in range(1<<n):
        e=reduced_energy(spins,n,kappa)
        stable1=all(reduced_energy(spins^f,n,kappa)>=e for f in flips)
        assert stable1==predicted(spins,n,kappa,1), (n,kappa,spins,1)
        if stable1:
            counts[0]+=1
            stable2=all(reduced_energy(spins^f,n,kappa)>=e for f in pairs)
            assert stable2==predicted(spins,n,kappa,2), (n,kappa,spins,2)
            counts[1]+=stable2
    return counts


def main():
    # Independent reconstruction from the original physical spin Hamiltonian.
    for n in (8,9,10):
        for kappa in (Fraction(1,4), Fraction(1,2), Fraction(3,4)):
            for spins in range(1<<n):
                assert original_energy(spins,n,kappa)==-(1-kappa)*n+reduced_energy(spins,n,kappa)
    for n in range(8,15):
        for kappa in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
            got1,got2=direct_check(n,kappa)
            predicted1=exact_count(n,range(2,n+1),True)
            if kappa<Fraction(1,2):
                predicted2=exact_count(n,range(3,n+1),True)
            elif kappa==Fraction(1,2):
                predicted2=predicted1
            else:
                predicted2=exact_count(n,range(2,6),False)
            assert got1==predicted1 and got2==predicted2, (n,kappa,(got1,got2),(predicted1,predicted2))
        print('n=',n, 'r1,r2 [low,critical,high]=', [direct_check(n,k)[1] for k in (Fraction(1,4),Fraction(1,2),Fraction(3,4))])
    # Check invariance throughout each open coupling interval.
    for n in range(8,12):
        for kappa in (Fraction(1,100),Fraction(49,100),Fraction(51,100),Fraction(99,100)):
            direct_check(n,kappa)
    # Dominant root equations on (1,2): sum over admissible lengths equals one.
    def bisect(func):
        lo,hi=1.0,2.0
        for _ in range(100):
            mid=(lo+hi)/2
            if func(mid)>0:hi=mid
            else:lo=mid
        return (lo+hi)/2
    lm=bisect(lambda x:x**3-x**2-1)
    l0=bisect(lambda x:x*x-x-1)
    lp=bisect(lambda x:x**5-x**3-x**2-x-1)
    assert 1<lm<lp<l0<2
    for root,func in ((lm,lambda x:x**3-x**2-1),(l0,lambda x:x*x-x-1),
                      (lp,lambda x:x**5-x**3-x**2-x-1)):
        assert abs(func(root))<1e-11
    print('entropy base roots:',lm,l0,lp)
    print('PASS: exact rational complete spin/pair enumeration, cyclic compositions, and root checks')

if __name__=='__main__':main()
