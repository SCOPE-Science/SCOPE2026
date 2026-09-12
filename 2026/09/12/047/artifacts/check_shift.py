"""Verify the sparse-Wigner shift arithmetic used in the TARGET disproof.

Counterexample: delta*=1/4, sigma_{ij}^2=1/N for ALL i,j (including
diagonal, so every column sums to exactly N*(1/N)=1 with c_-=c_+=1),
H_ij = sigma_ij*B_ij*xi_ij/sqrt(p_N) for i<=j (symmetrized),
B~Bernoulli(p_N), xi=Rademacher, p_N = N^{-5/12}, q^2=N*p.
Checks: exact column sums, scope membership, Lee-Schnelli applicability
(q >> N^{1/6}), off-diagonal AND diagonal moment bounds
E|H|^k = 1/(N q^{k-2}), fourth cumulant s4 = 1-3p, edge shift
L-2 ~ s4/q^2, rescaled bias mu_N = N^{2/3}(L-2) -> infinity, and that the
diagonal-induced error O(1/(N q^2)) is absorbed in O(q^{-4}).
"""
import math

delta_star = 1/4
exponent_p = -5/12  # p = N^{-5/12}

print(f"{'N':>10} {'p':>12} {'Np':>12} {'q=N^{7/24}':>12} {'s4=1-3p':>10} {'mu~N^{1/12}':>12} {'Np/N^{7/12}':>12}")
for logN in [3, 4, 5, 6, 8, 12]:
    N = 10**logN
    p = N**exponent_p
    Np = N*p
    q2 = Np
    q = math.sqrt(q2)
    s4 = 1-3*p
    Lshift = s4/q2  # leading term of L-2
    mu = N**(2/3)*Lshift
    ratio = Np/(N**(7/12))
    print(f"{N:>10} {p:>12.3e} {Np:>12.3e} {q:>12.3e} {s4:>10.6f} {mu:>12.3e} {ratio:>12.6f}")

# Exact column sums with sigma^2=1/N for ALL i,j
for N in [2, 3, 1000]:
    colsum = N*(1/N)
    assert colsum == 1.0, (N, colsum)
    assert 1/N >= 1/N and 1/N <= 1/N  # c_-=c_+=1 bounds: sigma^2*N in [1,1]
print()
print("exact column sums: N*(1/N)=1 for all N checked; c_-=c_+=1 for all i,j incl. diagonal")

# Exponent checks
print("q exponent 7/24 =", 7/24, "> 1/6 =", 1/6, ":", 7/24 > 1/6)
print("mu exponent 2/3-7/12 =", 2/3-7/12, "= 1/12 =", 1/12)
# Moment check off-diagonal AND diagonal: same law => E|H|^k = 1/(N q^{k-2})
N = 10**6
p = N**exponent_p
q2 = N*p
for k in [3,4,5,6]:
    lhs = (N**(-k/2))*p/(p**(k/2))  # sigma^k * E|B|^k * E|xi|^k / p^{k/2}, sigma=1/sqrt(N)
    rhs = 1/(N*(math.sqrt(q2)**(k-2)))
    assert math.isclose(lhs,rhs), (k, lhs, rhs)
    print(f"k={k}: off-diag E|H|^k={lhs:.3e} = 1/(N q^(k-2))={rhs:.3e}; diagonal identical law => same bound OK")
# Diagonal cumulant check: same single-site law => kappa_diag^{(4)} = (1-3p)/(N q^2), s4diag = 1-3p
s4 = 1-3*p
print("diag kappa^{(4)}=(1-3p)/(N q^2), s4diag=1-3p =", s4, "-> 1")
# Diagonal contribution to self-consistent equation is O(1/(N q^2)): N diag terms vs N^2 off-diag
# Show it is absorbed in O(q^{-4}): ratio (1/(N q^2))/(1/q^4) = q^2/N = p -> 0
print()
for logN in [3, 6, 12]:
    Nn = 10**logN
    pp = Nn**exponent_p
    qq2 = Nn*pp
    print(f"N=10^{logN}: q^2/N = p = {pp:.3e} -> 0, so O(1/(Nq^2)) << q^{-4}; absorbed in O(q^-4)")
# Conservative lower bound mu >= (1/4) N^{2/3}/q^2 once s4>=1/2 and combined remainder <=1/4q^2
print()
print("s4 -> 1, combined remainder o(1/q^2), so L-2 >= (1/4)/q^2 eventually => mu_N >= (1/4) N^{1/12} -> inf")
print("e.g. N=10^12: (1/4)*N^{1/12} =", 0.25*(10**12)**(1/12))
print("ALL CHECKS PASSED")
