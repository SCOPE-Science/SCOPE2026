# Sharp one-sided compact-recurrence confinement near a shared stable eigenvalue

## Finding
For the two-saddle, orientation-changing planar border-collision normal form, a stable-eigenvalue mismatch forces a precisely signed transverse displacement of **every bounded complete orbit**. Every compact two-sided invariant set is confined to an explicit one-sided strip about the right branch's stable-eigenvalue affine line. The coefficient of this strip cannot be reduced, even for compact invariant sets consisting of single fixed points. A stationary signed-displacement identity holds for all compactly supported invariant probabilities.

Let \(r_+=\max\{r,0}\). With the notation below, the exact complete-orbit response is
\[
H(p_n)=-\kappa\sum_{j=1}^\infty\lambda^{j-1}(-x_{n-j})_+.
\]
For each nonempty compact invariant set \(K\) with \(F(K)=K\), define \(R_K=\max_{(x,y)\in K}(-x)_+\). Then
\[
\begin{cases}-\kappa R_K/(1-\lambda)\le H(p)\le0,&\kappa\ge0,\\0\le H(p)\le-\kappa R_K/(1-\lambda),&\kappa\le0,\end{cases}\quad(p\in K).
\]
The bound is attained by the left fixed-point orbit. In particular the exact Euclidean perpendicular distance to \(H=0\) is at most \(|\kappa|R_K/((1-\lambda)\sqrt{1+\lambda^2})\), with the same sharp constant.

## Assumptions and scope
Consider \(F:\mathbb R^2\to\mathbb R^2\) defined by
\[
F(x,y)=\begin{cases}(\tau_Lx+y+1,-\delta_Lx),&x<0,\\(\tau_Rx+y+1,-\delta_Rx),&x\ge0.\end{cases}
\]
Assume \(\delta_L>0\), \(\tau_L>1+\delta_L\), \(\delta_R<0\), and \(\tau_R<-|1+\delta_R|\). The first two assumptions give left eigenvalues \(0<s_L<1<u_L\); the latter two give one negative right eigenvalue smaller than \(-1\) and a positive right eigenvalue \(0<\lambda<1\). Here \(\lambda\) is the positive root of \(\lambda^2-\tau_R\lambda+\delta_R=0\).

Define
\[
H(x,y)=y+\lambda x-\frac{\lambda}{1-\lambda},\qquad\kappa=\lambda\tau_L-\delta_L-\lambda^2.
\]
An entire orbit is indexed by all integers and satisfies \(F(p_n)=p_{n+1}\). Compact invariant means equality \(F(K)=K\), not merely \(F(K)\subset K\). The tube is relative to the natural left-excursion radius \(R_K\); no uniform bound independent of the size of \(K\) is claimed.

## Proof
**Exact affine defect.** Direct substitution into the two branch formulas and the right characteristic equation gives
\[
H(F(x,y))=\lambda H(x,y)+\kappa x\,\mathbf 1_{\{x<0\}}=\lambda H(x,y)-\kappa(-x)_+.
\]
The equality includes the switching line \(x=0\). Iterating from time \(n-m\) yields
\[
H(p_n)=\lambda^mH(p_{n-m})-\kappa\sum_{j=1}^m\lambda^{j-1}(-x_{n-j})_+.
\]
For a bounded entire orbit, \(H(p_{n-m})\) is bounded, so the first term vanishes as \(m\to\infty\). The sum converges absolutely because \(0<\lambda<1\), proving the formula.

**Every compact invariant set.** If \(F(K)=K\) and \(K\) is nonempty compact, each \(p\in K\) admits an infinite backward orbit in \(K\): recursively take any preimage in \(K\), possible by surjectivity of \(F|_K\). Compactness bounds all coordinates of this orbit. Each quantity \((-x_{n-j})_+\) is between \(0\) and \(R_K\), proving both signed inequalities. Dividing the absolute height by \(\sqrt{1+\lambda^2}\) gives the stated geometric distance.

**Sharpness.** The left branch has a fixed point \(Y=(u,-\delta_Lu)\) with \(u=(1-\tau_L+\delta_L)^-1<0\). The singleton \(K=\{Y\}\) is compact and satisfies \(F(K)=K\), with \(R_K=-u\). Applying the defect identity at \(Y\) gives \((1-\lambda)H(Y)=-\kappa(-u)\). Thus the nonzero strip boundary is exactly attained for every admissible parameter set with \(\kappa\ne0\); the zero-width case also has equality. Consequently no smaller universal coefficient multiplying \(|\kappa|R_K\) is valid.

**Stable mismatch and stationary measures.** Factor the left characteristic polynomial using its positive roots: \(\lambda^2-\tau_L\lambda+\delta_L=(\lambda-s_L)(\lambda-u_L)\). Hence \(\kappa=(\lambda-s_L)(u_L-\lambda)\), where \(u_L-\lambda>0\); the sign of \(\kappa\) is exactly the sign of the stable-eigenvalue mismatch. If \(\mu\) is compactly supported and \(F\)-invariant, all terms are bounded on its support, so integrating the defect identity immediately yields
\[
(1-\lambda)\int H\,d\mu=-\kappa\int(-x)_+\,d\mu.
\]
This identity is also sharp for \(\mu=\delta_Y\). If \(\kappa=0\), the complete-orbit formula gives \(H=0\) on all compact invariant sets, recovering the shared-eigenvalue phenomenon already in the literature; the new contribution is the exact **unequal-eigenvalue** signed confinement and its optimal quantitative coefficient.

## Verification
The symbolic proof requires only the two characteristic polynomials, an affine branch substitution, and convergence of a geometric series. An accompanying exact-rational checker independently evaluates branch identities and sharp singleton equality in multiple admissible rational coefficient families, including points on the switching boundary. It supports, but does not replace, the all-parameter proof.

For the example \((\tau_L,\delta_L,\tau_R,\delta_R)=(3,13/10,-2,-5/4)\), one has \(\lambda=1/2\), \(\kappa=-1/20\), \(Y=(-10/7,13/7)\), \(R_K=10/7\), and \(H(Y)=1/7\), exactly the positive endpoint of the predicted strip.

## Relationship to prior work
Ghosh, McLachlan, and Simpson (2024), Section 10 and Proposition 10.1, identify an invariant segment and skew-tent reduction when the stable eigenvalues **coincide**. Their discussion explicitly raises the behavior of nearly identical stable eigenvalues. Simpson (2025), Proposition 3.1, proves the more general exact affine contraction at a **shared** eigenvalue, forcing bounded invariant sets onto a hyperplane. Both equal-eigenvalue statements are prior results and are not asserted here as novel. The present theorem treats the unequal-eigenvalue regime and yields a signed, sharp, scale-aware tube and stationary defect balance where exact invariant-line reduction does not apply. It gives no assertion of an invariant manifold off the coincidence surface.

## Limitations
The strip is expressed relative to \(R_K\), which can be large or depend on parameters. It does not establish that chaotic attractors persist under perturbation, nor their Hausdorff continuity, entropy, connected-component counts, or a uniform global absorbing region. The bound is for bounded entire orbits/compact two-sided invariant sets; arbitrary bounded forward orbits have a corresponding limiting-width bound but need not satisfy the exact one-sided inequality at time zero. The shared-eigenvalue case is established prior work. Historical priority remains subject to literature outside the inspected texts, and no independent audit has been conducted.

## References
1. I. Ghosh, R. I. McLachlan, and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393v1 (first posted 2024-02-08), Section 10, Proposition 10.1. https://arxiv.org/html/2402.05393v1
2. D. J. W. Simpson, *Three forms of dimension reduction for border-collision bifurcations*, arXiv:2412.11114v1 (2024-12-15), Section 3, Proposition 3.1 and Remark 3.2. https://arxiv.org/abs/2412.11114
3. I. Ghosh, R. I. McLachlan, and D. J. W. Simpson, *Robust chaos in orientation-reversing and non-invertible two-dimensional piecewise-linear maps*, arXiv:2307.05144v1 (2023). https://arxiv.org/abs/2307.05144
