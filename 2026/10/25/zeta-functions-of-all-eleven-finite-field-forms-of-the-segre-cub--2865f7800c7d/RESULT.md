# Zeta functions of all eleven finite-field forms of the Segre cubic

## Finding
Let \(q\) be a prime power of characteristic \(p\ge5\). The Segre cubic primal is the projective threefold
\[
X:\quad \sum_{i=1}^{6}x_i=\sum_{i=1}^{6}x_i^3=0\quad\subset\mathbb P^5.
\]
For each permutation \(\sigma\in S_6\), let \(X_\sigma\) be the form whose geometric-coordinate Frobenius permutation is \(\sigma\). These forms are classified by the eleven partitions of six. **The complete point-count classification** is
\[
\#X_\sigma(\mathbb F_q)=q^3+a_\sigma q^2+b_\sigma q+1,
\]
with the following exhaustive table. The columns \(m,n,r\) count, respectively, Frobenius-fixed perfect matchings of six labels, fixed unordered \(3+3\) partitions, and fixed individual rulings of the ten nodal tangent quadrics.

| Cycle partition of \(\sigma\) | \(m\) | \(n\) | \(r\) | \(a_\sigma\) | \(b_\sigma\) | Count over \(\mathbb F_5\) |
|:--|--:|--:|--:|--:|--:|--:|
| \((1,1,1,1,1,1)\) | 15 | 10 | 20 | 6 | -4 | 256 |
| \((2,1,1,1,1)\) | 3 | 4 | 0 | 0 | 4 | 146 |
| \((2,2,1,1)\) | 3 | 2 | 4 | 2 | 0 | 176 |
| \((2,2,2)\) | 7 | 4 | 8 | 4 | 0 | 226 |
| \((3,1,1,1)\) | 0 | 1 | 2 | 0 | -1 | 121 |
| \((3,2,1)\) | 0 | 1 | 0 | 0 | 1 | 131 |
| \((3,3)\) | 3 | 1 | 2 | 3 | 2 | 211 |
| \((4,1,1)\) | 1 | 0 | 0 | 2 | 2 | 186 |
| \((4,2)\) | 1 | 2 | 0 | 0 | 2 | 136 |
| \((5,1)\) | 0 | 0 | 0 | 1 | 1 | 156 |
| \((6)\) | 1 | 1 | 2 | 1 | 0 | 151 |

This also determines **every extension-field count and the entire Hasse–Weil zeta function**, not merely the first point count. Write \(M\), \(N\), and \(R\) for the finite \(S_6\)-sets of 15 perfect matchings, ten unordered \(3+3\) partitions, and twenty individual rulings over those partitions, respectively. For every integer \(s\ge1\),
\[
\#X_\sigma(\mathbb F_{q^s})=q^{3s}+1
 +\bigl[1+\#M^{\sigma^s}-\#N^{\sigma^s}\bigr]q^{2s}
 +\bigl[1+\#M^{\sigma^s}-\#R^{\sigma^s}\bigr]q^s.
\]
For a finite \(\sigma\)-set \(U\), let \(\mathcal O_\sigma(U)\) be its cycles. Equivalently,
\[
Z(X_\sigma,T)=\frac{
\displaystyle\prod_{O\in\mathcal O_\sigma(N)}[1-(q^2T)^{|O|}]
\prod_{O\in\mathcal O_\sigma(R)}[1-(qT)^{|O|}]
}{
(1-T)(1-q^3T)(1-qT)(1-q^2T)
\displaystyle\prod_{O\in\mathcal O_\sigma(M)}[1-(qT)^{|O|}][1-(q^2T)^{|O|}]
}.
\]

## Assumptions and scope
The ground field is \(\mathbb F_q\), with characteristic at least five. Frobenius acts by permutation of the **six Segre coordinates** (as opposed to the distinct, outer-automorphism-related permutation of six marked points in the moduli description). An equivalent intrinsic definition of \(X_\sigma\) uses the étale algebra \(E=\prod_j\mathbb F_{q^{d_j}}\) for the cycle lengths \(d_j\) of \(\sigma\), and the equations \(\operatorname{Tr}_{E/\mathbb F_q}(u)=\operatorname{Tr}_{E/\mathbb F_q}(u^3)=0\) in the projectivization of the six-dimensional underlying \(\mathbb F_q\)-vector space of \(E\). Counts concern rational **points on the singular projective cubic**, rather than its resolution or its smooth locus. No small-characteristic assertion is made.

For \(A\subset\{1,\ldots,6\}\) of size three, the two subsets \(A\) and \(A^c\) represent one member of \(N\). The six planes containing the associated node are the perfect matchings pairing each element of \(A\) to one element of \(A^c\). They separate canonically into the two parity triples of bijections between the two size-three sets; these are the two rulings of the tangent quadric. The collection of two triples for all ten nodes defines the twenty-element \(S_6\)-set \(R\). It is independent of choices of ordering, since reordering can only interchange the two parity triples.

## Proof
**Geometry and resolution.** Over an algebraic closure, \(X\) has ten ordinary double points, represented by \([1:1:1:-1:-1:-1]\) and its coordinate permutations, and fifteen planes, indexed by perfect matchings of the six coordinates through equations of the form \(x_i+x_j=x_k+x_l=x_m+x_n=0\). Each node lies on exactly six of the fifteen planes. The blowup \(\pi:Y\to X\) of the ten nodes is smooth and is isomorphic to \(\overline M_{0,6}\); the exceptional surface at each node is \(Q\cong\mathbb P^1\times\mathbb P^1\). These standard geometric facts are documented in Dolgachev [2]. The description, including its incidence geometry, is valid in characteristic \(p\ge5\).

**The equivariant Picard character.** The cohomology of \(Y\) is algebraic and purely in even degrees; \(H^0\) and \(H^6\) each have rank one, while \(H^2\) and \(H^4\) have rank sixteen. The fifteen strict transforms of the planes give independent rational Picard classes, and their span is the 15-dimensional permutation module on \(M\). The sum of the ten exceptional quadrics adds an independent invariant class. To verify independence without a numerical conjecture, use Keel's presentation of \(\operatorname{Pic}(\overline M_{0,6})\otimes\mathbb Q\): 25 boundary classes (fifteen \((2,4)\) and ten \((3,3)\)), modulo nine independent four-point relations. The span of the fifteen \((2,4)\)-classes has rank fifteen modulo those relations, and adding the sum of the ten \((3,3)\)-classes raises the rank to sixteen. Under the standard Segre--moduli correspondence, these are respectively the plane and exceptional classes; its two symmetric-six coordinate actions differ by the classical outer automorphism, so \(M\) **must** be the matching action in the displayed equation. The rank statements are reproduced by `verify_segre.py`. Thus
\[
\operatorname{Tr}(\sigma\mid H^2(Y))=1+\#M^\sigma.
\]
Poincaré duality, an invariant ample class and Hard Lefschetz identify the corresponding traces on \(H^4\). The Lefschetz trace formula gives
\[
\#Y_\sigma(\mathbb F_{q^s})
 =1+q^{3s}+(1+\#M^{\sigma^s})(q^s+q^{2s}).
\]

**Blowdown correction and ruling character.** At a node of type \(A\mid A^c\), the six incident planes are indexed by bijections \(A\to A^c\). Two of these planes intersect along a line through the node precisely when their bijections differ by an odd permutation; hence the even and odd triple families are the two rulings of the exceptional quadric. This identification can also be read from the tangent quadratic form. The Frobenius-fixed exceptional quadric has \(q^{2s}+1+2q^s\) points when its rulings are individually fixed and \(q^{2s}+1\) when Frobenius exchanges them. Non-fixed nodes contribute no rational points to the exceptional locus. Accordingly, replacing the ten exceptional quadrics with their nodes removes exactly
\[
\#N^{\sigma^s}q^{2s}+\#R^{\sigma^s}q^s
\]
points. Subtract this from the \(Y\)-formula to obtain the theorem. Taking the logarithmic exponential of the point counts gives the displayed rational zeta product.

**Exhaustive conjugacy-class computation.** Every permutation of six labels has one of the eleven listed cycle partitions. The small finite sets \(M,N,R\) and their Frobenius fixed counts can be enumerated exactly; the code enumerates every matching, node, and parity triple and checks all eleven \((m,n,r)\)-profiles. This is an exhaustive **finite input** computation; the formulas for every prime power and extension degree follow from the proved geometry and trace formula, not extrapolation from a few finite fields.

## Verification
Run `python verify_segre.py` after installing `requirements.txt`: it prints all eleven fixed-set and coefficient profiles, verifies the rank of Keel's 25-by-relations presentation (nine independent relations), and verifies that the fifteen plane classes plus one invariant exceptional class span rank sixteen. Independently, run `python verify_finitefield.py`, which constructs actual extension fields of \(\mathbb F_5\), imposes the two trace equations in each of the eleven étale algebras, divides the number of nonzero affine solutions by four, and obtains exactly the eleven projective counts shown in the table. These independent point enumerations check every conjugacy type at \(q=5\) but are not substituted for the geometric proof over arbitrary finite fields.

## Relationship to prior work
Dolgachev [2] establishes the Segre primal's ten nodes, fifteen planes, symmetric coordinate equations and its relationship with the compactification \(\overline M_{0,6}\). Keel's Picard relations, explained by Carr [1], provide the requisite rational Picard character. Avilov [3] studies Galois forms and birational geometry of the Segre cubic; forms and the classification mechanism are therefore not claimed as original. The contribution here is the explicit **all-eleven-class arithmetic point-count and zeta classification**, with the non-split exceptional-ruling correction, rather than the known classification of forms itself. An equivalent formula in finite-field equivariant moduli literature remains a priority risk.

## Limitations
This result is restricted to characteristic at least five. It does not claim new facts about the known geometric Segre cubic, all possible arithmetic degenerations in characteristics two or three, or integral cohomological lattices. The finite-field enumerator tests \(q=5\) only; its agreement cannot on its own prove the uniform statement. A literature search cannot establish absolute originality, and independent mathematical review has not been performed.

## References
[1] S. Carr, *A polygonal presentation of Pic of the moduli space of genus-zero curves*, arXiv:0911.2649 (first publicly posted 2009-11-13). https://arxiv.org/abs/0911.2649

[2] I. Dolgachev, *Corrado Segre and nodal cubic threefolds*, arXiv:1501.06432 (first publicly posted 2015-01-26), especially §2. https://arxiv.org/abs/1501.06432

[3] A. Avilov, *On forms of the Segre cubic*, arXiv:1812.11363 (first publicly posted 2018-12-29), especially §§2–3. https://arxiv.org/abs/1812.11363
