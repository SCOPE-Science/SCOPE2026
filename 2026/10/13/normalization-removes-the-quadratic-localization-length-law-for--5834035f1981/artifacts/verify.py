from fractions import Fraction
import math

# For a centered finite geometric profile psi_n = r^|n|/sqrt(Z_L), n=-L,...,L.
def exact_geometric(L, r):
    assert L >= 1 and 0 < r < 1
    Z = 1.0 + 2.0*sum(r**(2*n) for n in range(1,L+1))
    S = 1.0 + 2.0*sum(r**n for n in range(1,L+1))
    K_direct = 0.0
    vals = [r**abs(n)/math.sqrt(Z) for n in range(-L,L+1)]
    for i in range(len(vals)):
        for j in range(i+1,len(vals)):
            K_direct += 2.0*abs(vals[i]*vals[j])
    K_formula = S*S/Z - 1.0
    return K_direct, K_formula

def K_infty(xi):
    r = math.exp(-1.0/xi)
    return 2*r*(r*r+r+2)/((1-r)*(1+r*r))

# Reconstruct the formula from direct pair sums on a range of finite chains.
max_err = 0.0
for L in range(1,16):
    for r in (0.05, 0.2, 0.5, 0.8, 0.95):
        a,b = exact_geometric(L,r)
        max_err = max(max_err, abs(a-b))
assert max_err < 2e-12

# Check convergence to the infinite-lattice expression and its linear large-xi asymptotic.
for xi in (0.4, 1.0, 2.0, 5.0, 10.0):
    r=math.exp(-1.0/xi)
    Linf = K_infty(xi)
    L=math.ceil(30*xi+30)
    _, Kfin=exact_geometric(L,r)
    assert abs(Kfin-Linf) < 1e-10*max(1.0,Linf)

# The normalized continuous exponential psi(x)=xi^{-1/2} exp(-|x|/xi)
# has L2 norm 1 and L1 norm 2 sqrt(xi), hence concurrence mass 4 xi - 1.
for xi in (0.25,1.0,4.0,20.0):
    norm2 = (1/xi)*xi  # integral exp(-2|x|/xi) dx = xi
    l1sq = (2*math.sqrt(xi))**2
    assert abs(norm2-1.0) < 1e-15
    assert abs((l1sq-1.0)-(4*xi-1.0)) < 1e-12

# Under the source's own truncated integral from 0 to xi and doubling,
# normalization gives a quantity linear in xi, not quadratic.
for xi in (0.5,2.0,10.0):
    trunc_mass = (2*math.sqrt(xi)*(1-math.exp(-1)))**2 - 1
    expected = 4*(1-math.exp(-1))**2*xi - 1
    assert abs(trunc_mass-expected) < 1e-12

# Verify the first asymptotic coefficients numerically at stable scales.
for xi in (20.0,40.0,80.0):
    appr = 4*xi - 1 - 2/(3*xi) + 59/(180*xi**3)
    err = abs(K_infty(xi)-appr)
    assert err*xi**5 < 0.16

print('VERIFY_OK')
print(f'max_pair_sum_error={max_err:.3e}')
for xi in (1,2,5,10,100):
    print(f'xi={xi} K_infty={K_infty(xi):.12f} K_over_4xi={K_infty(xi)/(4*xi):.12f}')
print(f'truncated_integral_linear_coefficient={4*(1-math.exp(-1))**2:.12f}')
