# Exact puncturing depth to GRS for an explicit \([9,3,7]_{17}\) non-GRS MDS code
## Finding
Let \(C\) be the code in Example 1 of Abdukhalikov--Verma with evaluation set
\[
S=\{0,2,3,4,5,7,9,10,16\}\subset \mathbb F_{17}
\]
and generator columns \(P(t)=(1,t^3,t^4)^T\).  The minimum number of coordinates that must be punctured before the resulting dimension-three MDS code is monomially equivalent to a generalized Reed--Solomon code is exactly \(3\).

More precisely, every one- or two-coordinate puncturing remains non-GRS.  Among the \(\binom{9}{3}=84\) three-coordinate puncturings, exactly six become GRS, namely those deleting
\[
\{4,10,16\},\ \{3,7,9\},\ \{3,5,16\},\ \{2,5,9\},\ \{2,4,7\},\ \{0,2,3\}.
\]
The other \(78\) three-coordinate puncturings remain non-GRS.  Every four-coordinate puncturing is GRS.

Equivalently, for surviving subset sizes \(m=9,8,7,6,5\), the ranks over \(\mathbb F_{17}\) of the quadratic-evaluation matrix described below have distributions
\[
\begin{array}{c|cc}
m&\operatorname{rank}=5&\operatorname{rank}=6\\\hline
9&0&1\\
8&0&9\\
7&0&36\\
6&6&78\\
5&126&0.
\end{array}
\]

## Assumptions and scope
The equivalence notion is the monomial equivalence used in the source: coordinate permutation and independent nonzero coordinate scaling.  Only puncturing is considered; shortening is not part of the claim.  The field is exactly \(\mathbb F_{17}\), and the generator matrix is exactly the one printed in Example 1 of arXiv:2512.13429v2.

For a surviving set \(T\subseteq S\), write \(C_T\) for the punctured code.  The source code is MDS, and the independent verifier also checks directly that every three displayed columns are linearly independent.  Hence every \(C_T\) considered here, with \(|T|\ge 5\), is a dimension-three MDS code.

## Proof
For \(t\in S\), let
\[
P(t)=[1:t^3:t^4]\in \mathrm{PG}(2,17).
\]
A dimension-three GRS code has, after row operations and nonzero column scalings, projective columns on a nondegenerate conic: the standard model is \([1:u:u^2]\).  Conversely, if an MDS column set of at least five points in \(\mathrm{PG}(2,17)\) lies on a nondegenerate conic, a projectivity sends that conic to the standard conic.  Because a conic over \(\mathbb F_{17}\) has \(18\) rational points and our surviving sets have at most nine points, the point used as infinity can be chosen outside the set; the remaining points then have finite parameters.  Thus, for every surviving set considered here, \(C_T\) is GRS if and only if the points \(P(t)\), \(t\in T\), lie on a conic.

Write a homogeneous quadratic as
\[
Q(X,Y,Z)=aX^2+bY^2+cZ^2+dXY+eXZ+fYZ.
\]
For each \(t\), the condition \(Q(P(t))=0\) is one homogeneous linear equation in \((a,b,c,d,e,f)\).  Let \(E_T\) be the matrix whose row for \(t\) is
\[
( X^2,Y^2,Z^2,XY,XZ,YZ )\big|_{P(t)}.
\]
Then a conic contains all points of \(T\) exactly when \(\operatorname{rank}(E_T)<6\).  Since the columns form an arc, no three points are collinear.  A degenerate conic is a union of two lines and therefore contains at most four points of the arc.  Consequently, for \(|T|\ge5\), any conic detected by \(\operatorname{rank}(E_T)<6\) is automatically nondegenerate.

Exact row reduction modulo \(17\) over every subset \(T\subseteq S\) of sizes five through nine gives the rank census in the Finding.  In particular, no surviving set of size seven, eight, or nine lies on a conic; exactly six surviving six-sets do; and every surviving five-set does.  Taking complements in \(S\) gives exactly the six deletion triples displayed above and proves the claimed puncturing depth.

## Verification
The included `verify.py` uses only exact integer arithmetic modulo \(17\).  It first checks all \(\binom{9}{3}=84\) three-column determinants through modular rank, independently confirming the MDS property of the displayed generator.  It then exhausts all \(1+9+36+84+126=256\) surviving subsets of sizes five through nine, computes the six-column quadratic-evaluation rank, checks the full rank census, and verifies the six exceptional six-point subsets.

For each exceptional six-set it also reconstructs an explicit nonzero quadratic coefficient vector.  The verification is exhaustive over the finite domain; no random sampling or floating-point calculation is used.

## Relationship to prior work
Abdukhalikov and Verma introduce the two modified-GRS families, prove MDS and non-GRS criteria, and give the present \([9,3,7]_{17}\) code as an explicit non-GRS MDS example.  Their paper does not state the puncturing-to-GRS profile above.

Wang, Liu, and Luo study GRS recognition and include a different phenomenon: a particular non-GRS MDS code for which a specified punctured and shortened code is GRS.  That establishes that GRS behavior can reappear under puncturing, but it neither concerns the Abdukhalikov--Verma Example 1 nor implies its minimum puncturing depth, the six exceptional deletion triples, or the complete size-by-size conic-rank census.

The finite-geometry correspondence between dimension-three MDS codes and projective arcs, and between dimension-three GRS codes and subsets of a normal rational curve (a conic in the plane), is standard and is also part of the background cited by the source paper.

## Limitations
The result is specific to the displayed \([9,3,7]_{17}\) code and does not assert a family-wide puncturing theorem.  It classifies puncturings with at least five surviving coordinates; it does not address shortening, arbitrary coordinate extensions, or cryptographic attack complexity.  Literature search cannot certify absolute novelty, and an unindexed computation of the same example could exist.

## References
1. K. Abdukhalikov and G. K. Verma, “Two Families of Linear Codes Containing Non-GRS MDS Codes,” arXiv:2512.13429v2; Designs, Codes and Cryptography 94, Article 143 (2026), DOI:10.1007/s10623-026-01890-2.
2. G. Wang, H. Liu, and J. Luo, “New Constructions of Non-GRS MDS Codes, Recovery and Determination Algorithms for GRS Codes,” arXiv:2512.02325 (2025), later IEEE Transactions on Information Theory 72 (2026), 3848–3861.
3. S. Ball and M. Lavrauw, “Arcs in finite projective spaces,” EMS Surveys in Mathematical Sciences 6 (2019), 133–172.
