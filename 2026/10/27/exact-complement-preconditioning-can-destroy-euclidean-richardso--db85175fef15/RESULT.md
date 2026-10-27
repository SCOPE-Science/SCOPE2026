# Exact-complement preconditioning can destroy Euclidean Richardson safety in three modes

## Finding
For every \(0<\varepsilon<1/2\) and \(0<\delta\le1\), define
\[
A_{\varepsilon,\delta}=\begin{pmatrix}1&\varepsilon&\varepsilon\sqrt{\delta}\\\varepsilon&1&0\\\varepsilon\sqrt{\delta}&0&\delta\end{pmatrix},\qquad p=e_1,\qquad T=\operatorname{diag}(1,1,\delta).
\]
The reduced Galerkin matrix is \(p^\top A_{\varepsilon,\delta}p=1\). In the terminology of Fan, Hu and Zhang, the Type-II and Type-III additive reduced-basis **inverse** preconditioners are
\[
F^{\mathrm{II}}_\beta=pp^\top+\beta(I-pp^\top),\quad
F^{\mathrm{III}}_\alpha=pp^\top+\alpha(I-pp^\top)T^{-1}(I-pp^\top),\qquad \alpha,\beta>0.
\]
All \(A_{\varepsilon,\delta}\) are real symmetric positive definite. At \(\beta=1\), the Type-II error propagator \(E^{\mathrm{II}}=I-F^{\mathrm{II}}_1A_{\varepsilon,\delta}=I-A_{\varepsilon,\delta}\) is a strict Euclidean contraction.

**Contrasting Type-III failure.** For every \(0<\delta\le\varepsilon^6/4\), **all** positive Type-III scalings satisfy
\[
\|E^{\mathrm{III}}_\alpha\|_2=\|I-F^{\mathrm{III}}_\alpha A_{\varepsilon,\delta}\|_2>1.
\]
Nevertheless, at \(\alpha=\delta\), its spectral radius is strictly less than \(1\). More strongly, its best possible one-step Euclidean amplification obeys the sharp asymptotic law
\[
\boxed{\displaystyle \lim_{\delta\downarrow0}\inf_{\alpha>0}\|E^{\mathrm{III}}_\alpha\|_2=\sqrt{1+\varepsilon^2}.}
\]
The Type-II/Type-III distinction is impossible with only one complementary coordinate; hence dimension three is minimal for this specific safety reversal.

## Assumptions and scope
The operators are real and exactly evaluated. The reduced subspace is fixed and one-dimensional; the fine-space basic preconditioner \(T\) is exactly the fine diagonal block of \(A_{\varepsilon,\delta}\), extended by a positive entry on the coarse coordinate. One Richardson step is \(x^+=x+F(b-Ax)\), whose error satisfies \(e^+=(I-FA)e\). Euclidean safety means \(\|I-FA\|_2\le1\) for every initial error; strict safety means \(<1\). Spectral convergence means \(\rho(I-FA)<1\), which is a distinct statement for nonsymmetric propagators. Here \(F\) is the **inverse** preconditioner as applied to the residual.

## Proof
**Positive definiteness and safe Type II.** Partition \(A_{\varepsilon,\delta}\) after its first coordinate. Its fine block is \(B=\operatorname{diag}(1,\delta)\), while the coupling is \(c=\varepsilon(1,\sqrt\delta)^\top\). The scalar Schur complement is
\[
1-c^\top B^{-1}c=1-2\varepsilon^2>0.
\]
Thus \(A_{\varepsilon,\delta}\succ0\). Every absolute row sum is at most \(1+2\varepsilon<2\) for \(0<\delta\le1\); symmetry implies \(0<\lambda_{\min}(A_{\varepsilon,\delta})\le\lambda_{\max}(A_{\varepsilon,\delta})<2\). Because \(F^{\mathrm{II}}_1=I\), every eigenvalue of \(I-A_{\varepsilon,\delta}\) lies strictly between \(-1\) and \(1\), and hence its induced Euclidean norm is strictly smaller than one.

**An all-parameter Type-III obstruction.** The exact complementary inverse gives
\[
F^{\mathrm{III}}_\alpha=\operatorname{diag}(1,\alpha,\alpha/\delta),\quad
E^{\mathrm{III}}_\alpha=\begin{pmatrix}0&-\varepsilon&-\varepsilon\sqrt\delta\\-\alpha\varepsilon&1-\alpha&0\\-\alpha\varepsilon/\sqrt\delta&0&1-\alpha\end{pmatrix}.
\]
Two unit test vectors give the independent lower bounds
\[
\|E^{\mathrm{III}}_\alpha e_1\|_2\ge \alpha\varepsilon/\sqrt\delta,\qquad
\|E^{\mathrm{III}}_\alpha e_2\|_2^2=\varepsilon^2+(1-\alpha)^2.
\]
Suppose \(\|E^{\mathrm{III}}_\alpha\|_2\le1\). The first bound entails \(\alpha\le\sqrt\delta/\varepsilon\le\varepsilon^2/2\). The second therefore yields
\[
\|E^{\mathrm{III}}_\alpha e_2\|_2^2\ge\varepsilon^2+(1-\varepsilon^2/2)^2=1+\varepsilon^4/4>1,
\]
a contradiction. The restriction on \(\delta\) is a sufficient obstruction range; no assertion is made that its endpoint is the exact fixed-\(\delta\) transition.

**Sharp asymptotic infimum.** For fixed \(\varepsilon\), choosing \(\alpha=\delta\) gives the operator-norm limit
\[
E^{\mathrm{III}}_\delta\longrightarrow E_0=
\begin{pmatrix}0&-\varepsilon&0\\0&1&0\\0&0&1\end{pmatrix},\qquad\|E_0\|_2=\sqrt{1+\varepsilon^2}.
\]
This establishes the upper bound for the limiting infimum. Conversely, for any \(\delta_j\downarrow0\), choose near-minimizers \(\alpha_j>0\) whose norms exceed the infima by at most \(1/j\). The displayed upper bound makes these norms bounded. The first test vector then forces \(\alpha_j=O(\sqrt{\delta_j})\to0\); the second forces \(\liminf_j\|E^{\mathrm{III}}_{\alpha_j}\|_2\ge\sqrt{1+\varepsilon^2}\). Every sequence has this bound, proving the exact limit.

**Spectral convergence despite transient amplification.** At \(\alpha=\delta\), the matrix \(F_\delta A_{\varepsilon,\delta}\) is similar to the SPD matrix
\[
F_\delta^{1/2}A_{\varepsilon,\delta}F_\delta^{1/2}=
\begin{pmatrix}1&\varepsilon\sqrt\delta&\varepsilon\sqrt\delta\\\varepsilon\sqrt\delta&\delta&0\\\varepsilon\sqrt\delta&0&\delta\end{pmatrix},
\qquad F_\delta=\operatorname{diag}(1,\delta,1).
\]
Its absolute row sums are below \(2\) when \(\varepsilon<1/2\) and \(\delta\le1\); all eigenvalues lie in \((0,2)\). Hence \(\rho(E^{\mathrm{III}}_\delta)<1\). The Euclidean amplification above is not a claim of spectral divergence.

**Minimal dimension.** In two dimensions with a one-dimensional reduced space, every positive-definite basic \(T\) has a positive scalar \(s=q^\top T^{-1}q\) on its one-dimensional orthogonal complement. Therefore \(F^{\mathrm{III}}_\alpha=pp^\top/a+\alpha s qq^\top=F^{\mathrm{II}}_{\alpha s}\). The two admissible families coincide after reparametrization, so the strict safety reversal cannot arise there. Dimension one has no nontrivial complement.

## Verification
For the rational witness \(\varepsilon=1/4\), \(\delta=1/65536\), the cross entry is \(1/1024\), the Schur complement is \(7/8\), and \(F^{\mathrm{III}}_\alpha=\operatorname{diag}(1,\alpha,65536\alpha)\). If \(\alpha\le1/64\), the second test vector has norm at least \(65/64>1\); if \(\alpha>1/64\), the first test vector has norm greater than one. This is an exact rational finite certificate for all \(\alpha>0\). The included `check.py` reproduces rational identities and tests 575 sampled scaling parameters plus 8,000 asymptotic grid evaluations; finite checks do not prove the uniform or limiting statements.

## Relationship to prior work
Fan, Hu and Zhang (2026), equation (8), introduce Type-III projected basic preconditioning and show nonsingularity, while their Richardson bounds use Type I. The present statement compares fixed Type II and exact-complement Type III using the **induced Euclidean error norm**, supplies an all-parameter strict separation, and proves a nonzero sharp asymptotic optimal gap. Earlier additive coarse-grid preconditioning comparisons by Nabben and Vuik (2008) and Tang, Nabben, Vuik and Erlangga (2009) emphasize spectral and algebraic properties; those properties alone cannot settle this nonnormal one-step norm. General results that Euclidean transients need not follow spectral contraction are acknowledged rather than claimed as new. Distinct two-mode Type-II safety classifications do not imply the present anisotropic Type-III three-mode separation.

## Limitations
This is a deliberately simple fixed-basis SPD counterexample. The condition \(\delta\le\varepsilon^6/4\) is sufficient, not an exact finite-\(\delta\) stability boundary. The limiting infimum is exact. No claim concerns adaptive reduced bases, right-preconditioned FGMRES, floating-point roundoff, typical PDE discretizations, or monotonicity in the problem condition number. The result does not imply Type III is generally inferior to Type II, only that an exact fine inverse plus one scalar need not be safer in Euclidean norm.

## References
Fan, X., Hu, Q., Zhang, S., *Additive Reduced Basis Preconditioners for Large-Scale Parametrized PDEs*, arXiv:2609.11097v1 (first public 2026-09-10), especially §3.1 equation (8), §3.2 and §3.4. https://arxiv.org/html/2609.11097v1

Nabben, R., Vuik, C., *A comparison of abstract versions of deflation, balancing and additive coarse grid correction preconditioners*, Numerical Linear Algebra with Applications **15** (2008), 355–372. doi:10.1002/nla.571.

Tang, J. M., Nabben, R., Vuik, C., Erlangga, Y. A., *Comparison of Two-Level Preconditioners Derived from Deflation, Domain Decomposition and Multigrid Methods*, Journal of Scientific Computing **39** (2009), doi:10.1007/s10915-009-9272-6.
