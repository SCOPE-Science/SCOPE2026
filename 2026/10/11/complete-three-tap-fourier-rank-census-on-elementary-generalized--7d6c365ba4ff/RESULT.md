# Complete three-tap Fourier-rank census on elementary generalized dihedral groups
## Finding
Let \(p\) be a prime, \(d\ge1\), \(A=\mathbb F_p^d\), \(N=p^d\), and \(G=A\rtimes C_2\), where the nonidentity element of \(C_2\) acts on \(A\) by inversion. For **every unordered three-element subset** \(S\subset G\), define the three-tap convolution on complex functions \(f:G\to\mathbb C\) by
\[
T_S f(x)=\sum_{s\in S}f(s^{-1}x),\qquad \nu(S)=\dim_{\mathbb C}\ker T_S.
\]
The exact nullity classification is as follows.

If \(p\ne3\), then \(\nu(S)=0\) for all \(\binom{2N}{3}\) supports. If \(p=3\), the possibilities depend only on how the three points occupy the two cosets of \(A\):

* **Mixed cosets:** when \(S\) has exactly one member in one coset and two in the other, \(\nu(S)=2N/3\).
* **Single coset, collinear:** when all members lie in one coset and their projections to \(A\) form an affine line over \(\mathbb F_3\), \(\nu(S)=4N/3\).
* **Single coset, noncollinear:** when all lie in one coset and their projections are affinely independent, \(\nu(S)=4N/9\). This last case requires \(d\ge2\).

These values and their **exact support multiplicities** are
\[
\begin{array}{c|c}
\nu(S)&\#\{S\subset G:|S|=3,\,\nu(S)\text{ as given}\}\\\hline
2N/3&N^2(N-1)\\
4N/3&N(N-1)/3\\
4N/9&N(N-1)(N-3)/3
\end{array}
\]
where the third row is omitted at \(d=1\). Thus for \(p=3\) the three-tap convolution is **always singular**, while for every other prime it is **always invertible**, regardless of the three taps. In each case the kernel is explicitly the inverse finite-group Fourier transform of the nullspaces of the two-dimensional blocks described below.

For example, at \(p=3,d=2\), among the \(816\) supports the nullities are \(4\) (\(144\) supports), \(6\) (\(648\) supports), and \(12\) (\(24\) supports).

## Assumptions and scope
The three taps are distinct, each has coefficient exactly one, and the group elements are arbitrary: they need not generate \(G\), need not form an inverse-closed set, and may include the identity. Rank and nullity are taken over \(\mathbb C\), not over \(\mathbb F_p\). We work with the finite group \(G\) and the unnormalized sum of three left translations; multiplying the operator by a nonzero scalar does not change its nullity. The case \(p=2\) is included: the inversion action is then trivial, and \(G\) is abelian.

## Proof
Write \(G\) as pairs \((a,\epsilon)\), where \(a\in A\), \(\epsilon\in\{0,1\}\), with multiplication
\[
(a,\epsilon)(b,\delta)=(a+(-1)^\epsilon b,\epsilon+\delta\pmod2).
\]
For each additive character \(\chi:A\to\mathbb T\), let
\[
R_\chi=\sum_{(a,0)\in S}\chi(a),\qquad
F_\chi=\sum_{(a,1)\in S}\chi(a).
\]
Inducing the character of the index-two subgroup \(A\), or equivalently Fourier transforming the two coset coordinates, produces one two-dimensional Fourier fiber for **each** \(\chi\in\widehat A\). On this fiber the sum of left translations is represented (up to a harmless unitary choice of coordinates) by
\[
B_\chi=
\begin{pmatrix}
R_\chi&F_\chi\\
\overline{F_\chi}&\overline{R_\chi}
\end{pmatrix}.
\]
These \(N\) blocks form a complete unitary decomposition of a \(2N\)-dimensional operator; this is still true when the induced representation is reducible. Consequently
\[
\nu(S)=\sum_{\chi\in\widehat A}\dim\ker B_\chi,
\qquad
\det B_\chi=|R_\chi|^2-|F_\chi|^2.
\]

When \(S\) meets both cosets, the sizes of its rotational and reflection parts are \(2\) and \(1\). Thus, after factoring out character values of modulus one, the determinant vanishes exactly when
\[
|1+z|=1,\qquad z=\chi(a-b),\quad a\ne b,
\]
where \(a,b\) are the locations of the two elements in the same coset. This is equivalent to \(z+\overline z=-1\), i.e. \(z\) is a primitive cube root of unity. Every singular block has rank \(1\), since its singleton character sum is nonzero. If \(p\ne3\), no \(p\)-th root of unity has this property. If \(p=3\), each nonzero \(a-b\) is sent to a primitive cube root by exactly \(2N/3\) characters. This proves the mixed-coset formula.

When all three taps lie in one coset, exactly one of \(R_\chi,F_\chi\) is a sum of three unit-modulus numbers, the other is zero. A singular block is then the **zero matrix** and contributes dimension \(2\). Three unit complex numbers sum to zero precisely when, up to a common phase and permutation, they are the three cube roots of unity. Thus no block is singular for \(p\ne3\). When \(p=3\), translate the locations so that their difference vectors are \(v_1=a_1-a_0\) and \(v_2=a_2-a_0\). The zero condition is
\[
(\chi(v_1),\chi(v_2))=(\omega,\omega^2)
\quad\text{or}\quad(\omega^2,\omega),
\qquad \omega=e^{2\pi i/3}.
\]
If the three locations are collinear, their distinctness forces \(v_2=-v_1\), so the condition holds for \(2N/3\) characters and gives nullity \(4N/3\). Otherwise \(v_1,v_2\) are linearly independent, the character map to \(\mathbb F_3^2\) is surjective, and exactly \(2N/9\) characters satisfy the condition, giving nullity \(4N/9\). In all cases this also describes the complete Fourier kernel: retain the full \(\mathbb C^2\) fiber for a zero block, or the line spanned by \((F_\chi,-R_\chi)\) for a nonzero singular block, and annihilate all other fibers.

To count supports, the mixed-coset choices number \(2\binom N2N=N^2(N-1)\). In \(\mathbb F_3^d\), every pair of distinct points belongs to exactly one affine three-point line. Hence the number of lines is \(\binom N2/3=N(N-1)/6\). Choosing one of the two cosets gives \(N(N-1)/3\) collinear supports. The remaining single-coset supports number
\[
2\binom N3-\frac{N(N-1)}3
=\frac{N(N-1)(N-3)}3.
\]
The three counts sum to \(\binom{2N}{3}\), proving exhaustiveness and the claimed exact census.

## Verification
The standalone Python 3 script `check_triads.py` constructs the entire finite group, the left-convolution matrix, and its rank using elimination modulo \(1000003\), independently of the Fourier-block proof. It exhaustively verifies all \(56\), \(560\), \(20\), \(816\), and \(120\) three-element supports in the tested groups \((p,d)=(2,2),(2,3),(3,1),(3,2),(5,1)\), respectively, and tests \(81\) additional supports at \((3,3)\). It checks the predicted nullities and the complete support census in the exhaustive cases. Invoke `python3 check_triads.py` from the directory containing that file. These finite-field modular tests are **not** complex-rank certificates for arbitrary sizes; unrestricted correctness follows from the Fourier decomposition and elementary character counting just proved.

## Relationship to prior work
Arezoomand and Taeri (2013) establish the general representation-theoretic decomposition and characteristic-polynomial method for Cayley digraphs. The decomposition itself is prior work; the present statement specializes it to three unweighted taps on a specific noncommutative group family, identifies all singular supports, resolves each complex nullity, and obtains a closed support census. Huang, Huang, and Lu (2016, §2) compute spectra of **undirected** cubic Cayley graphs on cyclic dihedral groups and classify their graph isomorphism types; some cyclic symmetric cases of the present formula are therefore already consequences of their results. The noncyclic elementary-abelian groups, arbitrary nonsymmetric/identity-containing supports, and exact census are not treated there. This statement makes no claim that the Fourier block method is new.

## Limitations
The result is confined to unit coefficients and elementary-abelian inversion kernels; unequal complex tap weights, larger supports, and other semidirect actions may behave differently. The nonsingularity statement is over characteristic zero and does not assert the same rank over every finite coefficient field. Generic finite-group spectral formulas and older case-by-case studies create a residual historical-equivalence risk; independent literature certification has not been performed. The script tests only finite instances and does not prove any general statement by enumeration.

## References
1. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of \(n\)-Cayley Digraphs*, Electronic Journal of Combinatorics 20(3) (2013), P57, published 2013-10-07. DOI: https://doi.org/10.37236/3105 ; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/ .
2. X. Huang, Q. Huang, and L. Lu, *Enumeration of Cubic Cayley Graphs on Dihedral Groups*, arXiv:1609.05419v1 (2016-09-18), https://arxiv.org/html/1609.05419v1 .
