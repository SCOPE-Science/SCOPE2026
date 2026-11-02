# The alternating CYBE quadric of the free six-dimensional class-two Lie algebra

## Finding

Let \(k\) be any field of characteristic different from \(2\). Let \(L=V\oplus Z\), with \(\dim V=3\), \(Z=\bigwedge^2 V\), and bracket \([v,w]=v\wedge w\) for \(v,w\in V\) and \([Z,L]=0\). This is the free class-two nilpotent Lie algebra on three generators. Fix bases \(x_1,x_2,x_3\) of \(V\) and \(z_1=[x_2,x_3]\), \(z_2=[x_3,x_1]\), \(z_3=[x_1,x_2]\) of \(Z\).

Every alternating tensor \(r\in\bigwedge^2 L\) has a unique decomposition
\[
r=A+\sum_{i=1}^3x_i\wedge w_i+C,\qquad A\in\bigwedge^2V,\quad C\in\bigwedge^2Z,\quad w_i=\sum_{j=1}^3B_{ij}z_j.
\]
Identify the exterior square with its alternating tensors \(u\wedge v\mapsto u\otimes v-v\otimes u\). Then the **ordinary tensor classical Yang–Baxter equation**
\[
[r_{12},r_{13}]+[r_{12},r_{23}]+[r_{13},r_{23}]=0
\]
holds **if and only if**
\[
A=0\qquad\text{and}\qquad Q(B):=\operatorname{tr}(\operatorname{adj}B)=0.
\]
Explicitly,
\[
Q(B)=B_{11}B_{22}+B_{11}B_{33}+B_{22}B_{33}-B_{12}B_{21}-B_{13}B_{31}-B_{23}B_{32}.
\]
There is no constraint on \(C\). Thus the **reduced solution variety**, as a closed subset of the \(15\)-dimensional alternating tensor space, is the product of a \(3\)-dimensional affine space and the affine quadric \(Q(B)=0\) in \(9\) variables. It is geometrically irreducible of dimension \(11\); its reduced singular locus is precisely the \(3\)-space \(B=0\), consisting of central alternating tensors.

For every **odd** prime power \(q\), the number of alternating tensor solutions over \(\mathbb F_q\), including zero, is exactly
\[
\boxed{q^{11}}.
\]
The number of **distinct triangular coboundary maps** \(\delta_r:L\to\bigwedge^2L\), given by \(\delta_r(x)=[x,r]\) for such solutions, is exactly
\[
\boxed{q^8}.
\]
These are counts of tensors and cobracket maps, respectively; neither number is asserted to count gauge-equivalence or isomorphism classes.

## Assumptions and scope

The Lie bracket is the displayed free class-two bracket. The underlying field is arbitrary except for the assumption \(2\ne0\); the counting statements require a finite field of odd cardinality. The skew tensors are *alternating* tensors in \(\bigwedge^2 L\), not arbitrary nonskew solutions in \(L\otimes L\). The solution variety is explicitly the **reduced** locus: this finding does not identify the possibly nonreduced scheme cut out by the unmodified list of tensor-coordinate equations.

## Proof

**1. Elimination of the \(\bigwedge^2V\)-part.** Use the grading in which elements of \(V\) have degree one and elements of \(Z\) degree two. The Schouten square of \(r=A+B+C\) splits into three types of terms: \([A,A]\in\bigwedge^2V\wedge Z\), \([A,B]\in V\wedge\bigwedge^2Z\), and \([B,B]\in\bigwedge^3Z\); all terms involving \(C\) vanish because \(Z\) is central. These three summands are linearly independent. Writing \(A=a_{12}x_1\wedge x_2+a_{13}x_1\wedge x_3+a_{23}x_2\wedge x_3\), the coefficient of \(x_i\wedge x_j\wedge[x_i,x_j]\) in \([A,A]\), for each \(i<j\), equals \(\pm2a_{ij}^2\). Cross-pair terms cannot contribute to this coefficient: a shared generator wedges with itself, while the remaining brackets label a different basis element of \(Z\). Because \(2\ne0\) and \(k\) is a field, CYBE forces all three \(a_{ij}=0\). The skew tensor equation is equivalent to vanishing of this Schouten square when the characteristic is different from \(2\).

**2. The single remaining equation.** With \(A=0\), write \(r=\sum_i x_i\wedge w_i+C\). Centrality of \(Z\) reduces the Schouten square, up to a nonzero scalar, to
\[
[x_1,x_2]\wedge w_1\wedge w_2+[x_2,x_3]\wedge w_2\wedge w_3+[x_3,x_1]\wedge w_3\wedge w_1.
\]
Using the chosen brackets, its coefficient on \(z_1\wedge z_2\wedge z_3\) is exactly the sum of the three principal \(2\times2\) minors of \(B\), namely \(Q(B)\). Hence the tensor CYBE is equivalent to \(A=0\) and \(Q(B)=0\), with arbitrary \(C\).

**3. Geometric structure.** The quadratic form \(Q\) has a three-variable diagonal part \(uv+uw+vw\), and three disjoint hyperbolic pairs from the off-diagonal entries. Its polar form has invertible diagonal-block matrix \(\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&0\end{psmallmatrix}\), whose determinant is \(2\). Thus \(Q\) is nondegenerate of rank \(9\) when \(2\ne0\). The rank-nine affine quadric is an irreducible cone of dimension \(8\) with singular support only at its vertex. Taking its product with the free \(3\)-dimensional \(C\)-space proves the stated geometric assertions. The reduced qualification does not assert that the original tensor-equation ideal is radical.

**4. Finite-field count.** For every odd \(q\), a nondegenerate quadratic form in an odd number \(m\) of variables over \(\mathbb F_q\) has exactly \(q^{m-1}\) zeros (including the origin). For completeness, this follows by averaging the additive-character sums for \(sQ\): for \(s\ne0\), the quadratic Gauss sum is multiplied by the nontrivial quadratic character \(\chi(s)^m\); when \(m\) is odd, these terms sum to zero over \(s\ne0\). Here \(m=9\), so \(Q(B)=0\) has \(q^8\) matrices \(B\). Each such matrix permits all \(q^3\) choices of \(C\), yielding \(q^{11}\) alternating CYBE tensors.

**5. Distinct triangular coboundary maps.** Put \(w_i=\sum_jB_{ij}z_j\). For \(r=\sum_i x_i\wedge w_i+C\), one has
\[
\begin{aligned}
\delta_r(x_1)&=z_3\wedge w_2-z_2\wedge w_3,\\
\delta_r(x_2)&=-z_3\wedge w_1+z_1\wedge w_3,\\
\delta_r(x_3)&=z_2\wedge w_1-z_1\wedge w_2,\\
\delta_r(Z)&=0.
\end{aligned}
\]
The six off-diagonal coordinates of \(B\) are individually read off from these three outputs. If every output is zero, the remaining diagonal constraints are \(B_{11}+B_{22}=B_{11}+B_{33}=B_{22}+B_{33}=0\). Because \(2\ne0\), this forces all diagonal coordinates to vanish as well. Therefore \(B\mapsto\delta_r\) is injective, and the only freedom in a solution representing a fixed cobracket is \(C\in\bigwedge^2Z\). There are exactly \(q^8\) distinct triangular coboundary maps. The CYBE hypothesis ensures their Lie cobracket compatibility; we do not identify different maps under automorphisms.

## Verification

The standalone \(verify.py\) implements the tensor equation directly from six-dimensional structure constants, without calling a Schouten-bracket package. It exhaustively compares the tensor equation with the predicted quadratic criterion for all \(2^{15}=32768\) alternating tensors over \(\mathbb F_2\), and for all \(3^9=19683\) matrices \(B\) over \(\mathbb F_3\) with vanishing \(A,C\). The \(\mathbb F_2\) check is an out-of-scope characteristic-boundary stress test, not part of the odd-characteristic proof. It finds \(2048\) and \(6561\) solutions, respectively, and independently checks ranks of the \(B\)-to-cobracket map over primes \(2,3,5\). These finite checks do not prove the arbitrary-field statement; the preceding algebraic proof does.

Reproduce with \(\texttt{python3 verify.py}\) using the Python standard library; the expected final line is \(\texttt{FREE\_CLASS\_TWO\_CYBE\_QUADRIC\_OK}\).

## Relationship to prior work

Zhang's arXiv:math/0603697 (first arXiv version 2006-03-30), a seven-page treatment of three-dimensional Lie algebras with two-dimensional derived algebra, establishes low-dimensional CYBE classifications but does not address this six-dimensional free class-two algebra. Bai–Guo–Ni, arXiv:1302.0408 (2013-02-02), studies the general tensor/operator CYBE correspondence; its definitions support the tensor equation here, but it does not enumerate its solutions for this algebra. Benito–de-la-Concepción (2014) describes the free two-step model \(V\oplus\bigwedge^2V\) and its automorphism/derivation framework, rather than a CYBE solution set.

The closest algebra-specific source is Farinati–Jancsa, arXiv:1607.00300 (2016-07-01), whose Section 3 develops nearly coboundary structures on graphical two-step Lie algebras, including the free three-generator case; Example 3.2 explicitly considers the \(V\wedge Z\) coboundary parameter space and Example 3.6 treats a restricted diagonalizable case. It does not state the **full alternating triangular** condition \(Q(B)=0\), the complete rank-nine quadric locus, or the finite-field counts for tensor solutions and distinct triangular cobrackets. Nearly coboundary and coboundary compatibility are weaker than the tensor CYBE: an arbitrary \(B\) may define a coboundary Lie bialgebra without satisfying \(Q(B)=0\). Thus the present finite-field classification does not follow from simply counting the unrestricted coboundary parameters in that source.

## Limitations

This is a classification of alternating solutions of the *ordinary* CYBE, not of every tensor solution, modified CYBE solutions, or isomorphism orbits of Lie bialgebra structures. The geometric statement is about the reduced zero set, not its scheme-theoretic nilpotent structure. The proof and the cobracket count are restricted to characteristic different from \(2\). The source comparison cannot exclude an unpublished or differently formulated prior solution of this exact six-dimensional case; independent assessment of publication priority and of the mathematics has not been performed.

## References

1. S. Zhang, *Classical Yang-Baxter Equation and Low Dimensional Triangular Lie Bialgebras Over Arbitrary Field*, arXiv:math/0603697v1, submitted 2006-03-30. https://arxiv.org/abs/math/0603697
2. C. Bai, L. Guo, X. Ni, *Generalizations of the Classical Yang-Baxter Equation and O-Operators*, arXiv:1302.0408v1, submitted 2013-02-02. https://arxiv.org/abs/1302.0408
3. P. Benito and D. de-la-Concepción, *An overview of free nilpotent Lie algebras*, Comment. Math. Univ. Carolin. 55 (2014), 325–339. https://investigacion.unirioja.es/documentos/5bbc696ab750603269e81ac8/f/617a4e5f2bb80f973acc38e7.pdf
4. M. A. Farinati and A. P. Jancsa, *Lie bialgebra structures on 2-step nilpotent graph algebras*, arXiv:1607.00300v1, submitted 2016-07-01. https://arxiv.org/abs/1607.00300
