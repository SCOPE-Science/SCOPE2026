# Exact enumeration of surjective bounded morphisms between layered Kripke frames

## Finding
For any positive level-size vectors \(\mathbf a=(a_1,\ldots,a_h)\) and \(\mathbf b=(b_1,\ldots,b_k)\), let \(W(\mathbf a)\) and \(W(\mathbf b)\) be ordinal sums of antichains of the indicated sizes. Regard these partial orders as reflexive, transitive Kripke frames. A **surjective bounded morphism** is an onto set map \(f:W(\mathbf a)\to W(\mathbf b)\) satisfying
\[
f(\uparrow x)=\uparrow f(x)\qquad\text{for every source point }x,
\]
where \(\uparrow x=\{y:x\le y\}\). This single equality incorporates the usual forth and back conditions.

Define the onto-function and partial-onto-function numbers, for positive integers \(n,q\), by
\[
S(n,q)=\sum_{r=0}^{q}(-1)^r\binom qr(q-r)^n,\qquad
T(n,q)=\sum_{r=0}^{q}(-1)^r\binom qr(q+1-r)^n.
\]
Thus \(S(n,q)\) counts functions onto a designated \(q\)-element set, while \(T(n,q)\) counts functions to that set together with one optional extra value, requiring all \(q\) designated values to appear.

There is an exact two-table recurrence for the number of surjective bounded morphisms. Let \(F_{i,j}\) count such morphisms between the first \(i\) source levels and first \(j\) target levels. Let \(G_{i,j}\) be the **terminal-subset sum**: choose a nonempty subset \(U\subseteq A_i\), replace the final source level \(A_i\) by \(U\), and count morphisms to the first \(j\) target levels, summing over all choices of \(U\). Set
\[
F_{0,0}=1,\qquad F_{0,j}=0\ (j>0),\qquad F_{i,0}=0\ (i>0).
\]
For \(i,j\ge1\), the following cases completely determine \(F\) and \(G\):

If \(b_j\ge2\), then
\[
F_{i,j}=S(a_i,b_j)F_{i-1,j-1},\qquad
G_{i,j}=T(a_i,b_j)F_{i-1,j-1}.
\]
If \(j=1\) and \(b_1=1\), then
\[
F_{i,1}=1,\qquad G_{i,1}=2^{a_i}-1.
\]
If \(j\ge2\) and \(b_j=1\), then
\[
F_{i,j}=\sum_{t=1}^{i-1}G_{t,j-1},\qquad
G_{i,j}=(2^{a_i}-1)F_{i,j}.
\]
**The required answer is \(F_{h,k}\).** Prefix sums give \(O(hk)\) table transitions once the values \(S(a_i,b_j)\) and \(T(a_i,b_j)\) have been computed. Direct inclusion-exclusion precomputation takes \(O(h\sum_j b_j)\) integer-arithmetic terms, disregarding bit complexity and exponentiation costs.

## Assumptions and scope
Every source and target level is nonempty. Within any level distinct points are incomparable; between levels, every point of a lower level is strictly below every point of a higher level. All points are individually labeled, so two maps differing on a point are counted separately. For two source points in one level there is no order relation except equality. The accessibility relation for the Kripke frame is exactly the reflexive partial order \(\le\), not only its strict cover relation.

The equality \(f(\uparrow x)=\uparrow f(x)\) forces order preservation because \(x\le y\) implies \(f(y)\in\uparrow f(x)\), and imposes the back condition because every target successor of \(f(x)\) must be the image of a source successor of \(x\). Onto is an additional global condition. Equivalently, in the upper Alexandrov topologies of the two posets, the maps counted are exactly the continuous open surjections: continuity is monotonicity, and a continuous map is open precisely when it sends each principal upper open set onto the principal upper set of its image point. Empty frames, preorders with nontrivial equivalence classes, arbitrary graded posets, and valuation-respecting maps are not included.

The auxiliary value \(G_{i,j}\) is a sum over nonempty subsets of the labeled *last* source level. It is not itself the count of maps from the full \(i\)-level source and is not another claimed invariant.

## Proof
First note that if \(x\) is maximal in the source frame, then \(\uparrow x=\{x\}\). Hence the back condition forces \(\uparrow f(x)=\{f(x)\}\), so \(f(x)\) is maximal in the target frame. In particular, every point of the last source level \(A_i\) maps to the final target antichain \(B_j\).

**Case \(b_j\ge2\).** Surjectivity requires all points of \(B_j\) to occur. They must all occur in \(f(A_i)\): if an earlier source point \(y\) mapped to some \(v\in B_j\), then \(y<x\) for every \(x\in A_i\), so order preservation would force all of \(f(A_i)\) to equal \(v\), contradicting surjectivity onto the at-least-two-point antichain \(B_j\). Therefore \(f|_{A_i}\) is onto \(B_j\) and all earlier source points map below \(B_j\). For each earlier source point, any original witness of a successor lying in the lower target prefix must belong to the earlier source prefix, because points of \(A_i\) all map to \(B_j\). Thus restriction gives a surjective bounded morphism between the two lower prefixes. Conversely, such a prefix morphism and any surjection \(A_i\to B_j\) combine to a bounded morphism: for every earlier source point, each new maximal target successor has a witness in \(A_i\). The factors are independent, giving \(F_{i,j}=S(a_i,b_j)F_{i-1,j-1}\). If only a nonempty subset of \(A_i\) is retained, the same factorization applies. Summing over subsets gives
\[
\left(\sum_{m=1}^{a_i}\binom{a_i}{m}S(m,b_j)\right)F_{i-1,j-1}
=T(a_i,b_j)F_{i-1,j-1},
\]
which is the claimed formula for \(G_{i,j}\).

**Case \(b_1=1\).** The target is a one-point frame. For every nonempty source prefix exactly one constant map exists and satisfies the bounded-morphism condition, proving \(F_{i,1}=1\). There are \(2^{a_i}-1\) nonempty terminal subsets, giving \(G_{i,1}=2^{a_i}-1\).

**Case \(j\ge2\) and \(b_j=1\).** All points of \(A_i\) map to the unique maximal target point \(v\). Given a surjective bounded morphism, let \(t<i\) be the final source level containing a point whose image is not \(v\), and let \(U\) be the nonempty subset of \(A_t\) mapped below \(v\). Every point of a lower source level maps below \(v\), since it lies below a point of \(U\); every point in a source level above \(t\) maps to \(v\). The image of each point of \(U\) is maximal within the penultimate target prefix. Otherwise its missing upper target successor in that prefix would require, by the back condition, a source witness above it: none can occur in another point of the same antichain or in any higher source level (which all map to \(v\)). Therefore those \(U\)-images lie in \(B_{j-1}\).

Restrict to the lower source prefix \(A_1\oplus\cdots\oplus A_{t-1}\oplus U\) and the target prefix \(B_1\oplus\cdots\oplus B_{j-1}\). This restriction is surjective because all lower target points were attained before the last image at \(t\); its back condition holds because a witness for a lower target successor cannot come from any of the discarded source points (all of which map to \(v\)). Conversely, choose \(t<i\), a nonempty \(U\subseteq A_t\), and a surjective bounded morphism between these truncated prefixes. Extend it uniquely by sending \(A_t\setminus U\) and every later source level to \(v\). Order preservation holds, and every source point mapped below \(v\) has a later source witness at \(v\), as \(t<i\); all lower-target successor witnesses are inherited from the restricted morphism. These constructions are inverse and disjoint for distinct \(t,U\), proving
\[
F_{i,j}=\sum_{t=1}^{i-1}G_{t,j-1}.
\]
Finally, whenever the final target level is the singleton \(\{v\}\), all points of the final source level, regardless of its positive cardinality, are forced to map to \(v\). Hence replacing that final level by any nonempty subset does not change the number of maps. There are \(2^{a_i}-1\) such subsets, proving \(G_{i,j}=(2^{a_i}-1)F_{i,j}\).

The three cases exhaust all positive level-size vectors. Induction on the total number of source and target levels establishes the recurrence for every admissible pair, and therefore the exact count \(F_{h,k}\).

## Verification
Running `python3 artifacts/check_pmorph.py` checks the recurrence against a separately implemented brute-force enumerator of all set functions. The enumerator tests *every set function*, checks surjectivity, and checks the defining equality \(f(\uparrow x)=\uparrow f(x)\) for every source point. It agrees on all \(687\) tested source-target level-vector pairs of heights at most three, with level sizes one, two or three, source total size at most seven, target total size at most six, and target size no larger than source size. Six larger recurrence anchors are also verified (they are not exhaustive-map checks). The output is `PASS: 687 exhaustive pairs; 6 anchors`.

For example, the recurrence counts \(12\) bounded morphisms from \(W(3,3)\) to \(W(2,1)\), but only \(6\) from \(W(3,3)\) to \(W(1,2)\). These unequal values reflect the structural effect of a singleton *terminal* target level, rather than mere cardinalities of the frames. When every target level has at least two elements, the recurrence also immediately forces the source and target heights to agree and gives the product of ordinary surjection counts between corresponding levels.

The numerical tests detect some boundary and indexing mistakes; the proof, not finite enumeration, establishes the universally quantified statement.

## Relationship to prior work
Kupke and Pattinson give the coalgebraic account of Kripke frames as set-valued successor maps and of structure-preserving coalgebra morphisms. For the powerset functor, their morphism equation specializes to the bounded-morphism equality used here; it does not provide an enumeration by weak-order level vectors. Barmak and Minian supply the finite-space/poset correspondence underlying the ordinal-sum constructions.

A published exact recurrence for all order-preserving maps between finite weak orders counts a strictly broader class: it neither requires surjectivity nor imposes local back conditions. The distinction persists even after imposing surjectivity: from \(W(1,3,1)\) onto \(W(1,2,1)\), map the bottom source point to the bottom target point, three middle source points to respectively the bottom and the two middle target points, and the top point to the top. This map is monotone and onto, but the middle source point mapped to the bottom target point has no successor mapping to either middle target point, so it violates the bounded-morphism back condition. Thus the published all-map count does not give the present count by substitution, although the objects are the same. A different published classification of weak-order mapping-space homotopy classes counts nonconstant levelwise maps when there are no singleton levels; its count is neither an enumeration of onto bounded morphisms nor a treatment of singleton gates. Huczynska and Ruškuc study orders induced by surjective homomorphisms of combinatorial structures. The accessible abstract does not specify bounded morphisms or a cardinality recurrence; the unavailable accepted manuscript is a residual literature-comparison risk.

## Limitations
The formula concerns surjective upper-back morphisms of finite *partial-order* frames with complete comparabilities between levels, not arbitrary Kripke frames, general finite posets, directed acyclic graphs with only cover edges, or maps that must preserve designated valuations. Distinct labeled maps are counted, not quotient isomorphism classes or bisimulation classes. The \(O(hk)\) statement concerns table transitions after the numerical surjection weights have been obtained; computing large integers has additional cost. The identified literature does not conclusively rule out an equivalent formula in unindexed modal, order-theoretic, or coalgebraic sources.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first posted 2006-11-06; in particular, Section 2 gives the finite-space/poset correspondence.
2. C. Kupke and D. Pattinson, *Coalgebraic Semantics of Modal Logics: an Overview*, *Theoretical Computer Science* 412 (2011), 5070–5094, DOI: 10.1016/j.tcs.2011.04.023; author manuscript: https://users.cecs.anu.edu.au/~dpattinson/Publications/tcs2011.pdf, especially Sections 2–4.
3. S. Huczynska and N. Ruškuc, *Homomorphic image orders on combinatorial structures*, *Order* 32 (2015), 205–226, DOI: 10.1007/s11083-014-9326-8, early online 2014-06-06.
4. *Exact cardinality recurrence for mapping spaces between finite weak orders*, published 2026-10-04, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-cardinality-recurrence-for-mapping-spaces-between-finite-w--1cee64311a06/RESULT.md.
5. *Off-diagonal homotopy rigidity for finite weak-order pseudospheres*, published 2026-10-04, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-off-diagonal-homotopy-rigidity-for-finite-weak-order-pseudospher--b0d3c63112c5/RESULT.md.
