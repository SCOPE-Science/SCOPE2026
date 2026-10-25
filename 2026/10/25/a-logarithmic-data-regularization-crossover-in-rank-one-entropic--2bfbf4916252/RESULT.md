# A logarithmic data–regularization crossover in rank-one entropic least squares

## Finding

The following theorem gives the exact vanishing-signal crossover scale and coordinatewise decay exponents in unnormalized entropic least squares with one positive measurement.

**Theorem.** Fix an integer \(d\ge2\), positive coefficients \(a_i\) and strictly positive reference weights \(q_i\), for \(1\le i\le d\). For \(\lambda>0\) and a nonnegative datum \(b\), let \(x^*(\lambda,b)\) be the unique minimizer of
\[
J_{\lambda,b}(x)=\frac{1}{2\lambda}\left(\sum_{i=1}^{d}a_i x_i-b\right)^2+\sum_{i=1}^{d}x_i\log\left(\frac{x_i}{q_i}\right),\qquad x\in[0,\infty)^d,
\]
using \(0\log0=0\). Set \(\alpha=\min_i a_i\), \(c_i=q_i/e\), \(p_i=a_i/\alpha\), \(C=\alpha\sum_{a_i=\alpha}c_i\), \(B=\alpha C\), and \(L_\lambda=\log(1/\lambda)\). Let \(b_\lambda\ge0\) tend to zero as \(\lambda\downarrow0\).

**Crossover regime.** If \(b_\lambda/(\lambda L_\lambda)\to\beta\in[0,\infty)\), then, for each coordinate,
\[
x_i^*(\lambda,b_\lambda)\sim c_i\left[\frac{(\beta+1/\alpha)\lambda L_\lambda}{C}\right]^{p_i}.
\]

**Data-dominated regime.** If \(b_\lambda/(\lambda L_\lambda)\to\infty\), still with \(b_\lambda\to0\), then
\[
x_i^*(\lambda,b_\lambda)\sim c_i\left(\frac{b_\lambda}{C}\right)^{p_i}.
\]

**Zero-signal refinement.** When \(b_\lambda=0\), write \(w_\lambda=W(B/\lambda)\), where \(W\) is the principal nonnegative Lambert function. If at least one \(a_i>\alpha\), put \(\delta=\min_{a_i>\alpha}(p_i-1)>0\). Then
\[
x_i^*(\lambda,0)=c_i\left(\frac{\lambda w_\lambda}{B}\right)^{p_i}\left[1+O\big(e^{-\delta w_\lambda}\big)\right].
\]
The constants implicit in the error may depend on the fixed coefficients and weights. When all coefficients are equal, this Lambert expression is **exact** without an error term. In every regime, the normalized shape converges:
\[
\frac{x_i^*(\lambda,b_\lambda)}{\sum_jx_j^*(\lambda,b_\lambda)}\longrightarrow
\begin{cases}
q_i/\sum_{a_j=\alpha}q_j,&a_i=\alpha,\\
0,&a_i>\alpha.
\end{cases}
\]
At zero signal, each minimum-coefficient coordinate satisfies \(x_i^*(\lambda,0)/\lambda\to\infty\); consequently the solution path has no Lipschitz extension in \(\lambda\) at \(\lambda=0\), although it extends continuously by zero. These are asymptotics for fixed dimension and fixed positive coefficients; no uniformity in changing coefficients is asserted.

## Assumptions and scope

The objective is the **variable-mass** unnormalized entropy \(\sum_i x_i\log(x_i/q_i)\), without the extra entropy linear terms used in some other normalizations. The data and regularization parameter vanish together, the single forward row has strictly positive entries, and the reference weights are fixed and strictly positive. No total-mass constraint is imposed. The asymptotic symbol \(\sim\) means that the ratio tends to one, coordinate by coordinate. There is no assertion concerning negative or nonvanishing data, zero or varying forward coefficients, multiple measurements, or changing dimension.

## Proof

**Positive unique minimizer and scalar equation.** Each entropy summand is continuous at zero, strictly convex on its nonnegative domain, and superlinear at infinity. Hence the objective has a unique minimizer. Its one-sided derivative at a zero coordinate is \(-\infty\), whereas the quadratic derivative there is finite. Thus each coordinate is positive. Setting the derivative of the objective to zero gives
\[
\log(x_i/q_i)+1+\frac{a_i}{\lambda}\left(\sum_j a_jx_j-b\right)=0.
\]
Define \(t=(\sum_j a_jx_j-b)/\lambda\). With \(c_i=q_i/e\), these equations are equivalent to
\[
x_i=c_i e^{-a_i t},\qquad F(t)=b+\lambda t,
\qquad F(t):=\sum_i a_ic_i e^{-a_it}.
\]
The function \(F(t)-\lambda t-b\) is strictly decreasing from \(+\infty\) to \(-\infty\), so its real zero is unique. For \(b_\lambda\to0\), eventually \(b_\lambda<F(0)\), hence \(t>0\). Since \(b_\lambda+\lambda t=F(t)\), the root tends to infinity: otherwise a bounded subsequence would have a positive lower bound on \(F\), contradicting \(b_\lambda\to0\) and the upper bound on \(\lambda t\) established below.

**Uniform logarithmic upper bound.** Put \(M=\sum_i a_ic_i\). For \(t\ge0\), \(F(t)\le M e^{-\alpha t}\). Hence \(\lambda t\le M e^{-\alpha t}\), which implies \(\alpha t\,e^{\alpha t}\le\alpha M/\lambda\) and therefore
\[
0<t\le\frac{1}{\alpha}W(\alpha M/\lambda)=O(L_\lambda).
\]
In particular \(\lambda t\to0\), verifying the claimed divergence of \(t\) as the datum tends to zero.

**The leading exponential.** Grouping minimum-coefficient terms gives
\[
F(t)=C e^{-\alpha t}\left(1+R(t)\right),\qquad
R(t)=\frac{\sum_{a_i>\alpha}a_ic_i e^{-(a_i-\alpha)t}}{C}.
\]
Here \(R(t)\to0\) as \(t\to\infty\); if every coefficient is minimal, \(R\equiv0\).

**Bounded crossover ratio.** Suppose \(b_\lambda/(\lambda L_\lambda)\to\beta<\infty\). The upper bound on \(t\) gives \(F(t)=b_\lambda+\lambda t=O(\lambda L_\lambda)\). Since \(F(t)\ge C e^{-\alpha t}\), we infer
\[
t\ge\frac{L_\lambda-\log L_\lambda-O(1)}{\alpha}.
\]
Together with the upper bound, this proves \(t/L_\lambda\to1/\alpha\). Therefore
\[
F(t)=b_\lambda+\lambda t\sim(\beta+1/\alpha)\lambda L_\lambda,
\quad e^{-\alpha t}\sim\frac{(\beta+1/\alpha)\lambda L_\lambda}{C}.
\]
Substitute \(x_i=c_i(e^{-\alpha t})^{p_i}\), proving the crossover formula.

**Dominant datum.** Suppose \(b_\lambda/(\lambda L_\lambda)\to\infty\). Because \(t=O(L_\lambda)\), we have \(\lambda t=o(b_\lambda)\). Thus \(F(t)\sim b_\lambda\), so \(e^{-\alpha t}\sim b_\lambda/C\), yielding the claimed coordinatewise law.

**Lambert refinement.** For \(b=0\), set \(z=\alpha t\). The scalar equation becomes
\[
z e^z=\frac{B}{\lambda}(1+R(z/\alpha)).
\]
Writing \(w=W(B/\lambda)\), monotonicity gives \(z\ge w\). Moreover
\[
0\le z-w\le\log\big(1+R(z/\alpha)\big).
\]
If the nonminimal set is nonempty, \(R(z/\alpha)=O(e^{-\delta z})=O(e^{-\delta w})\), so \(e^{-p_i(z-w)}=1+O(e^{-\delta w})\), for each fixed \(i\). Finally \(e^{-w}=\lambda w/B\), proving the refinement. If there are no nonminimal coefficients, \(R=0\) and \(z=w\) exactly.

**Shape and boundary regularity.** As \(t\to\infty\), only terms with \(a_i=\alpha\) survive in the shape ratio, and their relative weights are \(c_i/\sum_{a_j=\alpha}c_j\). For \(b=0\), any minimum-coefficient coordinate has \(x_i=c_i e^{-z}\sim c_i\lambda w/B\). Since \(w\to\infty\), the ratio \(x_i/\lambda\) diverges. The minimizer approaches zero and hence has a continuous extension, but this ratio rules out a Lipschitz extension at zero.

## Verification

`CHECK.py` uses 90-digit arithmetic, a 440-step monotone bisection of the exact scalar optimality equation, and direct recomputation of all KKT residuals. `CHECK_OUTPUT.txt` records 39 tests covering heterogeneous forward coefficients, tied minimum coefficients, all-equal coefficients, finite-ratio crossovers, data-dominant signals, and zero signal at three decreasing regularization scales. Every checked residual is below \(10^{-70}\); the reported asymptotic relative errors decrease in the expected small-parameter regimes (with nonuniform transient behavior permitted). These finite numerical checks support, but do not replace, the analytic proof.

For example, with \(a=(1,2)\) and \(q=(e,e)\), the scalar condition is \(e^{-t}+2e^{-2t}=b+\lambda t\). At zero signal, \(x_1\sim\lambda W(1/\lambda)\) and \(x_2\sim[\lambda W(1/\lambda)]^2\). At the crossover \(b=\lambda\log(1/\lambda)\), \(x_1\sim2\lambda\log(1/\lambda)\) and \(x_2\sim4[\lambda\log(1/\lambda)]^2\). These follow directly from the theorem.

## Relationship to prior work

Barnfield, Burke, Friedlander, and Hoheisel (2026) introduce the variable-mass scale-shape formulation and give primal-dual equations and Lambert-function bounds, as well as perturbation estimates for strictly positive regularization. Their Theorem 6.3 addresses a **fixed-mass** simplex-constrained limit; it does not state the present simultaneous vanishing-data, variable-mass crossover or individual coordinate exponents. The KKT reduction here is classical and not asserted to be new. Chuna and collaborators (2025) study the dual maximum-entropy reconstruction problem and noiseless limits in physical applications, without a matching one-row signal-versus-regularization crossover in the inspected texts. The claimed new result is specifically the combined \(\lambda\log(1/\lambda)\) crossover, coefficient-ratio hierarchy, and quantitative zero-data boundary law.

## Limitations

This is a rank-one positive-forward-model theorem, not a generic inverse-problem rate or multi-measurement theorem. The regularizer lacks the linear offset that would make its minimum occur at \(x=q\). Its mass tends to zero, whereas fixed-mass variants can have completely different endpoints. All asymptotics are pointwise for fixed finite coefficients and priors. A mathematically equivalent older special-case calculation may exist under entropy duality or exponential-family terminology. Independent validation has not been performed.

## References

1. N. Barnfield, J. V. Burke, M. P. Friedlander, and T. Hoheisel, *A Scale-Shape Dual Newton Method for Entropic Least Squares*, arXiv:2604.27154v1 (2026), https://arxiv.org/abs/2604.27154 . Equations (1.1), (1.5), and Section 6.
2. T. Chuna et al., *The noiseless limit and improved-prior limit of the maximum entropy method and their implications for the analytic continuation problem*, arXiv:2511.06915v1 (2025), https://arxiv.org/abs/2511.06915 .
3. T. Chuna et al., *Dual formulation of the maximum entropy method applied to analytic continuation of quantum Monte Carlo data*, arXiv:2501.01869 (2025), https://arxiv.org/abs/2501.01869 .
