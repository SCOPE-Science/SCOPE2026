# Boundary-layer concentration of the sharp univariate moment-SOS certificate

## Statement

Henrion and Safey El Din (2026, arXiv:2609.20544v1) exhibit the univariate problem

```text
min f(x) = 1 - x
subject to p(x) = (1 - x)^3 (1 + x) >= 0,
K = [-1,1],
```

whose order-r moment-SOS relaxation, for r >= 2, has exact gap

```text
e_r = 1 / [2 r (r - 1)].
```

Their sharp primal certificate is a positive atomic functional supported at the r simple roots of

```text
A_r(x) = r T_{r-1}(x) - (r - 1) T_r(x),
```

where T_j is the Chebyshev polynomial of the first kind. There are r - 1 roots in (-1,1) and one root x_r > 1. The source construction assigns weights proportional to (1 - x_i)^(-2).

The certificate has a universal boundary-layer limit that is not visible from the relaxation value alone. Let a > 0 be the unique solution of

```text
a tanh(a) = 1,
```

and for k >= 1 let z_k in ((k - 1/2)π, kπ) be the unique solution of

```text
cos(z) + z sin(z) = 0,
```

equivalently z tan(z) = -1. Then the normalized source weights are exactly

```text
w_{r,i} = 1 / [2 r^2 (r - 1)^2 (1 - x_i)^2].
```

For the unique exterior atom,

```text
r^2 (x_r - 1) -> a^2 / 2,
w_{r,r}        -> 2 / a^4.
```

Numerically,

```text
a       = 1.1996786402577338339...
a^2 / 2 = 0.7196144199453225754...
2 / a^4 = 0.9655400431061259952...
```

Thus about 96.554% of the positive atomic mass in this explicit optimal truncated-moment certificate remains outside the true feasible set for large r, even though that exterior atom approaches the boundary point 1 at distance Θ(r^-2).

For every fixed k >= 1, if x_{r-k} is the k-th interior root counted downward from 1, then

```text
r^2 (1 - x_{r-k}) -> z_k^2 / 2,
w_{r,r-k}          -> 2 / z_k^4.
```

Consequently, with

```text
ν_r = sum_i w_{r,i} δ_{r^2 (x_i - 1)},
```

the rescaled probability measures converge weakly on the real line to

```text
ν = (2/a^4) δ_{a^2/2}
    + sum_{k>=1} (2/z_k^4) δ_{-z_k^2/2}.
```

The masses add to one. In particular, the unscaled certificate measures converge weakly to δ_1, while their mass outside [-1,1] does not tend to zero. Weak convergence therefore hides a persistent total-variation defect concentrated in an O(r^-2) boundary layer.

The limiting law has first moment 1/2. Since the source objective is the expectation of 1 - x under these atomic weights,

```text
r^2 sum_i w_{r,i} (1 - x_i) -> -1/2.
```

Thus the sharp r^-2 relaxation gap has a concrete geometric mechanism: an order-one amount of truncated-moment mass leaks just outside the feasible endpoint at an order-r^-2 distance, with a small compensating interior tail.

## Proof

### 1. Exact normalization of the atomic weights

The source paper normalizes positive weights proportional to (1 - x_i)^(-2). Since A_r(1) = 1 and the Chebyshev endpoint derivatives are

```text
T_n'(1)  = n^2,
T_n''(1) = n^2 (n^2 - 1) / 3,
```

a direct calculation gives

```text
A_r'(1)  = -r(r - 1),
A_r''(1) = -r^2 (r - 1)^2.
```

For a polynomial with simple roots x_1,...,x_r, logarithmic differentiation yields

```text
sum_i 1/(1 - x_i)   = A_r'(1)/A_r(1) = -r(r - 1),
sum_i 1/(1 - x_i)^2 = [A_r'(1)/A_r(1)]^2 - A_r''(1)/A_r(1)
                     = 2 r^2 (r - 1)^2.
```

This proves the displayed formula for w_{r,i}. It also gives the objective directly:

```text
sum_i w_{r,i}(1 - x_i) = -1 / [2r(r - 1)].
```

### 2. Exterior root

Write the unique root above one as

```text
x_r = cosh(a_r/r),   a_r > 0.
```

The equation A_r(x_r) = 0 becomes

```text
r cosh((1 - 1/r)a_r) - (r - 1) cosh(a_r) = 0.
```

On compact a-intervals the left side converges uniformly to

```text
G(a) = cosh(a) - a sinh(a).
```

G has exactly one positive zero, characterized by a tanh(a) = 1. The source root separation, together with fixed bracketing signs, identifies the finite-r exterior root with this branch, so a_r -> a. Therefore

```text
r^2 (x_r - 1) = r^2 [cosh(a_r/r) - 1] -> a^2/2.
```

Substitution into the exact weight formula gives w_{r,r} -> 2/a^4.

### 3. Interior roots nearest the endpoint

For fixed k, write

```text
x_{r-k} = cos(z_{r,k}/r),   z_{r,k} > 0.
```

The root equation is

```text
r cos((1 - 1/r)z_{r,k}) - (r - 1) cos(z_{r,k}) = 0.
```

Uniformly on compact z-intervals this converges to

```text
F(z) = cos(z) + z sin(z).
```

The source ordering of the simple interior roots identifies the k-th endpoint root with the unique zero z_k in ((k - 1/2)π, kπ), hence z_{r,k} -> z_k. Taylor expansion of cosine and the exact weight formula give

```text
r^2 (1 - x_{r-k}) -> z_k^2/2,
w_{r,r-k}          -> 2/z_k^4.
```

### 4. The limiting masses sum to one

The even entire function

```text
F(z) = cos(z) + z sin(z)
```

is the characteristic function for the self-adjoint Sturm-Liouville problem

```text
-u'' = λu,
u'(0) = 0,
u'(1) = u(1).
```

Its real zeros are ±z_k and its only purely imaginary pair is ±ia, where a tanh(a) = 1. Passing to the entire function in z^2 gives a genus-zero product

```text
F(z) = (1 + z^2/a^2) product_{k>=1} (1 - z^2/z_k^2).
```

Meanwhile,

```text
F(z) = 1 + z^2/2 - z^4/8 + O(z^6).
```

Comparing the z^2 and z^4 coefficients of the logarithms gives

```text
1/a^2 - sum_{k>=1} 1/z_k^2 = 1/2,
1/a^4 + sum_{k>=1} 1/z_k^4 = 1/2.
```

The second identity is exactly

```text
2/a^4 + sum_{k>=1} 2/z_k^4 = 1.
```

For any fixed K, the exterior atom and first K interior endpoint atoms converge individually to the displayed limiting atoms and weights. Letting K grow makes the remaining limiting mass arbitrarily small, so the exact unit-mass identity supplies tightness and proves ν_r => ν. The first trace identity gives

```text
(2/a^4)(a^2/2) - sum_{k>=1} (2/z_k^4)(z_k^2/2) = 1/2,
```

which is the first-moment identity for the boundary-layer law.

## Numerical values and reproducibility

The first interior limiting atom is

```text
z_1          = 2.7983860457838871367...
-z_1^2 / 2   = -3.9154822306189898371...
2 / z_1^4    = 0.03261365626382151549...
```

Thus the exterior atom plus the first interior atom already carry more than 99.8% of the limiting mass.

The standalone script `artifacts/verify_boundary_layer.py` requires Python 3 and `mpmath`. It computes the limiting roots by bisection, verifies finite-r roots and weights, checks exact normalization and the exact source objective, and numerically checks the two spectral sum identities. Recorded output is in `artifacts/verification_output.txt`.

## Relation to prior work and originality boundary

Henrion and Safey El Din (2026) own the degree-four sharp example, the polynomial A_r, its root distribution, the positive atomic construction, and the exact relaxation error 1/[2r(r-1)]. Henrion (2025/2026) previously solved the related symmetric Stengle example in exact arithmetic using finitely atomic moment certificates and Chebyshev/Gegenbauer structure. Pseudo-moment certificates and truncated moment representations are also established concepts.

The contribution claimed here is narrower: for the specific sharp certificate of arXiv:2609.20544v1, it gives the exact weight normalizer, r^-2 endpoint scaling of all fixed near-boundary atoms, non-vanishing exterior mass 2/a^4, the complete discrete boundary-layer limit, and the trace identities that recover both total mass and the sharp relaxation-gap constant. Searches by the defining polynomial, limiting equations, and equivalent boundary-layer/exterior-mass terminology did not locate this source-specific asymptotic description.

## Limitations

This is a structural analysis of one explicit optimal truncated-moment certificate. It does not assert that every optimizer of the semidefinite relaxation has the same representing measure, nor that persistent exterior mass occurs for general moment-SOS hierarchies. The result concerns weak and total-variation behavior of this certificate, not numerical conditioning of SDP solvers. Classical asymptotics for special-function zeros and quadrature weights are broad; an older orthogonal-polynomial formulation could potentially imply parts of the root asymptotics even though no equivalent moment-SOS boundary-layer statement was located.

## References

1. D. Henrion and M. Safey El Din, *Convergence rate of the moment-SOS hierarchy for univariate polynomial optimization*, arXiv:2609.20544v1, 2026.
2. D. Henrion, *Solving Stengle's Example in Rational Arithmetic: Exact Values of the Moment-SOS Relaxations*, arXiv:2512.19141, 2025/2026.
3. D. Henrion, *Positively not SOS: pseudo-moments and extreme rays in exact arithmetic*, arXiv:2509.01382, 2025.
