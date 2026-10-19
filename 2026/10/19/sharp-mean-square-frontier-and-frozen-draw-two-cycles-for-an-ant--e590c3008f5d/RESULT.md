# Sharp mean-square frontier and frozen-draw two-cycles for an antithetic sampled Hamilton–Jacobi proximal

## Finding

For a one-dimensional strongly convex quadratic, the two-point **antithetic** finite-sample Hamilton–Jacobi proximal estimator has an exact, temperature-independent mean-square stability threshold. Let \(f(y)=\kappa y^2/2\), with \(\kappa,t,\delta>0\), and put \(c=\kappa t\), \(a=\sqrt{\delta t}\). From one standard Gaussian \(Z\), evaluate the normalized exponential-weight estimator at the paired proposals \(x+aZ\) and \(x-aZ\). It reduces exactly to
\[
T_Z(x)=x-aZ\tanh(cZx/a).
\]
Then, for every nonzero \(x\), strict one-step conditional mean-square descent \(\mathbb E[T_Z(x)^2]<x^2\) holds **if and only if** \(0<c\le 2/3\). At the endpoint \(c=2/3\), despite the neutral linearized second moment, the sharp local quartic correction is strictly negative:
\[
\mathbb E[T_Z(x)^2]=x^2-\frac{112}{81\delta t}x^4+O\!\left(x^6/(\delta t)^2\right).
\]
With fresh independent Gaussian pairs each iteration, \(x_{k+1}=T_{Z_k}(x_k)\) converges to zero almost surely from every deterministic initial point when \(0<c\le2/3\).

A contrasting phenomenon occurs when the same Gaussian draw is frozen and reused at every step. Conditional on any \(z\ne0\), if \(cz^2\le2\) all iterates converge to zero; if \(cz^2>2\), zero is unstable and the map has a locally attracting symmetric nonzero two-cycle. For one initially sampled Gaussian, the probability of this latter event is exactly
\[
\Pr(cZ^2>2)=\operatorname{erfc}(1/\sqrt c)>0
\]
for **every** \(c>0\), including the range where independent resampling converges almost surely.

These statements concern one finite-sample estimator and two precisely specified draw-reuse policies, not the error-free Gaussian integral operator or a general independent-proposal Monte Carlo implementation.

## Assumptions and scope

All computations are in exact real arithmetic. Fix arbitrary \(\kappa,t,\delta>0\), with \(a^2=\delta t\) and dimensionless curvature-step product \(c=\kappa t\). For each input \(x\in\mathbb R\), sample \(Z\sim N(0,1)\), set \(Y_\pm=x\pm aZ\) and \(w_\pm=\exp[-f(Y_\pm)/\delta]\), and define the **two-point antithetic Gibbs-averaged estimator**
\[
T_Z(x)=\frac{Y_+w_++Y_-w_-}{w_++w_-}.
\]
The two proposals have the correct Gaussian marginal law, but they are perfectly negatively correlated; this is a sampling **variant**, not two i.i.d. draws. The expectation \(\mathbb E\) in the one-step assertion is over this single standard Gaussian. The fresh-draw chain uses independent \(Z_k\) across iterations, while the frozen-draw iteration fixes one \(z\) for all iterations.

The infinite-sample population operator is
\[
P(x)=\frac{\mathbb E[Y\exp(-f(Y)/\delta)]}{\mathbb E[\exp(-f(Y)/\delta)]}=\frac{x}{1+c},\qquad Y\sim N(x,a^2),
\]
because completing the square gives a Gaussian mean of \(x/(1+c)\). Thus any instability described here is due to the two-point sampling-and-reuse rule, not the exact proximal operator.

## Proof

**Step 1: exact two-sample map.** Since
\[
\frac{w_+}{w_-}=\exp\!\left[-\frac{f(x+aZ)-f(x-aZ)}{\delta}\right]=\exp(-2cZx/a),
\]
we have \((w_+-w_-)/(w_++w_-)=-\tanh(cZx/a)\). Substitution yields \(T_Z(x)=x-aZ\tanh(cZx/a)\). It is odd in \(x\), and \(T_Z(0)=0\) for every draw.

**Step 2: sharp global mean-square descent.** By symmetry it suffices to take \(x>0\). Write \(b=cx/a>0\), \(h(s)=\tanh(s)/s\) for \(s>0\), and set \(h(0)=1\). Elementary differentiation shows that \(h\) is strictly decreasing on \((0,\infty)\) and \(0<h(s)<1\). Define
\[
\mu_b=\mathbb E[Z\tanh(bZ)]=b\,\mathbb E[Z^2h(b|Z|)],
\quad \nu_b=\mathbb E[Z^2\tanh^2(bZ)]=b^2\,\mathbb E[Z^4h(b|Z|)^2].
\]
Under \(dQ=Z^2\,dP\), \(Q\) is a probability measure and \(\mathbb E_Q[Z^2]=\mathbb E[Z^4]=3\); covariance monotonicity under \(Q\) gives
\[
\mathbb E[Z^4h(b|Z|)]=\mathbb E_Q[Z^2h(b|Z|)]\le3\mathbb E_Q[h(b|Z|)]=3\mathbb E[Z^2h(b|Z|)].
\]
Here strictness holds when \(b>0\). Since \(h^2<h\) for nonzero inputs,
\[
\nu_b < 3b^2\mathbb E[Z^2h(b|Z|)]=3b\mu_b.
\]
The exact conditional second-moment drift is
\[
\mathbb E[T_Z(x)^2]-x^2 = -2ax\mu_b+a^2\nu_b=a^2\bigl(-2b\mu_b/c+\nu_b\bigr) <a^2b\mu_b(3-2/c).
\]
Therefore it is strictly negative for every \(x\ne0\) whenever \(0<c\le2/3\).

For necessity, Taylor expansion at \(x=0\), using \(\mathbb E[Z^2]=1\), \(\mathbb E[Z^4]=3\) and \(\mathbb E[Z^6]=15\), yields
\[
\mathbb E[T_Z(x)^2]=(1-2c+3c^2)x^2+\frac{2c^3(1-5c)}{a^2}x^4+O(x^6/a^4).
\]
Gaussian moments justify termwise expansion via dominated Taylor remainder (all Gaussian moments exist; the derivatives of \(\tanh\) are bounded on the real axis). If \(c>2/3\), then \(1-2c+3c^2>1\), so sufficiently small nonzero inputs have positive mean-square drift. At \(c=2/3\), the displayed quartic coefficient is \(-112/(81a^2)\), proving the endpoint law.

**Step 3: fresh-draw almost-sure convergence.** For \(0<c\le2/3\), define \(q(x)=x^2-\mathbb E[T_Z(x)^2]\). Dominated convergence gives continuity, while Step 2 gives \(q(x)>0\) for all \(x\ne0\) and \(q(0)=0\). With independent draws \(Z_k\), the nonnegative process \(M_k=x_k^2\) is a supermartingale and
\[
\sum_{k\ge0}\mathbb E[q(x_k)]\le x_0^2.
\]
Therefore \(\sum_kq(x_k)<\infty\) almost surely and \(M_k\) converges almost surely to a finite limit \(M_\infty\). Were \(M_\infty>0\), then by symmetry and continuity \(q(x_k)=q(\sqrt{M_k})\to q(\sqrt{M_\infty})>0\), contradicting summability. Hence \(M_\infty=0\) and \(x_k\to0\) almost surely.

**Step 4: freezing the draw.** For fixed \(z\ne0\), put \(r=a|z|\), \(d=cz^2\) and \(v=x/r\). The normalized iteration is \(v\mapsto g_d(v)=v-\tanh(dv)\), independent of \(\delta\) and \(t\). For \(0<d\le2\) and \(v>0\), \(0<\tanh(dv)<2v\); by oddness \(|g_d(v)|<|v|\) for every nonzero \(v\). This gives global convergence to zero. For \(d>2\), \(g_d'(0)=1-d<-1\), so zero is linearly unstable. The ratio \(\tanh(dv)/v\) strictly decreases from \(d\) to zero as \(v\) increases from zero to infinity. Hence a unique \(v_*\in(0,1/2)\) satisfies \(\tanh(dv_*)=2v_*\); therefore \(g_d(v_*)=-v_*\) and \(g_d(-v_*)=v_*\). If \(s=dv_*>0\), the derivative at either cycle point is
\[
g_d'(v_*)=1-d\operatorname{sech}^2(s)=1-\frac{4s}{\sinh(2s)}\in(-1,1),
\]
using \(\sinh(2s)>2s\). Thus the two-step multiplier \([g_d'(v_*)]^2<1\), proving local attraction. Finally, a standard normal draw satisfies \(cz^2>2\) with probability \(2[1-\Phi(\sqrt{2/c})]=\operatorname{erfc}(1/\sqrt c)\).

## Verification

The accompanying `verify.py` performs 295 deterministic checks. It separately evaluates the original two-sample exponential-weight formula and the simplified hyperbolic expression; computes Gaussian expectations using 160-point Gauss–Hermite quadrature across both sides of the threshold; checks the second- and fourth-order coefficients and the strict tilted-moment inequality; and numerically finds the attracting cycles and their derivatives. Run with `python verify.py` using NumPy and SciPy. These finite checks are not an exhaustive proof; the arguments in Steps 1–4 supply the proof for all positive parameters.

## Relationship to prior work

Osher, Heaton, and Wu Fung (2023) introduced the Gaussian HJ-Prox sampling formula (arXiv:2211.12997). Di, Chi, and Wu Fung (2025, arXiv:2509.07914, Section 5) explicitly state that their splitting convergence theory treats exact integrals and does not incorporate finite Monte Carlo sampling errors. The full 2026 analysis of Naldi, Labarrière, Molinari, and Villa (arXiv:2605.11929, Theorem 7 and Section 4.2) addresses sampled zeroth-order proximal iteration with independent proposals and increasingly many samples satisfying a summability condition; that result neither covers a fixed, dependent antithetic pair nor determines the stated sharp \(2/3\) frontier or frozen-draw cycles. The 2026 expanded operator-splitting treatment (arXiv:2601.22370) could be evaluated from its publicly accessible abstract but not its complete text; any equivalent result in that inaccessible material remains an unresolved bibliographic risk rather than a demonstrated distinction.

The originality claim is restricted to this **combined antithetic two-sample stability/reuse classification**. It does not claim invention of the Gaussian proximal integral, antithetic sampling, Gaussian moment identities, or scalar period-doubling arguments.

## Limitations

Only the one-dimensional quadratic, exact exponential weighting, exactly two perfectly antithetic normal proposals and fixed positive parameters are considered. This result does not establish a sharp threshold for independent pairs, arbitrary sample sizes, general strongly convex objectives, higher dimensions, floating-point implementations, or compositions with other splitting maps. For \(c>2/3\), the conclusion is a **local mean-square one-step expansion**, not almost-sure divergence of the fresh-draw chain. For a frozen draw with \(d>2\), only existence and local attraction of the specified symmetric cycle are proved; a global basin classification is not asserted. Bibliographic novelty is subject to the explicitly identified inaccessible expanded 2026 source and possible unindexed equivalent calculations.

## References

1. S. Osher, H. Heaton, and S. Wu Fung, *A Hamilton–Jacobi-based Proximal Operator*, arXiv:2211.12997 (2023). https://arxiv.org/abs/2211.12997 .
2. N. Di, E. C. Chi, and S. Wu Fung, *A Monte Carlo Approach for Nonsmooth Convex Optimization via Proximal Splitting Algorithms*, arXiv:2509.07914 (first public version, 2025-09-09). https://arxiv.org/abs/2509.07914 .
3. E. Naldi, H. Labarrière, C. Molinari, and S. Villa, *Convergence of zeroth-order proximal point algorithms in the high-temperature regime*, arXiv:2605.11929 (2026). https://arxiv.org/abs/2605.11929 .
4. N. Di, E. C. Chi, and S. Wu Fung, *Operator Splitting with Hamilton-Jacobi-based Proximals*, arXiv:2601.22370 (2026; abstract inspected, full text inaccessible). https://arxiv.org/abs/2601.22370 .
