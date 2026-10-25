# Sharp facet-gap extremizers among pure rank-thin posets

## Finding
For a finite nonempty pure graded poset \(P\), write \(h\) for the number of elements on each maximal chain, \(n=|P|\), and \(m=n-h\). Assume each rank contains one or two elements, so \(0\le m\le h\). Define the **facet gap**
\[
G(P)=f_{n-1}(\mathcal C(P))-f_{n-1}(\mathcal O(P)),
\]
where \(\mathcal C(P)\) and \(\mathcal O(P)\) are its standard chain and order polytopes in \(\mathbb R^n\).

**Fixed height and order.** For every such \(P\),
\[
\boxed{G(P)\le 2^m-m-1-\max\{0,2m-h-1\}.}
\]
Equality is attained by complete layered posets whose rank sizes are one or two and whose doubleton ranks have as few adjacent pairs as possible. For \(h\ge3\), these are exactly all equality cases, up to rank-preserving isomorphism. For \(h\le2\), the gap vanishes for every such poset (including incomplete adjacent cover graphs).

**Fixed total size.** For every integer \(n\ge5\), the exact maximal gap over all pure graded rank-thin \(n\)-element posets is
\[
\boxed{M_n=\begin{cases}2^{n/2}-n,&n\text{ even},\\2^{(n-1)/2}-n+2,&n\text{ odd}.\end{cases}}
\]
For even \(n=2k\ge6\), the sole maximizing isomorphism type is the ordinal sum of \(k\) doubleton antichains. For odd \(n=2k+1\ge5\), the maximizing types are ordinal sums of \(k\) doubleton antichains and one singleton rank inserted at an **interior** position; the singleton has \(k-1\) distinct placements. For \(n\le4\) every admissible gap is zero. Every graded poset of width at most two is rank-thin, so these conclusions apply to that geometric subclass.

## Assumptions and scope
A poset is *pure graded* here if it has a rank function with ranks \(1,\ldots,h\) such that every maximal chain meets every rank once. A *complete layered poset* with rank sizes \(r_1,\ldots,r_h\) is the ordinal sum of antichains of those cardinalities, so each element of rank \(i\) is below each element of every higher rank. Each \(r_i\) belongs to \(\{1,2\}\). Height counts elements, not cover edges. The facet counts concern full-dimensional polytopes in their standard \(n\)-coordinate embeddings. No assumption is made that rank-thin posets themselves have width two; some have larger width, and the result covers them as well. All claimed sharpness and uniqueness assertions are relative to the stated class.

## Proof
**1. Facet-count identity.** Standard irredundant descriptions of finite-poset chain and order polytopes give
\[
f_{n-1}(\mathcal C(P))=n+c(P),\qquad
f_{n-1}(\mathcal O(P))=\operatorname{min}(P)+\operatorname{max}(P)+e(P),
\]
where \(c(P)\) counts maximal chains and \(e(P)\) counts Hasse-cover edges. Thus \(G(P)=n+c(P)-\operatorname{min}(P)-\operatorname{max}(P)-e(P)\).

**2. Completing cover graphs cannot decrease the gap.** In a pure graded poset every cover joins consecutive ranks. Suppose a missing comparability is inserted as a cover between elements \(u\) and \(v\) of consecutive ranks. There are already maximal chains from rank one to \(u\) and from \(v\) to rank \(h\), by purity. Let their counts be \(L(u)\ge1\) and \(U(v)\ge1\). The new cover increases the number of maximal chains by exactly \(L(u)U(v)\), and increases the number of covers by one. It does not change the rank sizes, minimum/maximum element counts, or purity; hence \(\Delta G=L(u)U(v)-1\ge0\). Insert all missing adjacent-rank edges. This yields the complete layered poset with the same rank sizes and at least the original gap. Insertion adds only comparabilities, so it also preserves any existing upper bound of two on width.

**3. Exact formula for complete layers.** Write \(r_i=1+x_i\) for \(x_i\in\{0,1\}\) and \(\sum_i x_i=m\), and put
\[a=\sum_{i=1}^{h-1}x_i x_{i+1}.\]
There are \(2^m\) maximal chains and \(\sum_{i=1}^{h-1}r_i r_{i+1}\) covers. Also
\[
\sum_{i=1}^{h-1}r_i r_{i+1}=h-1+2m-x_1-x_h+a,
\]
and the minimum and maximum rank sizes sum to \(2+x_1+x_h\). Substitution gives the exact identity
\[
G(P)=2^m-m-1-a.
\]

**4. The extremal binary placement problem.** The \(m\) doubleton ranks form at most \(h-m+1\) separated blocks, because each of the \(h-m\) singleton ranks can separate at most one pair of consecutive doubleton blocks. If the number of nonempty doubleton blocks is \(b\), then \(a=m-b\). Therefore
\[
a\ge\max\{0,2m-h-1\}.
\]
This is attainable by placing the doubletons in as many separated blocks as the singleton ranks permit. Combining with Steps 2–3 proves the first bound and its attainability.

**5. Equality characterization.** For \(h\ge3\), a rank-size profile attaining the bound must have the minimal adjacent-doubleton count, since any positive excess strictly decreases the complete-layer gap. Every edge between rank one and rank two when at least one of those ranks is a singleton is forced by purity. Thus any missing cover edge can only occur between adjacent doubleton ranks. If \(m\le2\) and the profile is optimal with \(h\ge3\), there are no adjacent doubleton ranks, so the poset is already complete. For \(m\ge3\), if the poset has a missing edge, complete every missing edge but one. In the resulting poset, inserting the last missing edge creates exactly \(2^{m-2}\) new full chains (arbitrary choices at the other \(m-2\) doubleton ranks), but only one cover, giving the strict gain \(2^{m-2}-1>0\). Hence no incomplete poset can achieve the bound. If \(h\le2\), direct substitution into the facet identity gives gap zero, regardless of the adjacent cover graph.

**6. Maximizing with \(n\) fixed.** Since \(h=n-m\) and \(m\le h\), the permissible range is \(0\le m\le\lfloor n/2\rfloor\). The fixed-height bound becomes
\[
H_n(m)=2^m-m-1-\max\{0,3m-n-1\}.
\]
Its consecutive increment is
\[
H_n(m+1)-H_n(m)=2^m-1-\bigl[\max\{0,3m+2-n\}-\max\{0,3m-n-1\}\bigr].
\]
The bracket lies between zero and three. Hence the increment is positive for \(m\ge3\). At \(m=2\), whenever \(m+1\) is permissible (so \(n\ge6\)), the increment is at least one. At \(m=1\), when \(m+1\) is permissible and \(n\ge5\), the increment equals one. Therefore for \(n\ge5\) the unique maximizing surplus count is \(m=\lfloor n/2\rfloor\); the initial tie between \(m=0\) and \(m=1\) is never globally optimal. For even \(n=2k\), this forces \(h=m=k\), all ranks doubleton, and \(a=k-1\), giving \(2^k-2k\). For odd \(n=2k+1\), this forces \(h=k+1,m=k\), exactly one singleton, and \(a\ge k-2\), with equality exactly when it is an interior rank, giving \(2^k-2k+1\). Step 5 supplies the stated uniqueness. For \(n\le4\), enumeration of permissible \(h,m\) or direct application of the fixed-height bound gives zero.

## Verification
The accompanying standalone `verify_facet_gap.py` uses Python integer arithmetic to enumerate every pure cover pattern for all rank-size sequences in \(\{1,2\}^h\) with \(1\le h\le7\); each adjacent bipartite cover graph must have no isolated vertices. It counts maximal chains by dynamic programming and cover edges directly, then checks the fixed-height sharp bound, the complete-layer formula, and the uniqueness statement for \(h\ge3\). It tests 206,516 admissible cover arrangements across 254 rank profiles. Additional symbolic-integer substitutions confirm the fixed-order formulas for sample dimensions. This finite enumeration corroborates but does not replace the all-dimension proof above.

## Relationship to prior work
The foundational facet formulas appear in Stanley's treatment of order and chain polytopes. The 2025 study by Bhandari–Cunningham–Morrell–Oh–Smith analyzes the facet-gap phenomenon and gives related constructions; Fourier's 2026 *On facet gaps of order and chain polytopes* provides a local gap formula and classification of small gaps. Neither inspected work states the sharp optimization over pure graded rank-thin posets simultaneously in fixed height and fixed total order, nor the complete maximizing configurations. The three-level family with a singleton middle rank is one narrower special case of the present theorem and cannot alone imply the all-height optimization. Related literature on maximal ranked posets and recent edge formulas addresses neighboring polytope invariants, leaving a possibility of unrecognized stronger implications.

## Limitations
This is a relative extremal theorem, not a claim about arbitrary finite posets without rank-width restrictions. It does not determine the facets or faces of every poset polytope beyond the standard facet identity used here. Exhaustive computations end at height seven; the unrestricted theorem follows from elementary chain-counting. Prior-art coverage includes the accessed primary texts and searches available here; an equivalent formulation in unindexed or inaccessible ranked-poset literature remains possible. No independent mathematical audit has been performed.

## References
1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. Standard facet descriptions.
2. Bhandari, Cunningham, Morrell, Oh, Smith, *Gap Between the Number of Facets of the Two Poset Polytopes*, Beiträge zur Algebra und Geometrie (2025), DOI: 10.1007/s00026-025-00776-9; preprint first public 2024-05-27.
3. G. Fourier, *On facet gaps of order and chain polytopes*, arXiv:2608.19989v1 (public 2026-08-20).
4. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626 (related ranked-poset literature).
5. J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413 (2026; concerns edge rather than facet counts).
