# Simultaneous spectral-optimal staggering of two Hardy and Bergman kernel polygons

## Finding
Fix an integer \(m\ge2\), radii \(0<r<s<1\), and \(p\in\{1,2\}\). Equip a holomorphic reproducing-kernel Hilbert space on the unit disk with kernel \(K_p(z,w)=(1-z\overline w)^{-p}\); \(p=1\) is Hardy space and \(p=2\) is normalized unweighted analytic Bergman space. For each \(\phi\in\mathbb R\), form \(2m\) unit-norm reproducing kernels at
\[
\{r e^{2\pi i j/m}:0\le j<m\}\ \cup\ \{s e^{i(\phi+2\pi j/m)}:0\le j<m\}.
\]
Let \(G_p(\phi)\) be their positive-definite Gram matrix, and let \(\boldsymbol\lambda_p(\phi)\) be its \(2m\) eigenvalues in nonincreasing order.

**Simultaneous spectral optimality.** For every \(\phi\), the vector \(\boldsymbol\lambda_p(\phi)\) majorizes \(\boldsymbol\lambda_p(\pi/m)\). Equivalently, for every real convex \(F\) defined on an interval containing the spectra,
\[
\operatorname{tr} F(G_p(\phi))\ge\operatorname{tr}F(G_p(\pi/m)).
\]
If \(F\) is strictly convex, equality occurs precisely when \(m\phi\equiv\pi\pmod{2\pi}\). In particular, the staggered relative rotation uniquely minimizes the largest eigenvalue, maximizes the smallest eigenvalue and determinant, minimizes the spectral condition number and every inverse Schatten trace \(\operatorname{tr}(G_p(\phi)^{-a})\), \(a>0\), all simultaneously, modulo rotations by \(2\pi/m\).

**Complete exact spectrum.** Put \(\rho=(rs)^m\), \(\zeta=e^{2\pi i/m}\), and
\[
S_{1,k}(z)=\frac1{1-z},\qquad
S_{2,k}(z)=\frac{k+1+(m-k-1)z}{(1-z)^2}
\quad(0\le k<m).
\]
For \(p\in\{1,2\}\), set
\[
A_{p,k}=m(1-r^2)^p r^{2k}S_{p,k}(r^{2m}),\qquad
B_{p,k}=m(1-s^2)^p s^{2k}S_{p,k}(s^{2m}),
\]
and
\[
C_{p,k}(\phi)=m[(1-r^2)(1-s^2)]^{p/2}(rs)^k e^{ik\phi}S_{p,k}(\rho e^{im\phi}).
\]
The \(2m\) eigenvalues are exactly the multiset of
\[
\lambda_{p,k}^{\pm}(\phi)=\frac{A_{p,k}+B_{p,k}\pm\sqrt{(A_{p,k}-B_{p,k})^2+4|C_{p,k}(\phi)|^2}}2,
\qquad 0\le k<m.
\]
Here the overall phase convention of \(C_{p,k}\) is immaterial because only its modulus enters the spectrum.

**Sharp determinant deficit in the Hardy case.** Write \(u=r^m\), \(v=s^m\), \(c=\cos(m\phi)\), and \(D_0=\prod_{k=0}^{m-1}A_{1,k}B_{1,k}>0\). Then
\[
\det G_1(\phi)=D_0\left(\frac{u^2+v^2-2uvc}{1+u^2v^2-2uvc}\right)^m.
\]
In particular the exact dimensionless angular deficit is
\[
\boxed{\displaystyle
\frac{\det G_1(\pi/m)}{\det G_1(\phi)}
=\left[1+\frac{2uv(1+c)(1-u^2)(1-v^2)}{(1+uv)^2(u^2+v^2-2uvc)}\right]^m.}
\]
It is strictly larger than one away from the staggered phases, and records the full nonlocal angular stability rather than just a local Hessian.

## Assumptions and scope
All integers \(m\ge2\), all \(0<r<s<1\), all real relative angles \(\phi\), and exactly the Hardy and unweighted Bergman kernel exponents \(p=1,2\) are included. Gram matrices consist of unit-norm point-evaluation representing vectors and are not the sampling operators for the full infinite-dimensional spaces. Majorization is the usual finite-dimensional Hardy–Littlewood–Pólya majorization, with equal total traces \(2m\). No assertion is made for arbitrary node placements, different orbit cardinalities, or other kernel exponents.

## Proof
The monomial kernel expansions are
\[
K_p(z,w)=\sum_{n=0}^\infty a_{p,n}(z\overline w)^n,\qquad a_{1,n}=1,\quad a_{2,n}=n+1.
\]
A normalized kernel at \(a\) is \(k_{p,a}(z)=(1-|a|^2)^{p/2}K_p(z,a)\). Apply the length-\(m\) discrete Fourier transform in each of the two cyclic orbits. Its residue-\(k\) vector has monomial support only in degrees \(n=k+m\ell\), with \(\ell\ge0\). Distinct residues are orthogonal. Consequently \(G_p(\phi)\) is unitarily equivalent to the orthogonal direct sum over \(0\le k<m\) of the Hermitian matrices
\[
\begin{pmatrix}A_{p,k}&C_{p,k}(\phi)\\\overline{C_{p,k}(\phi)}&B_{p,k}\end{pmatrix}.
\]
Geometric summation gives \(S_{1,k}\); the identity \(\sum_{\ell\ge0}(k+1+m\ell)z^\ell=[k+1+(m-k-1)z]/(1-z)^2\) gives \(S_{2,k}\). This proves the exact eigenvalues. Since all \(2m\) nodes are distinct, their kernel vectors are linearly independent: taking the coefficients of degrees \(0,\dots,2m-1\) in a hypothetical linear dependence produces a nonsingular Vandermonde system, after removing nonzero degree-dependent and node-dependent factors. Therefore every block is strictly positive definite.

Write \(t=(rs)^m\in(0,1)\) and \(c=\cos(m\phi)\). For \(p=1\),
\[
|S_{1,k}(t e^{im\phi})|^2=\frac1{1+t^2-2tc},
\]
which is strictly increasing in \(c\). For \(p=2\), put \(a=k+1>0\), \(b=m-k-1\ge0\), \(D=1+t^2-2tc>0\), and \(N=a^2+b^2t^2+2abt c\ge0\). Then
\[
|S_{2,k}(t e^{im\phi})|^2=\frac{N}{D^2},\qquad
\frac{d}{dc}\frac{N}{D^2}
=\frac{2abtD+4tN}{D^3}>0.
\]
Strictness holds because either \(b>0\) makes the first numerator summand positive, or \(b=0\) makes \(N=a^2>0\). Thus \(|C_{p,k}(\phi)|^2\) is strictly increasing with \(c\), in every residue block. The staggered phases are exactly those with \(c=-1\).

Each block's two eigenvalues have constant sum \(A_{p,k}+B_{p,k}\) and separation strictly increasing with \(|C_{p,k}|^2\). For each \(k\), the pair at any other phase majorizes its staggered pair. Concatenating finitely many pairwise mean-preserving spreads preserves majorization, proving the global eigenvalue result. The convex-trace inequality is the Hardy–Littlewood–Pólya characterization. Strictly convex equality, extremal-eigenvalue strictness, and inverse-moment strictness follow from strict pairwise spreading and finite positivity. For the condition number, the largest eigenvalue strictly increases and the smallest strictly decreases off the optimum.

For \(p=1\), the determinants of the blocks are
\[
A_{1,k}B_{1,k}\left(1-\frac{(1-r^{2m})(1-s^{2m})}{1+(rs)^{2m}-2(rs)^m c}\right).
\]
Factoring out \(D_0\) and simplifying the remaining fraction proves the determinant formula. Subtracting the fractions at \(c=-1\) and general \(c\) yields the boxed exact ratio. Positivity of every factor and strictness for \(c>-1\) are immediate.

## Verification
The standalone `verify.py` reconstructs the Gram matrix directly from the analytic kernels, independently constructs every Fourier block, compares all eigenvalues and spectral inequalities for \(p=1,2\), checks the Hardy determinant identity and exact deficit, and evaluates the symbolic positive Bergman derivative expression over finite test grids. Its recorded run passes 1,974 assertions. These computations are consistency checks only: the all-parameter statements follow from the analytical identities and majorization argument above. Run with Python 3 and NumPy: `python verify.py`.

## Relationship to prior work
Cabrelli–Molter–Suárez (2019) relate Hardy-kernel Riesz sequences and pseudo-hyperbolic geometry to multi-orbital frame criteria. Felder–Le (2021) develop Gram determinant constructions across Hardy and weighted analytic spaces. Boricheva (2022) studies reproducing-kernel Riesz families in model spaces. These supply context and standard tools; none of their inspected relevant statements fixes two unequal radii and proves simultaneous phase-optimality of the full Gram spectrum for both kernels. A published result titled *Sharp determinant stability and conditioning of concentric Szegő orbit frames* concerns placement of one fixed-radius orbit and does not logically imply the two-orbit relative-rotation result. The present theorem does **not** claim novelty of the DFT, Gram determinant, or Cauchy identities individually, nor any general frame characterization.

## Limitations
Only two equally sized regular orbits, only the two specified kernel exponents, and only relative angular design with fixed unequal radii are treated. The exact Hardy determinant identity may also be independently derived from the classical Cauchy determinant; novelty, if confirmed, rests on the simultaneous Hardy/Bergman spectral majorization and strict joint optimizer, not on that identity alone. Older specialized sampling-design literature may contain an equivalent result; exhaustive historical priority and independent verification are not claimed.

## References
1. C. Cabrelli, U. Molter, D. Suárez, *Multi-orbital frames through model spaces*, arXiv:1908.11011, first posted 2019-08-29. https://arxiv.org/abs/1908.11011
2. C. Felder, T. Le, *Analogues of Finite Blaschke Products as Inner Functions*, arXiv:2105.01766, first posted 2021-05-04. https://arxiv.org/abs/2105.01766
3. I. Boricheva, *Schur-Nevanlinna parameters, Riesz bases, and compact Hankel operators on the model space*, arXiv:2203.15372, first posted 2022-03-29. https://arxiv.org/abs/2203.15372
4. Published research record, *Sharp determinant stability and conditioning of concentric Szegő orbit frames*, record identifier `2026/10/11/SCOPE-sharp-determinant-stability-and-conditioning-of-concentric-szeg--44f30fce73fa` (single-radius-orbit comparison only).
