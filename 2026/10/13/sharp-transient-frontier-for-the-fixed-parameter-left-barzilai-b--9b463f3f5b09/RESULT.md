# Sharp transient frontier for the fixed-parameter LEFT Barzilai--Borwein extension
## Finding

Consider
\[
f(x)
=
\frac12(x-x_\star)^{\mathsf T}A(x-x_\star),
\qquad
\mu I\preceq A\preceq LI,
\qquad
\kappa=\frac L\mu>1.
\]
For the fixed-parameter LEFT variant analyzed by Xu, let
\[
p\in[1,2)
\]
and define
\[
\alpha_k^L
=
\frac1p
\frac{g_{k-1}^{\mathsf T}Ag_{k-1}}
{g_{k-1}^{\mathsf T}g_{k-1}},
\qquad
g_{k+1}
=
\left(I-(\alpha_k^L)^{-1}A\right)g_k.
\]

Every such LEFT step obeys the sharp bounds
\[
\frac{\|g_{k+1}\|^2}{\|g_k\|^2}
\le
(p\kappa-1)^2
\]
and
\[
\frac{f(x_{k+1})-f(x_\star)}
{f(x_k)-f(x_\star)}
\le
(p\kappa-1)^2.
\]

The same constant is the supremum even if the state before the LEFT step must be produced by one exact steepest-descent warm-up. Hence the exact universal stepwise-monotonicity frontier is
\[
p\kappa\le2.
\]

Equivalently,
\[
\kappa\le\frac2p.
\]
When
\[
p\kappa>2,
\]
there are two-dimensional strictly convex quadratics and ordinary exact-line-search warm-ups for which the very next LEFT step increases both the gradient norm and the objective gap.

This creates a finite-horizon tradeoff with the source's local stability analysis. The paper reports a stable positive equilibrium for much of the regime
\[
p\in[1.5,2)
\]
and describes that regime as having stable gradient-norm behavior. The sharp transient result shows that this does not provide a global monotonicity guarantee from the first LEFT step. Throughout
\[
p\in[1.5,2),
\]
universal one-step monotonicity requires
\[
\kappa\le\frac2p\le\frac43.
\]

## Assumptions and scope

The statement concerns the fixed-\(p\) LEFT variant introduced in the source's two-dimensional convergence and stability analysis, not the original angle-dependent rule
\[
p_k=1+\sin\theta_k.
\]

The quadratic is finite-dimensional and strictly convex. The upper bound is dimension independent. Sharpness already occurs in two dimensions.

The objective-gap statement uses
\[
f(x)-f(x_\star)
=
\frac12g^{\mathsf T}A^{-1}g.
\]

The sharpness construction uses one exact steepest-descent warm-up only to certify that the near-worst pair of consecutive gradients is algorithmically compatible. The upper bound itself holds at every fixed-\(p\) LEFT step.

The result is a transient statement. It does not contradict eventual or \(R\)-linear convergence of the fixed-\(p\) method after nonmonotone steps.

## Proof

Set
\[
r_{k-1}
=
\frac{g_{k-1}^{\mathsf T}Ag_{k-1}}
{g_{k-1}^{\mathsf T}g_{k-1}}.
\]
The Rayleigh quotient bounds give
\[
\mu\le r_{k-1}\le L.
\]
The actual gradient step length is
\[
h_k
=
(\alpha_k^L)^{-1}
=
\frac p{r_{k-1}},
\]
so
\[
\frac pL
\le
h_k
\le
\frac p\mu.
\]

For every eigenvalue
\[
\lambda_i\in[\mu,L],
\]
the modal multiplier is
\[
1-h_k\lambda_i.
\]
The product
\[
h_k\lambda_i
\]
lies in
\[
\left[\frac p\kappa,p\kappa\right].
\]
For
\[
p\ge1,\qquad \kappa\ge1,
\]
both endpoint deviations are bounded by
\[
p\kappa-1.
\]
Indeed,
\[
\left|1-\frac p\kappa\right|
\le
p\kappa-1,
\]
and
\[
|1-p\kappa|
=
p\kappa-1.
\]
Therefore
\[
\|I-h_kA\|_2
\le
p\kappa-1.
\]
Since
\[
g_{k+1}=(I-h_kA)g_k,
\]
this gives
\[
\|g_{k+1}\|^2
\le
(p\kappa-1)^2\|g_k\|^2.
\]

For the objective gap, diagonalize \(A\). Because \(A^{-1}\) commutes with \(I-h_kA\),
\[
f(x_{k+1})-f(x_\star)
=
\frac12
\sum_i
\frac{(1-h_k\lambda_i)^2}{\lambda_i}
(g_k^{(i)})^2.
\]
This is at most
\[
(p\kappa-1)^2
\left(
\frac12
\sum_i
\frac{(g_k^{(i)})^2}{\lambda_i}
\right),
\]
which proves the objective bound.

It remains to prove sharpness under an actual warm-up. Scale
\[
\mu=1
\]
and set
\[
A=\operatorname{diag}(\kappa,1),
\qquad
g_0=
(\sqrt{\varepsilon},1)^{\mathsf T},
\qquad
\varepsilon>0.
\]
The exact steepest-descent step length is
\[
\tau_0
=
\frac{g_0^{\mathsf T}g_0}
{g_0^{\mathsf T}Ag_0}
=
\frac{1+\varepsilon}{1+\kappa\varepsilon}.
\]
Thus
\[
g_1
=
(I-\tau_0A)g_0
=
\frac{\kappa-1}{1+\kappa\varepsilon}
\begin{pmatrix}
-\sqrt{\varepsilon}\\
\varepsilon
\end{pmatrix}.
\]
Hence the squared high-curvature to low-curvature component ratio of \(g_1\) is exactly
\[
\frac1{\varepsilon}.
\]

The first fixed-\(p\) LEFT scalar after this warm-up is computed from \(g_0\):
\[
\alpha_1^L
=
\frac1p
\frac{1+\kappa\varepsilon}
{1+\varepsilon}.
\]
Its step length is therefore
\[
h_1
=
p\frac{1+\varepsilon}
{1+\kappa\varepsilon}
\longrightarrow
p
\]
as
\[
\varepsilon\downarrow0.
\]
At the same time, \(g_1\) becomes concentrated in the \(\kappa\)-eigenspace. Consequently
\[
\frac{\|g_2\|^2}{\|g_1\|^2}
\longrightarrow
(1-p\kappa)^2
=
(p\kappa-1)^2
\]
and, because the same high-curvature component dominates the \(A^{-1}\)-weighted objective representation,
\[
\frac{f(x_2)-f(x_\star)}
{f(x_1)-f(x_\star)}
\longrightarrow
(p\kappa-1)^2.
\]
This proves sharpness.

Finally, because
\[
p\kappa\ge1,
\]
the sharp factor is at most one exactly when
\[
p\kappa\le2.
\]
If
\[
p\kappa>2,
\]
the sharp limit is strictly larger than one, so every sufficiently small positive \(\varepsilon\) produces a genuine increase in both quantities.

## Verification

The standalone script `artifacts/verify_left_transient.py` symbolically derives the exact warm-up gradients, both amplification ratios, and their common limit
\[
(p\kappa-1)^2.
\]
It also checks representative parameter values on both sides of the frontier.

The all-dimensional upper bound is analytic and follows from the spectral interval
\[
h_k\lambda_i\in[p/\kappa,p\kappa].
\]
The finite calculations are supporting checks, not an exhaustive proof.

## Relationship to prior work

The primary source introduces LEFT as a step longer than BB1, analyzes a fixed-\(p\) model with
\[
p\in(1,2),
\]
proves \(R\)-linear convergence on its quadratic model, and studies local equilibrium stability. It reports increasing stability as \(p\) moves toward \(2\), while also observing slower convergence and proposing spectral truncation because the LEFT scalar can fall below the Hessian spectrum.

Recent quadratic BB work proves \(R\)-linear convergence and develops Lyapunov laws for BB1, BB2, and fixed positive spectral-weight delayed Rayleigh rules. Those scalars remain Rayleigh quotients inside the Hessian spectral interval and do not cover the multiplicative extension
\[
\alpha^L=\frac1p\alpha^{BB1}
\]
with
\[
p>1.
\]

A closely related sharp result for ordinary BB interval steps establishes a \((\kappa-1)^2\) objective-amplification envelope and the frontier
\[
\kappa=2.
\]
The present statement is not a special case of that result because LEFT deliberately takes a step beyond the BB1 endpoint. Its sharp envelope becomes
\[
(p\kappa-1)^2,
\]
and its monotonicity frontier contracts to
\[
\kappa=\frac2p.
\]

Targeted searches using the primary identifier, fixed-\(p\) LEFT terminology, longer-than-BB1 steps, exact-line-search warm-ups, objective amplification, gradient-norm amplification, and the proposed
\[
p\kappa=2
\]
frontier did not locate this source-specific statement.

## Limitations

The theorem concerns the fixed-\(p\) analytical LEFT variant. The original source rule uses the data-dependent quantity
\[
p_k=1+\sin\theta_k,
\]
whose coupled transient envelope can be different.

The result gives a worst-case one-step factor and an exact monotonicity boundary. It does not give the optimal long-run rate of LEFT or contradict its eventual \(R\)-linear convergence.

Sharpness is a supremum approached by
\[
\varepsilon\downarrow0.
\]
At the boundary
\[
p\kappa=2,
\]
the universal factor is one, while the two-mode witness approaches rather than necessarily attains equality at a nonterminated state.

## References

1. X. Xu, *On Convergence and Stability of Two Extended BB-like Step Sizes*, arXiv:2506.12731v1, first public 15 June 2025; revised as arXiv:2506.12731v2.
2. S. Yang, Y.-x. Yuan, *Lyapunov Functions and \(R\)-Linear Convergence for Quadratic Barzilai--Borwein Dynamics*, arXiv:2609.12084v1, first public 10 September 2026.
3. S. Yang, Y.-x. Yuan, *\(R\)-Linear Convergence of Barzilai--Borwein Methods on Strictly Convex Quadratics via Closed-Cone Homogeneous Dynamics*, arXiv:2609.12100v1, first public 10 September 2026.
