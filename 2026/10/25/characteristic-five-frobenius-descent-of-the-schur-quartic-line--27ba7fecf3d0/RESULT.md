# Characteristic-five Frobenius descent of the Schur quartic line and four-line-plane configurations

## Finding
Let \(S\subset\mathbf P^3_{\mathbf F_5}\) be the smooth quartic
\[
X^4-XY^3=Z^4-ZW^3.
\]
Its geometric Fano scheme of lines consists of exactly 64 reduced points; all are defined over \(\mathbf F_{25}\), and geometric Frobenius has cycle type \(1^8 2^{28}\). The eight \(\mathbf F_5\)-rational lines have intersection graph \(K_{2,6}\).

Exactly 72 distinct geometric hyperplanes have sections consisting of four distinct lines. They are all defined over \(\mathbf F_{25}\), with Frobenius cycle type \(1^{12}2^{30}\). Every one of the 12 \(\mathbf F_5\)-rational four-line hyperplanes contains two rational lines and one pair of conjugate lines; none splits completely into four rational lines. For every integer \(n\geq1\), the numbers of lines and four-line hyperplanes defined over \(\mathbf F_{5^n}\) are respectively \(8\) and \(12\) for odd \(n\), or \(64\) and \(72\) for even \(n\). The line-scheme zeta function and reduced four-line-plane-configuration zeta function are, respectively,
\[
\frac{1}{(1-T)^8(1-T^2)^{28}},\qquad
\frac{1}{(1-T)^{12}(1-T^2)^{30}}.
\]

## Assumptions and scope
Work over \(\mathbf F_5\) and its extensions. Write \(\phi(U,V)=U^4-UV^3\). A line is a geometric projective line contained in \(S\), and a four-line plane is a hyperplane whose quartic section is a product of four distinct linear forms over an algebraic closure. Count geometric objects defined over the indicated finite field, not only field-rational points on those objects. The plane zeta function refers to the **reduced finite set** of such planes, not an unverified scheme-theoretic nonreduced structure.

## Proof
**Smoothness and exhaustion of lines.** The gradient of \(\phi(X,Y)-\phi(Z,W)\) is \((4X^3-Y^3,-3XY^2,-4Z^3+W^3,3ZW^2)\). In characteristic five the first two entries can vanish together only if \(X=Y=0\); likewise the last two imply \(Z=W=0\). Hence the projective surface is smooth. The sharp general bound of Rams–Schütt establishes at most 64 geometric lines on any smooth quartic in characteristic other than two and three [1]. We construct 64 distinct lines over \(\mathbf F_{25}\), proving both completeness and the splitting field.

Let \(K=\mathbf F_5[e]/(e^2-2)\). The binary form \(\phi\) has exactly four distinct zeros in \(\mathbf P^1(K)\), represented by \((r:1)\) with \(r\) ranging through the four roots of \(r^4-r=0\). Every ordered pair of roots \((r,s)\) yields the separated line spanned by \((r,1,0,0)\) and \((0,0,s,1)\), giving 16 lines. Every invertible \(2\times2\) matrix \(M=(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})\) with polynomial identity \(\phi(aZ+bW,cZ+dW)=\phi(Z,W)\) gives a graph line spanned by \((a,c,1,0)\) and \((b,d,0,1)\). Equality of the five binary quartic coefficients is a finite system of explicit equations. Exhaustive field arithmetic in the attached program over all \(25^4\) matrices gives 48 distinct solutions, all invertible. The two line classes are disjoint and total 64, so the published upper bound exhausts all geometric lines. (Alternatively, this 16/48 geometric arrangement is described in [2, §9.1]; its geometry is not claimed as new.)

**Arithmetic descent and rational intersections.** The Frobenius of \(K/\mathbf F_5\) fixes two of the four roots and interchanges the other two. Therefore four separated lines are rational. The coefficient check identifies exactly four graph matrices over \(\mathbf F_5\), the nonzero scalar matrices; hence precisely eight lines are rational. Since all 64 lines descend to \(K\), the remaining 56 form 28 Frobenius pairs. Adjunction on the smooth K3 quartic gives \(N_{L/S}\simeq\mathcal O_{\mathbf P^1}(-2)\). Thus \(H^0(N_{L/S})=0\), so the Fano scheme of these 64 lines is reduced and finite étale over the perfect field \(\mathbf F_5\). For the eight rational lines, two distinguished separated lines, of parameters \((0,0)\) and \((1,1)\), each meet the other six rational lines; no pair among the six intersects. This follows either by the rank-three test on pairs of spanning matrices or by the explicit separated/graph descriptions. Thus their intersection graph is \(K_{2,6}\).

**Four-line hyperplanes.** Two distinct intersecting lines span a unique hyperplane. For each pair among the 64 lines the attached exact-arithmetic program computes the row rank of their four spanning vectors, records the normalized hyperplane normal if that rank is three, and then counts every line contained in that plane. Exhausting the \(\binom{64}{2}\) pairs gives 144 distinct planes containing exactly two listed lines and 72 planes containing exactly four listed lines; there are no other planes containing two or more of the lines. In a plane with four listed lines, the plane section of \(S\) has degree four, so its section equals the reduced union of these four lines. Conversely every section that is four distinct lines occurs in the pair enumeration. This gives the exact 72. All planes have normals in \(K\). The same exact calculation finds exactly 12 normals fixed by Frobenius and verifies that each corresponding plane contains exactly two of the eight rational lines, with its other two lines exchanged by Frobenius. The remaining 60 plane normals form 30 Frobenius pairs.

Finally a finite reduced Galois set with \(a\) fixed points and \(b\) two-cycles has point count \(a+2b\) over even-degree extensions and \(a\) over odd-degree extensions, and zeta function \((1-T)^{-a}(1-T^2)^{-b}\). Apply this to the line scheme and the reduced four-line-plane set.

## Verification
Run `python3 verification/schur_verify.py` with Python 3 and the standard library only. The program constructs \(K\) exactly, tests all matrix quartic coefficients, enumerates line pairs and plane normals by exact Gaussian elimination, and checks the Frobenius fixed points, plane partitions and rational intersection degrees with assertions. Execution on the packaged source prints `VERIFY_OK`. No floating-point or probabilistic steps are used. The finite exhaustive enumeration proves the stated finite algebraic identities; the passage to *all geometric lines* independently uses the published characteristic-five upper bound.

## Relationship to prior work
Rams–Schütt [1] prove the geometric 64-line upper bound, not this finite-field splitting. Degtyarev–Itenberg–Sertöz [2, §9.1] explicitly describe the complex 16/48 line arrangement and related geometric planes and real forms. The 16/48 geometric counts and the existence of the Schur quartic are **not** new. The contribution here is the actual \(\mathbf F_5\)-Frobenius action, \(K_{2,6}\) rational incidence, and the descent and two-plus-conjugate-pair decomposition of the 12 rational four-line sections. A contemporary mathematical-record result on the 64-line incidence graph [3] addresses its geometric spectrum and transversals rather than these finite-field arithmetic assertions.

## Limitations
The exact finite-field results are for this explicit \(\mathbf F_5\) model, not arbitrary twists or unrelated quartics. This work does not compute the complete scheme structure of the locus of four-line planes, beyond its reduced set. The arithmetic conclusions are self-reviewed but not independently audited. Published full-text comparison focuses on the relevant geometric-classification sections; unseen specialized computations could overlap the arithmetic statements.

## References
[1] S. Rams and M. Schütt, *64 lines on smooth quartic surfaces*, first public arXiv v1, 2012-12-14, arXiv:1212.3511, https://arxiv.org/abs/1212.3511.

[2] A. Degtyarev, I. Itenberg and A. S. Sertöz, *Lines on quartic surfaces*, arXiv:1601.04238, §9.1 (2016), https://arxiv.org/abs/1601.04238.

[3] *Spectrum and common-transversal profile of the 64 Schur lines*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-spectrum-and-common-transversal-profile-of-the-64-schur-lines--76e63f54b379.
