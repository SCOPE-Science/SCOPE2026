# Rational linear spaces and the nine-plane grid of the Klein cubic fourfold over \(\mathbb F_2\)

## Finding
Let \(X\subset\mathbb P^5_{\mathbb F_2}\) be the Klein cubic fourfold
\[
X:\quad F=\sum_{i=0}^{5}x_i^2x_{i+1}=0,\qquad x_6=x_0.
\]
Its complete \(\mathbb F_2\)-rational Fano census in projective dimensions \(0,1,2\) is
\[
\#X(\mathbb F_2)=39,\qquad \#F_1(X)(\mathbb F_2)=75,\qquad
\#F_2(X)(\mathbb F_2)=9.
\]
The nine rational planes are indexed by a \(3\times3\) grid: pairs in the same column meet along a rational line; pairs in the same row meet at one rational point; planes in different rows and columns are disjoint. Thus the \(36\) unordered plane-pairs have intersection dimensions \(1,0,-1\) with multiplicities \(9,9,18\), where \(-1\) means empty.

The \(75\) rational lines are partitioned by the number of rational planes containing them: \(54\) lie on exactly one, \(3\) on three, and \(18\) on none. Among the \(39\) points, \(27\) lie on one rational plane and \(12\) on three. The rational line degrees at points are \(5\) (\(27\) points), \(7\) (\(9\) points) and \(9\) (\(3\) points).

## Assumptions and scope
All coefficients, rational points and rational projective linear subspaces are over \(\mathbb F_2\); geometric smoothness is considered over \(\overline{\mathbb F}_2\). Coordinates are labeled cyclically from \(0\) to \(5\). A projective \(d\)-plane corresponds to a \((d+1)\)-dimensional vector subspace of \(V=\mathbb F_2^6\). The result makes no count of planes or lines defined only over a proper extension.

In characteristic two, \(\partial F/\partial x_j=x_{j-1}^2\); all six partial derivatives vanish only at the zero affine vector. Consequently \(X\) is smooth.

## Proof
**Cubic-to-bilinear reduction.** Define the *ordered* bilinear form
\[
B(v,w)=\sum_{i=0}^5 v_i w_{i+1}\quad (\text{indices mod }6),\qquad Q(v)=B(v,v).
\]
For any basis \(b_1,\dots,b_r\) of a vector subspace \(U\subseteq V\), the polynomial restriction is
\[
F\!\left(\sum_{a=1}^r t_ab_a\right)
=\sum_{a,b=1}^r B(b_a,b_b)t_a^2t_b.
\]
The monomials \(t_a^2t_b\) for ordered pairs \((a,b)\) are distinct, including \(a=b\). Hence \(\mathbb P(U)\subset X\) as a projective subscheme if and only if \(B(U,U)=0\), not merely if the polynomial vanishes at binary-valued points. This coefficient criterion avoids confusing function-vanishing on \(\mathbb F_2\) with scheme-theoretic containment.

**Orthogonal splitting.** Let \(T\) be the \(2\)-dimensional space of repeating three-periodic coordinate pairs,
\[
T=\{(a,b,a,b,a,b):a,b\in\mathbb F_2\},
\]
and let
\[
E=\{v\in V:v_0+v_2+v_4=v_1+v_3+v_5=0\}.
\]
These spaces split \(V=T\oplus E\), are orthogonal in *both* orders for \(B\), and \(B|_T\) is the nondegenerate alternating form with matrix \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) in the repeating-even and repeating-odd basis. Therefore \(Q|_T=0\) and \(Q(t+e)=Q(e)\).

Encode \(v\) as the integer \(\sum_{i=0}^5 2^iv_i\) (this is only a convenient coordinate encoding). The ten zeros of \(Q|_E\), including zero, are exactly
\[
0,5,10,17,20,27,34,40,45,54.
\]
The six two-dimensional subspaces \(L\subseteq E\) on which \(Q\) vanishes identically are precisely the spans of the following encoded pairs:
\[
\begin{array}{c|ccc}
&L_0&L_1&L_2\\\hline
B(L,L)=0&(5,17)&(10,34)&(27,45)\\
B(L,L)\ne0&(5,40)&(10,17)&(20,34)
\end{array}
\]
The table is exhaustive: test the \(\binom92\) pairs of distinct nonzero elements from the displayed ten-point null set, retaining those for which their sum remains null, then identify repeated spans. For a \(Q\)-isotropic \(2\)-space \(L\), the restriction of \(B\) is alternating; in dimension \(2\) it is either zero or the unique nonzero symplectic form up to basis. Each of the three spaces in the first row contains three disjoint nonzero null vectors, and the first row partitions the nine nonzero null vectors.

**Points.** Each of the ten \(e\in E\) with \(Q(e)=0\) admits four lifts \(t+e\in V\) with \(t\in T\). Removing the zero vector gives \(4\cdot10-1=39\) rational projective points.

**Lines.** A two-dimensional \(B\)-isotropic \(U\) has \(\dim(U\cap T)\le1\), since \(B|_T\) is nondegenerate. If the dimension is one, \(U=\langle w,e\rangle\) for a nonzero \(w\in T\) and a nonzero \(Q\)-null \(e\in E\); there are \(3\cdot9=27\) such lines. If \(U\cap T=0\), the projection \(U\to E\) is one of the six listed \(Q\)-isotropic two-spaces \(L\), and \(U\) is the graph of a linear map \(f:L\to T\). Its bilinear isotropy is equivalent to
\[
B_T(f(x),f(y))=B_E(x,y)\quad\text{for all }x,y\in L.
\]
For the three \(L\) in the first row, the map has rank at most one: there are \(1+3\cdot3=10\) choices per \(L\). For the three in the second row, it must be an isomorphism preserving the two-dimensional alternating form: there are \(\lvert\operatorname{GL}_2(\mathbb F_2)\rvert=6\) choices per \(L\). Thus the line total is \(27+3\cdot10+3\cdot6=75\).

**Planes and the grid.** If a three-dimensional \(B\)-isotropic space \(U\) intersected \(T\) trivially, its projection to \(E\) would be a three-dimensional space on which \(Q_E\) vanishes. This is impossible from the exhaustive table of six maximal \(Q_E\)-isotropic two-spaces. An intersection of dimension two is excluded by nondegeneracy of \(B_T\). Therefore \(\dim(U\cap T)=1\). Write \(U\cap T=\langle w\rangle\). Orthogonality to \(w\) forces the \(T\)-components of all vectors of \(U\) into \(\langle w\rangle\), so
\[
U=\langle w\rangle\oplus L_i,
\quad 0\ne w\in T,\qquad
L_0=\langle5,17\rangle,\ L_1=\langle10,34\rangle,\ L_2=\langle27,45\rangle.
\]
All nine spaces are indeed bilinearly isotropic. They give the \(3\times3\) grid: the three possible \(w\)'s index rows and the three \(L_i\)'s index columns. Distinct columns have \(L_i\cap L_j=0\). Hence two planes with the same \(i\) meet in \(\mathbb P(L_i)\), with the same \(w\) in \(\mathbb P(\langle w\rangle)\), and otherwise do not meet.

A line of the \(\langle w,e\rangle\) type belongs to exactly one plane because the first-row \(L_i\)'s partition the nonzero null vectors. For a graph line over first-row \(L_i\), if \(f=0\), it lies in all three planes with that \(i\); the other nine nonzero rank-one graphs belong to one plane each. The \(18\) graph lines over second-row \(L\)'s belong to no rational plane. Thus \((54,3,18)\) is the asserted line-to-plane multiplicity profile. The remaining point-incidence histograms follow by the same grid containment and are also checked exhaustively below.

## Verification
The accompanying standalone \(\texttt{verify.py}\) enumerates all \(63\) vector one-spaces, \(651\) two-spaces, and \(1395\) three-spaces in \(\mathbb F_2^6\); tests every ordered bilinear coefficient on each subspace; reconstructs \(T\), \(E\) and the six null two-spaces; and recomputes plane intersections and incidence histograms. A separate exact evaluation over \(\mathbb F_4\) checks the cubic equation on each of the nine planes at every nonzero \(\mathbb F_4\)-valued parameter triple. The completed run printed \(\texttt{VERIFY_OK}\).

To reproduce from this package: execute \(\texttt{python3 verify.py}\) (Python standard library only).

## Relationship to prior work
González-Aguilera and Liendo [1] define Klein cubic \(n\)-folds and study their prime-order automorphisms over characteristic zero, including the Klein fourfold; their results do not count rational linear spaces for the characteristic-two reduction. Debarre–Laface–Roulleau [2] prove the existence of a rational line on any smooth cubic fourfold over \(\mathbb F_2\), and study the different Klein *threefold* in detail. Their Theorem 5.1 gives a general cohomological expression for the zeta function of the Fano variety of lines, but requires arithmetic input about the chosen fourfold; it does not supply this Klein fourfold’s exact input or rational plane census. Their Section 5.4 examples do not supply the exact line/plane counts or nine-plane grid for the characteristic-two Klein *fourfold*.

## Limitations
Only rational subspaces over \(\mathbb F_2\) are classified; no count of geometric lines or planes over \(\overline{\mathbb F}_2\) or of objects rational over \(\mathbb F_{2^r}\) for \(r>1\) is asserted. No Picard lattice, rationality classification, or independent audit is claimed. An equivalent special-purpose finite-geometry enumeration under bilinear-form terminology might predate this computation; the literature comparison is not an exhaustive uniqueness proof.

## References
[1] V. González-Aguilera and A. Liendo, *Automorphisms of prime order of smooth cubic n-folds*, arXiv:1002.4136 (first posted 2010-02-22), Definition 1.9 and Section 2. https://arxiv.org/abs/1002.4136

[2] O. Debarre, A. Laface, and X. Roulleau, *Lines on cubic hypersurfaces over finite fields*, arXiv:1510.05803 (first posted 2015-10-20), Section 4.5.2 and Sections 5.2–5.4. https://arxiv.org/abs/1510.05803
