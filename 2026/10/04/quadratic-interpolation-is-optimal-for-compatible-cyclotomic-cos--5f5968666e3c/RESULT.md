# Quadratic interpolation is optimal for compatible cyclotomic-cosine families
## Finding
Let \(F=(F_m)_{m\ge1}\) be truncation-compatible over \(\mathbb Q\):
\[
F_{m+1}(x_1,\ldots,x_m,0)=F_m(x_1,\ldots,x_m),
\]
and suppose \(\deg F_m\le1\) for every \(m\). Define
\[
b_n=F_{n-1}(\alpha_{1,n},\ldots,\alpha_{n-1,n}),\qquad
\alpha_{k,n}=\cos\!\left(\frac{2\pi k}{n}\right).
\]
Then
\[
2b_3=b_2+b_4.
\]
Conversely, every rational triple \( (b_2,b_3,b_4)\) satisfying this relation occurs from a truncation-compatible family of degree at most one.

Therefore uniform degree one cannot interpolate arbitrary rational-valued sequences. Vélez--Cadavid prove that every rational-valued sequence is interpolated by a compatible family of uniform degree at most two. Consequently their quadratic bound is optimal: the least universal interpolation degree is exactly two. For example, a sequence beginning \(b_2=0\), \(b_3=1\), \(b_4=0\) cannot come from uniform degree one, while their theorem supplies a uniform degree-two interpolant.

## Assumptions and scope
The coefficient field is \(\mathbb Q\), compatibility is exactly specialization of the newest variable to zero, and degree means total polynomial degree. The lower-bound relation uses only levels \(2,3,4\), so it is independent of any asymptotic or stable-range hypothesis. The upper bound is the arbitrary-rational-tail theorem of arXiv:2609.27084v1.

The claim concerns the minimum degree needed for a theorem that works for every rational sequence. It does not classify which infinite rational sequences happen to admit degree-one interpolants beyond the necessary first-three-level relation.

## Proof
Because every \(F_m\) is affine linear and the family is truncation-compatible, there are rational numbers \(c,a_1,a_2,\ldots\) such that
\[
F_m(x_1,\ldots,x_m)=c+\sum_{j=1}^m a_jx_j
\]
for every \(m\). Compatibility fixes the old coefficients when a new variable is introduced.

At the first three cyclotomic levels,
\[
\alpha_{1,2}=-1,
\]
\[
(\alpha_{1,3},\alpha_{2,3})=\left(-\frac12,-\frac12\right),
\]
and
\[
(\alpha_{1,4},\alpha_{2,4},\alpha_{3,4})=(0,-1,0).
\]
Hence
\[
b_2=c-a_1,
\qquad
b_3=c-\frac{a_1+a_2}2,
\qquad
b_4=c-a_2.
\]
Eliminating \(c,a_1,a_2\) gives \(2b_3=b_2+b_4\).

For the converse, assume \(2b_3=b_2+b_4\). Set \(c=0\), \(a_1=-b_2\), \(a_2=-b_4\), and \(a_j=0\) for \(j\ge3\). Then the compatible linear family
\[
F_m=\sum_{j=1}^m a_jx_j
\]
has the prescribed values at levels \(2,3,4\). Thus the image of degree-one compatible families on these three levels is exactly the rational plane \(2b_3=b_2+b_4\).

Taking \( (b_2,b_3,b_4)=(0,1,0)\) violates the plane equation, so no uniform degree-one family can realize every rational sequence.

For completeness, the matching upper bound can be reconstructed from Theorem 2.6 of arXiv:2609.27084v1. The exceptional levels \(2,3,4\) are fitted by a quadratic correction in the second variable that vanishes both under compatibility and at level \(3\). For the induction step from level \(n\) to \(n+1\), the desired discrepancy lies in the maximal real cyclotomic field \(K_{n+1}^+\). Since \(\alpha_{n,n+1}=\alpha_{1,n+1}\ne0\), divide the discrepancy by this cosine. The quotient lies in \(K_{n+1}^+\), which is spanned over \(\mathbb Q\) by \(1,\alpha_{1,n+1},\ldots,\alpha_{n-1,n+1}\). Represent that quotient by a rational affine-linear form \(L_n\) and set
\[
F_n=F_{n-1}+x_nL_n.
\]
This preserves compatibility and keeps total degree at most two while forcing the next prescribed rational value. Thus degree two always suffices, and the lower bound above proves optimality.

## Verification
The included `verify.py` checks the affine coefficient identities over exact rational arithmetic, exhaustively reconstructs all rational triples with bounded integer endpoints satisfying \(2b_3=b_2+b_4\), verifies that \( (0,1,0)\) is excluded by degree one, and checks the explicit quadratic correction used for arbitrary values at levels \(2,3,4\). Its output is stored in `verification_output.txt`.

The finite replay is corroborative. The universal lower bound is the symbolic coefficient elimination above, and the universal upper bound follows from the reconstructed cyclotomic-field induction.

## Relationship to prior work
Vélez--Cadavid, arXiv:2609.27084v1, introduce the same truncation-compatible cosine-point framework and prove that every rational-valued sequence is realizable with uniform total degree at most two. Their theorem and surrounding discussion do not state that degree two is minimal, and targeted searches of the paper found no degree-one classification or optimality statement.

Their earlier arXiv:2602.07638v1 develops the symmetric compatible-family framework and stable-range rigidity, but it addresses a different structural regime and does not provide this low-level degree-one obstruction. The present finding is a sharpness result for the sequel's arbitrary-sequence interpolation theorem: the first three levels already force a codimension-one constraint in degree one.

## Limitations
The relation \(2b_3=b_2+b_4\) is a complete classification only of the first three evaluated levels for degree-one compatible families. It is not claimed to characterize all infinite sequences admitting a degree-one realization. No claim is made about minimal degree under additional symmetry, integrality, positivity, or other coefficient restrictions.

## References
1. J. D. Vélez and C. A. Cadavid, *Galois-Orbit Structure, Ramanujan Sums, and Stable-Range Collapse for Cyclotomic Cosine Formulas*, arXiv:2609.27084v1, 22 September 2026. See Definition 2.1--2.4 and especially Theorem 2.6.
2. J. D. Vélez and C. A. Cadavid, *Inverse-Limit Formulas and Stable-Range Rigidity for Cyclotomic Sums*, arXiv:2602.07638v1, 7 February 2026.
