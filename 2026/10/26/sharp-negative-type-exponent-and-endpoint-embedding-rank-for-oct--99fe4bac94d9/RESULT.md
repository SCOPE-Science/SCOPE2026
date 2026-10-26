# Sharp negative-type exponent and endpoint embedding rank for octahedral rotations

## Finding
Let \(O\) be the group of the 24 signed \(3\times3\) permutation matrices with determinant \(+1\), acting as the rotational symmetry group of the cube. For \(R,S\in O\), let \(d(R,S)\in[0,\pi]\) be the principal angle of the relative rotation \(R^{-1}S\). For every \(p>0\), define \(D_p=[d(R,S)^p]_{R,S\in O}\), including zeros on the diagonal. Then
\[
 D_p\text{ is conditionally negative semidefinite}
 \quad\Longleftrightarrow\quad 0<p\le p_*:=\frac{\log(4/3)}{\log(3/2)}.
\]
The numerical value of the threshold is \(p_*\approx0.7095112913514545\). The conditional inequality is strict on nonzero zero-sum vectors precisely when \(0<p<p_*\).

For \(0<p\le p_*\), the finite squared-distance matrix \(D_p\) admits an exact Euclidean realization, of least dimension \(23\) below the threshold and \(19\) at equality. In particular, precisely four nontrivial spectral dimensions disappear at the threshold. For every \(t>0\), the Gaussian-form angular kernel \(\exp(-t d(R,S)^p)\) is positive semidefinite for all \(t>0\) exactly in the same exponent interval, and it is strictly positive definite at every positive scale throughout this interval. When \(p>p_*\), the kernel is indefinite for every sufficiently small positive \(t\) and strictly positive definite for every sufficiently large \(t\).

## Assumptions and scope
The angle is the intrinsic shortest principal rotation angle, not the Frobenius chordal distance. Conditional negative semidefiniteness means \(\sum_{R,S\in O}c_Rc_S d(R,S)^p\le0\) for all real coefficients satisfying \(\sum_R c_R=0\). Its strict version requires a strict inequality for every nonzero such coefficient vector. The Euclidean embedding assertion realizes \(d(R,S)^p\) as a **squared** Euclidean distance, not as an ordinary Euclidean distance. The group is finite, and the theorem does not assert a corresponding cutoff for the entire manifold \(SO(3)\).

## Proof
The rotation classes can be indexed by cycle type under the induced permutation of the four cube body diagonals. Their types, cardinalities, and angles are, respectively:
\[
\begin{array}{c|ccccc}
\text{cycle type}&1& (12)&(12)(34)&(123)&(1234)\\ \hline
\text{cardinality}&1&6&3&8&6\\
\text{angle}/\pi&0&1&1&2/3&1/2
\end{array}.
\]
The five irreducible character rows, in this column order, are
\[
\begin{array}{c|rrrrr}
\text{trivial}&1&1&1&1&1\\
\text{sign}&1&-1&1&1&-1\\
\text{standard three-dimensional}&3&1&-1&0&-1\\
\text{sign-twisted standard}&3&-1&-1&0&1\\
\text{two-dimensional}&2&0&2&-1&0
\end{array}.
\]
These rows follow from the permutation representation on four body diagonals, its sign twist, and the standard representation of the three pair partitions; their squared dimensions sum to \(24\), proving completeness. In particular, the two-dimensional representation factors through the action on the three pair partitions.

Write \(a=2^{-p}\) and \(b=(2/3)^p\). Since \(d(e,g)^p\) is central, its convolution matrix is scalar on each irreducible block. Dividing its eigenvalues by \(\pi^p\), the nonconstant blocks have exactly the following eigenvalues, with multiplicities given in parentheses:
\[
\begin{array}{c|cc}
\text{block}&\text{eigenvalue}/\pi^p&\text{multiplicity}\\\hline
\text{sign}&-3+8b-6a&1\\
\text{two-dimensional}&3-4b&4\\
\text{standard three-dimensional}&1-2a&9\\
\text{sign-twisted standard}&-3+2a&9.
\end{array}
\]
The trivial block is irrelevant to the zero-sum conditional inequality. Because \(p_*<1\), for \(0<p\le p_*\) we have \(a>1/2\) and \(b\ge3/4\). Thus the two-dimensional eigenvalue is nonpositive, while the standard and sign-twisted eigenvalues are strictly negative. Moreover, \((2/3)^p<2^{-p/2}=\sqrt a\) and \(2\sqrt a\le1+a\), hence
\[
-3+8b-6a<-3+4(1+a)-6a=1-2a<0.
\]
Therefore every nonconstant block is negative except that the two-dimensional block is zero when \(p=p_*\). Conversely, if \(p>p_*\), then \(b<3/4\) and the two-dimensional block is positive, contradicting conditional negative semidefiniteness. This completes the exact exponent classification and proves strictness in the interior.

Let \(H=I-\frac1{24}{\bf1}{\bf1}^{\mathsf T}\). Classical Euclidean distance-matrix theory identifies the centered squared-distance Gram matrix as \(B_p=-\frac12 H D_p H\). Its rank equals the least dimension of a Euclidean realization. All \(23\) nonconstant eigenvalues are negative for \(0<p<p_*\). At the endpoint, exactly the four eigenvectors in the two-dimensional isotypic block vanish, so \(\operatorname{rank}B_{p_*}=19\).

For admissible \(p\), write \(d(R,S)^p=\|u_R-u_S\|_2^2\) using this Euclidean realization. The \(u_R\) are distinct since every off-diagonal angular distance is positive. The Euclidean Gaussian is strictly positive definite on any finite set of distinct points, proving the asserted all-scale strict positivity. For \(p>p_*\), a zero-sum vector \(c\) in the positive two-dimensional block satisfies \(c^{\mathsf T}D_pc>0\). Consequently \(c^{\mathsf T}[e^{-t d(R,S)^p}]c=-t c^{\mathsf T}D_pc+O(t^2)<0\) as \(t\downarrow0\). Finally, as \(t\to\infty\), this exponential Gram matrix converges to the identity, so it is strictly positive definite for all sufficiently large \(t\).

## Verification
The companion standalone program `rotation_negative_type_check.py` constructs all 24 signed-permutation rotation matrices and their exact angle classes from integer traces, independently computes the distance-power matrices, and compares their numerical eigenvalues with the character formulas at eight exponents spanning the threshold. It also verifies the four-dimensional nullity and the resulting endpoint embedding rank. The code checks finite-dimensional identities; the proof above establishes the universal statement for every real exponent.

## Relationship to prior work
Sánchez [1] gives general criteria and examples for supremal negative type of finite metric spaces, rather than this octahedral intrinsic-angle classification. Robertson [2] proves failure of negative type for geodesic distance on continuous projective spaces; that global result does not determine the sharp positive interval on the finite cube-rotation subgroup. An analogous finite icosahedral angular-metric classification does not imply this result by restriction: the octahedral rotation group has order \(24\), contains quarter-turns, and is not a subgroup of the order-\(60\) icosahedral rotation group. The present new statement concerns the complete octahedral spectrum and its four-dimensional endpoint defect.

## Limitations
The theorem does not characterize the entire set of admissible positive scales when \(p>p_*\). The spectral character proof requires the octahedral group and does not establish positive definiteness for arbitrary rotations in \(SO(3)\). The numerical checker is corroborative and cannot replace the exact character calculation. A fully exhaustive bibliographic priority search is not claimed.

## References
[1] S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (first public version, 2 August 2011).

[2] G. Robertson, *Crofton formulae and geodesic distance in hyperbolic spaces*, arXiv:1302.5790v1 (public version, 23 February 2013).
