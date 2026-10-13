# Exact noise-optimal weighting and the negative-feedback frontier for two-lag iterations

## Finding

For real \(a\), consider the two-lag fixed-point iteration with fresh additive noise
\[
X_n=a\bigl(pX_{n-1}+(1-p)X_{n-2}\bigr)+\xi_n,\qquad 0\le p\le1.
\]
The iteration is stable for some convex two-lag weighting if and only if \(-3<a<1\). For uniform weights \(p=1/2\), stability instead requires \(-2<a<1\). For every \(a\in(-3,1)\setminus\{0\}\), the unique stable convex weight minimizing stationary variance is
\[
p_*(a)=\frac{\sqrt{1-a}}{1+\sqrt{1-a}},\qquad
\operatorname{Var}_*(a)=\frac{\sigma^2}{(1-a)(2-\sqrt{1-a})^2}.
\]
At \(a=0\), all weights have variance \(\sigma^2\). For nonzero feedback the optimizer favors the older state for positive feedback and the newer state for negative feedback; at zero feedback all weights, including balanced averaging, tie. The variance cost of maximal negative stabilization has the sharp singularity
\[
\lim_{a\downarrow-3}\frac{(a+3)^2\operatorname{Var}_*(a)}{\sigma^2}=4.
\]

## Assumptions and scope

The coefficient \(a\in\mathbb R\) and weight \(p\in[0,1]\) are constant. Innovations \((\xi_n)_{n\in\mathbb Z}\) are independent, identically distributed, independent of the deterministic initialization when an initialization is used, centered, and have finite positive variance \(\sigma^2\). No Gaussianity is assumed. Stability means both characteristic roots are strictly inside the unit disk; equivalently, there is a unique mean-zero causal stationary solution with finite variance attracting any deterministic initial state in mean square when the same innovations are coupled. A noncausal stationary solution outside that stability region is not considered a stable fixed-point computation.

The precise claim concerns the real scalar eigenmode of a linear map, not an arbitrary jointly coupled or nonnormal matrix. Noise is injected **after** the weighted deterministic update, with the same variance at every weight. Changing the noise injection law or optimizing transient error defines a different problem.

## Proof

**1. Exact stability.** Put \(\phi_1=ap\) and \(\phi_2=a(1-p)\). The companion matrix is
\[
B=\begin{pmatrix}\phi_1&\phi_2\\1&0\end{pmatrix},
\]
with characteristic polynomial \(z^2-\phi_1z-\phi_2\). The real second-degree Schur/Jury test gives the necessary and sufficient strict conditions
\[
|\phi_2|<1,\qquad 1-\phi_1-\phi_2>0,\qquad1+\phi_1-\phi_2>0.
\]
Substitution yields \(|a|(1-p)<1\), \(a<1\), and \(1+a(2p-1)>0\).

For \(a\ge1\), the middle inequality fails. For \(a=-r\le-1\), with \(r\ge1\), the first and last inequalities imply respectively \(p>1-1/r\) and \(p<(1+1/r)/2\). A feasible interval exists exactly for \(r<3\) (at \(r=1\), strict \(0<p<1\)). For \(-1<a<1\), the uniform choice is stable. Therefore the union of all stable real \(a\) is exactly \((-3,1)\). Setting \(p=1/2\) instead gives \((-2,1)\). At \(a=-3\) the two weight bounds touch without attaining strict stability; for smaller \(a\) they are incompatible.

**2. Stationary variance.** For a stable pair, write \(\gamma_j=\mathbb E[X_nX_{n-j}]\) for stationary covariances. The Yule--Walker identities give
\[
\gamma_1=\frac{\phi_1\gamma_0}{1-\phi_2},\quad
\gamma_2=\phi_1\gamma_1+\phi_2\gamma_0,\quad
\gamma_0=\phi_1\gamma_1+\phi_2\gamma_2+\sigma^2.
\]
As \(|\phi_2|<1\) and the Schur factors are positive, elimination yields the exact strictly positive variance
\[
\frac{\gamma_0}{\sigma^2}=
\frac{1-\phi_2}{(1+\phi_2)((1-\phi_2)^2-\phi_1^2)}
=\frac{1-a+ap}{(1+a-ap)(1-a)(1-a+2ap)}.
\]
The same identities follow by summing the square-summable causal impulse response. All denominators here are strictly positive in the Schur region.

**3. Optimize over every stable weight.** Differentiating this rational formula in \(p\), the derivative has the same sign as
\[
Q_a(p)=ap^2-2ap+a+2p-1
\]
for nonzero \(a\); an explicit expression with a manifestly positive prefactor on the stable domain is
\[
\frac1{\sigma^2}\frac{\partial\gamma_0}{\partial p}
=\frac{2a^2Q_a(p)}{(1-a)(1+a-ap)^2(1-a+2ap)^2}.
\]
Let \(t=\sqrt{1-a}\in(0,2)\). The roots of \(Q_a\), if \(a\ne0\), are \(p_*=t/(1+t)\) and \(p_{\rm other}=t/(t-1)\). The latter is negative for \(0<t<1\), and greater than one for \(1<t<2\). Moreover \(Q_a(0)=a-1<0\) and \(Q_a(1)=1>0\). Consequently the variance strictly decreases until \(p_*\) and strictly increases afterward in the stable interval. The claimed minimum is unique provided \(p_*\) is stable.

At the proposed optimizer the AR coefficients simplify to \(\phi_1=t(1-t)\), \(\phi_2=1-t\). They satisfy
\[
|\phi_2|=|1-t|<1,\quad
1-\phi_1-\phi_2=t^2>0,\quad
1+\phi_1-\phi_2=t(2-t)>0.
\]
Thus \(p_*\) is feasible throughout the full possible interval \((-3,1)\). Substitution into the variance identity gives
\[
\frac{\operatorname{Var}_*}{\sigma^2}=\frac1{t^2(2-t)^2}.
\]
At \(a=0\) both autoregressive coefficients vanish and \(X_n=\xi_n\), so every weight is optimal, with no uniqueness assertion.

**4. Sharp boundary behavior.** As \(a\downarrow-3\), \(t=\sqrt{1-a}\uparrow2\) and \(2-t=(a+3)/(2+t)\). Hence
\[
\frac{(a+3)^2\operatorname{Var}_*}{\sigma^2}
=\frac{(2+t)^2}{t^2}\longrightarrow4.
\]
This divergence is intrinsic even for the optimal choice; no weight remains Schur-stable at the boundary.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to check 2,658 stationary covariance instances against all three Yule--Walker identities, including the analytic Schur test. It independently solves the discrete two-state Lyapunov equation for 801 stable random instances and evaluates the global optimality inequality over 997 parameters with 101 weights each. It also tests boundary behavior and the exact nonuniform example \(a=3/4\), where \(p_*=1/3\), \(\operatorname{Var}_*/\sigma^2=16/9\), and uniform weighting has greater variance. All reported checker tests passed. These finite computations support but do not substitute for the all-real analytic argument.

Install the standard computational dependencies from `requirements.txt`, then run `python verify.py`. No external data are needed.

## Relationship to prior work

Epperlein and Wirth study fixed-width, uniformly weighted moving-average iteration of linear maps, deriving sharp deterministic spectral stability regions. The present claim concerns *nonuniform two-lag convex weighting chosen to minimize the stationary error caused by fresh additive noise*, and gives a sharp extension of the real negative stability frontier. Classical AR(2) Schur tests and Yule--Walker covariance identities are used as established tools, not asserted as new. The contribution is their exact combination with the constrained weight optimization, complete feasible-feedback range, and sharp critical variance law.

Comparisons with published related work include an exact stochastic-delay law for randomized two-coordinate Gauss--Seidel (random stale-read distributions rather than fixed simultaneous two-lag mixtures), and classic AR(1) covariance transformations (single-lag covariance, rather than this constrained AR(2) optimizer). None of these inspected statements establishes the present three-part classification. The complete text of the 2026 moving-average source could not be inspected; its public abstract is the evidence for the scope comparison, which leaves a genuine originality risk.

## Limitations

This is a scalar linear and stationary mean-square theorem. It does not imply that optimized memory improves finite-time bias, worst-case transients, nonlinear optimization, or arbitrary nonnormal matrix iterations. A large variance near \(a=-3\) persists under the optimal memory weight. The main motivating preprint's full text remained inaccessible, so an unindexed equivalent constrained-noise analysis cannot be excluded. Correctness of the derivation does not establish independent originality verification.

## References

1. J. Epperlein and F. Wirth, *Moving-Average Iteration of Linear Maps* (first submitted 18 September 2026), arXiv:2609.21442, https://arxiv.org/abs/2609.21442 .
2. Classical second-order Schur/Jury stability criterion and Yule--Walker equations for autoregressive models. Background description: https://en.wikipedia.org/wiki/Autoregressive_model .
3. *Exact delay-distribution law for two-coordinate randomized Gauss--Seidel* (2026), published research record 9ae0040f2dac. This result concerns stochastic stale-read delays, not deterministic weighted-lag stationary-noise optimization.
