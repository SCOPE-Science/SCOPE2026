# Exact harmonic sampling spectrum of the 56 Gosset vertices

## Finding
Let \(X\subset S^6\) be the 56 normalized vertices of the seven-dimensional Gosset \(3_{21}\) polytope as specified below. For every integer \(k\ge0\), the exact-degree spherical-harmonic evaluation on \(X\) has ranks
\[
1,\ 7,\ 27,\ 21,\ 27,\ 28,\ 28,\ 28,\ldots
\]
for degrees \(k=0,1,2,3,4,5,6,7,\ldots\), respectively. In every degree \(k\ge5\), evaluation maps onto the entire 28-dimensional antipodal parity sector. The **first** consecutive pair of degrees spanning all 56 point values is \(5,6\); degrees \(4,5\) attain rank 55. The complete Gram eigenvalues and multiplicities are given in the proof.

## Assumptions and scope
Put \(W=\{y\in\mathbb R^8:\sum_{i=1}^8y_i=0\}\), an inner-product space of dimension 7. For each unordered two-element set \(e\subset\{1,\ldots,8\}\), let \(v_e=(w_{e,1},\ldots,w_{e,8})/\sqrt{24}\), where \(w_{e,i}=3\) for \(i\in e\) and \(w_{e,i}=-1\) otherwise. Thus \(\|v_e\|=1\) and \(X=\{v_e,-v_e:|e|=2\}\subset S(W)=S^6\) has exactly 56 points.

Let \(\mathcal H_k(W)\) denote the real restrictions to \(S(W)\) of homogeneous harmonic polynomials of exact degree \(k\), where \(k\) is any integer at least zero. Write \(E_k:\mathcal H_k(W)\to\mathbb R^X\) for point evaluation. Let \(P_k\) denote the normalized degree-\(k\) zonal Gegenbauer polynomial in dimension seven, specified uniquely by \(P_0(t)=1\), \(P_1(t)=t\), and
\[
(k+4)P_k(t)=(2k+3)tP_{k-1}(t)-(k-1)P_{k-2}(t),\qquad k\ge2.
\]
Thus \(P_k(1)=1\). Define \(c_k=P_k(1/3)\) and \(\Gamma_k=(P_k(x\cdot y))_{x,y\in X}\). The addition theorem makes \(\Gamma_k\) a positive multiple of \(E_kE_k^{\mathsf T}\), so their ranks coincide. This result concerns the real exact-degree harmonic spaces; the complexified ranks are the same.

## Proof
**Step 1: two inner products and the Seidel matrix.** For different two-element sets \(e,f\), direct substitution gives
\[
v_e\cdot v_f=\frac{2|e\cap f|-1}{3}\in\{-1/3,1/3\}.
\]
Index the 28 sets \(e\) by the edges of \(K_8\). Let \(B\) be their 28-by-8 incidence matrix, \(A=BB^{\mathsf T}-2I\) the adjacency matrix of the triangular graph \(T(8)\), and \(J\) the all-one 28-by-28 matrix. Define
\[
S=2A-J+I=2BB^{\mathsf T}-3I-J.
\]
Then \(S_{ee}=0\) and, for \(e\ne f\), \(S_{ef}=3(v_e\cdot v_f)\). The identity \(B^{\mathsf T}B=6I_8+J_8\) shows that \(S\) has eigenvalue \(9\) on the seven-dimensional image of the coordinate-sum-zero space under \(B\) and eigenvalue \(-3\) on its 21-dimensional orthogonal complement. On the constants, \(S\mathbf1=-3\mathbf1\). Equivalently, \(S^2-6S-27I=0\), with eigenvalue multiplicities \(9^{(7)}\) and \((-3)^{(21)}\).

**Step 2: the complete Gram spectra.** Since \(P_k(-t)=(-1)^kP_k(t)\), the 56-by-56 Gram matrix has block form
\[
\Gamma_k=\begin{pmatrix}K_k&(-1)^kK_k\\(-1)^kK_k&K_k\end{pmatrix},
\]
where, for even \(k\), \(K_k=(1-c_k)I+c_kJ\), and for odd \(k\), \(K_k=I+c_kS\). Hence 28 eigenvalues are zero from the wrong antipodal parity. The 28 eigenvalues in the correct parity sector are
\[
\begin{array}{ll}
2(1+27c_k)\ (1\text{ time}),\quad2(1-c_k)\ (27\text{ times}),&k\text{ even},\\
2(1+9c_k)\ (7\text{ times}),\quad2(1-3c_k)\ (21\text{ times}),&k\text{ odd}.
\end{array}
\]
These are *all* the eigenvalues, with multiplicities; their zeros are accounted for in the rank claim.

**Step 3: low degrees.** The recurrence gives the exact values
\[
(c_0,c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9)
=(1,\tfrac13,-\tfrac1{27},-\tfrac19,-\tfrac1{27},\tfrac{23}{729},\tfrac{25}{729},\tfrac1{2187},-\tfrac{389}{19683},-\tfrac{215}{19683}).
\]
Substitution in Step 2 yields ranks \(1,7,27,21,27\) for degrees \(0\) through \(4\). Moreover \(|c_k|<1/27\) for each \(5\le k\le9\), so no eigenvalue is zero in the permitted parity sector for these degrees.

**Step 4: strict nonvanishing in all high degrees.** The normalized Gegenbauer integral representation at the argument \(t=1/3\) is
\[
c_k=\mathbb E\left(\frac13+\frac{2\sqrt2}{3}iU\right)^k,
\qquad U^2\sim\operatorname{Beta}(1/2,5/2).
\]
Its even moments satisfy \(\mathbb E U^{2j}=\prod_{r=0}^{j-1}(2r+1)/(2r+6)\). Since \(|(1+2\sqrt2 iU)/3|\le1\), for every integer \(k\ge10\) we have
\[
|c_k|\le\mathbb E\left(\frac{1+8U^2}{9}\right)^{k/2}
\le\mathbb E\left(\frac{1+8U^2}{9}\right)^5
=\frac{965}{59049}<\frac1{27}.
\]
For even \(k\), both \(1+27c_k\) and \(1-c_k\) are then positive; for odd \(k\), both \(1+9c_k\) and \(1-3c_k\) are positive. Thus every exact harmonic degree \(k\ge5\) has rank 28 and spans the corresponding antipodal parity sector. Consecutive degrees have opposite parity and complementary images. The pair \(4,5\) has rank \(27+28=55\), whereas every pair \(k,k+1\) with \(k\ge5\) has rank \(28+28=56\). Every earlier pair has rank less than 56. This completes the proof.

## Verification
The self-contained `check_gosset.py` uses exact rational arithmetic and no third-party packages. It reconstructs all 28 edge labels, verifies the 28-by-28 Seidel quadratic relation and eigenspace multiplicities, calculates exact Gegenbauer values through degree 30, independently checks the beta-moment constant \(965/59049\), and calculates exact rational ranks of the 28-by-28 Gram blocks through degree 12. Reproduce with `python3 check_gosset.py`; the expected terminating line starts with `GOSSET_HARMONIC_EXACT_CHECK_OK`.

The **all-degree** proof is the analytic moment bound in Step 4; the finite checker is supplementary and not claimed as an infinite certificate.

## Relationship to prior work
Normalized spherical harmonic addition kernels and the notion of harmonic-index designs are developed by Bannai, Okuda, and Tagami [1]. The classical Seidel-matrix approach to equiangular line sets is described by Greaves, Koolen, Munemasa, and Szöllősi [2]; a positive-semidefinite programming approach using Gegenbauer polynomials appears in Barg and Yu [3]. The 56-point Gosset configuration and its tight spherical-design geometry are classical. Those sources supply known ingredients. In the sections actually inspected, none states this all-degree rank sequence, the precise fourth-degree defect, or the sharp consecutive-degree interpolation threshold. The result is an explicit application of those ingredients to a specific canonical finite configuration, with no assertion that older literature could not contain an equivalent formulation.

## Limitations
The statement is restricted to the 56-vertex Gosset configuration and exact-degree spherical harmonics; it neither classifies arbitrary finite spherical codes nor gives stability under perturbations. Some older work on tight spherical 5-designs and association schemes was not available as full text, so an implicit equivalent spectral statement remains an originality risk. The numerical checks do not replace the infinite-degree argument. No independent mathematical audit or external validation has been performed.

## References
[1] E. Bannai, T. Okuda, and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101 (first posted 2013-08-23), https://arxiv.org/abs/1308.5101.

[2] G. Greaves, J. H. Koolen, A. Munemasa, and F. Szöllősi, *Equiangular lines in Euclidean spaces*, arXiv:1403.2155 (first posted 2014-03-10), https://arxiv.org/abs/1403.2155.

[3] A. Barg and W.-H. Yu, *New bounds for equiangular lines*, arXiv:1311.3219 (first posted 2013-11-13), https://arxiv.org/abs/1311.3219.
