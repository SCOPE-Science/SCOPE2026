# Exact diameter three for binary two-dimensional LCD neighbor graphs
## Finding
For every integer \(n\ge4\), let \(\mathcal G_2(n,2)\) be the graph whose vertices are the two-dimensional subspaces \(C\le\mathbb F_2^n\) satisfying \(C\cap C^\perp=\{0\}\), with two vertices adjacent exactly when their intersection has dimension one. Then
\[
\operatorname{diam}\mathcal G_2(n,2)=3.
\]
The same conclusion holds in codimension two: \(\operatorname{diam}\mathcal G_2(n,n-2)=3\).

An explicit pair at distance three is
\[
C=\langle e_1,e_2\rangle,
\qquad
D=\langle e_1+e_2+e_3,\ e_3+e_4\rangle,
\]
with zero tail coordinates when \(n>4\).

## Assumptions and scope
The ambient space is \(V=\mathbb F_2^n\) with the standard symmetric bilinear form \(B(x,y)=\sum_i x_i y_i\). A two-dimensional code is LCD exactly when the restriction of \(B\) to it is nondegenerate. The neighbor relation is the one used for the LCD neighbor graph: two two-dimensional codes are neighbors exactly when they meet in a line.

The claim concerns the full binary LCD neighbor graph, not a quotient by code equivalence and not a graph restricted to one orthogonal-group orbit.

## Proof
Write
\[
q(x)=B(x,x),\qquad w=(1,\ldots,1),\qquad T(z)=z+q(z)w.
\]
Over \(\mathbb F_2\), one has \(q(x)=B(x,w)\). If \(c\ne0\) and \(z\notin\langle c\rangle\), the Gram determinant of \(\langle c,z\rangle\) is
\[
q(c)q(z)+B(c,z)=B(c,T(z)).
\]
Hence \(\langle c,z\rangle\) is LCD exactly when \(B(c,T(z))=1\).

Let \(C,D\) be arbitrary two-dimensional LCD codes. Define
\[
A_C=T^{-1}(C^\perp),\qquad A_D=T^{-1}(D^\perp).
\]
If \(z\notin C\cup D\cup A_C\cup A_D\), then the linear functional \(c\mapsto B(c,T(z))\) is nonzero on \(C\), so some \(c\in C\) satisfies \(B(c,T(z))=1\). Thus \(E_C=\langle c,z\rangle\) is an LCD neighbor of \(C\). Similarly, some \(d\in D\) gives an LCD neighbor \(E_D=\langle d,z\rangle\) of \(D\). Since \(E_C\) and \(E_D\) both contain \(z\), they are either equal or adjacent. Therefore such a \(z\) gives a path from \(C\) to \(D\) of length at most three.

It remains to show that such a \(z\) always exists. If \(n\) is even, then \(T\) is invertible, so each of \(A_C,A_D\) has dimension \(n-2\). Consequently
\[
|A_C\cup A_D|\le 2^{n-1}.
\]
Since \(|C\cup D|\le7\), the total number of forbidden vectors is at most \(2^{n-1}+7<2^n\) for every even \(n\ge4\).

If \(n\) is odd, then \(\ker T=\langle w\rangle\) and \(\operatorname{im}T=w^\perp\). Hence \(\dim A_C\le n-1\) and \(\dim A_D\le n-1\). The union of two proper subspaces of dimension at most \(n-1\) has size at most \(3\cdot2^{n-2}\). For odd \(n\ge5\),
\[
3\cdot2^{n-2}+7<2^n.
\]
Thus a suitable \(z\) exists in every case, proving \(\operatorname{diam}\mathcal G_2(n,2)\le3\).

For the lower bound, take the displayed pair \(C,D\). The Gram matrices with the displayed bases are respectively
\[
I_2
\quad\text{and}\quad
\begin{pmatrix}1&1\\1&0\end{pmatrix},
\]
so both planes are LCD, and they intersect trivially. Every \(c=a e_1+b e_2\in C\) and every
\[
d=u(e_1+e_2+e_3)+v(e_3+e_4)\in D
\]
satisfy
\[
B(c,d)=q(c)q(d).
\]
Therefore for every nonzero \(c\in C\) and nonzero \(d\in D\), the Gram determinant of \(\langle c,d\rangle\) is zero. Any common neighbor of two disjoint two-planes would have to be \(\langle c,d\rangle\) for such a pair \((c,d)\). Hence \(C,D\) have no common LCD neighbor and their graph distance is at least three. Combined with the upper bound, their distance is exactly three and the graph diameter is three.

Finally, \(C\mapsto C^\perp\) preserves the LCD property and the neighbor relation, giving an isomorphism from \(\mathcal G_2(n,2)\) to \(\mathcal G_2(n,n-2)\).

## Verification
The standalone verifier `verify.py` checks the lower-bound pair by exact binary arithmetic for every tested ambient length, exhaustively constructs all two-dimensional LCD subspaces for \(n=4,5,6\), and computes the graph diameter in each case. It also checks the key Gram-determinant identity used in the proof. The exhaustive computations are finite corroboration; the all-\(n\) conclusion follows from the symbolic counting argument above.

## Relationship to prior work
The recent LCD-neighbor work of de la Cruz, Horlemann, Newman, Vela Cabello, and Willems defines \(\mathcal G_q(n,k)\), proves the binary graph regular and connected, and analyzes its orthogonal-group orbit subgraphs. Its arXiv text does not state a diameter theorem for the binary graph. A publicly available conference version states the diameter \(\min\{k,n-k\}\) only for odd \(q\), leaving the binary metric untreated. The present result closes the first nontrivial binary dimension and shows a genuine characteristic-two deviation: for \(n\ge4\), the binary dimension-two diameter is \(3\), whereas the odd-field formula gives \(2\).

Harada and Tanaka classify binary LCD codes in low dimensions and tabulate dimension-two equivalence classes, but do not study this neighbor-graph diameter. A previously checked result on the same binary LCD neighbor graph determines edge-regularity and triangle counts; those local intersection numbers do not determine global diameter and do not imply the theorem here.

## Limitations
No diameter formula is claimed here for binary dimensions \(3\le k\le n-3\). The proof uses the special two-dimensional fact that any nonzero linear functional on a code selects a line giving an LCD neighbor through a prescribed external vector. The finite verifier is not used as an infinite proof.

## References
1. A.-L. Horlemann and M. Newman, *The Neighbor Graph of Linear Complementary Dual Codes*, public presentation record dated 2025-04-03, University of St. Gallen repository, https://www.alexandria.unisg.ch/handle/20.500.14171/124507 .
2. J. de la Cruz, A.-L. Horlemann, M. Newman, C. Vela Cabello, and W. Willems, *The Neighbor Graph of Linear Complementary Dual (LCD) Codes*, arXiv:2609.07580v1, 2026.
3. C. Vela Cabello, *The Neighbor Graph of Linear Complementary Dual Codes*, 5th Pythagorean Conference slides, 2026, https://cargo.wlu.ca/5thPythagorean/talks/Carlos_Vela.pdf .
4. M. Harada and Y. Tanaka, *On the classification of binary LCD codes*, Advances in Mathematics of Communications, 2026, DOI 10.3934/amc.2025034.
