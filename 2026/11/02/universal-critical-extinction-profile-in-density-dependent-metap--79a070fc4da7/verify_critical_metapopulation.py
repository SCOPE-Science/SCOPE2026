"""Self-contained mathematical checks for the critical metapopulation example.

The analytic theorem for arbitrary patch numbers is proved separately;
finite computation here verifies an exact two-patch instance and asymptotic diagnostics.
"""
from fractions import Fraction as Q

M = ((Q(3, 4), Q(1, 3)), (Q(1, 4), Q(2, 3)))
v = (Q(4, 7), Q(3, 7))
w = (Q(1), Q(1))
assert sum(v) == 1
assert sum(w[i] * v[i] for i in range(2)) == 1
assert all(sum(M[i][j] * v[j] for j in range(2)) == v[i] for i in range(2))
assert all(sum(w[i] * M[i][j] for i in range(2)) == w[j] for j in range(2))
assert M[0][0] + M[1][0] == M[0][1] + M[1][1] == 1
# g_j(u)=2/(1+2u); d_ij(u)=M_ij/(2(1+u)).
# The quadratic coefficient B_ij=d_ij(0)g'_j(0)+d'_ij(0)g_j(0)=-3M_ij.
B = tuple(tuple(-3 * M[i][j] for j in range(2)) for i in range(2))
kappa = -sum(w[i] * B[i][j] * v[j] ** 2 for i in range(2) for j in range(2))
assert kappa == Q(75, 49)
limit = tuple(v[i] / kappa for i in range(2))
assert limit == (Q(28, 75), Q(7, 25))
# For a density-independent dispersal matrix D_ij=M_ij/2,
# the same local recruitment gives B_ij=-2M_ij: the difference is genuine.
kappa_constant_dispersal = 2 * sum(t*t for t in v)
assert kappa_constant_dispersal == Q(50, 49)
assert kappa == Q(3, 2) * kappa_constant_dispersal
# Direct positivity and locally strict decrease of F(x) relative to Mx.
for a,b in ((Q(0),Q(1)),(Q(1,4),Q(1,5)),(Q(3),Q(7))):
    x=(a,b)
    f=tuple(sum(M[i][j]*x[j]/((1+x[j])*(1+2*x[j])) for j in range(2)) for i in range(2))
    lin=tuple(sum(M[i][j]*x[j] for j in range(2)) for i in range(2))
    assert all(Q(0) <= f[i] <= lin[i] for i in range(2))
    assert all(f[i] < lin[i] for i in range(2))
# Float-time iteration checks only, not the basis of the infinite-time proof.
x = [1.4, .2]
for t in range(1, 200001):
    x = [sum(float(M[i][j]) * x[j] / ((1+x[j])*(1+2*x[j])) for j in range(2)) for i in range(2)]
    if t in (10000, 100000, 200000):
        err=max(abs(t * x[i] - float(limit[i])) for i in range(2))
        print('time',t,'scaled_population',tuple(t*z for z in x),'max_error',err)
        assert err < 0.0002 if t >= 100000 else err < 0.002
print('PASS: Perron normalization, rational curvature and example, numerical diagnostic')
