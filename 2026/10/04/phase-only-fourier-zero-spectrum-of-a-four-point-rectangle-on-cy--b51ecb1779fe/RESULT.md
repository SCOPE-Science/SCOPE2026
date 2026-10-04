# Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups

## Finding
Let \(m,n\ge2\), let \(G=\mathbb Z_m\times\mathbb Z_n\), and let
\[
A=\{(0,0),(1,0),(0,1),(1,1)\}\subset G.
\]
Suppose \(f:G\to\mathbb C\) has support exactly \(A\) and its four nonzero values have one common magnitude. Then the attainable Fourier-zero counts are exactly
\[
\begin{cases}
\{0,2,m,n,m+n-1\},&m\text{ and }n\text{ are both even},\\
\{0,1,m,n,m+n-1\},&\text{otherwise}.
\end{cases}
\]
Equivalently, the Fourier-support sizes are obtained by subtracting those cardinalities from \(mn\).

There is also a structural classification. Write
\[
a=f(0,0),\quad b=f(1,0),\quad c=f(0,1),\quad d=f(1,1),
\]
and define the unimodular cross phase
\[
\eta=\frac{ad}{bc}.
\]
If \(\eta=1\), the Fourier zero set is the union of at most one full character row and at most one full character column. If \(\eta\ne1\), there are at most two Fourier zeros. Two occur only when both \(m\) and \(n\) are even; otherwise at most one occurs.

## Assumptions and scope
The Fourier transform is
\[
\widehat f(k,\ell)=\sum_{(x,y)\in G}f(x,y)
\exp\!\left(-2\pi i\left(\frac{kx}m+\frac{\ell y}n\right)\right),
\]
although any nonzero normalization gives the same zero set. The statement concerns the fixed Cartesian four-point rectangle and the phase-only condition that \(|a|=|b|=|c|=|d|>0\). It does not classify arbitrary four-point supports or arbitrary coefficient magnitudes.

## Proof
Divide by \(a\), and put
\[
\alpha=\frac ba,\qquad \beta=\frac ca,\qquad \gamma=\frac da.
\]
All three numbers are unimodular. At a character \((k,\ell)\), set
\[
z=e^{-2\pi i k/m},\qquad w=e^{-2\pi i\ell/n}.
\]
Then, up to the harmless scalar \(a\),
\[
\widehat f(k,\ell)=1+\alpha z+\beta w+\gamma zw.
\]
Now set \(Z=\alpha z\), \(W=\beta w\), and
\[
\eta=\frac{\gamma}{\alpha\beta}=\frac{ad}{bc}.
\]
Thus \(Z\) ranges over the rotated regular \(m\)-gon \(\alpha\mu_m\), \(W\) ranges over the rotated regular \(n\)-gon \(\beta\mu_n\), and the zero equation is
\[
1+Z+W+\eta ZW=0.
\]

If \(\eta=1\), then
\[
1+Z+W+ZW=(1+Z)(1+W).
\]
The condition \(Z=-1\) either misses \(\alpha\mu_m\) or selects exactly one value of \(z\), and in the latter case it contributes a full row of \(n\) Fourier zeros. Similarly \(W=-1\) contributes either no zeros or a full column of \(m\) zeros. If both occur, their intersection is counted once, so the possible counts in this factorable case are
\[
0,\qquad n,\qquad m,\qquad m+n-1.
\]

Assume now that \(\eta\ne1\). The equation cannot have \(1+\eta Z=0\), because then it would also force \(1+Z=0\), hence \(\eta=1\). Therefore
\[
W=-\frac{1+Z}{1+\eta Z}.
\]
Since \(Z\) and \(W\) lie on the unit circle, a zero must satisfy
\[
|1+Z|=|1+\eta Z|.
\]
Using \(|Z|=|\eta|=1\), squaring and multiplying by \(Z\) gives
\[
(1-\eta)Z^2=\eta^{-1}-1,
\]
hence
\[
Z^2=\eta^{-1}.
\]
Choose \(s\) with \(s^2=\eta^{-1}\). Because \(\eta\ne1\), \(s\ne\pm1\). Direct substitution gives exactly two unit-torus zeros:
\[
(Z,W)=(s,-s),\qquad (Z,W)=(-s,s).
\]

A rotated \(m\)-th-root grid contains both \(s\) and \(-s\) exactly when \(m\) is even. Consequently, once one of these two torus zeros lies in \(\alpha\mu_m\times\beta\mu_n\), the other lies there as well exactly when both \(m\) and \(n\) are even. Thus the nonfactorable case has zero count \(0\) or \(2\) when both factors are even, and zero count \(0\) or \(1\) otherwise.

It remains to show attainability. Let
\[
u_r=e^{\,i\pi/(2r)}.
\]
The following unimodular coefficient quadruples \((a,b,c,d)\) realize the required counts:
\[
(1,u_m,u_n,u_mu_n)\quad\text{gives }0,
\]
\[
(1,-1,u_n,-u_n)\quad\text{gives }n,
\]
\[
(1,u_m,-1,-u_m)\quad\text{gives }m,
\]
\[
(1,-1,-1,1)\quad\text{gives }m+n-1.
\]
Indeed, \(u_r\mu_r\) does not contain \(-1\). Finally,
\[
(1,i,-i,-1)
\]
has \(\eta=-1\) and a zero at \((z,w)=(1,1)\). Its second unit-torus zero corresponds to \((z,w)=(-1,-1)\), so this witness has two Fourier zeros when both \(m,n\) are even and exactly one otherwise. This proves both necessity and sufficiency.

## Verification
The analytic argument proves the theorem for all \(m,n\ge2\). The standalone checker `artifacts/verify.py` corroborates the explicit witnesses on every \(2\le m,n\le40\) and verifies the parity-dependent isolated-zero count directly from the discrete Fourier sums. It also checks the two-unit-torus-zero formula for a deterministic family of nonfactorable phase choices. The finite replay is corroborative and is not used to infer the universal statement.

## Relationship to prior work
Bonami and Ghobber study uncertainty minima and equality cases for finite Abelian groups, including \(\mathbb Z_p\times\mathbb Z_p\). Their fixed-\(k\) results classify functions attaining the minimum possible Fourier-support size, rather than the complete zero-count spectrum on one prescribed rectangle under equal-magnitude coefficients. In particular, the phase-only cross-ratio dichotomy above is not a consequence of their stated equality-case theorem.

Delvaux and Van Barel study rank-deficient submatrices of Kronecker products of Fourier matrices. That framework is directly relevant to rectangular Fourier structure but allows unrestricted null vectors and focuses on maximal rank deficiency. The official abstract inspected for their Kronecker-product paper does not impose equal coefficient magnitudes or state the cross-phase classification above. The full report was not available during this review, so an equivalent formulation hidden there remains a residual literature risk.

Two prior fixed-support computations classify unrestricted coefficient spectra for affine parallelograms over \(\mathbb F_3\) and \(\mathbb F_5\). Those statements allow arbitrary nonzero coefficients and therefore do not imply this all-\((m,n)\) phase-only classification; conversely, the present result is a coefficient-rigidity refinement rather than an unrestricted support-spectrum theorem.

## Limitations
The argument uses both the rectangular support and equality of all four coefficient magnitudes. Removing either hypothesis can create additional zero counts. No assertion is made for non-Cartesian four-point configurations or for higher-dimensional boxes. The strongest residual originality risk is older Fourier-matrix or sequence-design literature phrased in terms of unimodular null vectors rather than sparse Fourier zeros.

## References
1. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, submitted 26 March 2010; later published in *Acta Scientiarum Mathematicarum* 79 (2013), 507-528. The paper lists primary MSC \(42A99\).
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, *Linear Algebra and its Applications* 426 (2007), 349-367, DOI 10.1016/j.laa.2007.05.009.
