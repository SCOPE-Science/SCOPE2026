# Quadratic onset and quartic gain of anisotropy in sharp harmonic Jacobians

## Finding

For
\[
n\ge3,
\]
let
\[
\mathcal J_n(r)
=
\frac1{n^n}
\min_{q>0}
\frac{L_{n,r}(q)^n}{q}
\]
be the exact pointwise Jacobian supremum for harmonic self-maps of the unit ball, and let
\[
q_n(r)
\]
be the unique minimizer introduced in the recent source.

The source proves qualitatively that
\[
q_n(r)<1
\qquad
(r>0),
\]
so the sharp extremal derivative is anisotropic away from the origin. The anisotropy has the exact local onset
\[
q_n(r)
=
1-c_n r^2+O(r^4),
\]
where
\[
c_n
=
\frac{(n-2)(3n+2)}
{2n^2(n+1)}.
\]

Since the extremal derivative has radial-to-tangential singular-value ratio
\[
1/q_n(r),
\]
this is equivalently
\[
\frac1{q_n(r)}
=
1+c_n r^2+O(r^4).
\]

There is a second scale hidden in the same variational problem. Define the isotropic scalar trial
\[
\mathcal J_n^{\mathrm{iso}}(r)
=
\frac{L_{n,r}(1)^n}{n^n}.
\]
Then
\[
\log
\frac{\mathcal J_n^{\mathrm{iso}}(r)}
{\mathcal J_n(r)}
=
\delta_n r^4+O(r^6),
\]
where
\[
\delta_n
=
\frac{(n-2)^2(n-1)(3n+2)^2}
{4n^5(n+1)(n+2)}.
\]
Hence
\[
\frac{\mathcal J_n^{\mathrm{iso}}(r)}
{\mathcal J_n(r)}
=
1+\delta_n r^4+O(r^6).
\]

Thus the extremal ellipsoid leaves isotropy at quadratic order, while the determinant improvement produced by that anisotropy begins only at quartic order.

## Assumptions and scope

The functions
\[
L_{n,r}(q),
\quad
q_n(r),
\quad
\mathcal J_n(r)
\]
are exactly those in Theorem 9.3 of arXiv:2609.09316v1.

The dimension satisfies
\[
n\ge3,
\]
and the expansion is taken as
\[
r\downarrow0.
\]

The comparison quantity
\[
\mathcal J_n^{\mathrm{iso}}(r)
\]
is the value of the source's exact one-variable variational objective at the scalar choice
\[
q=1.
\]
It is not the source's separate Poisson-information \(L^2\) relaxation.

The result concerns local behavior of the exact extremal family near the center. It does not give a closed form for
\[
q_n(r)
\]
at arbitrary radius.

## Proof

Put
\[
\Psi_n(s,r)
=
n\log L_{n,r}(e^s)-s.
\]
The unique minimizer is
\[
s_n(r)=\log q_n(r),
\]
and it satisfies
\[
\partial_s\Psi_n(s_n(r),r)=0.
\]

The source gives
\[
D_r(t)=1+r^2-2rt
\]
and
\[
N_{n,r}(t)
=
nt-(n+2)r+(4-n)r^2t+(n-2)r^3,
\]
with
\[
L_{n,r}(q)
=
c_n^{\mathrm{sph}}
\int_{-1}^1
\frac{
\sqrt{
n^2(1-r^2)^2(1-t^2)
+
q^2N_{n,r}(t)^2
}
}{
D_r(t)^{n/2+1}
}
(1-t^2)^{(n-3)/2}\,dt.
\]
Replacing
\[
(r,t)
\]
by
\[
(-r,-t)
\]
leaves this integral unchanged. Therefore
\[
L_{n,-r}(q)=L_{n,r}(q),
\]
and uniqueness of the minimizer implies that
\[
s_n(r)
\]
is even near the origin.

At
\[
r=0,
\]
the Poisson gradient is
\[
g_0(\eta)=n\eta.
\]
Writing
\[
t=\eta_n
\]
for a uniformly distributed point of
\[
S^{n-1},
\]
we obtain
\[
L_{n,0}(e^s)
=
n\,\mathbb E
\sqrt{
1+(e^{2s}-1)t^2
}.
\]
The standard spherical moments are
\[
\mathbb E(t^2)=\frac1n,
\qquad
\mathbb E(t^4)=\frac{3}{n(n+2)}.
\]
Differentiating twice at
\[
s=0
\]
gives
\[
H_n
:=
\partial_s^2\Psi_n(0,0)
=
\frac{2(n-1)(n+1)}{n(n+2)}
>0.
\]

Next, at
\[
q=1,
\]
the source identity
\[
\partial_s\Psi_n(0,r)
=
\frac{
nL_{n,r}'(1)-L_{n,r}(1)
}{
L_{n,r}(1)
}
\]
reduces the perturbation calculation to the Poisson-gradient formulas in Theorem 9.3 and Proposition 9.4.

Expanding those formulas to second order in
\[
r
\]
and using only
\[
\mathbb E(t^2)=1/n
\]
and
\[
\mathbb E(t^4)=3/[n(n+2)]
\]
gives
\[
nL_{n,r}'(1)-L_{n,r}(1)
=
\frac{
(n-2)(n-1)(3n+2)
}{
n^2(n+2)
}
r^2
+
O(r^4).
\]
Because
\[
L_{n,0}(1)=n,
\]
it follows that
\[
\partial_s\Psi_n(0,r)
=
A_n r^2+O(r^4),
\]
where
\[
A_n
=
\frac{
(n-2)(n-1)(3n+2)
}{
n^3(n+2)
}.
\]

The implicit-function theorem now gives
\[
s_n(r)
=
-\frac{A_n}{H_n}r^2+O(r^4).
\]
The quotient simplifies to
\[
\frac{A_n}{H_n}
=
\frac{(n-2)(3n+2)}
{2n^2(n+1)}
=
c_n.
\]
Since
\[
q_n(r)=e^{s_n(r)},
\]
\[
q_n(r)
=
1-c_nr^2+O(r^4).
\]

For the determinant gain, use Taylor expansion in the strictly convex variable
\[
s.
\]
Since
\[
\partial_s\Psi_n(0,r)
=
A_nr^2+O(r^4)
\]
and
\[
\partial_s^2\Psi_n(0,r)
=
H_n+O(r^2),
\]
the minimizing displacement gives
\[
\Psi_n(0,r)
-
\Psi_n(s_n(r),r)
=
\frac{A_n^2}{2H_n}r^4
+
O(r^6).
\]
The left side is exactly
\[
\log
\frac{
\mathcal J_n^{\mathrm{iso}}(r)
}{
\mathcal J_n(r)
}.
\]
Finally,
\[
\frac{A_n^2}{2H_n}
=
\frac{
(n-2)^2(n-1)(3n+2)^2
}{
4n^5(n+1)(n+2)
}
=
\delta_n.
\]
Exponentiating gives the ratio expansion.

## Verification

The primary source was inspected at Theorem 9.1, Theorem 9.3, Proposition 9.4, and the explicit Poisson-gradient formulas used in the one-variable reduction.

The source verifies uniqueness of the minimizer by strict log-convexity and proves only the qualitative inequality
\[
0<q_n(r)<1
\]
for
\[
n\ge3,\ r>0.
\]
Its extremal derivative formula identifies
\[
1/q_n(r)
\]
as the radial-to-tangential singular-value ratio.

The perturbation calculation uses the exact source integral, standard spherical moments through order four, and the implicit-function theorem. The resulting constants were independently sanity-checked by direct numerical minimization in dimensions
\[
3,\ 4,\ 5.
\]
For example,
\[
c_3=\frac{11}{72},
\qquad
\delta_3=\frac{121}{9720},
\]
and numerical minimization at small radii converges to these coefficients.

The proof of the infinite asymptotic statements is analytic; numerical calculations are not used as a substitute for the Taylor argument.

## Relationship to prior work

The recent paper introduces the exact higher-dimensional Jacobian variational profile and proves that its extremal derivative is strictly anisotropic away from the center. Its statement does not quantify how the unique minimizer leaves
\[
q=1
\]
or how much determinant improvement the non-scalar minimizer produces near the center.

The paper also develops a distinct Poisson-information quadratic relaxation. The present result does not repackage that relaxation: it compares the exact variational minimum with the scalar point
\[
q=1
\]
inside the exact problem itself.

The abstract ellipsoid mechanism behind the matrix minimization is related to Lewis-type determinant formulations, but the radius-dependent Poisson-gradient family and the parameter
\[
q_n(r)
\]
are specific to the recent harmonic-map theorem.

Earlier Schwarz-type harmonic-map results primarily give norm, metric, or planar Jacobian estimates. They do not contain this newly introduced higher-dimensional minimizer.

Targeted searches under the source identifier, small-radius anisotropy, the exact radial Jacobian profile, and quartic isotropic-trial deficit did not locate an implication-equivalent expansion.

## Limitations

The result is local near
\[
r=0.
\]
It does not provide a closed formula for
\[
q_n(r)
\]
on the full interval
\[
0<r<1.
\]

The quartic coefficient measures the benefit of optimizing over the anisotropy parameter instead of fixing
\[
q=1
\]
in the exact variational problem. It is not the leading gap to the separate Poisson-information upper bound.

The expansion is dimension-dependent and is stated for each fixed
\[
n\ge3;
\]
no joint large-dimension, small-radius uniformity is claimed.

## References

1. D. Zhong and D. Kalaj, *Sharp mean-width and Jacobian bounds for Euclidean and hyperbolic harmonic maps*, arXiv:2609.09316v1, 2026.
2. D. R. Lewis, *Ellipsoids defined by Banach ideal norms*, Mathematika 26 (1979), 18--29.
3. D. Kalaj and M. Vuorinen, *On harmonic functions and the Schwarz lemma*, Proceedings of the American Mathematical Society 140 (2012), 161--165; arXiv:1010.4905.
4. D. Kalaj, *A sharp inequality for harmonic diffeomorphisms of the unit disk*, Journal of Geometric Analysis 29 (2019), 392--401; arXiv:1706.01990.
