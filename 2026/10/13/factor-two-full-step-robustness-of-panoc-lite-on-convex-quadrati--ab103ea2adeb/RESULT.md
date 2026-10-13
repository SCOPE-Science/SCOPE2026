# Factor-two full-step robustness of PANOC-lite on convex quadratic composites
## Finding

Consider the PANOC-lite method on
\[
\phi(x)=f(x)+g(x),
\]
with
\[
f(x)=\frac12x^{\mathsf T}Ax+a^{\mathsf T}x,
\qquad
g(x)=\frac12x^{\mathsf T}Bx+b^{\mathsf T}x+c,
\]
where
\[
A\succeq0,\qquad B\succeq0,\qquad H=A+B\succ0.
\]
Let
\[
L_f=\lambda_{\max}(A)>0.
\]

For every PANOC-lite stepsize and decrease parameter satisfying
\[
0<\gamma<\frac{2}{L_f},
\qquad
0<\sigma<\frac{\gamma(2-\gamma L_f)}2,
\]
consider an iterate \(\hat x\), its forward point
\[
\bar x=\hat x-\gamma\nabla f(\hat x),
\]
and the exact Newton direction \(d_N\) of the normal residual at \(\bar x\).

If the direction supplied to PANOC-lite is
\[
\bar d=\theta d_N
\]
with
\[
0\le\theta\le2,
\]
then PANOC-lite accepts its full line-search step
\[
\tau=1
\]
at every nonstationary iterate.

Writing
\[
y=\operatorname{prox}_{\gamma g}(\bar x)
\]
and denoting the unique minimizer by \(x_\star\), the accepted proximal candidate is exactly
\[
\hat x^+
=
x_\star+(1-\theta)(y-x_\star).
\]
Consequently
\[
\phi(\hat x^+)-\phi(x_\star)
=
(1-\theta)^2
\bigl[\phi(y)-\phi(x_\star)\bigr].
\]

The endpoints have a direct interpretation. At
\[
\theta=0,
\]
the candidate is the ordinary proximal-gradient point. At
\[
\theta=2,
\]
it is the quadratic-energy reflection of that point about the minimizer and has exactly the same objective value. At
\[
\theta=1,
\]
the candidate is
\[
\hat x^+=x_\star,
\]
so exact normal Newton solves the quadratic composite in one accepted PANOC-lite iteration from any initialization.

The direction-scaling interval
\[
[0,2]
\]
is sharp in a universal sense. For every fixed
\[
\theta\notin[0,2],
\]
there is a scalar smooth quadratic together with source-admissible \(\gamma\) and \(\sigma\) for which the full step fails the PANOC-lite sufficient-decrease test.

## Assumptions and scope

The result concerns convex quadratic \(f\) and \(g\), with the total Hessian
\[
H=A+B
\]
positive definite.

The result uses the exact Newton direction for the source normal residual, optionally multiplied by a scalar \(\theta\). It does not classify arbitrary quasi-Newton directions.

The source permits the global range
\[
0<\gamma<\frac{2}{L_f}.
\]
The theorem here holds throughout that entire interval. In particular, it includes
\[
\frac1{L_f}\le\gamma<\frac2{L_f},
\]
where the source's Dennis--Moré theorem is not stated.

Sharpness of \([0,2]\) means uniform full-step acceptance over all legal source decrease parameters and all quadratic instances. For a fixed generous choice of \(\sigma\), some larger under- or over-relaxations can still be accepted.

## Proof

Set
\[
P=(I+\gamma B)^{-1}.
\]
The quadratic proximal map is affine:
\[
\operatorname{prox}_{\gamma g}(z)
=
P(z-\gamma b).
\]

Let
\[
u=\operatorname{prox}_{\gamma g}(z).
\]
The proximal optimality condition gives
\[
z-u=\gamma(Bu+b).
\]
Hence the source normal residual becomes
\[
R_\gamma^{\mathrm{nor}}(z)
=
\nabla f(u)+\gamma^{-1}(z-u)
=
(A+B)u+(a+b).
\]
Therefore
\[
R_\gamma^{\mathrm{nor}}(z)
=
H P(z-\gamma b)+(a+b)
\]
is affine, with nonsingular Jacobian
\[
J=HP.
\]

The unique minimizer is
\[
x_\star=-H^{-1}(a+b).
\]
Define its normal-residual preimage by
\[
\bar x_\star=(I+\gamma B)x_\star+\gamma b.
\]
Then
\[
\operatorname{prox}_{\gamma g}(\bar x_\star)=x_\star
\]
and
\[
R_\gamma^{\mathrm{nor}}(\bar x_\star)=0.
\]
Since the residual is affine with Jacobian \(J\), its exact Newton direction at any \(\bar x\) is
\[
d_N
=
-J^{-1}R_\gamma^{\mathrm{nor}}(\bar x)
=
\bar x_\star-\bar x.
\]

Take the scaled direction
\[
\bar d=\theta d_N
\]
and a full PANOC-lite trial
\[
z^+
=
\bar x+\bar d
=
\bar x_\star+(1-\theta)(\bar x-\bar x_\star).
\]
Affineness of the proximal map gives
\[
\hat x^+
=
\operatorname{prox}_{\gamma g}(z^+)
=
x_\star+(1-\theta)(y-x_\star),
\]
where
\[
y=\operatorname{prox}_{\gamma g}(\bar x)
=
T_\gamma(\hat x).
\]

Because \(\phi\) is quadratic with Hessian \(H\) and minimizer \(x_\star\),
\[
\phi(x)-\phi(x_\star)
=
\frac12
(x-x_\star)^{\mathsf T}H(x-x_\star).
\]
Thus
\[
\phi(\hat x^+)-\phi(x_\star)
=
(1-\theta)^2
\bigl[\phi(y)-\phi(x_\star)\bigr].
\]
For
\[
0\le\theta\le2,
\]
one has
\[
(1-\theta)^2\le1,
\]
so
\[
\phi(\hat x^+)\le\phi(y).
\]

The source proximal-gradient decrease inequality is
\[
\phi(y)-\phi(\hat x)
\le
-\frac{\gamma(2-\gamma L_f)}2
\left\|R_\gamma^{\mathrm{nat}}(\hat x)\right\|^2.
\]
Since the source chooses
\[
\sigma<
\frac{\gamma(2-\gamma L_f)}2,
\]
every nonstationary iterate satisfies
\[
\phi(\hat x^+)-\phi(\hat x)
<
-\sigma
\left\|R_\gamma^{\mathrm{nat}}(\hat x)\right\|^2.
\]
This is exactly the PANOC-lite acceptance condition with
\[
\tau=1.
\]

At
\[
\theta=1,
\]
the affine identity gives
\[
\hat x^+=x_\star,
\]
proving one-step exact solution after the direction is formed.

To prove sharpness, let
\[
f(x)=\frac L2x^2,
\qquad
g(x)=0,
\qquad
r=\gamma L\in(0,2)\setminus\{1\}.
\]
Then
\[
y=(1-r)x,
\qquad
d_N=-y.
\]
For a scaled full Newton direction, the candidate is
\[
x^+=(1-\theta)(1-r)x.
\]
The PANOC-lite full-step test is equivalent to
\[
(1-\theta)^2(1-r)^2
\le
1-2\sigma L.
\]
The admissible upper limit for \(\sigma\) is
\[
\sigma L<
\frac{r(2-r)}2,
\]
so the right-hand side can be made arbitrarily close from above to
\[
1-r(2-r)=(1-r)^2.
\]
If
\[
\theta\notin[0,2],
\]
then
\[
|1-\theta|>1.
\]
Choosing an admissible \(\sigma\) sufficiently close to its upper limit makes the displayed full-step inequality fail. Therefore no larger universal scaling interval is possible.

## Verification

The standalone script `artifacts/verify_panoc_lite_quadratic.py` performs an exact rational two-dimensional check with noncommuting positive-semidefinite \(A\) and \(B\). It verifies the affine normal residual, exact Newton displacement, the candidate identity, and full-step acceptance for several values of \(\theta\in[0,2]\) at a stepsize strictly larger than \(1/L_f\).

The same script checks scalar rejection examples for \(\theta<0\) and \(\theta>2\).

The universal result is analytic. The script is supporting evidence rather than an exhaustive computation.

## Relationship to prior work

The PANOC-lite paper introduces a cheaper merit function, uses natural residuals in its sufficient-decrease test and normal residuals for Newton-type directions, and enlarges the globally permitted proximal-gradient stepsize from the forward-backward-envelope range
\[
(0,1/L_f)
\]
to
\[
(0,2/L_f).
\]

Its general superlinear theorem states eventual unit-step acceptance for superlinear directions, while its Dennis--Moré specialization is stated under
\[
\gamma\in(0,1/L_f).
\]
The result here is different: on convex quadratic composites it gives global, from-any-start unit-step acceptance throughout the doubled range and identifies every scalar multiple of exact normal Newton that shares this property.

Earlier forward-backward-envelope linesearch methods such as ZeroFPR use a different merit function and the traditional smaller stepsize range. Bregman forward-backward linesearch theory establishes local superlinear convergence under broad assumptions but does not imply the quadratic identity or its sharp factor-two direction cone.

Targeted searches using the primary source identifier, normal-residual Newton terminology, full-step acceptance, the doubled proximal stepsize range, quadratic composites, and scaled Newton directions did not locate an equivalent theorem.

## Limitations

The theorem is specific to convex quadratic composites with
\[
A+B\succ0.
\]
It does not extend the source's general Dennis--Moré theorem to
\[
\gamma\ge1/L_f.
\]

Exact normal-Newton directions require the true residual Jacobian. Practical quasi-Newton approximations need separate analysis.

The sharpness construction is uniform over legal \(\sigma\). It does not say that every fixed \(\sigma\) rejects every scaling outside
\[
[0,2].
\]

The one-step statement refers to one PANOC-lite iteration after the exact direction is formed; it does not account for the cost of forming or solving the Newton system.

## References

1. A. Bodard, P. Pas, A. Themelis, P. Patrinos, *PANOC-lite: A simpler and more efficient algorithm for composite minimization*, arXiv:2604.14503v1, first public 16 April 2026.
2. A. Themelis, L. Stella, P. Patrinos, *Forward-Backward Envelope for the Sum of Two Nonconvex Functions: Further Properties and Nonmonotone Linesearch Algorithms*, SIAM Journal on Optimization 28(3), 2018, DOI: 10.1137/16M1080240.
3. M. Ahookhosh, A. Themelis, P. Patrinos, *A Bregman Forward-Backward Linesearch Algorithm for Nonconvex Composite Optimization: Superlinear Convergence to Nonisolated Local Minima*, SIAM Journal on Optimization 31(1), 2021, DOI: 10.1137/19M1264783.
