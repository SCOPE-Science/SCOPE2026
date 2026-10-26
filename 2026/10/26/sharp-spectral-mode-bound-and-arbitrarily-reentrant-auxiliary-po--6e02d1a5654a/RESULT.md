# Sharp spectral-mode bound and arbitrarily reentrant auxiliary positivity in original SAV backward Euler

## Finding
Fix the state and positive auxiliary variable at the beginning of one original scalar-auxiliary-variable backward-Euler (SAV-BE) step, and vary only its stepsize \(h>0\). Suppose that \(m\) distinct positive spectral modes participate in the source's exact sign criterion. Then the positive-stepsize set for the updated auxiliary variable has at most \(\lfloor m/2\rfloor+1\) connected components. The bound is sharp for every \(m\): **any \(m\) prescribed distinct positive sign-change stepsizes can occur, from consistent initial auxiliary data, with identity mobility and a globally positive strictly convex quadratic nonlinear energy**. Consequently, increasing the step beyond a sign-loss interval can restore auxiliary positivity, and the number of such reentrant intervals is unbounded with spectral complexity.

For two modes, an explicit strictly convex example yields
\[
 r^+(h)=\frac{16(h-1)(h-2)}{609h^2+449h+32},
\]
so positivity holds exactly on \((0,1)\cup(2,\infty)\), and is lost for \(1<h<2\). Two active positive modes are the minimum for this recovery phenomenon.

## Assumptions and scope
All spaces are finite-dimensional real Euclidean spaces. The mobility \(G\) is symmetric positive definite, the implicit operator \(L\) is symmetric positive semidefinite, and \(E_N\) is differentiable, with \(E_N(x)+C>0\) at the fixed initial state \(x\). Set \(g=\nabla E_N(x)\), \(Q=\sqrt{E_N(x)+C}>0\), and fix \(r>0\). The **original**, uncorrected SAV-BE update (not a new positivity-preserving SAV variant) is
\[
 \frac{x^+-x}{h}=-G\left(Lx^++\frac{r^+}{Q}g\right),\qquad
 r^+-r=\frac{g^{\mathsf T}(x^+-x)}{2Q}.
\]
Here \(h>0\) varies, while \(x,g,Q,r,G,L\) remain fixed. Define \(S=G^{1/2}LG^{1/2}\). For every **distinct** positive eigenvalue \(\lambda_i\) of \(S\), let \(P_i\) be its orthogonal spectral projector and let
\[
 c_i=(G^{1/2}g)^{\mathsf T}P_iG^{-1/2}x.
\]
Only the \(m\) positive eigenvalues with \(c_i\ne0\) are counted. Multiplicities do not count separately; zero eigenvalues do not contribute.

## Proof
**1. Exact sign reduction.** Solve the state update as \(x^+=p+r^+q\), with
\[
 p=(I+hGL)^{-1}x,\qquad q=-\frac{h}{Q}(I+hGL)^{-1}Gg.
\]
Substitution into the auxiliary update gives \(r^+=B(h)/A(h)\), where
\[
 A(h)=1-\frac{g^{\mathsf T}q}{2Q}
 =1+\frac{h}{2Q^2}(G^{1/2}g)^{\mathsf T}(I+hS)^{-1}G^{1/2}g>0
\]
and \(2Q B(h)=F(h)\), where the spectral decomposition yields
\[
 F(h)=2rQ-\sum_{i=1}^{m}c_i\frac{h\lambda_i}{1+h\lambda_i}.
 \tag{1}
\]
Thus \(\operatorname{sgn}r^+(h)=\operatorname{sgn}F(h)\). Formula (1) specializes the already published necessary-and-sufficient one-step positivity criterion, rather than claiming that criterion as new.

**2. Component upper bound.** Every denominator in (1) is strictly positive for positive \(h\). Hence \(F(h)\prod_{i=1}^m(1+h\lambda_i)\) is a real polynomial of degree at most \(m\), with constant coefficient \(2rQ>0\). Its zeros on \((0,\infty)\), counted with multiplicity, total at most \(m\). Since \(F(0)>0\), between any two distinct positive connected components of \(\{h>0:F(h)>0\}\) there must be at least two zeros counted with multiplicity: either two distinct crossings, or a repeated zero that punctures a positive interval. If there are \(k\) such components, \(2(k-1)\le m\), establishing \(k\le\lfloor m/2\rfloor+1\).

**3. Arbitrary prescribed sign-change locations with a positive convex energy.** Fix any \(m\ge1\), pairwise distinct \(\lambda_1,\ldots,\lambda_m>0\), and any \(0<t_1<\cdots<t_m\). Take \(G=I\), \(L=\operatorname{diag}(\lambda_1,\ldots,\lambda_m)\), \(x=\mathbf1\), \(r=Q=1\), and choose the nonlinear gradient vector \(c\) by
\[
 c_i=\frac{2\prod_{k=1}^{m}\left(1+\frac{1}{\lambda_i t_k}\right)}
 {\prod_{j\ne i}\left(1-\frac{\lambda_j}{\lambda_i}\right)}.
 \tag{2}
\]
The products in (2) are finite and all denominators are nonzero. Set
\[
 E_N(z)=1+c^{\mathsf T}(z-\mathbf1)+\kappa\|z-\mathbf1\|^2,
 \qquad \kappa>\frac{\|c\|^2}{4},\qquad C=0.
\]
Then \(E_N(z)\ge1-\|c\|^2/(4\kappa)>0\) for every \(z\), and \(\nabla^2 E_N=2\kappa I\succ0\). Moreover \(E_N(x)=1\), \(\nabla E_N(x)=c\), so \(r=Q=1\) is a consistent starting value.

The functions
\[
 F(h)=2-\sum_i c_i\frac{h\lambda_i}{1+h\lambda_i}
 \quad\text{and}\quad
 H(h)=2\frac{\prod_k(1-h/t_k)}{\prod_i(1+h\lambda_i)}
 \tag{3}
\]
are identical: their simple-pole residues at \(h=-1/\lambda_i\) match exactly by (2), their difference therefore has no poles and is constant, and both equal \(2\) at \(h=0\). Equation (3) has exactly the prescribed simple positive zeros, with alternating signs. Therefore there are \(\lfloor m/2\rfloor+1\) positive-stepsize components, proving sharpness and arbitrary prescribed threshold placement. The **total** continuous energy \(\frac12 z^{\mathsf T}Lz+E_N(z)\) is also strictly convex.

**4. Smallest explicit recovery example.** In dimension two let
\[
 G=I,\quad L=\operatorname{diag}(1,4),\quad x=(1,1)^{\mathsf T},\quad C=0,
\]
\[
 E_N(z)=1-2(z_1-1)+\frac{15}{4}(z_2-1)+5\big((z_1-1)^2+(z_2-1)^2\big).
\]
Its minimum is \(31/320>0\). Start with \(r=\sqrt{E_N(x)}=1\). Direct elimination of the two state components and the auxiliary equation gives
\[
 r^+(h)=\frac{16(h-1)(h-2)}{609h^2+449h+32}.
\]
The denominator is strictly positive for \(h>0\). This realizes positivity, failure, and recovery. With at most one active positive mode, the numerator has degree at most one, so such a recovery cannot occur.

## Verification
A standalone exact-rational checker, `verify.py`, reconstructs the interpolation weights, tests the rational identity in (3) for dimensions one through seven at 79 rational stepsizes each, verifies alternating signs between prescribed zeros, and independently eliminates both state coordinates in the two-dimensional original SAV-BE update. The checks include the energy lower bound and sign values at stepsizes on both sides of the two thresholds. All checks passed. The infinite-family statements and the global upper bound follow from the proof, not from finite experimentation.

## Relationship to prior work
Huang, Liu, Wang, and Yan (arXiv:2610.01063v1, Section 2, equations (2.3)–(2.10), Proposition 1 and Example 1) establish the original SAV-BE scheme, its exact one-step sign criterion, and sign loss in a single scalar mode. Their exact criterion is **used** as a starting point here; it does not itself give the maximal number of connected positive-stepsize intervals or a globally positive strictly convex construction attaining arbitrarily prescribed sign-change thresholds. Zhang and Shen (arXiv:2606.18551v1) study modified pullback-corrected SAV schemes, low-rank corrections, and energy stability, not this threshold-topology classification for the original scheme. Early SAV formulations provide the algorithmic foundation rather than the claimed sharp spectral-mode topology. Related positivity results for other integrators concern different step maps and do not mathematically imply arbitrary sign-change interpolation for this SAV auxiliary variable.

## Limitations
The theorem varies the first-step size while **holding the initial data fixed**; it does not imply that one adaptive trajectory can revisit an earlier state or exhibit the same sign pattern at successive time indices. The component bound uses the number of **active distinct positive spectral modes** in finite dimension, not an infinite-dimensional mode count. The construction gives a strictly convex quadratic \(E_N\), not a nonconvex double-well benchmark. The positive-stepsize set concerns only the sign of the auxiliary scalar, not positivity of state coordinates, energy accuracy, order of convergence, or finite-precision robustness. The exact stepwise criterion was known; no originality is claimed for its derivation. Older, unindexed numerical-analysis results could contain equivalent threshold-topology consequences.

## References
1. Q.-A. Huang, Z.-H. Liu, Y.-W. Wang, and L.-N. Yan, *Positivity-preserving scalar auxiliary variable schemes for gradient flows via a quadratic reformulation*, arXiv:2610.01063v1 (2026-10-01), especially Section 2, equations (2.3)–(2.18): https://arxiv.org/html/2610.01063v1.
2. S. Zhang and J. Shen, *Scalar-Tracking SAV Schemes with Pullback Corrections for Gradient Flows*, arXiv:2606.18551v1 (2026-06-17): https://arxiv.org/html/2606.18551v1.
3. J. Shen, J. Xu, and J. Yang, *A new class of efficient and robust energy stable schemes for gradient flows*, arXiv:1710.01331: https://arxiv.org/abs/1710.01331.
