# Sharp observable-error threshold for inexact proximal trust-region Cauchy points

## Finding

A Type-1 approximate proximal step can use **any fixed relative error strictly below one**, measured against the **computed** step, while retaining the sharp sufficient-decrease guarantee and the resulting limiting stationarity theorem for the proximal trust-region method of Baraldi, Kouri, and Maia [1]. The source method specifies an inner tolerance below one half. The precise universal coefficient is
\[
\langle g,u-x\rangle+\phi(u)-\phi(x)
\le -\frac{1-\kappa}{r}\|u-x\|^2,
\qquad 0\le\kappa<1.
\]
For each admissible tolerance the coefficient is attained on a one-dimensional smooth example. A uniform positive coefficient fails at the endpoint, and an admissible ascent step exists above it.

## Assumptions and scope

Let \(X\) be a real Hilbert space and let \(\phi:X\to(-\infty,+\infty]\) be proper, lower-semicontinuous, and convex. Fix \(x\in\operatorname{dom}\phi\), \(g\in X\), and \(r>0\). Define
\[
 z=x-rg,\quad H(w)=\phi(w)+\frac{1}{2r}\|w-z\|^2,\quad
 p=\operatorname{argmin}_{w\in X}H(w).
\]
A point \(u\) is a Type-1 approximation with precision \(\varepsilon\ge0\) if
\[
 H(u)-H(p)\le\frac{\varepsilon^2}{2r}.
\]
This is equivalent to the Type-1 approximate-subdifferential condition of [1, Definition 4]. The observable relative stopping criterion is \(\varepsilon\le\kappa\|u-x\|\), where \(\kappa\ge0\); it uses no unavailable exact proximal step. Set
\[
 s=u-x,\qquad Q=\langle g,s\rangle+\phi(u)-\phi(x).
\]
The first claim applies to every such choice of \(X,\phi,x,g,r,u,\varepsilon\), with the value \(Q\) defined whenever \(H(u)<\infty\).

The algorithmic consequence concerns the **modified tolerance** in [1, Algorithm 2], not a claim that the printed algorithm already permits the larger interval. Fix \(0<\kappa<1\) and a geometric precision reduction factor \(0<\beta<1\). At each nonterminal iteration suppose \(p_k\ne x_k\), and use an inexact Type-1 proximal point at some \(r_k\in[r_{\min},r_{\max}]\) with \(0<r_{\min}\le r_{\max}<\infty\). Let \(g_k\) be the model gradient, let \(B_k\) be the bounded self-adjoint model curvature, and let the trust-region radius be \(\Delta_k>0\). The trial point is the minimizer along the segment from \(x_k\) toward \(u_k\) of the scalar quadratic model described in [1, Section 3.1]. The outer assumptions are exactly the problem-data assumptions [1, Assumption 2.1], inexact-value, gradient and stationarity-metric bounds [1, Assumption 3.1], and
\[
 \sum_{k\ge1}\frac{1}{1+\max_{1\le j\le k}\|B_j\|}=+\infty.
\]
In particular, [1, Assumption 3.1] fixes a reference proximal length \(r_0>0\), bounds computed-objective reduction errors with exponent greater than one, requires \(\|g_k-\nabla f(x_k)\|\le\kappa_{\mathrm{grad}}\min\{\psi_k(r_0),\Delta_k\}\), and bounds the reference residual approximation error by a vanishing tolerance \(\xi_k\to0\) raised to an exponent greater than one. The statement assumes the outer trust-region acceptance/update mechanism of [1, Algorithm 1]. At an exact proximal stationary point \(p_k=x_k\), the *positive-error* inner loop is not asserted to terminate: such a case is instead terminal or handled separately.

## Proof

**Sharp universal descent.** Strong convexity of \(H\) with modulus \(1/r\) and optimality of \(p\) give
\[
 H(x)-H(p)\ge\frac{\|p-x\|^2}{2r},\qquad
 \|u-p\|^2\le2r[H(u)-H(p)]\le\varepsilon^2.
\]
Since \(H(u)-H(x)=Q+\|u-x\|^2/(2r)\), the approximate-minimum inequality yields
\[
 2rQ\le-\|s\|^2-\|p-x\|^2+\varepsilon^2.
\]
If \(0\le\kappa<1\), the triangle inequality and observable stopping test imply
\[
 \|p-x\|\ge\|s\|-\|u-p\|
 \ge(1-\kappa)\|s\|,\qquad
 \varepsilon\le\kappa\|s\|.
\]
Consequently
\[
 2rQ\le-[1+(1-\kappa)^2-\kappa^2]\|s\|^2
 =-2(1-\kappa)\|s\|^2.
\]
The conclusion includes zero steps, where the test forces zero accuracy and \(Q=0\).

**Equality and sharp boundary.** Set \(X=\mathbb R\), \(\phi=0\), \(x=0\), \(r=1\), and for any \(0\le\kappa<1\) choose \(g=-(1-\kappa)\), \(p=1-\kappa\), \(u=1\), \(\varepsilon=\kappa\). Then \(H(u)-H(p)=\kappa^2/2\), \(\varepsilon=\kappa\|u-x\|\), and \(Q=-(1-\kappa)\), attaining equality. The example is compatible with smooth, bounded-below fidelity \(f(t)=t^2/2-(1-\kappa)t\). At \(\kappa=1\), take any \(0<\delta<1\), choose \(g=-\delta\), \(p=\delta\), \(u=1\), \(\varepsilon=1-\delta\); the admissible ratio \(-Q/\|s\|^2=\delta\) tends to zero. For every \(\kappa>1\), set \(g=\kappa-1\), \(p=1-\kappa\), \(u=1\), \(\varepsilon=\kappa\): then \(H(u)-H(p)=\kappa^2/2\), the same relative test holds at equality, and \(Q=\kappa-1>0\). Thus no uniformly positive coefficient is possible at or above one, and above one a permitted step can increase the affine model.

**Inner-loop termination and Cauchy fraction.** At a nonstationary \(p_k\ne x_k\), the Type-1 bound gives \(\|u_k^{(\ell)}-p_k\|\le\varepsilon_k^{(\ell)}\). Hence
\[
 \|u_k^{(\ell)}-x_k\|\ge\|p_k-x_k\|-\varepsilon_k^{(\ell)}.
\]
For any fixed \(0<\kappa<1\), the geometric precision sequence eventually obeys \(\varepsilon_k^{(\ell)}\le\kappa\|p_k-x_k\|/(1+\kappa)\), sufficient for the *observable* stopping test. This reproduces [1, Proposition 11] without the source's smaller tolerance restriction. The proved descent bound gives [1, Equation (29)] with the uniform constant \(\kappa_{\mathrm{desc}}=1-\kappa>0\). By convexity of \(\phi\), the line-model decrease is bounded below by \(-\alpha Q_k-\alpha^2\langle B_ks_k,s_k\rangle/2\) for feasible \(\alpha\), exactly the setting of the three curvature cases in [1, Theorem 12]. Minimizing that scalar quadratic on the permitted segment yields its proved fraction-of-Cauchy-decrease bound with constants
\[
 \kappa_{\mathrm{rad}}=1,\qquad
 \kappa_{\mathrm{fcd}}=\frac{1-\kappa}{2}\min\{1-\kappa,r_{\min}\}>0.
\]
The curvature operator may be indefinite; the proof of [1, Theorem 12] treats positive, zero, and negative directional curvature. No extra convexity of the smooth fidelity is assumed.

**Limiting stationarity without an exact-step error test.** Let
\[
 \Psi_k=\frac{\|u_k-x_k\|}{r_k},\quad
 \bar\Psi_k=\frac{\|p_k-x_k\|}{r_k},\quad
 \bar\psi_k(t)=\frac{\|\operatorname{Prox}_{t\phi}(x_k-tg_k)-x_k\|}{t}.
\]
The fraction-of-Cauchy-decrease guarantee plus the outer assumptions permit [1, Theorem 10, first assertion], which establishes \(\liminf_k\Psi_k=0\). At each index, the triangle inequality and Type-1 gap give the **observable-to-exact comparison**
\[
 \bar\Psi_k\le\Psi_k+\frac{\varepsilon_k}{r_k}
 \le(1+\kappa)\Psi_k.
\]
This differs from [1, Equation (25)], which imposes accuracy relative to the unknown exact step. Along an infinite subsequence where \(\Psi_k\to0\), the true model-gradient residual \(\bar\Psi_k\to0\). The monotonic proximal-length inequalities in [1, Lemma 2] and the uniform bound \(r_k\le r_{\max}\) yield
\[
 \bar\psi_k(r_0)\le\max\{1,r_{\max}/r_0\}\bar\Psi_k\to0
\]
along that same subsequence. The reference-stationarity error in [1, Assumption 3.1(23)] is bounded above by a fixed multiple of \(\xi_k^{\zeta_{\mathrm{stat}}}\), so it tends to zero and gives \(\psi_k(r_0)\to0\) along the subsequence. Assumption 3.1(22), with the nonexpansivity of the proximity operator, now gives
\[
 \frac{\|\operatorname{Prox}_{r_0\phi}(x_k-r_0\nabla f(x_k))-x_k\|}{r_0}
 \le\kappa_{\mathrm{grad}}\psi_k(r_0)+\bar\psi_k(r_0)\to0.
\]
Applying [1, Lemma 2] once more compares any fixed \(r>0\) with \(r_0\) by a finite factor, giving the claimed \(\liminf\) stationarity statement for every \(r>0\). This is the same subsequence for every fixed \(r\), but not an assertion that the entire sequence converges.

## Verification

The optional standalone checker `verify.py` uses exact rational arithmetic to validate the scalar equalities for eight representative tolerance values, including the limiting boundary and an ascent witness. The universal inequality and the global consequence rest on the analytic derivation above and the stated, fully identified lemmas/theorems of [1], not on finite numerical tests. A direct reconstruction checks all signs and norms of the one-dimensional witnesses. Running `python verify.py` prints `VERIFY_OK` only after every exact check passes.

## Relationship to prior work

Baraldi, Kouri, and Maia [1] define Type-1 inexact proximity operators and prove the trust-region convergence framework. Their Algorithm 2 fixes \(0<\kappa<1/2\); Proposition 11 yields the weaker (not sharp) one-step coefficient \((1-\kappa^2)/2\), and Theorem 10's stationarity clause asks for accuracy relative to the exact step. This finding changes the *admissible observable inner tolerance and its stationarity justification*, not the outer trust-region mechanism. Their earlier inexact weighted method [2] uses a different \(\delta\)-Fréchet error criterion and does not state this Type-1 sharp bound or the enlarged observable tolerance theorem. Barré, Taylor, and Bach [3] develop general performance-estimation methods for inexact proximal algorithms but do not supply this trust-region sufficient-decrease-to-stationarity statement. The proximal subproblem solvers of Baraldi and Kouri [4] target fraction-of-Cauchy decrease with exact proximal subproblems, not this Type-1 relative-error boundary.

## Limitations

The descent threshold concerns **all Type-1 approximate points** under the specified observable relative test, not all possible notions of inexactness. At or above the endpoint, the examples disprove a *uniform* FCD certificate from this information; they do not prove every particular implementation diverges. The global conclusion is **limit-inferior stationarity**, conditional on the full outer convergence hypotheses and on nonterminal inner steps being computed, not convergence to a minimizer, full-sequence convergence, or a rate bound. At \(p_k=x_k\), positive-error geometric refinement cannot be guaranteed to stop and must be handled by a separate terminal procedure. An updated or unindexed equivalent publication may affect priority.

## References

[1] R. J. Baraldi, D. P. Kouri, L. F. Maia, *Convergence Analysis of an Inexact Proximal Trust-Region Method*, arXiv:2609.26747v1 (first public posting 2026-09-22), Sections 2.2 and 3.1, Definition 4, Lemmas 1, 2, 6, 9, Proposition 11, Theorems 10 and 12. https://arxiv.org/html/2609.26747v1

[2] L. F. Maia, R. Baraldi, D. P. Kouri, *An Inexact Weighted Proximal Trust-Region Method*, arXiv:2601.09024v1 (2026). https://arxiv.org/pdf/2601.09024

[3] M. Barré, A. B. Taylor, F. Bach, *Principled Analyses and Design of First-Order Methods with Inexact Proximal Operators*, arXiv:2006.06041v3 (2021 revision). https://arxiv.org/pdf/2006.06041

[4] R. J. Baraldi, D. P. Kouri, *Efficient Proximal Subproblem Solvers for a Nonsmooth Trust-Region Method*, open-access manuscript, 2023. https://optimization-online.org/wp-content/uploads/2023/11/main.pdf
