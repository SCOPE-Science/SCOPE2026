# All minimum one-limited dominating sets of two generalized Petersen families

## Finding
For every integer \(n\ge3\), the generalized Petersen prism \(\operatorname{GP}(n,1)\) has \(1\)-limited domination number \(n\), and the number of its *vertex-labelled* minimum \(1\)-limited dominating sets is
\[
N_1(n)=2+4\mathbf 1_{4\mid n}.
\]
For every integer \(n\ge5\), the generalized Petersen graph \(\operatorname{GP}(n,2)\) has \(1\)-limited domination number \(n\), and its number of vertex-labelled minimum \(1\)-limited dominating sets is
\[
N_2(n)=2+10\mathbf 1_{5\mid n}.
\]
In each family, every minimum set belongs to the explicit periodic families classified below; there are no other minimum sets. The two baseline sets are the whole outer ring and the whole inner ring. These are counts of **subsets** of the labelled vertex set, not counts of isomorphism classes or of distinct matching-edge sets.

## Assumptions and scope
The simple cubic graph \(\operatorname{GP}(n,k)\) has vertex set \(\{u_i,v_i:i\in\mathbb Z/n\mathbb Z\}\) and edge set consisting of \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\), for all indices \(i\). The claims apply to \(k=1\), \(n\ge3\), and to \(k=2\), \(n\ge5\); in particular \(n>2k\), so every vertex has three distinct neighbors.

A set \(D\subseteq V(G)\) is \(1\)-limited dominating if every vertex outside \(D\) has at least one neighbor in \(D\), and every vertex in \(D\) has at most one neighbor outside \(D\). Write \(N_k(n)\) for the number of sets of minimum possible cardinality.

A word of columns specifies an optimal set by putting \(u_i\) (respectively \(v_i\)) into \(D\) exactly when the first (respectively second) entry in column \(i\) is \(1\). Besides the two constant column words \((1,0)\) and \((0,1)\), all optimal sets are precisely:

- For \(k=1\) and \(4\mid n\): all four cyclic shifts of the repeating four-column word \((0,0),(0,0),(1,1),(1,1)\).
- For \(k=2\) and \(5\mid n\): all five cyclic shifts of each of the repeating five-column words \((1,0),(1,1),(0,0),(0,0),(1,1)\) and \((1,1),(0,0),(0,1),(0,0),(1,1)\).

## Proof
**Lower bound and equality rigidity.** Let \(D\) be any \(1\)-limited dominating set in a cubic graph with \(2n\) vertices; put \(T=V(G)\setminus D\). Each vertex in \(T\) has a neighbor in \(D\), so \(e(D,T)\ge |T|\). Each vertex in \(D\) has at most one neighbor in \(T\), so \(e(D,T)\le |D|\). Therefore \(2n-|D|\le |D|\), or \(|D|\ge n\). In \(\operatorname{GP}(n,k)\), choosing all \(u\)-vertices produces a \(1\)-limited dominating set of size \(n\) (its only exterior edges are spokes), proving the claimed minimum.

For equality \(|D|=n\), both edge-count inequalities are equalities. Consequently, **every vertex** is incident to exactly one edge whose other endpoint lies in the opposite class of \(\{D,T\}\). Conversely any binary vertex labelling with exactly one opposite-labelled neighbor at each vertex gives a minimum \(1\)-limited dominating set upon taking the vertices labelled \(1\). Complementary labellings give distinct sets and must not be identified.

**Finite-state formulation.** Write \(a_i,b_i\in\{0,1\}\) for the membership indicators of \(u_i,v_i\). The equality conditions at every \(i\) are precisely
\[
[a_i\ne a_{i-1}]+[a_i\ne a_{i+1}]+[a_i\ne b_i]=1,
\]
\[
[b_i\ne b_{i-k}]+[b_i\ne b_{i+k}]+[b_i\ne a_i]=1,
\]
where square brackets denote truth values \(0\) or \(1\). Encode each column \((a_i,b_i)\) by the integer \(q_i=a_i+2b_i\in\{0,1,2,3\}\). Define a directed transition graph with all \(4^{2k}\) states \((q_{i-k},\ldots,q_{i+k-1})\). From each state, append one of the four columns \(q_{i+k}\), retain the rightmost \(2k\) columns, and draw the directed transition exactly when both displayed equalities at index \(i\) hold. This constructs the graph from explicit finite arithmetic without optimization or conjectural pruning.

The standalone `verify.py` contains complete deterministic enumeration of every candidate transition and a second, explicit strongly-connected-component computation. The actual finite certificate is:

| \(k\) | States | Edges | All strongly connected components containing cycles |
|---:|---:|---:|---|
| 1 | 16 | 10 | two singleton self-loops, one directed \(4\)-cycle |
| 2 | 256 | 160 | two singleton self-loops, two directed \(5\)-cycles |

Every nontrivial cyclic component has exactly one incoming and one outgoing edge at each of its vertices **within the component**; all other components are acyclic singletons. The two loops encode the constant column words. The \(4\)- and \(5\)-cycles encode the three explicit nonconstant words stated above. For independent reproduction, the integer-encoded cyclic components are \(\{5\},\{10\},\{0,3,12,15\}\) at \(k=1\), and \(\{85\},\{170\},\{13,55,112,195,220\},\{35,60,143,200,242\}\) at \(k=2\); the encoding is \(s=\sum_{j=0}^{2k-1}q_{i-k+j}4^j\).

**Infinite conclusion from finite certificate.** For \(n>2k\), specifying a cyclic sequence of \(n\) columns satisfying the equalities is equivalent, with no overcounting, to specifying a directed closed walk of length \(n\) in this transition graph with a marked starting state. A closed walk never leaves its strongly connected component. Because each cyclic component is a simple directed cycle, a directed cycle of length \(d\) contributes exactly \(d\) closed walks of length \(n\) when \(d\mid n\) and zero otherwise. Hence the total is \(2+4\mathbf 1_{4\mid n}\) for \(k=1\) and \(2+10\mathbf 1_{5\mid n}\) for \(k=2\). By equality rigidity, these closed walks bijectively enumerate all minimum dominating subsets. This proves the assertions for **every** allowed \(n\), not merely the experimentally checked small orders.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. The checker constructs the full transition graph, independently computes all strongly connected components by a two-pass graph traversal, verifies cycle degrees and the stated component list, computes closed-walk counts for selected larger orders, and separately enumerates every binary labelling using the original neighborhood conditions for \(3\le n\le8\) when \(k=1\) and \(5\le n\le8\) when \(k=2\). The run returns `VERIFY_OK`. All integer calculations are exact. The exhaustive transition certificate, rather than the finite sample of direct labellings, is the step that establishes the infinite theorem.

## Relationship to prior work
Radić and Tepeh, arXiv:2610.01796v1, study \(1\)-limited domination on cubic graphs, prove complexity results, and determine values for Goldberg snarks. The half-order lower bound is also compatible with known generic cubic-graph bounds; the claim of contribution here is specifically the **complete census and periodic classification of all minimizers** for the prism and \(\operatorname{GP}(n,2)\) families, not discovery of the half-order bound.

Alaeiyan and Karami (2016, §3.1) establish existence of a perfect two-colouring with quotient matrix \(\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\) in all generalized Petersen graphs using the constant outer/inner colouring. Karami (arXiv:2606.14190) states arithmetic existence criteria for quotient matrices in the whole family. Neither cited existence statement gives the exact number of such colourings in these two infinite subfamilies. The present classification is a quantitative strengthening for the specified quotient matrix, not a new existence theorem. The standard perfect-matching-cut literature concerns an edge cut contained in a perfect matching, which is not automatically the same as an entire matching edge-cut arising from a two-class partition; the latter is what equality uses here. Matching-forcing polynomials count a different statistic on perfect matchings.

## Limitations
The theorem treats two specified skips only and does not classify the minimizers of arbitrary \(\operatorname{GP}(n,k)\). The finite transition classification is backed by an executable certificate, not by a short hand-written case table; the certificate and all boundary conventions are explicit. Historical priority for the exact minimizer counts remains independently unverified, and complete full-text comparison with the June 2026 generalized-Petersen intersection-array preprint was not possible; its accessible abstract describes existence criteria rather than counts. No independent audit is claimed.

## References
1. G. Radić and A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796v1 (first posted 2026-10-01), https://arxiv.org/abs/2610.01796.
2. M. Alaeiyan and H. Karami, *Perfect 2-colorings of the generalized Petersen graph*, Proceedings of the Indian Academy of Sciences (Mathematical Sciences) 126 (2016), 289–294, https://doi.org/10.1007/s12044-016-0285-4.
3. H. Karami, *Intersection Arrays of Completely Regular Codes of Covering Radius One in Generalized Petersen Graphs*, arXiv:2606.14190v1 (2026), https://arxiv.org/abs/2606.14190.
4. V. Bouquet and C. Picouleau, *The complexity of the perfect matching-cut problem*, arXiv:2011.03318 (2020), https://arxiv.org/abs/2011.03318.
5. S. Zhao, *Matching forcing polynomial of generalized Petersen graph GP(n,2)*, arXiv:2110.03978v1 (2021), https://arxiv.org/abs/2110.03978.
