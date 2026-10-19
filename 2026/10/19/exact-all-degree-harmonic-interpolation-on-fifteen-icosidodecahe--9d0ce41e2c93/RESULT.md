# Exact all-degree harmonic interpolation on fifteen icosidodecahedral root lines

## Finding
Let \(X\subset S^2\) consist of one unit representative from each of the fifteen antipodal lines of the noncrystallographic root system \(H_3\), equivalently the vertices of an icosidodecahedron modulo antipodes. For each integer \(\ell\ge0\), let \(E_\ell\colon\mathcal H_\ell(S^2;\mathbb C)\to\mathbb C^{15}\) evaluate homogeneous spherical harmonics of the **single** degree \(\ell\) on these representatives. Then the complete rank sequence is
\[
\bigl(\operatorname{rank}E_\ell\bigr)_{\ell=0}^{15}
=(1,3,5,7,9,11,10,15,14,15,15,15,15,15,14,15),
\]
and \(\operatorname{rank}E_\ell=15\) for **every** integer \(\ell\ge15\).

Thus arbitrary complex data are interpolable already in degree \(7\), not in degree \(8\), again in degrees \(9\) through \(13\), not in degree \(14\), and then in every degree \(\ell\ge15\). At each of the exceptional degrees \(\ell=8,14\), the image consists **exactly** of the data \(y\in\mathbb C^{15}\) satisfying \(\sum_j y_j=0\). The degree-\(6\) image has dimension \(10\).

Whenever a datum \(y\) is attainable, the theorem supplies its minimum-norm harmonic interpolant and norm through the explicit reproducing-kernel Gram pseudoinverse described below. In particular, the permanent full-rank cutoff \(15\) is sharp because the rank at degree \(14\) is \(14\).

## Assumptions and scope
All dimensions, ranks and norms are over \(\mathbb C\). Use rotation-invariant **probability** surface measure on \(S^2\). Let \(\varphi=(1+\sqrt5)/2\). Choose the fifteen sample representatives to be the three positive coordinate vectors together with the twelve vectors obtained from cyclic permutations of \((1/2,\varphi/2,1/(2\varphi))\) by independently changing the signs of its second and third coordinates. These are unit vectors and represent fifteen distinct antipodal lines. No weights or lower harmonic degrees are added.

Write \(P_\ell\) for the Legendre polynomial normalized by \(P_\ell(1)=1\). Define the unscaled matrix \(L_\ell=(P_\ell(x_i\cdot x_j))_{1\le i,j\le15}\) and the reproducing-kernel Gram matrix \(G_\ell=(2\ell+1)L_\ell\). The ordering of the samples is immaterial. An arbitrary replacement \(x_j\mapsto-x_j\) conjugates the odd-degree Gram matrix by a diagonal sign matrix and does not change its rank.

## Proof
**Kernel reduction.** The spherical-harmonic addition theorem for probability surface measure gives the kernel \(K_\ell(x,z)=(2\ell+1)P_\ell(x\cdot z)\), hence \(G_\ell=E_\ell E_\ell^*\). Consequently \(L_\ell\) is positive semidefinite and \(\operatorname{rank}E_\ell=\operatorname{rank}L_\ell\) for every nonnegative integer \(\ell\).

**Exact root geometry.** Direct multiplication of the coordinates specified above shows that each sample is unit length, no two are antipodal, and each row of \(L_\ell\) has exactly two off-diagonal inner products equal to zero and four each with absolute inner product \((\sqrt5-1)/4\), \(1/2\), and \((\sqrt5+1)/4\). This yields precisely \(15\), \(30\), \(30\), \(30\) unordered pairs in the four respective absolute-inner-product classes. All calculations consequently lie in the quadratic field \(\mathbb Q(\sqrt5)\).

**Finite exact degrees.** The recurrence
\[
P_0(t)=1,\qquad P_1(t)=t,\qquad
(k+1)P_{k+1}(t)=(2k+1)tP_k(t)-kP_{k-1}(t)
\]
computes every matrix entry exactly. Gaussian elimination in \(\mathbb Q(\sqrt5)\) gives the complete sixteen ranks for \(0\le\ell\le15\) displayed in the Finding. The same exact field calculation shows \(L_8\mathbf1=L_{14}\mathbf1=0\); their rank \(14\) therefore proves that their kernels are precisely \(\mathbb C\mathbf1\), giving the asserted mean-zero images.

For each \(16\le\ell\le215\), the separately embedded integer certificate records a **nonzero** determinant of the reduction of \(L_\ell\) in \(\mathbb F_{1009}\), under \(\sqrt5\mapsto244\), where \(244^2\equiv5\pmod{1009}\). The recurrence denominators are products of integers not divisible by \(1009\) in this range, and the sample coordinates have only powers of two in their denominators. Hence all reductions are well-defined. A nonzero reduced determinant implies a nonzero determinant in characteristic zero. This certifies all \(200\) intermediate degrees without a floating-point rank threshold. The attached `checker.py` reconstructs the matrices, performs the field arithmetic, and verifies every recorded residue in `certificate.json`.

**All remaining degrees.** Bernstein's classical Legendre bound (Szegő, *Orthogonal Polynomials*, Theorem 7.3.3) gives for \(-1<t<1\)
\[
|P_\ell(t)|\le\sqrt{\frac{2}{\pi(\ell+1/2)}}\,(1-t^2)^{-1/4}.
\]
Among distinct sample lines the maximum absolute inner product is \((1+\sqrt5)/4\), and therefore \(1-t^2\ge(5-\sqrt5)/8>81/256=(3/4)^4\). Thus each of the twelve nonzero off-diagonal terms obeys the bound with extra factor strictly below \(4/3\), and the two zero-inner-product terms have factor one. The sum of absolute off-diagonal entries in any row is consequently strictly smaller than
\[
\left(2+12\cdot\frac43\right)\sqrt{\frac{2}{\pi(\ell+1/2)}}
=18\sqrt{\frac{2}{\pi(\ell+1/2)}}
<18\sqrt{\frac{2}{3(\ell+1/2)}}<1
\]
for every integer \(\ell\ge216\). Since the diagonal entries of \(L_\ell\) equal one, strict diagonal dominance makes \(L_\ell\) nonsingular. Combining the finite certificate and this analytic tail proves the all-degree rank classification.

**Reconstruction.** For any attainable vector \(y\), let \(G_\ell^\dagger\) be the Moore–Penrose inverse of the explicitly defined Gram matrix. Then
\[
 f_y(x)=\sum_{j=1}^{15}(G_\ell^\dagger y)_j\,K_\ell(x,x_j),
 \qquad \|f_y\|_{L^2(S^2)}^2=y^*G_\ell^\dagger y.
\]
The formula follows from the adjoint evaluation operator and Hilbert-space projection onto the orthogonal complement of its kernel. It is the unique interpolant of least \(L^2\) norm. If \(G_\ell\) is invertible, this interpolates every \(y\).

## Verification
Execute `python3 checker.py` with the attached `certificate.json` in the same directory; no nonstandard Python packages are required. The checker constructs every coordinate in \(\mathbb Q(\sqrt5)\), independently verifies unit lengths and all four pair classes, performs exact Gaussian elimination for the first sixteen degrees, checks exact constant-vector annihilation at degrees \(8\) and \(14\), and verifies \(200\) separate nonzero modular determinants for degrees \(16\) through \(215\). The analytical Bernstein argument covers the infinite tail, which is **not** claimed to be verified by finite computation.

## Relationship to prior work
Spherical-harmonic reproducing kernels and harmonic-index spherical designs are classical. Bannai, Okuda and Tagami explicitly discuss an antipodal half of the regular **icosahedron** as a harmonic-index design in degrees \(8\) and \(14\); their studied six-line orbit differs from the present fifteen-line **icosidodecahedral** orbit. Cohan's earlier icosahedral symmetry-harmonic expansions cover irreducible representation bases through degree \(14\); they do not explicitly supply an all-degree pointwise evaluation-rank classification in the accessible summary, although their tables might imply some of the low-degree comparisons. The present claim concerns the complete image of each single-degree evaluation map, not only the vanishing of its mean or the existence of invariant harmonics.

## Limitations
No exact condition-number optimization, noisy reconstruction guarantee, or interpolation theorem for arbitrary point perturbations is asserted. The finite rank certificate is an exact, reproducible characteristic-zero nonvanishing argument via modular reductions, but the unrestricted degree range additionally relies on the stated classical analytic inequality. Prior full-text comparison with Cohan (1958) was unavailable, so an implicit older low-degree equivalent remains a priority risk. The claim is not independently audited.

## References
1. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1, publicly submitted 2013-08-23, especially Introduction, Definition 1.1 and Lemma 2.1. https://arxiv.org/abs/1308.5101
2. N. V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group*, Proceedings of the Cambridge Philosophical Society 54 (1958), 28–38. https://doi.org/10.1017/S0305004100033156
3. G. Szegő, *Orthogonal Polynomials*, fourth edition, American Mathematical Society, 1975, Theorem 7.3.3 (Bernstein bound).
4. Y. Zheng and P. C. Doerschuk, *Explicit Computation of Orthonormal Symmetrized Harmonics with Application to the Identity Representation of the Icosahedral Group*, SIAM Journal on Mathematical Analysis. https://doi.org/10.1137/S0036141098341770
