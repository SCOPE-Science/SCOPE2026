# Exact edge-open-packing numbers of the five- and six-dimensional cubes

## Finding

Let \(Q_n\) be the binary \(n\)-dimensional hypercube. The edge-open-packing number satisfies
\[
\boxed{\rho_e^{\mathrm{o}}(Q_5)=12,\qquad \rho_e^{\mathrm{o}}(Q_6)=24.}
\]
Consequently, these two orders both have an edge-open packing strictly larger than their maximum induced matching (of respective sizes \(8\) and \(16\)). The contributions are the exact values at these two dimensions, not the pre-existing general definition, algorithmic results or power-of-two-dimensional formula.

## Assumptions and scope

All graphs are simple and finite. Vertices of \(Q_n\) are the binary \(n\)-tuples, represented in the proof and the verifier as integers from \(0\) to \(2^n-1\); vertices are adjacent precisely when their bitwise exclusive-or has one set bit. An edge-open packing is a subset \(S\subseteq E(Q_n)\) for which no two distinct chosen edges have a **third**, different graph edge joining an endpoint of the first to an endpoint of the second. Its maximum cardinality is \(\rho_e^{\mathrm{o}}(Q_n)\). We prove exactly the cases \(n=5\) and \(n=6\); no general formula for other dimensions is asserted.

## Proof

**Lower bound at dimension five.** The following twelve unordered edges of \(Q_5\), with vertices in binary-integer notation, form an edge-open packing:

```text
(0,1) (0,2) (0,4)
(11,15) (13,15) (14,15)
(19,23) (21,23) (22,23)
(24,25) (24,26) (24,28)
```

Each triple is a star. Among endpoints from different triples there is no cube edge; equivalently, every pair of selected disjoint edges has no cross-endpoint edge. This can be checked from the one-bit exclusive-or adjacency rule and is directly checked by the standalone verifier. Thus \(\rho_e^{\mathrm{o}}(Q_5)\ge12\).

**Lower bound at dimension six.** Choose all six edges incident to each of the four centers \(0,15,51,60\) of \(Q_6\). Every pair of these centers differs in exactly four coordinates. Each endpoint of a chosen edge differs in at most one coordinate from its star center; hence endpoints of distinct stars differ in at least two coordinates and are nonadjacent. The 24 edges form an edge-open packing, so \(\rho_e^{\mathrm{o}}(Q_6)\ge24\).

**Exact finite upper bounds.** We give a self-contained, completely exhaustive finite upper-bound certificate, `verify_eop.py`, not an extrapolation from smaller graphs. Enumerate the \(n2^{n-1}\) edges of \(Q_n\) lexicographically as \(e_0,e_1,\ldots\) and construct a compatibility graph \(H_n\) whose vertices are these edges. Two distinct members of \(E(Q_n)\) are adjacent in \(H_n\) exactly when they are permitted together in an edge-open packing. For disjoint edges, incompatibility holds exactly when there is a cross-endpoint cube edge. For incident edges, the absence of triangles in \(Q_n\) means they have no *third* connecting edge, so they are compatible. Therefore **edge-open packings of \(Q_n\) are exactly the cliques of \(H_n\)**, without exceptions.

Cube translations by exclusive-or and coordinate permutations act transitively on cube edges. Any nonempty edge-open packing can therefore be mapped to one containing \(e_0=(0,1)\). To exclude size \(t\), it suffices to exclude a clique of size \(t\) containing that fixed vertex of \(H_n\). The verifier starts with the exact bitset of its compatible neighbors and recursively enumerates every clique extension.

At every recursive node, the candidate induced compatibility graph is greedily **properly colored** by successive independent color classes: within one color class no two candidate vertices are adjacent. If there are \(c\) such classes, every clique extension has size at most \(c\). The algorithm scans candidates in reverse coloring order, branching on the last candidate of the extension and intersecting the remaining candidate set with its exact adjacency bitset. A coloring upper bound prunes only branches for which current clique size plus the maximum available color index is below the target. Because every clique has a last candidate and every color class is independent, the recursion cannot omit an admissible target clique. All operations are finite integer comparisons, bitwise operations and exact popcounts; there are no floating-point thresholds, external libraries, heuristics used as proof, or timeouts.

Running `python3 verify_eop.py` proves nonexistence of a clique of size \(13\) containing \((0,1)\) in \(H_5\) after 59 recursive nodes, and nonexistence of a clique of size \(25\) containing \((0,1)\) in \(H_6\) after 54,111 recursive nodes. By edge transitivity there is no larger edge-open packing. Combining with the explicit constructions proves both stated equalities.

## Verification

`verify_eop.py` is a standalone Python 3 script with no external dependencies. Run from any directory with `python3 verify_eop.py`. It validates both explicit packings against every pair of their edges; constructs the exact 80-vertex and 192-vertex compatibility graphs; and exhaustively eliminates packings of cardinalities 13 and 25. Its recorded output is embedded as `VERIFIER_OUTPUT.txt` and ends with `VERIFY_OK`. The checker enumerates a finite configuration space **exhaustively**; the result is confined to the two stated finite dimensions. The validity of its search bound follows from the coloring and branching argument above rather than from a bare execution log.

## Relationship to prior work

Brešar, Dravec, Hedžet and Samadi [2], Section 5.1 and Table 1, study this very invariant in hypercubes. They give a numerical lower bound of 10 for \(Q_5\), a lower bound of 24 for \(Q_6\), and an exact formula for cube dimensions that are powers of two. Neither five nor six is a power of two, and those lower bounds do not establish either present equality. The general upper bound from Brešar and Samadi [1] gives only \(\rho_e^{\mathrm{o}}(Q_5)\le16\) and \(\rho_e^{\mathrm{o}}(Q_6)\le32\), not the new sharp bounds. The vertex-open-packing problem in [3] has a distinct ground set and cannot supply this edge-packing equality. The more general characterizations in [4] do not explicitly determine these hypercube values. Prior lower bounds, definitions and algorithms are not claimed here as new.

## Limitations

The exactness proof is computer-assisted, via a small reproducible exhaustive branch-and-bound certificate whose completeness is argued above; an independent audit has not been performed. No structural classification or enumeration of all optimizers is claimed. Searches of accessible indexed literature and one mathematical-results database did not reveal these two exact values, but cannot rule out historical or unindexed equivalents. The full 2025 characterization preprint was checked for relevant statements, but a possible independently circulated computation remains a residual priority risk. No value for other cube dimensions follows from these two cases alone.

## References

1. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (first public 2024-03-01), https://arxiv.org/abs/2403.00750.
2. B. Brešar, T. Dravec, J. Hedžet, and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first public 2024-06-06), https://arxiv.org/abs/2406.04020.
3. B. Brešar, S. Klavžar, and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963, https://arxiv.org/abs/2309.04963.
4. A. Pandey and K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935, https://arxiv.org/abs/2508.01935.
