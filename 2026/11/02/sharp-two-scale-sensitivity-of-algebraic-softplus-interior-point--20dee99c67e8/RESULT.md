# Sharp two-scale sensitivity of algebraic-softplus interior-point Newton matrices

## Finding

Define, for every \(\mu>0\) and \(t\in\mathbb R\), the *algebraic-softplus retraction* and its derivative by
\[
 b_\mu(t)=\frac{t+\sqrt{t^2+4\mu}}2,
 \qquad d_\mu(t)=b'_\mu(t)=\frac12\left(1+\frac{t}{\sqrt{t^2+4\mu}}\right).
\]
These are not the logarithmic-exponential softplus and its logistic derivative. For every shrink factor \(0<\sigma<1\) and every \(\mu>0\), the exact uniform change in this derivative is
\[
 \boxed{\sup_{t\in\mathbb R}|d_{\sigma\mu}(t)-d_\mu(t)|
 =D(\sigma):=\frac{1-\sigma^{1/3}}{2\sqrt{1+\sigma^{1/3}+\sigma^{2/3}}}.}
\]
Equality is attained exactly at the two points
\[
 t=\pm\frac{2\sqrt\mu\,\sigma^{1/3}}{\sqrt{1+\sigma^{1/3}}}.
\]
Independently, for every real displacement \(h\), the exact uniform change at a fixed barrier is
\[
 \boxed{\sup_{t\in\mathbb R}|d_\mu(t+h)-d_\mu(t)|
 =H_\mu(h):=\frac{|h|}{\sqrt{h^2+16\mu}}.}
\]
For \(h\ne0\), equality is attained exactly at \(t=-h/2\); for \(h=0\), every point attains zero. The sharp logarithmic-barrier derivative modulus is
\[
 \boxed{\sup_{t\in\mathbb R}|\partial_{\log\mu}d_\mu(t)|=\frac1{6\sqrt3}.}
\]
The two finite-step moduli jointly yield a dimension-independent perturbation criterion for the algebraic-softplus quadratic-programming KKT matrix; see below. No claim is made that their sum is the sharp *joint* modulus.

## Assumptions and scope

Fix integers \(n\ge1\), \(m\ge1\), \(p\ge0\), a symmetric \(Q\in\mathbb R^{n\times n}\), and constant matrices \(A\in\mathbb R^{m\times n}\) and \(C\in\mathbb R^{p\times n}\). In the convex quadratic-programming application, \(Q\) is positive semidefinite. Let \(v\in\mathbb R^m\), \(\mu>0\), and define the symmetric condensed Jacobian associated with algebraic-softplus complementarity by
\[
 J_\mu(v)=
 \begin{pmatrix}
 Q-A^{\mathsf T}A&-A^{\mathsf T}&-C^{\mathsf T}\\
 -A&-\operatorname{diag}(d_\mu(-v_i))&0\\
 -C&0&0
 \end{pmatrix}.
\]
The empty equality block is omitted when \(p=0\). The formula and the context of frozen linear-system factorizations originate in Arrizabalaga–Manchester (2026). All assertions here concern the stated algebraic kernel and these fixed matrix blocks in exact arithmetic. No inequality-feasibility, convergence, or nonsingularity hypothesis is needed to bound the Jacobian difference; nonsingularity is required only for the inexact-Newton application.

For \(\mu_1=\mu\), \(\mu_2=\sigma\mu\), and any \(v,v'\in\mathbb R^m\), with \(h_i=v'_i-v_i\), one has the **exact identity**
\[
 \|J_{\sigma\mu}(v')-J_\mu(v)\|_2
 =\max_{1\le i\le m}|d_{\sigma\mu}(-v'_i)-d_\mu(-v_i)|,
\]
and the **valid two-scale bound**
\[
 \boxed{\|J_{\sigma\mu}(v')-J_\mu(v)\|_2\le
 \min\left\{1,\ D(\sigma)+\max_i\frac{|h_i|}{\sqrt{h_i^2+16\sigma\mu}}\right\}.}
\]
The first bound is exactly sharp when \(v'=v\), and the second scalar component is exactly sharp for fixed \(\mu\) with \(\sigma=1\). These two statements are **separate sharpness assertions**, not a claim of joint sharpness for arbitrary nonzero barrier and state changes. For any admissible \(n,m\), the bound is independent of dimension, and its sharp fixed-variable example is realized with \(n=m=1\), \(p=0\), \(Q=1\), \(A=1\).

## Proof

**1. Uniform barrier shrink.** By oddness of the centered part \(d_\mu(t)-1/2\), it suffices to maximize the positive difference over \(t\ge0\). Set \(x=t/(2\sqrt\mu)\). Then
\[
 d_{\sigma\mu}(t)-d_\mu(t)
 =g_\sigma(x)
 =\frac{x}{2}\left(\frac1{\sqrt{x^2+\sigma}}-\frac1{\sqrt{x^2+1}}\right).
\]
The function is nonnegative, vanishes at \(x=0\), and tends to zero as \(x\to\infty\). Its derivative is
\[
 g'_\sigma(x)=\frac12\left(\frac{\sigma}{(x^2+\sigma)^{3/2}}
 -\frac1{(x^2+1)^{3/2}}\right).
\]
The stationarity equation is equivalent, with \(r=\sigma^{1/3}\in(0,1)\), to
\[
 r^2(x^2+1)=x^2+r^3,
 \qquad x^2=\frac{r^2}{1+r}.
\]
It has exactly one positive solution, so this solution is the global maximum. Substituting \(x=r/\sqrt{1+r}\) yields
\[
 g_\sigma(x)=\frac{1-r}{2\sqrt{1+r+r^2}}.
\]
Reflection to negative \(t\) gives the absolute-value supremum and its two equality points. The expression has no remaining dependence on \(\mu\).

**2. Uniform state displacement.** Direct differentiation gives
\[
 d'_\mu(t)=\frac{2\mu}{(t^2+4\mu)^{3/2}}>0.
\]
It is even and strictly decreases with \(|t|\). For fixed \(h>0\), the difference \(d_\mu(t+h)-d_\mu(t)\) equals the integral of this even unimodal density over an interval of length \(h\). Such an interval has strictly maximal integral when centered at zero, namely \(t=-h/2\). Explicit subtraction gives
\[
 d_\mu(h/2)-d_\mu(-h/2)=\frac{h}{\sqrt{h^2+16\mu}}.
\]
The cases \(h<0\) and \(h=0\) follow by symmetry.

**3. Differential barrier sensitivity.** Differentiating with respect to \(\log\mu\), while holding \(t\) fixed, yields
\[
 \partial_{\log\mu}d_\mu(t)=-\frac{\mu t}{(t^2+4\mu)^{3/2}}.
\]
Its absolute value is maximized at \(|t|=\sqrt{2\mu}\), where it equals \(1/(6\sqrt3)\). The finite-step formula agrees with the infinitesimal limit
\[
 \lim_{\sigma\uparrow1}\frac{D(\sigma)}{|\log\sigma|}=\frac1{6\sqrt3}.
\]

**4. KKT matrix and frozen-factorization consequence.** All blocks of \(J_\mu(v)\) except the inequality diagonal are independent of \(\mu,v\). Their difference is a diagonal real symmetric block, whose spectral norm is exactly the largest absolute diagonal entry. Insert an intermediate matrix \(J_{\sigma\mu}(v)\), apply the triangle inequality and the first two sharp scalar moduli, then cap by one because \(d_\mu\in(0,1)\). This proves the stated joint bound. The fixed-variable sharp case is realized by a one-constraint QP with \(Q=A=1\), whose KKT matrix is \(\begin{psmallmatrix}0&-1\\-1&-d_\mu(-v)\end{psmallmatrix}\) and is always nonsingular; the matrix difference has norm exactly \(D(\sigma)\) at the maximizing \(v\).

More precisely, if a *frozen* matrix \(J_0=J_\mu(v)\) is nonsingular, a current matrix is \(J_1=J_{\sigma\mu}(v')\), and a frozen step is defined by \(J_0z=-r\), then
\[
 \frac{\|r+J_1z\|_2}{\|r\|_2}
 \le\frac{\|J_1-J_0\|_2}{\sigma_{\min}(J_0)}
 \le\frac{\min\{1,D(\sigma)+\max_iH_{\sigma\mu}(h_i)\}}
 {\sigma_{\min}(J_0)},\qquad r\ne0.
\]
Thus requiring the last expression to be at most a selected forcing tolerance \(\theta\) is a **sufficient**, not necessary, certificate for the full-residual inexact Newton condition. It is not a convergence theorem. No lower bound on \(\sigma_{\min}(J_0)\) is claimed.

## Verification

The companion `verify.py` uses only Python's standard library. It independently maximizes the barrier-change function by a golden-section computation; tests analytic equality points, sign symmetry, the centered state-shift maximum, the joint estimate, exact two-by-two KKT differences and frozen-system residual bounds over positive barrier scales and seeded parameter grids. It passes **10,565 deterministic/seeded assertions**. These are finite numerical cross-checks; the proof above supplies the universal argument. Run with `python verify.py` after extracting that file. The exact logarithmic-derivative maximum is tested independently.

Two instructive boundary choices are \(\sigma=1/8\), for which \(D(\sigma)=1/(2\sqrt7)\approx0.1889822365\) at a state of magnitude \(\sqrt{2\mu/3}\), and \(h=4\sqrt\mu\), for which \(H_\mu(h)=1/\sqrt2\). In both cases the parameter or state displacement approaches zero with \(\mu\downarrow0\), while the matrix-change norm stays bounded away from zero. Consequently, a small *absolute* barrier parameter alone does not certify small changes in this KKT matrix.

## Relationship to prior work

Arrizabalaga and Manchester introduce the algebraic-softplus complementarity retraction, give its derivative and the condensed KKT block, prove bounds on primal/slack *values for fixed nonzero state* under barrier reduction (Theorem 2), and use observed smooth KKT evolution to motivate frozen factorizations with a residual test (their equation (18)). All of those foundations and the generic inexact-Newton inequality are previously known. They do not give the exact uniform-over-state barrier derivative modulus, the exact state-displacement modulus, or the explicit two-scale bound derived here in the inspected sections of the primary paper. Their fixed-nonzero-state \(O(\mu)\) control does not imply uniform smallness over states of size \(O(\sqrt\mu)\).

Kanzow and Pieper (1999) analyze Jacobian smoothing of Fischer–Burmeister complementarity functions, using the distinct two-variable kernel \(\sqrt{a^2+b^2+2\mu}-a-b\); that work is conceptually adjacent, and the underlying square-root smoothing family is classical. The present claim is **not** the novelty of square-root smoothing, bounded derivatives, or inexact Newton. It is a sharp finite-barrier, finite-state perturbation statement for the *specific algebraic-softplus inequality block* used in the 2026 condensed symmetric QP Newton system. A later 2026 paper by Arrizabalaga, Tracy, and Manchester uses related implicit complementarity; only its abstract and third-party exposition were accessible during comparison, so unseen treatment of these perturbation moduli remains a historical-priority risk. No independence from all earlier numerical-optimization literature is asserted.

## Limitations

The estimates hold only when the remaining KKT matrix blocks remain unchanged, and all are exact-arithmetic deterministic statements. When \(Q,A,C\) or scaling changes, additional matrix-difference terms must be included. The two-scale sum may be conservative when barrier and state change together; no joint-sharpness result is claimed. A usable forcing certificate requires information about the smallest singular value of the frozen matrix. No overall convergence, finite-precision performance, rank robustness, or factorization count is proved. Equivalent moduli could appear in older smoothing literature; complete historical priority remains unverified. In particular, an inaccessible same-method follow-up precludes definitive novelty certification.

## References

1. J. Arrizabalaga and Z. Manchester, *Implicit Primal-Dual Interior-Point Methods for Quadratic Programming*, arXiv:2604.00364v1, first public April 1, 2026. https://arxiv.org/abs/2604.00364 . Especially equations (13)–(15), Theorem 2, Section IV-B, and equation (18).
2. J. Arrizabalaga, K. Tracy, and Z. Manchester, *A Differentiable Interior-Point Method in Single Precision*, arXiv:2605.17913v1, first public May 18, 2026. https://arxiv.org/abs/2605.17913 . Accessible abstract only; full text not evaluated.
3. C. Kanzow and H. Pieper, *Jacobian Smoothing Methods for Nonlinear Complementarity Problems*, SIAM Journal on Optimization 9(2), 342–373 (1999), DOI:10.1137/S1052623497328781. Open preprint (1997): https://www.mathematik.uni-wuerzburg.de/fileadmin/10040700/paper/smooth.pdf . Inspected introductory and kernel-defining sections; not an exhaustive examination of 38 pages.
4. B. Chen and P. T. Harker, *Smooth Approximations to Nonlinear Complementarity Problems*, SIAM Journal on Optimization 7(2), 403–420 (1997), DOI:10.1137/S1052623495280615. Abstract consulted, not the full text.
