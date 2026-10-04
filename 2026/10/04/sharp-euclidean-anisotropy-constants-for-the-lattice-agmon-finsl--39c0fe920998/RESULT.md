# Sharp Euclidean anisotropy constants for the lattice Agmon–Finsler norm
## Finding
For \(d\ge 2\) and \(E<0\), define
\[
K^E=\{\xi\in\mathbb R^d:4\sum_{j=1}^d\sinh^2(\xi_j/2)\le |E|\}
\]
and \(\rho_E(x)=\sup_{\xi\in K^E}\langle x,\xi\rangle\). Then
\[
2\operatorname{arsinh}(\sqrt{|E|}/2)|x|_2\le \rho_E(x)\le 2\sqrt d\operatorname{arsinh}(\sqrt{|E|}/(2\sqrt d))|x|_2.
\]
Both constants are sharp. For nonzero \(x\), lower equality holds exactly on coordinate-axis directions and upper equality exactly when \(|x_1|=\cdots=|x_d|\). Thus the sharp anisotropy ratio tends to \(1\) as \(E\uparrow0\) and to \(\sqrt d\) as \(E\to-\infty\).

## Assumptions and scope
The normalization is the standard nearest-neighbor lattice Schrödinger operator, whose complexified kinetic symbol is \(q(\xi)=4\sum_{j=1}^d\sinh^2(\xi_j/2)\). The claim concerns the constant-energy Agmon body \(K^E=\{q\le |E|\}\) and its support norm. It does not assert that arbitrary potentials possess eigenfunctions saturating every extremal rate.

## Proof
Put \(r=|\xi|_2\) and \(t_j=\xi_j^2\). Then
\[
q(\xi)=2\sum_j(\cosh\xi_j-1)=\sum_{m\ge1}\frac{2}{(2m)!}\sum_j t_j^m.
\]
At fixed \(\sum_jt_j=r^2\), for every \(m\ge1\),
\[
d^{1-m}r^{2m}\le\sum_jt_j^m\le r^{2m}.
\]
For \(m\ge2\), left equality holds exactly when all \(t_j\) are equal, and right equality exactly when all but at most one vanish. Summing the positive series coefficients gives
\[
4d\sinh^2\left(\frac{r}{2\sqrt d}\right)\le q(\xi)\le4\sinh^2\left(\frac r2\right).
\]
Hence, with
\[
r_-=2\operatorname{arsinh}(\sqrt{|E|}/2),\qquad r_+=2\sqrt d\operatorname{arsinh}(\sqrt{|E|}/(2\sqrt d)),
\]
one has the sharp inclusions \(r_-B_2^d\subset K^E\subset r_+B_2^d\). Taking support functions proves the bounds. Strictness of the radial inequalities away from their equality sets gives the axis and main-diagonal equality classification. Finally \(\operatorname{arsinh}s\sim s\) as \(s\downarrow0\) and \(\operatorname{arsinh}s=\log(2s)+o(1)\) as \(s\to\infty\), yielding the ratio limits.

## Verification
The proof is analytic. The bundled verifier independently checks the two boundary radii, solves the support maximization through its Lagrange multiplier equation for representative directions, and stress-tests the radial inequalities. Finite checks are corroborative only.

## Relationship to prior work
Kameoka defines exactly this \(K^E\) and \(\rho_E\) for the standard discrete Schrödinger operator and proves Agmon decay controlled by this anisotropic support norm. The inspected paper leaves the sharp Euclidean inner and outer radii implicit. Klein and Rosenberger develop a broader Agmon–Finsler framework for difference operators without these explicit nearest-neighbor constants. Ito and Jensen give low-dimensional resolvent formulas rather than this all-dimensional convex-body invariant.

## Limitations
The result is a sharp norm comparison for the constant-energy body, not a converse eigenfunction-realization theorem. In \(d=1\), axis and diagonal coincide and both constants are identical. Targeted searches found no equivalent sharp Euclidean-envelope statement, but an equivalent elementary convex-body calculation may exist under different terminology.

## References
1. Kentaro Kameoka, “Semiclassical analysis and the Agmon-Finsler metric for discrete Schrödinger operators,” arXiv:2108.11078; DOI 10.3934/cpaa.2023024.
2. Markus Klein and Elke Rosenberger, “Agmon-Type Estimates for a Class of Difference Operators,” DOI 10.1007/s00023-008-0383-7.
3. Koji Ito and Arne Jensen, “Hypergeometric expression for the resolvent of the discrete Laplacian in low dimensions,” arXiv:2004.05866.
