# Exact logarithmic modulus of the hyperbolic endpoint counterexample

## Finding

Let
\[
n\ge3,
\qquad
d=n-1,
\]
and consider the lacunary trace
\[
F(x)
=
\sum_{j=1}^{\infty}
2^{-j}\sin(2^jx_1),
\qquad
x\in\mathbb R^d,
\]
used in the recent hyperbolic-harmonic endpoint counterexample.

For a bounded function \(G\) on a Euclidean metric space, define its first-difference modulus by
\[
\omega_G(r)
=
\sup_{\lvert X-Y\rvert\le r}
\lvert G(X)-G(Y)\rvert.
\]
Then
\[
\lim_{r\downarrow0}
\frac{\omega_F(r)}
{r\log(1/r)}
=
\frac1{\log2}.
\]

Let
\[
U=\mathcal P[F]
\]
be the hyperbolic Poisson extension from the same counterexample. Then the complete extension has exactly the same leading modulus:
\[
\lim_{r\downarrow0}
\frac{\omega_U(r)}
{r\log(1/r)}
=
\frac1{\log2}.
\]

Thus this endpoint example is globally log-Lipschitz with an exact coefficient, and its failure of global Lipschitz regularity is precisely one logarithm. The coefficient does not depend on the hyperbolic dimension.

## Assumptions and scope

The source works on the upper half-space
\[
\mathbb H^n
=
\mathbb R^{n-1}\times(0,\infty),
\qquad
n\ge3,
\]
with the real hyperbolic Laplacian.

The trace and extension are exactly those in Proposition 1.3:
\[
F(x)
=
\sum_{j=1}^{\infty}
2^{-j}\sin(2^jx_1)
\]
and
\[
U(x,y)
=
\sum_{j=1}^{\infty}
2^{-j}m_d(2^jy)\sin(2^jx_1).
\]

The modulus \(\omega_U\) uses ordinary Euclidean distance on the closed upper half-space. The result concerns this explicit counterexample; it is not a universal log-Lipschitz theorem for all vertically Lipschitz hyperbolic harmonic functions.

## Proof

Fix
\[
0<r<\frac12
\]
and let
\[
J=\left\lfloor\log_2\frac1r\right\rfloor.
\]
Then
\[
2^{-(J+1)}<r\le2^{-J}.
\]

For
\[
\lvert h\rvert\le r,
\]
the elementary sine estimate gives, for every \(j\),
\[
\begin{aligned}
&\left|
2^{-j}\sin(2^j(x_1+h_1))
-
2^{-j}\sin(2^jx_1)
\right|
\\
&\qquad\le
\min\{2^{1-j},\lvert h_1\rvert\}.
\end{aligned}
\]
Therefore
\[
\begin{aligned}
\lvert F(x+h)-F(x)\rvert
&\le
\sum_{j\le J}r
+
2\sum_{j>J}2^{-j}
\\
&=
Jr+2^{1-J}.
\end{aligned}
\]
Since
\[
2^{-J}<2r,
\]
\[
\omega_F(r)
\le
Jr+4r
=
\frac{r\log(1/r)}{\log2}+O(r).
\]

For the reverse estimate, choose
\[
x=0,
\qquad
h=re_1.
\]
For
\[
1\le j\le J
\]
put
\[
t_j=2^jr.
\]
Then
\[
0<t_j\le1
\]
and
\[
\frac{2^{-j}\sin(2^jr)}r
=
\frac{\sin t_j}{t_j}.
\]
Uniformly on
\[
0\le t\le1,
\]
\[
\frac{\sin t}{t}
=
1+O(t^2).
\]
Thus
\[
\sum_{j=1}^{J}
\frac{2^{-j}\sin(2^jr)}r
=
J+
O\!\left(
\sum_{j=1}^{J}(2^jr)^2
\right).
\]
The error is bounded because
\[
\sum_{j=1}^{J}(2^jr)^2
\le
r^2\frac{4^{J+1}}3
=
O(1).
\]
The remaining tail is also bounded after division by \(r\):
\[
\frac1r
\left|
\sum_{j>J}2^{-j}\sin(2^jr)
\right|
\le
\frac{2^{-J}}r
=
O(1).
\]
Consequently
\[
\frac{F(re_1)-F(0)}r
=
J+O(1)
=
\frac{\log(1/r)}{\log2}+O(1).
\]
It follows that
\[
\omega_F(r)
\ge
\frac{r\log(1/r)}{\log2}+O(r).
\]
Together with the upper bound this proves
\[
\omega_F(r)
=
\frac{r\log(1/r)}{\log2}+O(r).
\]

Now consider the extension \(U\). The source proves
\[
\sup_{(x,y)\in\mathbb H^n}
\lvert\partial_yU(x,y)\rvert
\le
C_d.
\]
At a fixed height \(y\), the hyperbolic Poisson representation has a nonnegative translation-invariant kernel of total mass one. Hence
\[
\begin{aligned}
\lvert U(x+h,y)-U(x,y)\rvert
&=
\left|
\mathcal P_y
\bigl[
F(\,\cdot+h)-F
\bigr](x)
\right|
\\
&\le
\omega_F(\lvert h\rvert).
\end{aligned}
\]

Take two points
\[
X=(x,y),
\qquad
Y=(x',y')
\]
in the closed upper half-space with
\[
\lvert X-Y\rvert\le r.
\]
Split the difference at
\[
(x',y).
\]
Then
\[
\lvert x-x'\rvert\le r,
\qquad
\lvert y-y'\rvert\le r,
\]
and therefore
\[
\lvert U(X)-U(Y)\rvert
\le
\omega_F(r)+C_dr.
\]
Thus
\[
\omega_U(r)
\le
\frac{r\log(1/r)}{\log2}+O(r).
\]

The extension converges uniformly to \(F\) on the boundary, so boundary pairs are admissible in the closed-half-space modulus and
\[
\omega_U(r)\ge\omega_F(r).
\]
The exact limit for \(U\) follows.

## Verification

The primary source was inspected at Proposition 1.3, its complete lacunary construction, the uniform vertical derivative estimate, and Remark 3.2.

The source proves non-Lipschitzness by testing the dyadic sequence
\[
h_N=2^{-N}
\]
and obtaining only a linear-in-\(N\) lower bound for the difference quotient. It also identifies the trace as a borderline Zygmund function through dyadic Besov blocks.

The present proof separately establishes a uniform upper first-difference modulus for every sufficiently small \(r\), then matches it with a lower asymptotic at the explicit pair
\[
0,\ re_1.
\]
No finite experiment is used.

For the extension, the only source-specific analytic input beyond the Poisson representation is the already-proved estimate
\[
\sup\lvert\partial_yU\rvert<\infty.
\]
The horizontal contraction follows directly from positivity and unit mass of the Poisson kernel.

## Relationship to prior work

Classical lacunary-series theory explains why critical dyadic series with coefficients of size inverse to their frequencies belong naturally to the Zygmund rather than Lipschitz scale. The recent source explicitly invokes this classical framework and records the Besov characterization of its trace.

The source does not determine the trace's exact first-difference asymptotic. Its proof of endpoint failure uses only a coarse positive lower bound along dyadic increments, and its Zygmund remark gives scale-wise comparability rather than an exact modulus coefficient.

Targeted searches for the exact series, the coefficient
\[
1/\log2,
\]
critical Weierstrass-type moduli, and the hyperbolic Poisson extension did not locate a statement implying the two exact limits above. The closest published mathematical finding concerns a different harmonic-quasiregular conjugate-function endpoint and has a different object, mechanism, and coefficient.

## Limitations

The exact coefficient is proved for the explicit lacunary counterexample from the source. It is not asserted to be a universal coefficient for arbitrary Zygmund functions or arbitrary vertically Lipschitz hyperbolic harmonic mappings.

The result uses Euclidean first-difference modulus on the closed upper half-space. No claim is made here for intrinsic hyperbolic distance, which behaves differently near the boundary.

Because this lacunary series is a classical-type object, there remains a residual possibility that the trace asymptotic appears in older literature under different terminology even though the targeted searches did not surface it. The extension statement and its dimension-independent transfer of the same leading coefficient are tied specifically to the recent hyperbolic construction.

## References

1. H.-P. Li and S. Tan, *Transversal Hölder Criteria and Dini--Zygmund Endpoint Regularity for Hyperbolic Harmonic Mappings*, arXiv:2608.13927v1, 2026.
2. A. Zygmund, *On the convergence of lacunary trigonometric series*, Fundamenta Mathematicae 16 (1930), 90--107.
3. R. Salem and A. Zygmund, *On Lacunary Trigonometric Series*, Proceedings of the National Academy of Sciences of the United States of America 33 (1947), 333--338.
