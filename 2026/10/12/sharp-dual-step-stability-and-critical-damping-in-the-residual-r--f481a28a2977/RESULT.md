# Sharp dual-step stability and critical damping in the residual-reduction core of b-ASADMM
## Finding

Consider the deterministic scalar specialization of b-ASADMM
\[
\min_{x,y\in\mathbb R}\frac12y^2
\qquad\text{subject to}\qquad x=0.
\]
Use
\[
N=1,\qquad f\equiv0,\qquad A=1,\qquad B=0,\qquad c=0,
\]
initialize \(y_0=0\), set
\[
\theta=1,
\]
and take the scalar metric
\[
Q=q>0.
\]
Let
\[
a=\frac{q}{\eta}>0.
\]

For arbitrary source inputs
\[
\beta>0,\qquad \sigma>0,
\]
the b-ASADMM inner iteration reduces exactly to
\[
(a+\beta)x_{k+1}
=
\left(a+\frac{\beta}{2}\right)x_k+\lambda_k,
\]
followed by
\[
\lambda_{k+1}
=
\lambda_k-\frac1\sigma(2x_{k+1}-x_k).
\]

The origin is Schur stable if and only if
\[
\sigma>\frac{3}{4a+3\beta}.
\]
At the boundary
\[
\sigma=\frac{3}{4a+3\beta},
\]
one characteristic root equals \(-1\). Below the boundary, one root has modulus greater than one.

Among all stable \(\sigma\), the unique spectral-radius minimizer is
\[
\sigma_\star
=
\frac{2}{
a+\beta/2+\sqrt{a(a+\beta)}
}.
\]
At this value the characteristic roots coalesce, and the exact optimal factor is
\[
\rho_\star
=
\frac12
\left(
1-\sqrt{\frac{a}{a+\beta}}
\right).
\]

The convergence analysis in the primary source uses the coupling
\[
\sigma=\frac2\beta.
\]
On the scalar mode above, that value is rate-optimal exactly when
\[
\frac a\beta=\frac18.
\]
For the source-coupled value, the exact asymptotic factor is
\[
\rho_{\rm src}
=
\begin{cases}
\dfrac{\beta+4a+\sqrt{\beta(\beta-8a)}}{4(a+\beta)},
&
0<a\le\beta/8,
\\[2mm]
\sqrt{\dfrac{a}{a+\beta}},
&
a\ge\beta/8.
\end{cases}
\]

Hence
\[
\rho_{\rm src}\to1
\]
as
\[
a/\beta\to\infty,
\]
whereas
\[
\rho_\star
\sim
\frac{\beta}{4a}.
\]
The proof-oriented coupling can therefore be arbitrarily rate-suboptimal on this minimal deterministic constraint mode while remaining strictly stable.

## Assumptions and scope

The example is a literal deterministic specialization of the source algorithm. The finite-sum smooth term vanishes, the constraint is scalar and full-row-rank, and the \(y\)-block is decoupled from the constraint.

Take, for example,
\[
g(y)=\frac12y^2
\]
and a quadratic Bregman generator. Starting from \(y_0=0\), the \(y\)-subproblem keeps
\[
y_k=0
\]
for every iteration.

The choice
\[
\theta=1
\]
removes the outer convex combination, so
\[
x_k=\hat x_k.
\]
The epoch and stochastic-gradient machinery is inactive because \(N=1\) and \(f\equiv0\).

The stability theorem varies the algorithm input \(\sigma\). The primary convergence proof imposes
\[
\sigma=2/\beta;
\]
the statement here does not claim that the paper's general stochastic convergence theorem remains valid for every scalar-stable \(\sigma\).

## Proof

The first-order condition of the source \(\hat x\)-subproblem contains the proximal metric term, the augmented residual term, the multiplier term, and the residual-reduction correction:
\[
0
=
\frac{q}{\eta}(x_{k+1}-x_k)
+
\beta x_{k+1}
-
\lambda_k
-
\frac{\beta}{2}x_k.
\]
With
\[
a=q/\eta,
\]
this gives
\[
x_{k+1}
=
r x_k+\frac{1}{a+\beta}\lambda_k,
\qquad
r=
\frac{a+\beta/2}{a+\beta}.
\]
Because
\[
a>0,
\]
one has
\[
\frac12<r<1.
\]

The source dual update becomes
\[
\lambda_{k+1}
=
\lambda_k-\frac1\sigma(2x_{k+1}-x_k).
\]
Introduce
\[
u=\frac{1}{\sigma(a+\beta)}.
\]
The state matrix for
\[
(x_k,\lambda_k)^{\mathsf T}
\]
has trace and determinant
\[
T=1+r-2u,
\qquad
D=r-u.
\]
Thus the characteristic polynomial is
\[
p(z)=z^2-Tz+D.
\]

The three Jury conditions are
\[
1-T+D>0,\qquad
1+T+D>0,\qquad
1-D>0.
\]
Here they simplify to
\[
u>0,
\qquad
2+2r-3u>0,
\qquad
1-r+u>0.
\]
Only the middle inequality is restrictive. Therefore stability is equivalent to
\[
u<\frac{2(1+r)}3.
\]
Substituting the definitions gives
\[
\sigma>\frac{3}{4a+3\beta}.
\]

At equality,
\[
p(-1)=1+T+D=0.
\]
If \(\sigma\) is smaller, then \(p(-1)<0\); since \(p(z)\to+\infty\) as \(z\to-\infty\), a real root lies below \(-1\).

For the rate optimum, the discriminant is
\[
\Delta
=
T^2-4D
=
4u^2-4ru+(1-r)^2.
\]
Because
\[
2r-1=\frac{a}{a+\beta}>0,
\]
the two discriminant zeros are
\[
u_\pm
=
\frac{
r\pm\sqrt{2r-1}
}{2}.
\]
On
\[
0<u<u_-,
\]
the larger positive real root decreases with \(u\). On
\[
u_-<u<u_+,
\]
the roots are conjugate and their common modulus is
\[
\sqrt{D}=\sqrt{r-u},
\]
which also decreases with \(u\). For
\[
u>u_+,
\]
the dominant real-root modulus increases. For example, on the positive-trace real-root branch its derivative is
\[
-1+\frac{2u-r}{\sqrt{\Delta}}>0,
\]
because
\[
(2u-r)^2-\Delta=2r-1>0.
\]
After the trace changes sign, the dominant negative-root modulus is even more plainly increasing.

Hence the unique minimum occurs at
\[
u=u_+.
\]
Converting back to \(\sigma\) yields
\[
\sigma_\star
=
\frac{2}{
a+\beta/2+\sqrt{a(a+\beta)}
}.
\]
At the double root,
\[
\rho_\star
=
\frac12
\left(
1-\sqrt{\frac{a}{a+\beta}}
\right).
\]

Now impose the source proof coupling
\[
\sigma=2/\beta.
\]
The trace, determinant, and discriminant become
\[
T_{\rm src}
=
\frac{\beta+4a}{2(a+\beta)},
\qquad
D_{\rm src}
=
\frac{a}{a+\beta},
\]
and
\[
\Delta_{\rm src}
=
\frac{\beta(\beta-8a)}
{4(a+\beta)^2}.
\]
The displayed piecewise formula for
\[
\rho_{\rm src}
\]
follows immediately.

Finally,
\[
\sigma_\star=\frac2\beta
\]
is equivalent to
\[
a=\frac{\beta}{8}.
\]
Uniqueness of the rate minimizer proves the if-and-only-if statement. The large-\(a/\beta\) asymptotics follow from
\[
\sqrt{\frac{a}{a+\beta}}
=
1-\frac{\beta}{2a}+O(a^{-2}).
\]

## Verification

The standalone script `artifacts/verify_basadmm_scalar.py` reconstructs the scalar state matrix symbolically, verifies the Jury reductions, factors the source-coupled discriminant, checks the critical-damping formulas, and compares representative parameter choices on both sides of the stability threshold.

The script also verifies numerically that the proposed \(\sigma_\star\) gives the smallest spectral radius on a dense grid for several metric-to-penalty ratios. The continuum proof is analytic and does not rely on that grid.

## Relationship to prior work

The primary b-ASADMM paper introduces the residual-reduction \(\hat x\)-update and the extrapolated residual in the dual step. Its discussion emphasizes that
\[
1/\sigma
\]
is the dual step size and presents \(\sigma\) as controlling the propagation of stochastic fluctuations. In the convergence derivation, however, the relation
\[
\sigma=2/\beta
\]
is imposed.

The paper establishes global convergence and a local linear rate under its general stochastic assumptions, but it does not state a necessary-and-sufficient scalar stability boundary, a rate-optimal \(\sigma\), or the exact dependence of the source-coupled rate on the proximal metric strength.

The earlier balanced augmented Lagrangian method of He and Yuan uses a different primal update and a matrix-valued dual preconditioner. Its full text explicitly notes that there is no generic unified optimal tuning rule for its penalty parameter. It does not contain the residual-reduction recurrence analyzed here.

A 2025 balanced augmented Lagrangian correction method studies convergence-rate coefficients through spectral decomposition, but it employs a prediction-correction scheme with a different state map. It does not imply the source-specific scalar matrix, stability threshold, or critical-damping parameter above.

Targeted searches using b-ASADMM, balanced augmented Lagrangian, residual reduction, scalar equality feasibility, dual step size, spectral radius, and critical damping did not locate an equivalent result.

## Limitations

The finding is an exact deterministic scalar benchmark, not a global theorem for stochastic b-ASADMM.

The \(y\)-block is deliberately decoupled and remains at zero. Coupled constraints, nonzero stochastic-gradient noise, \(\theta<1\), epoch resets, nonquadratic Bregman terms, and nonconvex objectives can change the spectrum.

The exact scalar stability interval includes values of \(\sigma\) outside the coupling used by the source convergence proof. Those values are not claimed to inherit the paper's general stochastic guarantees.

The result optimizes asymptotic spectral radius on this single mode. It does not optimize wall-clock time or stochastic variance.

## References

1. Q. Zhang, C. Yang, H. Shao, *Stochastic ADMM with Balanced Augmented Lagrangian Method for Nonconvex and Nonsmooth Finite-Sum Optimization*, Numerical Mathematics: Theory, Methods and Applications 19(3), 603--644, 2026. DOI: 10.4208/nmtma.oa-2025-0132.
2. B. He, X. Yuan, *Balanced Augmented Lagrangian Method for Convex Programming*, arXiv:2108.08554.
3. Y. Li, H. Xu, W. Zhang, *A Balanced Augmented Lagrangian Method with Correction for Linearly Constrained Optimization*, Journal of Scientific Computing 104, 20, 2025. DOI: 10.1007/s10915-025-02935-9.
