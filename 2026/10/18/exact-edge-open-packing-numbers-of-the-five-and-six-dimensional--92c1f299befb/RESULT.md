# The edge-open-packing number of the six-dimensional cube

## Finding

The six-dimensional binary hypercube satisfies
\[
\boxed{\rho_e^{\mathrm{o}}(Q_6)=24.}
\]
The contribution is the upper bound of 24, which matches the lower bound already reported in [2, Table 1]. The general published upper bound gives 32, and the known equality theorem for power-of-two dimensions does not apply at dimension six.

## Assumptions and scope

Represent the vertices of \(Q_6\) by integers from 0 to 63, with adjacency when their bitwise exclusive-or has exactly one set bit. An edge-open packing is an edge subset \(S\) with no two distinct members \(e,f\) for which a third edge, different from both \(e\) and \(f\), joins an endpoint of \(e\) to an endpoint of \(f\). This is not an induced matching: incident selected edges are allowed in the triangle-free cube. The number \(\rho_e^{\mathrm{o}}\) is the maximum cardinality of such an edge subset. No equality for another dimension or classification of the maximizers is claimed.

## Proof

**Lower bound.** Choose the six edges incident to each of the four centers \(0,15,51,60\). Each pair of centers differs in four coordinates. An endpoint at one center's star has distance at most one from that center. Hence all endpoints in different stars have distance at least two and are disjoint and nonadjacent. Within each star, any two selected edges share their center and there is no third joining edge because the cube is triangle-free. The resulting packing has 24 edges.

**Compatibility graph.** List the 192 cube edges, represented by their endpoints in increasing order, lexicographically as \(e_0,\ldots,e_{191}\). Two distinct edges are adjacent in a new graph \(H\) if they are permitted together. If the two cube edges are disjoint, incompatibility is exactly the existence of a one-bit adjacency between their endpoint sets. If they are incident, there is no third edge between their endpoints, since such an edge would close a triangle. This gives an exact criterion for the adjacency bits of \(H\), and packings are exactly cliques in \(H\). Cube translations and coordinate permutations preserve all conflicts and act transitively on cube edges. A clique of size at least 25 would therefore give a clique of size 25 containing \(e_0=(0,1)\).

**Exhaustive exclusion of size 25.** The retained `verify_eop.py` computes the exact adjacency bitsets and searches from the neighborhood of \(e_0\) at depth 1, where depth is the number already selected. Here is the search invariant at an arbitrary recursive node: every candidate is adjacent to all selected vertices, and the question is whether a clique of total size 25 can be formed by extending with the candidates. Greedily split the candidate set into independent color classes: extract an independent set by removing the chosen candidate and excluding its neighbors from the rest of that class, then repeat on uncolored candidates. In an order listing classes by increasing index, the prefix ending at an index with color \(c\) is properly colored with at most \(c\) colors. Search that order backwards. For candidate \(i\) there, search its adjacency intersection with the current candidate set, after the later candidates have been removed. Every nonempty clique extension has a last vertex in the order, so the corresponding branch includes it unless pruned. A prefix can be skipped when depth plus its color bound is less than 25, since an extension uses at most one vertex of each color. A simple candidate-count bound is applied as well. All tests are exact integer or bitset operations. Induction on the candidate set proves that a negative return rules out every target clique; no time limit or approximate bound enters the certificate.

On the 192-vertex graph, this search returns false at the root after 54,111 recursive nodes (retained `VERIFIER_OUTPUT.txt`, Q6 line). Thus there is no 25-edge packing, which proves the upper bound.

## Verification

In the directory containing the retained script, run `python3 verify_eop.py` using standard Python without optimization flags that disable assertions. The Q6 line reports `edges=192, witness=24, exact_upper=24, search_nodes=54111`, followed by `VERIFY_OK`. The script also checks a separate, previously settled five-cube case for regression; that case is not a contribution of this result.

## Relationship to prior work and limitations

The bound of Chelladurai–Kalimuthu–Soundararajan, discussed and characterized in [1], gives \(\rho_e^{\mathrm{o}}(Q_6)\le |E(Q_6)|/6=32\). Section 5 and Table 1 of [2] give the lower bound 24; their Theorem 5.10 gives exact numbers only for positive power-of-two dimensions in its stated range, not six. The parity-split lower bound of [3] also specializes to 24 in dimension six but does not exclude 25; that record also gives the separately known exact five-cube value. This result settles the finite six-cube interval without making any claim about optimizer counts, new lower bounds, or higher-dimensional asymptotics. The upper-bound proof is an exhaustive finite computation with a justified search invariant, not a general structural classification. Accessible literature and catalogue comparisons are not an exhaustive priority proof.

## References

1. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, [arXiv:2403.00750](https://arxiv.org/abs/2403.00750).
2. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, [arXiv:2406.04020](https://arxiv.org/abs/2406.04020).
3. *Parity-split Hamming stars improve hypercube edge-open packing, with an exact five-cube census*, [Resultary d4fb72f17bca](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-parity-split-hamming-stars-improve-hypercube-edge-open-packing-w--d4fb72f17bca/RESULT.md).
