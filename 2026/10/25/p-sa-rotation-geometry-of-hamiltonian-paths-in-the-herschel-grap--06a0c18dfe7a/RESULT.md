# Pósa rotation geometry of Hamiltonian paths in the Herschel graph

## Finding

Let \(H\) be the eleven-vertex Herschel graph defined explicitly below. Let \(\mathcal P(H)\) denote the set of undirected Hamiltonian paths, with a path and its reversal identified. Form \(\mathcal R(H)\) by joining two members when an elementary Pósa rotation at either endpoint transforms one into the other. Then \(\mathcal P(H)\) has exactly \(222\) elements, and \(\mathcal R(H)\) is a connected \(4\)-regular graph with \(222\) vertices and \(444\) edges. Its radius is \(8\), its diameter is \(9\), and its complete eccentricity distribution is

\[
\#\{P:\operatorname{ecc}(P)=8\}=198,\qquad
\#\{P:\operatorname{ecc}(P)=9\}=24.
\]

In particular, any two undirected Hamiltonian paths in \(H\) can be transformed into one another using at most nine elementary rotations while preserving a spanning path at every step; nine moves are sometimes necessary.

## Assumptions and scope

Define \(H\) on vertices \(\{0,1,\ldots,10\}\). The red class is \(\{5,6,7,8,9,10\}\) and the blue class is \(\{0,1,2,3,4\}\). For each \(r\in\{5,6\}\), join \(r\) to \(0,1\); for each \(r\in\{7,8\}\), join \(r\) to \(1,2\); and for each \(r\in\{9,10\}\), join \(r\) to \(2,0\). Finally join \(3\) to \(5,7,9\), and join \(4\) to \(6,8,10\). This standard presentation has \(11\) vertices, \(18\) edges, and degree multiset \(\{4,4,4,3,3,3,3,3,3,3,3\}\).

For an oriented representation \(P=(p_0,p_1,\ldots,p_{10})\) and an edge \(p_{10}p_i\) with \(0\le i\le8\), one Pósa rotation produces

\[
(p_0,\ldots,p_i,p_{10},p_9,\ldots,p_{i+1}).
\]

Rotations are allowed at either endpoint, by also reversing the path representation. Adjacent configurations always have the same eleven vertices; no added graph edge or vertex is permitted.

## Proof

Since \(H\) is bipartite with unequal parts of sizes five and six, every Hamiltonian path starts and ends in the six-vertex red part; it has no Hamiltonian cycle. Every red vertex has degree three. At either endpoint, one graph edge is used by the Hamiltonian path and exactly two edges are unused; neither can join the other endpoint, since that would close a Hamiltonian cycle. Thus each endpoint admits exactly two nontrivial elementary rotations. The four resulting paths are distinct: an operation at one endpoint adds an edge incident to that endpoint, and no operation at the opposite endpoint can add the same edge. Hence \(\mathcal R(H)\) is \(4\)-regular.

The remaining assertions are exact finite enumeration, independently certified by two complete algorithms given in the accompanying source files. First, `code/posa_paths.py` starts a depth-first traversal at each of the six red vertices and recursively appends unused adjacent vertices. Once eleven vertices have been visited, it canonicalizes the path under reversal. This visits *all* Hamiltonian paths because every such path has a red endpoint. It obtains exactly \(222\) distinct undirected paths. It then generates every elementary rotation from both orientations of each path, asserts that every result is one of the enumerated paths, constructs the adjacency sets, and runs breadth-first search from **every** one of the \(222\) vertices. The resulting eccentricities are \(8\) for exactly \(198\) vertices and \(9\) for exactly \(24\), with all searches reaching all \(222\) vertices.

Independently, `code/edge_subsets.py` enumerates all \(\binom{18}{10}=43{,}758\) ten-edge subsets of \(H\). A subset forms a spanning undirected Hamiltonian path precisely when its degree multiset has two ones and nine twos and it is connected. The checker obtains \(222\) such subsets. It joins two valid paths whenever their edge sets differ by exactly one deletion and one addition. This is equivalent to a Pósa rotation here: deleting an edge of a spanning path splits it into two paths, and reconnecting their endpoints by one edge without using the original removed edge must produce an elementary endpoint rotation or add an edge joining the two original endpoints. The latter is impossible because \(H\) has no Hamiltonian cycle. The independent edge-subset checker again finds \(444\) edges, one component, and eccentricity multiplicities \(198\) and \(24\) at distances \(8\) and \(9\), respectively.

Both enumerations have finite, explicit bounds and no randomization or search cutoff. These exhaustive checks establish the radius and diameter, not merely upper bounds.

## Verification

Using Python 3 and no third-party dependencies, run `python3 code/posa_paths.py` and `python3 code/edge_subsets.py` from the package root. Both terminate with asserted expected counts and print a single success line. The corresponding recorded outputs are `verification/posa_stdout.txt` and `verification/edge_stdout.txt`. Source files and recorded outputs are embedded with exact per-file SHA-256 checksums in the accompanying envelope.

## Relationship to prior work

The Herschel graph is a classical smallest non-Hamiltonian polyhedral graph. Kriesell and Pedersen (2011) identify its dual in a different colouring-number problem, without treating Hamiltonian path rotations. Krivelevich (2015), Section 2.3, describes the general Pósa rotation-extension operation and its application to long paths, but does not give this finite rotation graph. Pósa's original 1976 rotation method is acknowledged as background, not claimed here. A distinct known result on Hamiltonian-path Pósa rotations of the Petersen graph has a different underlying graph and does not imply the Herschel counts or distances. Searches for the same graph and operation found no covering theorem; this is not a proof of publication priority.

## Limitations

The result applies to the exactly defined eleven-vertex Herschel graph and rotations at either endpoint, with path reversal identified. It establishes no general connectivity theorem for non-Hamiltonian planar graphs. Exact finite enumeration is a proof for this one graph, not evidence for all larger graphs. Independent external validation and exhaustive publication-priority certification are not claimed. Unindexed Hamiltonian-path tables might overlap this computation.

## References

1. M. Kriesell and A. S. Pedersen, *On graphs double-critical with respect to the colouring number*, arXiv:1108.1036v1 (4 August 2011), especially the Herschel-dual observation following Theorem 15. https://arxiv.org/html/1108.1036v1
2. M. Krivelevich, *Long paths and Hamiltonicity in random graphs*, arXiv:1507.00205 (1 July 2015), Section 2.3, for Pósa rotations. https://arxiv.org/abs/1507.00205
3. L. Pósa, *Hamiltonian circuits in random graphs*, Discrete Mathematics 14 (1976), 359–364, for the original rotation technique.
4. E. W. Weisstein, *Herschel Graph*, MathWorld, https://mathworld.wolfram.com/HerschelGraph.html (standard graph identification; undated web reference).
