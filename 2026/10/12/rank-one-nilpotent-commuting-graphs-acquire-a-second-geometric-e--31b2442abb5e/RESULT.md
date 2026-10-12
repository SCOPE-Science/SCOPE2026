# Rank-one nilpotent commuting graphs acquire a second geometric edge class in dimension four
## Finding
Let \(q\) be a prime power and \(n\ge 4\). Let \(\mathcal N_{n,q}\) denote the subgraph induced by the nonzero rank-one nilpotent matrices in the ordinary commuting graph of \(M_n(\mathbb F_q)\). Write
\[
[m]_q=\frac{q^m-1}{q-1},\qquad a=[n-1]_q,\qquad b=[n-2]_q,\qquad c=[n-3]_q,
\]
and put \(T=a+(a-1)b\).

The nonzero scalar-multiple classes in \(\mathcal N_{n,q}\) are naturally indexed by the incident point-hyperplane flags \((P,H)\) of \(\operatorname{PG}(n-1,q)\), and every class has size \(q-1\). Two distinct classes \((P,H)\) and \((Q,K)\) are completely joined if and only if
\[
Q\subset H\quad\text{and}\quad P\subset K.
\]
Consequently
\[
|V(\mathcal N_{n,q})|=(q-1)[n]_q a,
\qquad
\deg_{\mathcal N_{n,q}}=(q-1)T-1.
\]

In the quotient by scalar classes, adjacent distinct flags have exactly two possible common-neighbor counts. If the flags have the same point or the same hyperplane, then
\[
\lambda_s=a+(b-1)b-2.
\]
If their points and hyperplanes are both distinct, then
\[
\lambda_c=(q+1)b+(b-q-1)c-2.
\]
Both edge types occur for every \(n\ge4\), and
\[
\lambda_s-\lambda_c=q c\bigl((q-1)c+1\bigr)>0.
\]
Thus the quotient is not edge-regular from dimension four onward. The boundary is sharp: for \(n=3\), the second edge type is impossible and every quotient edge has exactly \(q-1\) common neighbors.

The common-neighbor profile lifts explicitly to the full matrix graph. Two distinct vertices in one scalar class, a case that occurs when \(q>2\), have \((q-1)T-2\) common neighbors. If two vertices lie in distinct adjacent scalar classes whose quotient edge has common-neighbor count \(\lambda\), then they have
\[
2(q-2)+(q-1)\lambda
\]
common neighbors. Therefore the dimension-four transition survives before scalar compression.

## Assumptions and scope
The commuting graph used here has the noncentral matrices as vertices, with two distinct matrices adjacent when they commute; restricting to the nonzero rank-one nilpotents gives the induced graph \(\mathcal N_{n,q}\). Since a nonzero rank-one nilpotent matrix is never scalar, every matrix under discussion is a legitimate commuting-graph vertex. The theorem applies to every prime power \(q\) and every \(n\ge4\); the \(n=3\) statement is included only as the sharp boundary comparison.

The geometric quotient identifies only nonzero scalar multiples of the same rank-one matrix. It is not an assertion that arbitrary commuting-graph equivalence relations coincide with scalar equivalence.

## Proof
Write a rank-one matrix as \(A=u\varphi\), where \(u\ne0\) is a column vector and \(\varphi\ne0\) is a linear functional. Then
\[
A^2=\varphi(u)A.
\]
Hence \(A\) is nilpotent exactly when \(\varphi(u)=0\). Its image is the projective point \(P=\langle u\rangle\), its kernel is the projective hyperplane \(H=\ker\varphi\), and nilpotence is exactly the incidence \(P\subset H\). Conversely every incident flag \((P,H)\) determines a one-dimensional vector space of rank-one maps with image \(P\) and kernel \(H\), so exactly \(q-1\) nonzero matrices represent that flag.

Let \(A=u\varphi\) and \(B=v\psi\) represent two different flags \((P,H)\) and \((Q,K)\). Their products are
\[
AB=\varphi(v)u\psi,
\qquad
BA=\psi(u)v\varphi.
\]
If these two rank-one maps were equal and nonzero, they would have the same image and kernel, forcing the two flags to coincide. Thus, for different flags, \(AB=BA\) holds exactly when both products vanish. Equivalently,
\[
Q\subset H\quad\text{and}\quad P\subset K.
\]
This proves the quotient adjacency rule and also shows that every quotient edge lifts to a complete join of two scalar classes.

Fix an incident flag \((P,H)\). To count quotient neighbors together with the flag itself, first choose \(Q\subset H\). There are \(a=[n-1]_q\) possibilities. If \(Q=P\), there are \(a\) hyperplanes \(K\) containing \(P\). If \(Q\ne P\), there are \(b=[n-2]_q\) hyperplanes containing the projective line spanned by \(P\) and \(Q\). Hence the number including the original flag is
\[
T=a+(a-1)b,
\]
so the quotient degree is \(T-1\). Replacing every quotient vertex by a clique of size \(q-1\) gives the asserted matrix-graph order and degree.

Now consider two adjacent quotient flags. Suppose first that they share their point, say \((P,H)\) and \((P,K)\) with \(H\ne K\). A common neighbor \((R,L)\), before excluding the two endpoints, must have \(R\subset H\cap K\) and \(P,R\subset L\). The intersection \(H\cap K\) contains exactly \(b\) projective points. For \(R=P\), there are \(a\) choices for \(L\); for each of the other \(b-1\) points, there are \(b\) choices. Removing the two endpoints gives
\[
\lambda_s=a+(b-1)b-2.
\]
The same formula holds dually when the hyperplane is shared.

For the second type, take adjacent flags \((P,H)\) and \((Q,K)\) with \(P\ne Q\) and \(H\ne K\). Let \(U=\langle P,Q\rangle\) and \(J=H\cap K\). Adjacency gives \(U\subset J\). A common-neighbor flag \((R,L)\), again before excluding the endpoints, is characterized by \(R\subset J\) and \(U,R\subset L\). The projective line \(U\) has \(q+1\) points, and for each of them there are \(b\) hyperplanes containing \(U\). The remaining \(b-q-1\) points of \(J\) each enlarge \(U\) to a three-dimensional vector subspace, which is contained in exactly \(c=[n-3]_q\) hyperplanes. Removing the two endpoints yields
\[
\lambda_c=(q+1)b+(b-q-1)c-2.
\]
For \(n\ge4\), such a cross edge exists: choose a projective line \(U\), two distinct points on it, and two distinct hyperplanes containing it. In dimension three two distinct points already determine the unique hyperplane containing both, so the cross type cannot occur.

Using \(a=1+qb\) and \(b=1+qc\), direct simplification gives
\[
\lambda_s-\lambda_c=q c\bigl((q-1)c+1\bigr),
\]
which is strictly positive for \(n\ge4\). For \(n=3\), \(b=1\), so the surviving same-point/same-hyperplane edges have \(\lambda_s=q-1\).

Finally let \(s=q-1\) be the scalar-class size. Two different vertices in the same class share the other \(s-2\) vertices of that class and all \(s(T-1)\) vertices in neighboring classes, giving \(sT-2\). For an edge between different classes, the common neighbors consist of \(s-1\) additional vertices in each endpoint class and all \(s\lambda\) vertices over the \(\lambda\) quotient common neighbors, giving \(2(s-1)+s\lambda\). This is exactly the stated full-graph profile.

## Verification
A standalone checker constructs the projective flag quotient directly for \((n,q)=(3,2),(3,3),(4,2),(4,3),(5,2)\). It verifies the vertex and degree formulas, classifies every quotient edge, and recomputes every common-neighbor count. The observed quotient profiles are respectively: no cross edge in the two dimension-three cases; \((\lambda_s,\lambda_c)=(11,7)\) for \((4,2)\); \((23,14)\) for \((4,3)\); and \((55,31)\) for \((5,2)\).

As an independent finite check of the algebra-to-geometry step, the checker also constructs all \(105\) nonzero rank-one nilpotent matrices in \(M_4(\mathbb F_2)\), multiplies every matrix pair, and verifies that matrix commutation is equivalent to the mutual-incidence rule on the associated point-hyperplane flags. The script finishes with `VERIFY_OK`.

These finite computations test representative boundaries and the matrix/geometry translation; the general theorem is established by the counting proof above, not by finite enumeration.

## Relationship to prior work
Dolinar, Kuzma, and Oblak use rank-one and square-zero matrices as canonical intermediates in matrix commuting graphs and characterize maximal-distance phenomena through rank-one behavior. That work supplies the algebraic motivation but does not give the finite-field induced rank-one-nilpotent flag graph or its local common-neighbor profile.

Ou and Zhong study automorphisms of a graph on rank-one upper triangular matrices. Their vertex set depends on a fixed triangular coordinate structure and is different from the conjugacy-invariant set of all rank-one nilpotent matrices considered here.

Boroja, Kokol Bukovšek, and Stopar identify the rank-one-nilpotent compressed vertices of the \(3\)-by-\(3\) finite-prime-field commuting graph with incident point-line pairs and show that their compressed adjacency is same-point or same-line adjacency. That is exactly the dimension-three boundary recovered here. The present claim starts at \(n=4\), where two distinct hyperplanes can contain the line through two distinct points; this creates the second cross-incidence edge class and the unequal common-neighbor count. Their dimension-three structure therefore does not imply the higher-dimensional transition proved here.

## Limitations
The theorem concerns only the induced subgraph on nonzero rank-one nilpotent matrices. It does not describe the full commuting graph of \(M_n(\mathbb F_q)\), nor does it classify the automorphism group of the induced graph. The quotient is taken only by nonzero scalar multiples. No claim is made that the two common-neighbor values constitute a complete graph-isomorphism invariant.

The literature comparison found no statement of the higher-dimensional cross-incidence transition or the two formulas above. A residual risk remains that the same flag graph has been studied under a different finite-geometry name; the mathematical claim is therefore presented with that literature risk explicitly recorded in the review materials.

## References
1. G. Dolinar, B. Kuzma, P. Oblak, “On maximal distances in a commuting graph,” arXiv:1009.5543, first public 28 September 2010; later published in *Electronic Journal of Linear Algebra* 23 (2012), DOI 10.13001/1081-3810.1518.
2. H. Ou, P. Zhong, “Automorphisms of a commuting graph of rank one upper triangular matrices,” *Electronic Journal of Linear Algebra* 31 (2016), DOI 10.13001/1081-3810.3064.
3. J. Boroja, D. Kokol Bukovšek, T. Stopar, “Unital compressed commuting graph of 3×3 matrices over a finite prime field,” arXiv:2602.07467.
