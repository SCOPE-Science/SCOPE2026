# Zeta function and Frobenius descent of the sixty-line characteristic-two quartic

## Finding
Let \(\alpha\) be a root of \(\alpha^4+\alpha^3+\alpha^2+\alpha+1=0\) in \(\mathbb F_{16}\) and put \(\mu=1+\alpha^2+\alpha^3\), a primitive cube root of unity in \(\mathbb F_4\). In \(\mathbb P^4_{\mathbb F_4}\), write \(s_i\) for the elementary symmetric polynomial of degree \(i\) in five homogeneous coordinates and set
\[
S=V(s_1,s_4+\mu s_2^2).
\]
This is the Rams--Schütt smooth quartic K3 surface with sixty geometric lines. Its arithmetic data are
\[
\#S(\mathbb F_4)=20,\qquad \#S(\mathbb F_{16})=554,
\]
\[
\operatorname{rk}\operatorname{Pic}(S/\mathbb F_4)=10,\qquad
\operatorname{rk}\operatorname{Pic}(S_{\overline{\mathbb F}_2})=20,
\]
\[
Z(S/\mathbb F_4,T)=\frac{1}{(1-T)(1-16T)(1-16T^2)^{10}(1-3T+16T^2)}.
\]
Arithmetic \(\mathbb F_4\)-Frobenius permutes the sixty lines in thirty transpositions: none is \(\mathbb F_4\)-rational, and all are defined over \(\mathbb F_{16}\). The surface is ordinary, with second crystalline cohomology slopes \(0,1^{20},2\).

## Assumptions and scope
The base field is exactly \(\mathbb F_4=\mathbb F_2(\mu)\), not \(\mathbb F_2\). The two primitive choices of \(\mu\) give conjugate models, and the assertions are unchanged by that conjugation. All geometric Picard ranks refer to base change to an algebraic closure; all stated line orbits refer to the sixty distinct geometric lines. For an extension \(\mathbb F_{4^m}\), the zeta function determines the count \(\#S(\mathbb F_{4^m})\) without claiming a formula for arbitrary deformations of the symmetric quartic pencil.

## Proof
**Smoothness.** In the symmetric affine chart \(x_0=1\) of the hyperplane \(s_1=0\), use coordinates \(x=x_1,y=x_2,z=x_3\) and \(x_4=1+x+y+z\). In characteristic two the derivative of \(\mu s_2^2\) is zero, so a singularity requires all three derivatives of \(s_4\) to vanish. An exact reduced lexicographic Gröbner basis over \(\mathbb F_2\) for their ideal is
\[
\begin{gathered}
 x^2+x+z^2+z,\quad xy+xz+yz,\quad xz^2+z^3+z^2,\\
 y^2+y+z^2+z,\quad yz^2+z^3+z^2,\quad z^4+z^2.
\end{gathered}
\]
Thus \(z\in\{0,1\}\), then \(x,y\in\{0,1\}\), also after algebraic closure. At every such binary point in the chart, \((s_2,s_4)\) is either \((1,0)\) or \((0,1)\); hence \(s_4+\mu s_2^2\ne0\). Every projective point has a nonzero homogeneous coordinate, and symmetry lets us move it to \(x_0\), so \(S\) is geometrically smooth.

**Lines and Frobenius.** The primary construction [1, Section 8] provides a line spanned by the following two vectors in \(\mathbb F_{16}^{5}\):
\[
\begin{aligned}
v_1&=(\alpha^3,1,0,\alpha^3+\alpha+1,\alpha),\\
v_2&=(\alpha^3+\alpha^2+\alpha+1,0,1,1,\alpha^3+\alpha^2+\alpha+1).
\end{aligned}
\]
Permuting the five coordinates produces sixty different two-dimensional subspaces, each entirely inside \(S\). Source [1] establishes that this orbit is the entire geometric line set (independently also bounded by [2]). Use the finite-field model \(\mathbb F_{16}=\mathbb F_2[a]/(a^4+a^3+a^2+a+1)\) with \(a=\alpha\). Reduced row echelon forms of all 120 permuted pairs give sixty distinct planes. Raising each coordinate to its fourth power permutes these sixty planes in exactly thirty 2-cycles, with no fixed plane.

**Incidence and Picard descent.** Two different lines intersect exactly when the four spanning vectors in \(\mathbb F_{16}^{5}\) have rank three. Each line meets seventeen others. Let \(A\) be the resulting sixty-by-sixty adjacency matrix. Exact integer linear algebra yields
\[
\chi_A(U)=(U-17)(U-2)^{40}(U+3)^5(U+4)^4(U+5)^5(U+8)^4(U+9).
\]
Every line has self-intersection \(-2\) on the smooth quartic K3 surface, so the divisor Gram matrix is \(G=A-2I\) and has rank twenty. For \(D\), the sum of the sixty line classes, one has \(H\cdot D=60\) and \(D^2=60(17-2)=900=(15H)^2\), with \(H^2=4\). Equality in the Hodge index theorem gives \(D=15H\) numerically, so the rational line span contains an ample class; its intersection form is nondegenerate. Consequently its dimension is exactly twenty. Let \(N\) denote the sixty-by-thirty incidence matrix of the Frobenius pairs. An exact calculation gives \(\operatorname{rank}_{\mathbb Q}(GN)=10\); since the line span has nondegenerate pairing, this is the dimension of its fixed part.

**Cohomology and zeta function.** A K3 surface has \(\dim H^2_{\mathrm{et}}=22\) and vanishing odd cohomology. The twenty line-class eigenvalues of geometric \(\mathbb F_4\)-Frobenius on \(H^2\) are ten copies of \(4\) and ten copies of \(-4\). Exhaustive projective enumeration uses exactly \(4^3+4^2+4+1=85\) representatives over \(\mathbb F_4\), and \(16^3+16^2+16+1=4369\) over \(\mathbb F_{16}\). The defining equation holds at 20 and 554 representatives, respectively. By the Lefschetz trace formula the remaining two Frobenius eigenvalues \(\beta,\gamma\) satisfy
\[
\beta+\gamma=20-(1+16)=3,
\qquad \beta^2+\gamma^2=554-(1+256)-20\cdot16=-23.
\]
Therefore \(\beta\gamma=16\), yielding \(1-3T+16T^2\) and the displayed zeta function. The eigenvalues \(\beta/4,\gamma/4\) cannot be roots of unity because their sum is \(3/4\), not an algebraic integer. Since any geometric divisor descends to some finite extension, no further divisor class can occur in the two-dimensional quotient. Thus the geometric Picard rank is twenty. The Frobenius-fixed divisor subspace has rank ten; the Brauer group of a finite field is zero, so this is the rank of \(\operatorname{Pic}(S/\mathbb F_4)\). Over \(\mathbb F_{16}\) all sixty line classes descend and the rank is twenty. Finally, the polynomial \(U^2-3U+16\) has \(2\)-adic root valuations \(0\) and \(4\), whereas \(4\) has valuation \(2\), so the normalized crystalline slopes are \(0,1^{20},2\): the K3 surface is ordinary.

## Verification
Run `python verify.py` after installing SymPy. The included code uses exact \(\mathbb F_{16}\) polynomial arithmetic, tests smoothness via the full projective Jacobian criterion, enumerates every projective representative over \(\mathbb F_4\) and \(\mathbb F_{16}\), computes the complete sixty-line permutation orbit and Frobenius action, and performs the rational Gram and invariant-rank computations. It terminates with `VERIFY_OK`. The independent arithmetic orbit breakdown gives one orbit of twenty points over \(\mathbb F_4\); over \(\mathbb F_{16}\), the symmetric-group orbit lengths are \(20,24,30,60,60,60,60,120,120\), summing to \(554\). These finite calculations are exhaustive because the proof explicitly enumerates a unique normalized representative of every point, not because a sample is deemed representative.

## Relationship to prior work
Rams--Schütt [1] introduced the exact symmetric pencil, supplied the sixty-line orbit, stated geometric smoothness and Picard rank twenty with discriminant \(-55\), and observed that the lines are defined over \(\mathbb F_{16}\). None of those antecedent facts is claimed as new here. Degtyarev [2] gave the characteristic-two sharp bound and large-line configuration classification. The new arithmetic conclusion is the full \(\mathbb F_4\)-zeta function together with the ten-dimensional Frobenius-invariant Picard space and exact absence of \(\mathbb F_4\)-rational lines. Geometric line counts and geometric lattice discriminants alone do not imply this arithmetic Frobenius characteristic polynomial; the explicit descent and complete point counts are needed.

## Limitations
The result is for this one distinguished smooth quartic, not every symmetric quartic or every sixty-line quartic. All point counts, line-orbit assertions and ranks have exact reproducible finite certificates, while the use of K3 cohomological properties, Hodge index, and the Lefschetz trace formula relies on standard theorems. Published sources were inspected for implication overlap, but undiscovered or unindexed prior arithmetic tables could contain the same zeta function.

## References
[1] S. Rams and M. Schütt, *At most 64 lines on smooth quartic surfaces (characteristic 2)*, preprint first posted 2015-12-04, arXiv:1512.01358, Section 8; later Nagoya Mathematical Journal **232** (2018), 76–95, DOI 10.1017/nmj.2017.21.

[2] A. Degtyarev, *Lines in supersingular quartics*, preprint first posted 2016-04-20, arXiv:1604.05836, especially Theorem 1.3 and Remark 8.9.
