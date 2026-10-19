# Exact exchange distances among minimum decycling sets of the dodecahedral graph

## Finding

Let \(D=GP(10,2)\) be the dodecahedral graph. Its feedback vertex number is \(6\), and there are exactly \(2520\) feedback vertex sets of that minimum size. Join two minimum sets \(S,T\) if \(|S\setminus T|=|T\setminus S|=1\); write \(R\) for this exchange graph.

The graph \(R\) is connected and has \(23940\) edges. Every vertex has eccentricity \(6\), so both its radius and diameter are \(6\). The exact numbers of *unordered distinct* pairs at each exchange distance are:

| Exchange distance | Pair count |
| --- | ---: |
| \(1\) | \(23940\) |
| \(2\) | \(162870\) |
| \(3\) | \(572230\) |
| \(4\) | \(1088390\) |
| \(5\) | \(993990\) |
| \(6\) | \(332520\) |

For any pair \(S,T\), every exchange sequence has length at least \(|S\setminus T|\). The numbers of unordered distinct pairs for which the true distance exceeds this lower bound by \(0,1,2\) are exactly \(3124960,48800,180\), respectively; no greater excess occurs. Thus connectivity does not imply isometric embedding into the ambient Johnson graph. Of the minimum sets, \(660\) are independent and \(1860\) induce exactly one edge.

## Assumptions and scope

The vertices are \(u_i,v_i\), with \(i\in\mathbb Z/10\mathbb Z\). The undirected edges are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\) for all indices, with no others. A *feedback vertex set* (or decycling set) is a subset \(S\subseteq V(D)\) such that the induced graph on \(V(D)\setminus S\) is a forest. The *exchange graph* has the six-element feedback vertex sets as vertices; one edge is permitted exactly when the symmetric difference has two elements. All distances are ordinary unweighted graph distances in this exchange graph, and all pair counts refer to unordered pairs of distinct configurations. No claim is made for any other generalized Petersen graph.

## Proof

There are \(20\) vertices and \(30\) edges and every vertex has degree \(3\). If \(|S|=k\) and the subgraph induced by \(S\) contains \(e(S)\) edges, the complement contains exactly \(30-3k+e(S)\) edges on \(20-k\) vertices. For that complement to be a forest requires
\[
30-3k+e(S)\le 19-k,\qquad 2k\ge11+e(S).
\]
Hence every feedback vertex set has size at least \(6\). At size \(6\), any feedback vertex set must induce at most one edge; the converse is **not** assumed.

The remaining assertions have a finite exhaustive proof by the accompanying standalone program `decycling_checker.py`. Here are the exact logical steps certified by its fully specified loops.

First, it generates the entire set of \(\binom{20}{6}=38760\) labeled six-vertex subsets as bitmasks. For each mask it scans all thirty explicitly constructed edges and runs a disjoint-set cycle test on the fourteen surviving vertices. An independently implemented depth-first-search cycle test accepts exactly the same \(2520\) masks. Thus existence at size six and exhaustive classification by the forest property are certified, rather than merely estimated.

Second, it counts induced edges in every accepted set and obtains \(660\) sets with none and \(1860\) with one. It generates every possible one-out/one-in exchange of each accepted six-set, retaining exactly those resulting masks in the enumerated family. The membership test has no heuristic pruning; every possible swap is tested. Reciprocal adjacency is checked. The resulting degree sum is \(47880\), hence there are exactly \(23940\) exchange edges.

Third, the program independently performs an ordinary breadth-first search from each of the \(2520\) configurations through those explicit exchange edges. It verifies that all other configurations are reached, records every eccentricity, and counts the distances over all index pairs with first index smaller than second. Its six distance totals add up to \(\binom{2520}{2}=3173940\). For every such pair it subtracts the elementary lower bound \(|S\setminus T|\), obtaining the excess counts reported above. Because breadth-first search on an unweighted finite graph computes shortest-path length exactly, and because every configuration and legal exchange was enumerated, these loops prove the complete finite distance census, including radius and diameter.

## Verification

Run `python3 decycling_checker.py` with Python \(3.8\) or later. The checker has no third-party imports; its transcript is included as `decycling_checker.stdout`. The verified transcript ends `ALL_CHECKS_PASS` and includes the minimum-set count, edge count, every eccentricity, the complete pair-distance histogram, and the complete Hamming-excess histogram. Two different cycle-detection routines supply an internal cross-check. The calculation is exhaustive for this finite labeled graph; no random sampling, timeout inference, or extrapolation is used.

## Relationship to prior work

The reconfiguration framework for feedback vertex sets is already developed in Mouawad et al. [1], and broader complexity results are given by van der Zanden [2]. Bousquet et al. [3] establish connectivity of same-size feedback vertex set reconfiguration in planar subcubic graphs, and their construction yields a general length bound of \(7k\); connectivity here is therefore **not** claimed as new. Nedela et al. [4] discuss general cubic decycling lower bounds and independent/near-independent minimum sets, using earlier work of Payan and Sakarovitch; those general structural observations are likewise **not** claimed as new. The particular contributions here are the exact \(2520\)-state exchange geometry, the sharp distance/eccentricity profile, and the non-geodesic-pair counts. In the compared accessible statements, neither the general reachability theorems nor the static structural theorems supply these quantitative conclusions for the dodecahedral graph.

## Limitations

This is one finite, explicitly specified graph. It does not give a general formula for arbitrary cubic graphs or \(GP(n,k)\), nor does it establish a new general connectivity theorem. The finite verification uses a reproducible computer-assisted exhaustive proof; its assertions can also be checked from the included algorithm without a separate compiled certificate. The complete publisher PDF of [3] was not accessible in this review, so overlap with examples or appendices not exposed in the inspected indexed sections remains a specific literature risk. An equivalent unindexed computation may also exist. Independent external verification has not been performed.

## References

1. A. E. Mouawad, N. Nishimura, V. Raman, N. Simjour, A. Suzuki, *On the Parameterized Complexity of Reconfiguration Problems*, arXiv:1308.2409 (initial public version 2013-08-11), https://arxiv.org/abs/1308.2409.
2. T. C. van der Zanden, *Parameterized Complexity of Graph Constraint Logic*, arXiv:1509.02683 (2015-09-09), https://arxiv.org/abs/1509.02683.
3. N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler, A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, Theoretical Computer Science 979 (2023) 114188, https://doi.org/10.1016/j.tcs.2023.114188.
4. R. Nedela, M. Seifrtová, M. Škoviera, *Decycling cubic graphs*, arXiv:2309.11606 (2023-09-20), https://arxiv.org/abs/2309.11606.
