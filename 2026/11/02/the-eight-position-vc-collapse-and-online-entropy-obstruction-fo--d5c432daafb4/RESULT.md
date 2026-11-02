# The eight-position VC collapse and online entropy obstruction for two-descent permutations
## Finding
For each integer \(n\ge1\), let \(\mathcal E_{n,2}\) be the set of permutations of \(\{0,\ldots,n-1\}\) with at most two adjacent descents. For each \(a<b\), the Boolean query \(q_{a,b}\) receives label \(1\) precisely when \(\pi(a)>\pi(b)\). Under these positional comparison queries, the exact dimensions at eight positions are
\[
\operatorname{VCdim}(\mathcal E_{8,2})=6,\qquad
\operatorname{Ldim}(\mathcal E_{8,2})=11.
\]
There are exactly \(4541\) concepts, so the adaptive dimension fails its hypothesis-count ceiling \(\lfloor\log_2(4541)\rfloor=12\) by one. Eight positions is the first size at which either the full-permutation VC ceiling \(n-1\) fails or the concept-count Littlestone ceiling fails in this at-most-two-descent family.

For \(1\le n\le8\), the exact \((|\mathcal E_{n,2}|,\operatorname{VCdim},\operatorname{Ldim})\) triples are \((1,0,0),(2,1,1),(6,2,2),(23,3,4),(93,4,6),(360,5,8),(1312,6,10),(4541,6,11)\), respectively.

There is also an infinite-family implication. For every integer \(s\ge1\), let \(\mathcal E_{8s,2s}\) consist of permutations on \(8s\) positions having at most \(2s\) adjacent descents, with the same comparison-query convention. Then
\[
\operatorname{Ldim}(\mathcal E_{8s,2s})\ge11s,\quad
\operatorname{VCdim}(\mathcal E_{8s,2s})\le8s-1,\quad
\operatorname{Ldim}-\operatorname{VCdim}\ge3s+1.
\]
This is not an asserted exact all-size formula.

## Assumptions and scope
Positions and permutation values are \(0,\ldots,n-1\); a descent is an index \(i<n-1\) with \(\pi(i)>\pi(i+1)\). All queries compare values at **positions**, rather than positions of named values; this distinction matters for descent restrictions. For Littlestone dimension, the query at a decision-tree node may depend on earlier query answers; every root-to-leaf response path must be realized by a permutation, but different leaves may use different permutations. The finite computations use every allowed permutation and every one of the \(\binom n2\) possible queries.

## Proof
**Finite-domain exhaustiveness.** Enumerate all \(n!\) permutations and retain exactly those with at most two descents. Independently generate the same family by starting at length one and inserting the new largest value at each possible position, retaining the descent restriction. Removal of the largest value cannot increase the descent count: at an internal insertion a former adjacent comparison is replaced by an ascent followed by a descent, and at an endpoint the descent count stays the same or increases by one. Thus every admissible permutation is generated and the second method is independent of brute-force iteration. The two enumerators agree for each \(1\le n\le8\).

**Exact VC recursion.** Let \(P\) be the finite set of admissible permutations and \(P_{q,b}\) its restriction to response \(b\) at query \(q\). For a set of queries \(S\), keep one nonempty version space for each response pattern on \(S\). Adding a query \(q\notin S\) preserves shattering exactly if **each** current version space has nonempty response-zero and response-one restrictions. Recursing on queries in increasing lexicographic order examines every potentially shattered support once; a support that fails cannot have a shattered extension. The eight-position recursion visits \(31{,}827\) shattered-support nodes, finds maximum size six, and finds no size-seven support. One size-six witness in zero-indexed coordinates is
\[
\{(0,1),(0,2),(0,4),(0,5),(2,6),(3,7)\}.
\]
The bundled program recomputes all \(64\) distinct patterns for this support, and also verifies the exact lower-size VC values in the theorem.

**Exact online recursion.** For every version space \(V\subseteq P\), let \(T(V,d)\) mean that a complete response tree of depth \(d\) is feasible. The base case is \(T(V,0)\) true precisely for nonempty \(V\). For \(d>0\),
\[
T(V,d)\iff\bigvee_q\big(T(V_{q,0},d-1)\wedge T(V_{q,1},d-1)\big).
\]
Every depth-\(d\) tree needs at least \(2^d\) distinct permutations, allowing safe branch-count pruning. Exhaustive memoized evaluation gives \(T(P,11)\) true and \(T(P,12)\) false at \(n=8\), and establishes all lower-order dimensions in the table. The supplied `certificate.json` contains an explicit depth-eleven tree with \(2047\) internal queries and \(2048\) distinct terminal permutation indices; `eulerian_certificate.py verify certificate.json` checks each leaf against every decision on its path. As the recursion exhausts all query choices and all smaller version spaces, false at depth twelve proves impossibility, not a timeout inference.

**Infinite-family lower bound.** For each of \(s\) disjoint consecutive eight-position blocks, independently select a member of \(\mathcal E_{8,2}\), translate its values into the corresponding consecutive value range, and concatenate the blocks in increasing value order. Every cross-block adjacent comparison is an ascent. Thus the resulting permutation has at most \(2s\) descents. Queries internal to one block reproduce that block's depth-eleven tree, irrespective of all other blocks. Sequentially attaching an independent copy of the depth-eleven tree at every terminal node gives a full decision tree of depth \(11s\). For any permutation concept class queried by pairs, a shattered support cannot contain an undirected cycle: label its edges to impose a strictly cyclic inequality, impossible for a total order. Every forest on \(8s\) vertices has at most \(8s-1\) edges, giving the VC upper bound and the claimed gap.

## Verification
Reproduce using Python 3 standard library only: `python eulerian_certificate.py verify certificate.json`. This independently cross-checks direct permutation enumeration against insertion-of-maximum enumeration; exactly enumerates shattered fixed-query supports; evaluates all viable adaptive splits by a cached recurrence; replays the complete depth-eleven witness; and checks the asserted table and exact concept counts. The reported eight-position run has \(77{,}182\) cached adaptive subproblems, and the verifier explicitly rejects depth twelve. Independent scientific audit has not been performed.

## Relationship to prior work
Chase and Freitag (2018), in the setting of model-theoretic VC and thicket/Littlestone dimensions, establish general shattering principles, not the Eulerian restriction or the specific finite dimensions here. Zhao, Sun and Zhao (2021) study Eulerian descent statistics and refined enumeration, supplying motivation and the standard descent terminology; their inspected results concern enumeration and ballot permutations rather than positional online comparison shattering. Pasteris et al. (2018) study online pairwise clustering from same-block feedback; this differs from inversion comparisons on descent-restricted total orders. The combination of an exact finite VC collapse, an online entropy obstruction, and an amplified gap is not an implication of these compared results. Previously known unrestricted-permutation and pattern-avoidance learning dimensions do not fix the restricted two-descent value because taking a subclass can decrease both shattering dimensions.

## Limitations
The exact classification is only established for \(n\le8\) at the **fixed** descent budget two. The infinite-family result allows the budget to grow as \(2s\); it does not establish a fixed-budget asymptotic formula. The correctness certificate is a complete finite proof conditional on standard-language integer arithmetic and accurate implementation; the finite enumeration is not being extrapolated to uncomputed values. A broader historical search might uncover an equivalent formulation under bounded-runs permutations or sorting constraints. No independent audit or independent historical-priority certification is claimed.

## References
- H. Chase and J. Freitag, *Model theory and combinatorics of banned sequences*, arXiv:1801.07640v1 (first public 2018-01-23), *Journal of Symbolic Logic* 87 (2022), 1–20; https://arxiv.org/abs/1801.07640.
- T. Zhao, Y. Sun and F. Zhao, *Refined Eulerian numbers and ballot permutations*, arXiv:2102.08508v1 (first public 2021-02-17); https://arxiv.org/abs/2102.08508.
- S. Pasteris, F. Vitale, C. Gentile and M. Herbster, *On Similarity Prediction and Pairwise Clustering*, PMLR 83 (2018), 654–681; https://proceedings.mlr.press/v83/pasteris18a.html.
