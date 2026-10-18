# A sharp cone-preservation phase diagram for the third-order exponential Rosenbrock Riccati step

## Finding

Consider the full-matrix third-order `exprb32` exponential Rosenbrock step applied to the differential Riccati equation
\[
\dot X=-2aX+Q-XGX,\qquad X(0)=0,
\]
where \(a\ge0\) and \(Q,G\in\mathbb R^{d\times d}\) are symmetric positive semidefinite. No commutativity of \(Q\) and \(G\) is assumed. Let \(S=Q^{1/2}GQ^{1/2}\), and let \(\mu=\lambda_{\max}(S)\) (with \(\mu=0\) when \(S=0\)). For a positive step \(h\), define
\[
\kappa_a(h)=2h^2\varphi_1(-2ah)\varphi_3(-2ah),\qquad
c_a(h)=h\varphi_1(-2ah).
\]
The **exact** next matrix is
\[
X_+(h)=c_a(h)Q^{1/2}\bigl(I-\kappa_a(h)S\bigr)Q^{1/2}.
\]
Consequently, \(X_+(h)\succeq0\) if and only if \(\mu\kappa_a(h)\le1\). Its positive, zero and negative eigenvalue counts on the range of \(Q\) are exactly the counts of \(1-\kappa_a(h)\mu_j\) of each sign, where \(\mu_j\) are the eigenvalues of \(S\) restricted to that range. Independently of any commutation assumptions, the entire phase diagram is:

- If \(\mu=0\), every positive step is positive semidefinite.
- If \(a=0\) and \(\mu>0\), the admissible steps are exactly \(0<h\le\sqrt{3/\mu}\).
- If \(a>0\) and \(\mu\le4a^2\), every finite positive step is positive semidefinite, and the result is strictly positive on \(\operatorname{ran}Q\).
- If \(a>0\) and \(\mu>4a^2\), there is a unique critical positive step \(h_*\) satisfying \(\mu\kappa_a(h_*)=1\); the next matrix is positive semidefinite exactly for \(0<h\le h_*\). At \(h_*\) its rank drops by the multiplicity of \(\mu\) on \(\operatorname{ran}Q\).

For fixed \(\mu>0\), the critical step tends to \(\sqrt{3/\mu}\) as \(a\downarrow0\), and diverges at the damping boundary according to
\[
h_*\sim\frac{1}{a(1-4a^2/\mu)}\quad\text{as }a\uparrow\sqrt{\mu}/2.
\]

A second, global statement is available for the undamped **scalar** Riccati equation \(x'=q-gx^2\), with \(q,g>0\). The exact `exprb32` one-step map sends **every** \(x\ge0\) to a nonnegative value if and only if
\[
\boxed{h\sqrt{qg}\le\sqrt3.}
\]
The threshold is attained at the boundary initial state \(x=0\): at equality the method has a spurious zero one-step fixed point, even though the exact solution from zero is strictly positive at every later time. For any larger step the method produces a negative value from zero.

## Assumptions and scope

For \(j\ge1\) the exponential-integrator functions are
\[
\varphi_j(z)=\int_0^1 e^{(1-\theta)z}\frac{\theta^{j-1}}{(j-1)!}\,d\theta.
\]
The full-matrix arithmetic uses exact action of these functions and **no** low-rank compression, approximate Lyapunov function evaluation, rounding or adaptive-step acceptance rule. The specific `exprb32` formula, as in Li, Li and Yang, equation (22), is
\[
U=X+h\varphi_1(hL_X)[F(X)],\qquad
X_+=U+2h\varphi_3(hL_X)[-(U-X)G(U-X)],
\]
where \(L_X(H)=(A-XG)H+H(A-XG)^T\) and \(A=-aI\). The first assertion concerns only a step **from the zero matrix**; the scalar assertion covers every nonnegative input with \(a=0\). The usual norm-error step accept/reject criterion is not a cone constraint.

## Proof

**Exact factorization.** At \(X=0\), \(F(0)=Q\), \(L_0(H)=-2aH\), and therefore \(U=c_a(h)Q\). The quadratic remainder is exactly \(-c_a(h)^2QGQ\), giving
\[
X_+=c_a(h)Q-2hc_a(h)^2\varphi_3(-2ah)QGQ
    =c_a(h)Q^{1/2}\bigl(I-\kappa_a(h)S\bigr)Q^{1/2}.
\]
Since \(c_a(h)>0\), Sylvester's inertia law on \(\operatorname{ran}Q\) proves the spectral sign classification. The kernel of \(Q\) is also in the kernel of \(X_+\); positivity holds exactly when the largest active eigenvalue satisfies \(\mu\kappa_a(h)\le1\). At a simple or multiple first crossing, the rank decreases by precisely the multiplicity of the maximal active eigenvalue.

**Monotonicity and damping transition.** Using the integral defining the \(\varphi\)-functions,
\[
 c_a(h)=\int_0^h e^{-2as}\,ds,\qquad
 h\varphi_3(-2ah)=\frac12\int_0^h e^{-2as}\left(1-\frac{s}{h}\right)^2 ds.
\]
Both integrals are positive and strictly increasing for \(h>0\); in the second integrand the factor \((1-s/h)^2\) increases with \(h\) for every fixed \(0<s<h\), and its integration domain expands. Therefore \(\kappa_a(h)=2c_a(h)[h\varphi_3(-2ah)]\) is continuous and strictly increasing from zero. If \(a=0\), \(\varphi_1(0)=1\) and \(\varphi_3(0)=1/6\), so \(\kappa_0(h)=h^2/3\). If \(a>0\), the limits of the two integrals are \(1/(2a)\) and \(1/(4a)\), whence \(\lim_{h\to\infty}\kappa_a(h)=1/(4a^2)\), never attained at finite \(h\). This gives the entire if-and-only-if diagram, uniqueness, and strictness at the borderline \(\mu=4a^2\).

For \(a>0\), putting \(z=2ah\) into the closed forms of \(\varphi_1\) and \(\varphi_3\) yields
\[
\kappa_a(h)=\frac{(1-e^{-z})(1-z+z^2/2-e^{-z})}{2a^2z^2}
=\frac{1}{4a^2}\left(1-\frac{1}{ah}+O((ah)^{-2})\right)
\]
for \(ah\to\infty\). Inverting the monotone critical equation yields the displayed asymptotic as \(a\uparrow\sqrt\mu/2\). Continuity in \(a\) at zero and uniqueness show \(h_*(a)\to\sqrt{3/\mu}\) as \(a\downarrow0\).

**All-state scalar assertion.** Rescale time and state by \(t=h\sqrt{qg}\) and \(y=x\sqrt{g/q}\). For the normalized equation \(y'=1-y^2\), define \(z=2ty\) and
\[
\Delta=t\varphi_1(-z)(1-y^2),\qquad
\mathcal E_t(y)=y+\Delta-2t\varphi_3(-z)\Delta^2.
\]
For \(0\le y\le1\), \(0\le\Delta\le t\), \(\varphi_3(-z)\le1/6\), and so
\[
\mathcal E_t(y)\ge y+\Delta(1-t^2/3)\ge0
\]
whenever \(t\le\sqrt3\). For \(y\ge1\), the increment is nonpositive and obeys
\[
|\Delta|\le\frac{y^2-1}{2y}<\frac y2,
\]
using \(t\varphi_1(-2ty)=(1-e^{-2ty})/(2y)\). Also, for \(z>0\), \(\varphi_3(-z)\le1/(2z)\); consequently \(y+\Delta\ge y/2\) and \(2t\varphi_3(-z)\Delta^2\le y/8\). Hence \(\mathcal E_t(y)\ge3y/8>0\), **without any restriction on \(t\)**. Finally \(\mathcal E_t(0)=t(1-t^2/3)\), which is zero at \(t=\sqrt3\) and strictly negative for larger steps. This supplies necessity, sufficiency for all nonnegative inputs, the boundary artifact, and an invariant nonnegative iteration when every step obeys the bound.

**Exact-flow contrast.** When \(Q\succeq0\) and \(G\succeq0\), the Riccati differential field is tangent to the positive cone and its exact trajectory from zero remains positive semidefinite. If \(Q\succ0\), its exact trajectory is positive definite for all positive times. One can see this from the variation-of-constants representation with \(M_X(t)=-aI-\tfrac12X(t)G\): \(\dot X=M_XX+XM_X^T+Q\), whence \(X(t)=\int_0^t\Phi(t,s)Q\Phi(t,s)^T\,ds\) for the invertible principal fundamental matrix \(\Phi\). In the normalized scalar case from zero, the exact solution is \(\tanh(t)>0\).

## Verification

Run `python verify.py` using Python 3 standard library; it prints the actual number of successful assertion checks. The program checks exact rational zero-damping updates for noncommuting \(2\times2\) coefficient matrices, normalized scalar sign boundaries, the Gram-inertia equivalence on random positive-definite noncommuting matrices, monotonicity and uniqueness of the critical step, and limiting regimes. These tests are supporting computational diagnostics, not a proof of the universal statements, which follow from the exact formulas and inequalities above.

## Relationship to prior work

The third-order matrix-valued update itself was published **before 2026**: Li, Zhang and Liu's 2019 preprint (subsequently appearing in 2021), equation (23), gives precisely the same method under the name `Erow3`, and discusses accuracy and low-rank numerical experiments. Hochbruck, Ostermann and Schweitzer (2009) introduced its underlying exponential Rosenbrock-type method and order theory. Li, Li and Yang (2026), equation (22), incorporate that established third-order step into a concrete embedded adaptive low-rank framework. The numerical update itself is **not** presented as novel. Chen and Borzì (2023) developed distinct **exponential Euler and exponential midpoint** Riccati schemes that preserve positivity unconditionally. Their result cannot imply unconditional preservation for the higher-order `exprb32` correction and motivates identifying its precise admissible regimes. The present claim concerns the exact three-part classification of the `exprb32` output itself: spectral inertia, damping-dependent sharp horizon, and the scalar all-input cone threshold. These facts are not asserted here to be first of their kind for all exponential integrators.

## Limitations

Only the full-matrix `exprb32` method with exact \(\varphi\)-actions is analyzed. Matrix results begin at \(X=0\) and require \(A=-aI\); they do **not** characterize arbitrary nonnegative matrix initial conditions or arbitrary stabilizing matrices \(A\). The scalar all-state result has no linear drift and assumes strictly positive \(q,g\). No guarantee is made for truncated low-rank factors, floating-point error, adaptive rejection thresholds, higher-order `exprb43`, or long-time convergence, except the elementary cone invariance of the scalar iteration under steps satisfying its criterion. A first-step loss of positivity is not a claim of divergence. The third-order algorithm and all classical matrix inertia identities are prior knowledge; novelty is subject to earlier specialized numerical-analysis literature and independent bibliographic review.

## References

1. J. Li, D. Li and H. Yang, *Adaptive low-rank exponential integrators for large-scale differential Riccati equation*, arXiv:2603.26429v1 (first public 2026-03-27), Section 3.1, equation (22). https://arxiv.org/pdf/2603.26429
2. M. Hochbruck, A. Ostermann and J. Schweitzer, *Exponential Rosenbrock-Type Methods*, SIAM Journal on Numerical Analysis 47 (2009), 786–803. DOI:10.1137/080717717. Open manuscript: https://publikationen.bibliothek.kit.edu/1000041838/3153466
3. H. Chen and A. Borzì, *Positivity Preserving Exponential Integrators for Differential Riccati Equations*, Journal of Scientific Computing 96 (2023), Article 50. DOI:10.1007/s10915-023-02275-6. Its accessible publisher abstract and first-page preview identify exponential Euler and midpoint schemes; its full text was not available for complete comparison.
4. D. Li, X. Zhang and R. Liu, *Exponential integrators for large-scale stiff matrix Riccati differential equations*, arXiv:1907.12971v2 (2019 preprint; published 2021), Section 3, equation (23), `Erow3`. https://arxiv.org/pdf/1907.12971; published article DOI:10.1016/j.cam.2020.113360.
