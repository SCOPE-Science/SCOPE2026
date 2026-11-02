"""Finite and numerical checks for periodic K# probability profiles.

Standalone: Python 3 standard library only.  This is a finite checker, not an
infinite proof.  The proof uses binomial/local central-limit estimates.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, lgamma, log, pi, sqrt


def plurality_probability_exact(m, n):
    """Chance that binomial count 1 is the unique maximum of m fair counts."""
    cumulative = 0
    numerator = 0
    for k in range(n+1):
        numerator += comb(n, k) * cumulative**(m-1)
        cumulative += comb(n, k)
    return Fraction(numerator, 2**(m*n))


def exact_e_probability(m, n, residue):
    """Chance that m times the number of plurality-winning children is n-r."""
    if (n-residue) % m or n < residue:
        return Fraction(0)
    p = plurality_probability_exact(m, n)
    t = (n-residue)//m
    return comb(n, t) * p**t * (1-p)**(n-t)


def exact_f_probability(m, n, residues):
    r = n % m
    if r not in residues:
        return Fraction(0)
    e = exact_e_probability(m, n, r)
    return 1 - (1-e)**n


def plurality_at_node(leaves, m):
    counts = [sum(row[i] for row in leaves) for i in range(m)]
    return all(counts[0] > counts[j] for j in range(1, m))


def direct_e(m, n, residue, flat_bits):
    # n child subtrees; each has n leaves, each with m independent labels.
    hits = 0
    for child in range(n):
        leaves = [[flat_bits[(child*n+leaf)*m+i] for i in range(m)]
                  for leaf in range(n)]
        hits += int(plurality_at_node(leaves, m))
    return m*hits == n-residue


def direct_f(m, n, residues, flat_bits):
    # At the root, n children, n grandchildren per child, n labelled leaves.
    block = n*n*m
    for child in range(n):
        bits = flat_bits[child*block:(child+1)*block]
        if any(direct_e(m, n, r, bits) for r in residues):
            return True
    return False


def check_plurality():
    cases = 0
    for m, n in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,2),(4,3)]:
        positive = 0
        for bits in product((0,1), repeat=m*n):
            leaves = [bits[j*m:(j+1)*m] for j in range(n)]
            positive += int(plurality_at_node(leaves,m))
        assert Fraction(positive,2**(m*n)) == plurality_probability_exact(m,n)
        cases += 2**(m*n)
    return cases


def check_middle():
    cases = 0
    for m, n in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
        successes=[0]*m
        for bits in product((0,1),repeat=m*n*n):
            for residue in range(m):
                successes[residue]+=int(direct_e(m,n,residue,bits))
            cases+=1
        for r in range(m):
            assert Fraction(successes[r],2**(m*n*n)) == exact_e_probability(m,n,r)
    return cases


def check_root():
    m,n = 2,2
    successes=[0,0,0]
    cases=0
    for bits in product((0,1),repeat=m*n*n*n):
        for i,S in enumerate(({0},{1},{0,1})):
            successes[i]+=int(direct_f(m,n,S,bits))
        cases+=1
    for i,S in enumerate(({0},{1},{0,1})):
        assert Fraction(successes[i],cases)==exact_f_probability(m,n,S)
    return cases


def check_gate():
    cases=0
    for b,n in [(2,2),(2,3),(3,2),(3,3)]:
        counts=[0]*b
        for bits in product((0,1),repeat=b*n):
            cnt=[sum(bits[j*b+i] for j in range(n)) for i in range(b)]
            tops=[i for i in range(b) if cnt[i]==max(cnt)]
            if len(tops)==1:
                counts[tops[0]]+=1
            cases+=1
        for i in range(b):
            assert Fraction(counts[i],2**(b*n))==plurality_probability_exact(b,n)
    return cases


def plurality_probability_float(m,n):
    probs=[exp(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)-n*log(2))
           for k in range(n+1)]
    out=0.; below=0.
    for p in probs:
        out+=p*below**(m-1)
        below+=p
    return out


def check_local_asymptotics():
    # For m=2,3, the integral D_m equals 1/(2 sqrt(pi)).
    for m in (2,3):
        n=m*400
        p=plurality_probability_float(m,n)
        d=sqrt(n)*(1/m-p)
        assert abs(d-1/(2*sqrt(pi)))<0.005, (m,d)
        sigma2=(m-1)/(m*m)
        alpha=1/sqrt(2*pi*sigma2)*exp(-d*d/(2*sigma2))
        t=n//m
        e=exp(lgamma(n+1)-lgamma(t+1)-lgamma(n-t+1)
              +t*log(p)+(n-t)*log(1-p))
        assert abs(sqrt(n)*e-alpha)<0.01, (m,e,alpha)
    return 2


if __name__ == '__main__':
    output = dict(plurality_assignments=check_plurality(),
                  middle_assignments=check_middle(),
                  root_assignments=check_root(),
                  root_gate_assignments=check_gate(),
                  asymptotic_parameter_checks=check_local_asymptotics())
    print('ALL_CHECKS_OK',output)
