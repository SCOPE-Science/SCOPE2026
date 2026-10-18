# Two-cycle wedge rank polynomials and Jordan strata of finite incidence algebras

## Finding

Let \(q\) be any prime power, and let \(n,m\ge 2\). Form the bipartite graph \(B_{n,m}\) by identifying one vertex on the same color side of the two even cycles \(C_{2n}\) and \(C_{2m}\), with no other identifications. Its color classes have sizes \(n+m-1\) and \(n+m\), and it has \(2n+2m\) distinct edges. For each assignment of independent edge weights in \(\mathbb F_q\), let \(M\) denote the associated \((n+m-1)\times(n+m)\) bipartite matrix.

The *complete rank polynomial*
\[
\mathcal W_{n,m}(q,z)=\sum_{M}z^{\operatorname{rank}M}
\]
is given by the following explicit formulas involving only powers of a fixed \(2\times2\) matrix. Put \(a=q-1\), \(c=q(q-1)\), and
\[
T=\begin{pmatrix}1&az\\q&0\end{pmatrix},\qquad
P_n(q,z)=(1,0)T^{2n-2}\binom{1}{1}.
\]
Define the Lucas polynomials \(L_0=2\), \(L_1=1\), and \(L_j=L_{j-1}+czL_{j-2}\) for \(j\ge2\). Define
\[
S_n(q,z)=L_{2n}+(q-1)^{2n-1}z^{n-1}-q(q-1)^{2n-1}z^n
\]
and
\[
Q_n(q,z)=\frac{S_n(q,z)-q^2zP_n(q,z)}{1-z}.
\]
This quotient is a polynomial in the indeterminates \(q,z\) with integer coefficients. Then
\[
\boxed{\mathcal W_{n,m}(q,z)=q^4zP_n(q,z)P_m(q,z)+(1-z)Q_n(q,z)Q_m(q,z).}
\]
Thus every rank stratum is the corresponding coefficient of this explicitly evaluable polynomial, for every finite field, including characteristic two. The formula uses \(O(n+m)\) polynomial-matrix recurrence steps and does not enumerate the \(q^{2n+2m}\) matrices.

More generally, if bipartite graphs \(G,H\) share exactly one vertex in the row color class, let \(M_G^-\) denote a weighted biadjacency matrix with that row removed. Define
\[
F_G(z)=\sum_{M_G}z^{\operatorname{rank}(M_G^-)}
\]
and
\[
D_G(z)=\sum_{M_G}z^{\operatorname{rank}(M_G^-)}
\mathbf 1\!\left[\text{the removed row lies in }\operatorname{Row}(M_G^-)\right].
\]
Then the complete rank polynomial of their vertex wedge satisfies
\[
\boxed{\mathcal W_{G\vee H}(z)=zF_G(z)F_H(z)+(1-z)D_G(z)D_H(z).}
\]
The weights on all edges are independently summed over \(\mathbb F_q\). The same formula holds for identifying vertices in the column color class after transposing the matrices. This is the underlying rank-gluing mechanism.

For all-nonzero edge weights in the two-cycle wedge, exactly \((q-1)^{2n+2m-2}\) assignments have rank \(n+m-2\), and all other \((q-1)^{2n+2m}-(q-1)^{2n+2m-2}\) assignments have full row rank \(n+m-1\). In particular, for \(q=2\) the unique all-nonzero assignment has rank defect one; for larger fields the rank-defect probability conditioned on full support is exactly \((q-1)^{-2}\).

Let \(\mathcal P_{n,m}\) be the height-two poset with minimal and maximal elements given by the two color classes and order relations given exactly by the edges. Its incidence algebra \(I(\mathcal P_{n,m},\mathbb F_q)\) has radical \(J\) with \(J^2=0\). Each element of \(J\), acting on the natural \((2n+2m-1)\)-dimensional representation, has Jordan type
\[
(2^r,1^{2n+2m-1-2r})
\]
precisely when the corresponding \(M\) has rank \(r\). The coefficient \([z^r]\mathcal W_{n,m}(q,z)\) therefore gives its exact nilpotent Jordan-type census.

For \(n=m=2\) the polynomial simplifies to
\[
\boxed{\mathcal W_{2,2}(q,z)=1+(q-1)(q+1)^3z+q(q-1)^2(q+1)(3q^2+3q+2)z^2+q^2(q-1)^3(q+1)^3z^3.}
\]
The rank vectors are \((1,27,120,108)\) over \(\mathbb F_2\), \((1,128,1824,4608)\) over \(\mathbb F_3\), and \((1,375,11160,54000)\) over \(\mathbb F_4\).

## Assumptions and scope

All fields are finite fields \(\mathbb F_q\) of prime-power size \(q\). The integers \(n,m\) range independently over all integers at least two. Every edge represents a distinct matrix entry; one cycle vertex is shared, but no edge is shared. Rank is ordinary rank over \(\mathbb F_q\), with no nonzero-weight restriction unless explicitly stated. The incidence-algebra interpretation uses the standard faithful incidence representation ordered with all minimal elements first. The statement counts labelled matrices and radical elements, not equivalence classes of matrices or posets.

## Proof

**1. Rank of a weighted bipartite forest.** Let \(F\) be any bipartite forest with nonzero weights on exactly the edges of \(F\), and let \(M_F\) be its rectangular bipartite matrix. Every nonzero minor of size \(r\) corresponds to a matching of size \(r\), hence \(\operatorname{rank}M_F\le\nu(F)\), the maximum matching size. Conversely, choose a maximum matching and restrict to its selected rows and columns. The induced graph is a forest with a perfect matching, which must be unique: two different perfect matchings would have alternating-cycle symmetric difference. Thus this square minor is one nonzero monomial, so \(\operatorname{rank}M_F=\nu(F)\) in every characteristic and for every assignment of nonzero edge weights.

**2. Cycles with one row deleted.** Label a cycle \(C_{2n}\) so that its \(n\times n\) matrix has entries on the diagonal and the cyclic superdiagonal. Delete row zero. The remaining \((n-1)\times n\) matrix is an ordinary bidiagonal path matrix. Its \(2n-2\) potential edges form a path alternating between \(n\) column vertices and \(n-1\) row vertices. A support consisting of runs of \(\ell\) consecutive present edges has matching number \(\sum\lceil\ell/2\rceil\). Reading the path edges from left to right, use the two states even/odd current nonzero-run length. A zero edge resets to even; a nonzero edge changes parity and contributes a factor of \(z\) precisely when its previous parity was even. The transfer matrix is \(T\) above, since the odd-to-even transition has weight \(1+(q-1)=q\). Hence the rank polynomial for the deleted-row matrices is \(P_n\).

Write \(E\subseteq\mathbb F_q^n\) for the span of the two column coordinate vectors incident to the deleted row. For a deleted-row matrix \(B\), the number of possible deleted rows lying in \(\operatorname{Row}(B)\) is \(q^t\), where \(t=\dim(E\cap\operatorname{Row}(B))\). Let \(B^\circ\) be \(B\) restricted to its \(n-2\) interior columns. Restriction to these columns maps \(\operatorname{Row}(B)\) to \(\operatorname{Row}(B^\circ)\) with kernel its intersection with \(E\). Rank-nullity therefore gives
\[
t=\operatorname{rank}(B)-\operatorname{rank}(B^\circ).
\]
Both support graphs are forests, so this dimension depends only on the zero pattern, not on any nonzero values. This also proves that the polynomial \(Q_n\) defined below has a direct sum-of-nonnegative-terms interpretation.

**3. Single-cycle rank polynomial.** When at least one cycle weight is zero, the nonzero support is a disjoint union of paths, and its rank is the matching number by Step 1. The cyclic parity-state transfer calculation gives \(L_{2n}\), with recurrence \(L_j=L_{j-1}+q(q-1)zL_{j-2}\). For the all-nonzero support, the determinant is the signed difference of the products of the two alternating perfect matchings. Exactly \((q-1)^{2n-1}\) of the \((q-1)^{2n}\) nonzero assignments make it vanish; their rank is exactly \(n-1\), since deleting any cycle row leaves a rank-\((n-1)\) path matrix. The cyclic transfer trace counts the all-nonzero support twice in the formal parity states. Subtracting those two formal contributions and adding the actual full-support contributions gives precisely \(S_n\).

There are \(q^2\) possible deleted rows for each path matrix \(B\), so the full-cycle rank polynomial equals \(Q_n+z(q^2P_n-Q_n)\): the row increases rank by one exactly when it is outside the rowspace of \(B\). Hence
\[
Q_n=\frac{S_n-q^2zP_n}{1-z}.
\]
The preceding rowspace count proves that this rational expression is polynomial and has a nonnegative integer count for every prime-power evaluation.

**4. Gluing at the row vertex.** Delete the identified row from the two-cycle wedge. The remaining matrix is block diagonal on disjoint column supports, with path components \(B_n\) and \(B_m\). Its rank is their rank sum. The single identified row lies in the direct-sum rowspace exactly when its two respective components separately lie in \(\operatorname{Row}(B_n)\) and \(\operatorname{Row}(B_m)\). For a fixed pair of deleted-row matrices, the number of identified rows yielding no rank increase is the product of the two individual counts; all other identified rows raise the rank by exactly one. Summing gives the general vertex-wedge identity and, with \(F_{C_{2n}}=q^2P_n\) and \(D_{C_{2n}}=Q_n\), the boxed formula for \(\mathcal W_{n,m}\).

**5. Full-support boundary and Jordan form.** With all cycle edges nonzero, each deleted-row path matrix has full row rank. The glued matrix has rank \(n+m-2\) precisely when the shared row lies in both path rowspaces, equivalently when both separate cycle determinants vanish. Each vanishing cycle determinant imposes one independent multiplicative equation on its own \(2n\) or \(2m\) nonzero edge weights, yielding \((q-1)^{2n-1}(q-1)^{2m-1}\) simultaneous solutions. Otherwise the glued matrix has rank \(n+m-1\). Finally, the incidence-algebra radical matrix has block form \(\left(\begin{smallmatrix}0&M\\0&0\end{smallmatrix}\right)\). Its square is zero, so the number of Jordan blocks of size two equals its rank, and every other block has size one. This gives the claimed Jordan-type correspondence.

## Verification

The standalone checker `figure_eight_checker.py` enumerates all matrix entries and computes matrix rank directly, independently of the support-polynomial proof, for \((n,m,q)=(2,2,2),(2,2,3),(2,2,4),(2,2,5),(2,3,2),(2,3,3),(3,3,2)\). Its finite-field implementation includes a direct arithmetic model of \(\mathbb F_4\). It also checks the total mass of the predicted polynomials in three additional parameter configurations. The reported result is `ALL_FIGURE_EIGHT_RANK_CHECKS_PASSED`. Finite checks do not replace the proof for arbitrary \(n,m,q\).

Reproduction requires Python 3 only; execute `python3 figure_eight_checker.py` from the directory containing this file. No external dependencies or network connections are required.

## Relationship to prior work

The single-cycle part \(S_n\), including the full-support determinant correction, is already established in the publicly available result *Cycle graphical groups have an explicit character-degree enumerator* (2026). Its exact cycle rank polynomial is **not claimed as new**. *Tree graphical groups have matching-support character polynomials* (2026) establishes the forest matching-rank mechanism, also prior art. The new statement treated here is the rank-stratified vertex-gluing identity and its explicit interacting two-cycle wedge evaluation, yielding the Jordan-type distribution for a different family of sparse algebras. Neither cited result states the two-cycle wedge formula or the joint shared-row condition needed for it.

Fuchs and Kirillov (2022) study unrestricted upper-triangular nilpotent matrices grouped by Jordan partition, not matrices constrained by the relations of the specified height-two incidence poset. Their aggregate Jordan-type polynomials do not determine the restricted incidence-algebra counts. The classical generic-rank/matching theorem for Edmonds bipartite matrices also does not count finite-field rank cancellations on full cycle support.

## Limitations

The formula concerns two *even* cycles joined at a single vertex of the same bipartition side, and finite-field weights. It does not count similarity or automorphism orbits, arbitrary graphs with overlapping edges, or higher nilpotency indices. The cut-vertex identity applies more generally, but does not by itself supply explicit component polynomials for all bipartite graphs. An equivalent rooted-rank gluing formula in unindexed matrix-enumeration literature remains a priority risk. The finite checks cover only the listed small parameters; independent external mathematical audit has not been performed.

## References

1. Dmitry Fuchs and Alexandre Kirillov, *Jordan types of triangular matrices over a finite field*, arXiv:2204.00066, first posted 2022-03-31; Arnold Mathematical Journal 8 (2022), 543–559. https://arxiv.org/abs/2204.00066
2. *Cycle graphical groups have an explicit character-degree enumerator*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e
3. *Tree graphical groups have matching-support character polynomials*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-tree-graphical-groups-have-matching-support-character-polynomial--fb80c871ed65
4. J. Edmonds, *Systems of distinct representatives and linear algebra*, Journal of Research of the National Bureau of Standards Section B 71B (1967), 241–245 (generic bipartite matrix rank and matching background).
