# Inertia-robust bistability of a scalar logarithmic reweighting method

## Finding

Consider the scalar Gaussian-fidelity/log-penalty model
\[
F(x)=\frac{a}{2}(x-b)^2+\frac{1}{\rho}\log(1+\rho x^2),\qquad a>0,\ \rho>0,\ b\in\mathbb R.
\]
For every proximal curvature \(\ell>a\) and every fixed inertia \(0\le\beta<1\), the scalar specialization of the generalized inertial iteratively reweighted algorithm described in Reference [1] is the **two-state** dynamical system
\[
(x_{k+1},x_k)=\left(\Phi(x_k,x_{k-1}),x_k\right),\qquad
\Phi(x,y)=\frac{(\ell-a)((1+\beta)x-\beta y)+ab}{\ell+2/(1+\rho x^2)}.
\]
Its fixed points are precisely \((x_*,x_*)\) with \(F'(x_*)=0\). At every nondegenerate fixed point, the equilibrium is locally asymptotically attracting **if and only if** \(F''(x_*)>0\), and it has a multiplier strictly greater than \(1\) if \(F''(x_*)<0\). This equivalence holds for every admissible \(\ell\) and \(\beta\), including zero inertia.

The exact multiplicity window can be expressed without solving a cubic. Let \(H_a(u)=u\bigl(1+2/[a(1+u^2)]\bigr)\), \(t=\sqrt\rho\,|b|\). If \(a\ge1/4\), the stationary point is unique. If \(0<a<1/4\), define
\[
w_\pm=\frac{1-a\pm\sqrt{1-4a}}a,\quad
 t_{\min}=H_a(\sqrt{w_+}),\quad t_{\max}=H_a(\sqrt{w_-}).
\]
Then \(0<t_{\min}<t_{\max}\), and the system has exactly three distinct fixed points precisely for \(t_{\min}<t<t_{\max}\). In that window two equilibria (the outer roots) are locally attracting and the middle equilibrium is linearly unstable, **independently of inertia and proximal curvature**. At either equality endpoint there are two distinct fixed points, one degenerate; outside the closed window there is one. At \(a=1/4\) and \(t=3\sqrt3\), the unique stationary point is degenerate; no nonlinear stability conclusion is asserted at any degenerate point.

The coexistence can trap the algorithm at a strictly *suboptimal* local minimum. With \(a=1/8,\rho=1,b=9\), the fixed-point locations are \(1,4-\sqrt7,4+\sqrt7\). For every \(\ell>1/8\) and \(0\le\beta<1\), the two outer points \(1\) and \(4+\sqrt7\) attract all two-state initial conditions in respective nonempty open neighborhoods. Nevertheless \(F(1)>F(4+\sqrt7)\). Consequently even the prescribed diagonal initialization \(x_{-1}=x_0\) has a nonempty open set of scalar choices converging to a non-global local minimum.

## Assumptions and scope

The functions are \(p\equiv0\), \(q(x)=a(x-b)^2/2\), \(g(x)=x^2\), and \(h(v)=\rho^{-1}\log(1+\rho v)\) on \(v\ge0\). Here \(q\) has \(a\)-cocoercive gradient, \(g\) is convex, and \(h\) is increasing and concave. The algorithm uses an exact minimizer of its scalar weighted quadratic subproblem, a fixed \(\beta\in[0,1)\), and a scalar positive metric \(\ell>a\). Data \(b\) can have either sign, including zero. All claims concern discrete local fixed-point stability, not generic global convergence or a global basin classification.

## Proof

**Exact update and equilibrium equation.** The weight at state \(x\) is \(\omega(x)=1/(1+\rho x^2)\). Minimizing the source's subproblem
\[
q'(\bar x)(z-\bar x)+\omega(x)z^2+\frac\ell2(z-\bar x)^2,
\qquad \bar x=(1+\beta)x-\beta y,
\]
gives \([\ell+2\omega(x)]z=(\ell-a)\bar x+ab\), hence \(z=\Phi(x,y)\). At equilibrium \(x=y=x_*\), this is equivalent to
\[
a(x_*-b)+\frac{2x_*}{1+\rho x_*^2}=F'(x_*)=0.
\]
The objective is coercive, and there is no missing finite root.

**Sharp fold count.** Set \(u=\sqrt\rho\,x\) and \(h=\sqrt\rho\,b\). The stationary equation becomes \(h=H_a(u)\). The odd function \(H_a\) has the sign of \(u\), and
\[
H_a'(u)=\frac{a(1+u^2)^2+2(1-u^2)}{a(1+u^2)^2}.
\]
Its numerator, regarded as a polynomial in \(w=u^2\ge0\), is \(aw^2+(2a-2)w+a+2\), with discriminant \(4(1-4a)\). For \(a>1/4\), the numerator is positive everywhere. At \(a=1/4\) it is nonnegative, zero only for \(w=3\), so \(H_a\) remains strictly increasing. For \(0<a<1/4\), its two simple zeros obey \(1<w_-<w_+\); thus on the positive half-line \(H_a\) increases, decreases, and increases, with local maximum \(t_{\max}\) at \(\sqrt{w_-}\) and local minimum \(t_{\min}\) at \(\sqrt{w_+}\). Since \(H_a(0)=0\), \(H_a(u)>0\) for \(u>0\) and \(H_a(u)\to\infty\), the asserted exact root counts and signs follow by monotonicity and symmetry. Furthermore
\[
F''(x)=a+\frac{2(1-\rho x^2)}{(1+\rho x^2)^2}
 =aH_a'(\sqrt\rho\,x).
\]
The outer roots have positive curvature and the middle root has negative curvature. The equalities produce double stationary roots; the cusp at \(a=1/4\) produces a degenerate but unique root.

**Exact inertial stability test.** At an equilibrium put
\[
D=\ell+\frac{2}{1+\rho x_*^2},\quad
c=\frac{\ell-a}{D},\quad
s=\frac{4\rho x_*^2}{D(1+\rho x_*^2)^2}.
\]
Here \(0<c<1\), \(s\ge0\). Differentiating the two-state map at the fixed point yields
\[
J_*=\begin{pmatrix}(1+\beta)c+s&-\beta c\\1&0\end{pmatrix},\qquad
P(\lambda)=\lambda^2-[(1+\beta)c+s]\lambda+\beta c.
\]
The following identity is exact:
\[
P(1)=1-c-s=\frac{F''(x_*)}{D}.
\]
The remaining two strict Schur/Jury tests are automatically satisfied: \(1-\beta c>0\) and \(P(-1)=1+(1+\beta)c+s+\beta c>0\). Thus both multipliers lie in the open unit disk exactly when \(F''(x_*)>0\). If \(F''(x_*)<0\), continuity and \(P(\lambda)\to\infty\) for \(\lambda\to\infty\) imply a real root \(\lambda>1\). If \(F''(x_*)=0\), \(\lambda=1\) and the other multiplier is \(\beta c<1\); the linearization alone does not settle nonlinear attraction. Smoothness of the map and the standard hyperbolic fixed-point theorem yield the local attraction assertions for positive curvature; negative curvature gives linear instability.

**Exact non-global basin.** With \((a,\rho,b)=(1/8,1,9)\), multiplying \(F'(x)=0\) by \(8(1+x^2)\) yields
\[
(x-1)(x^2-8x+9)=0.
\]
At the three ascending roots the Hessians are, respectively,
\[
F''(1)=\frac18,\qquad
F''(4-\sqrt7)=-\frac{\sqrt7}{32},\qquad
F''(4+\sqrt7)=\frac{\sqrt7}{32}.
\]
In particular the first and third roots have locally attracting two-state neighborhoods. Moreover
\[
F(1)-F(4+\sqrt7)
=2+\frac{5\sqrt7}{8}-\log\bigl(4(3+\sqrt7)\bigr)>0.
\]
For a purely analytic strict proof, \(12/5<\sqrt7<3\) gives the nonlogarithmic term greater than \(7/2\), while \(4(3+\sqrt7)<24<32\) and \(\log2<7/10\) give the logarithm less than \(\log32=5\log2<7/2\). The bound \(\log2<7/10\) follows, for instance, from \(e^{7/10}>1+7/10+(7/10)^2/2+(7/10)^3/6>2\). The attracting two-state neighborhood around \((1,1)\) intersects the diagonal \(x=y\) in an open interval, proving the diagonal-initialization claim.

## Verification

Run `python3 verify.py` using Python 3 and SymPy. The standalone checker verifies the differentiated two-state map, its fixed-point Jacobian identity, the fold derivative identity, the exact factorization and Hessian signs for the witness, the strict unit-disk tests for a representative admissible inertia/curvature pair, and the elementary objective-ordering inequalities. Output: `VERIFY_OK`. The universal conclusions above follow from the displayed analytic proof; finite symbolic checks do not substitute for the quantified proof. The checker has no network or external dataset dependencies.

## Relationship to prior work

Kang [1] defines this reweighting algorithm and the log-quadratic penalty family and proves convergence to *a critical point*, without classifying the local fixed-point spectrum or the inertia-robust bistable regime. Karakus, Mayo, and Achim [2] already derive the Cauchy proximal cubic and the penalty-convexity threshold, so those components are used here as background rather than claimed as independently new. Bai, Hu, Wang, and Yang [3] prove strict-saddle avoidance for different, damped reweighted algorithms (including DIRL2), but their update is not the two-state inertial GIRL1E map above and does not imply its exact all-\(\beta\), all-\(\ell\) stability/multiplicity phase diagram or the exhibited suboptimal attracting basin. The substantive assertion here is the coupling between the **specified two-state algorithm's exact multipliers**, the natural fold window, and a parameter-robust suboptimal attractor.

## Limitations

This is a one-dimensional Gaussian/Cauchy sparse-recovery building block, not a statement about coupled high-dimensional instances. The model uses fixed admissible \(\beta\) and exact subproblem solutions, not variable inertial schedules or inexact arithmetic. The two degenerate fold endpoints and the \(a=1/4\) cusp have a multiplier exactly equal to \(1\); no claim about their nonlinear stability is made. The open attraction neighborhoods are local and their sizes are not quantified. The historical cubic, Cauchy-penalty normalization, and convexity threshold are not asserted as novel. Independent audit has not been performed.

## References

[1] M. Kang, “An inertial generalized iteratively reweighted ℓ1 algorithm for nonconvex and nonsmooth optimization,” *AIMS Mathematics* 11 (2026), 16414–16447. First published June 9, 2026. DOI: https://doi.org/10.3934/math.2026674 . See Algorithm 1, Theorem 3.1, Section 4.1 and Appendix.

[2] O. Karakus, P. Mayo, A. Achim, “Convergence Guarantees for Non-Convex Optimisation with Cauchy-Based Penalties,” 2020, arXiv:2003.04798, https://arxiv.org/abs/2003.04798 . See equations (10)–(11), Lemma 2 and Theorem 1.

[3] L. Bai, Y. Hu, H. Wang, X. Yang, “Avoiding strict saddle points of nonconvex regularized problems,” 2024, arXiv:2401.09274, https://arxiv.org/abs/2401.09274 . See Sections 3–4, especially their distinct damped IRL2 map and strict-saddle results.
