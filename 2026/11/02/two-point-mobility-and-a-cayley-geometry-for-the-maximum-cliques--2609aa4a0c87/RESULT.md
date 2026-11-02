# Two-point mobility and a Cayley geometry for the maximum cliques of the Paley graph of order 41

## Finding

Let \(P_{41}\) be the Paley graph on \(\mathbb F_{41}\), with two distinct residues adjacent exactly when their difference is a nonzero quadratic residue. There are exactly \(205\) maximum cliques, all of cardinality \(5\). No pair of these cliques differs in exactly one vertex. Connect two maximum cliques when they differ in exactly **two** vertices (equivalently, they share three). The resulting reconfiguration graph \(\mathcal R_2\) is a connected, \(8\)-regular Cayley graph on \(205\) vertices, with \(820\) edges, radius and diameter both \(4\). From every clique, the numbers of cliques at distances \(0,1,2,3,4\) are exactly

\[
(1,8,36,98,62).
\]

More precisely, let \(F=\mathbb F_{41}\rtimes\langle10\rangle\) act on residues by \((b,a)\cdot x=ax+b\), where \(\langle10\rangle=\{1,10,16,18,37\}\) is the multiplicative subgroup of order \(5\). Then \(F\) acts **regularly** on the \(205\) maximum cliques. With the reference clique \(B=\{0,1,2,10,33\}\), the Cayley connection set (under left-regular action) is

\[
\mathcal S=\{(0,10),(0,37),(1,37),(9,37),(10,37),(23,10),(31,10),(33,10)\}.
\]

Its elements are closed under inversion, and the Cayley graph \(\operatorname{Cay}(F,\mathcal S)\) is exactly \(\mathcal R_2\).

## Assumptions and scope

The underlying vertex set is \(\{0,1,\ldots,40\}\) with addition and multiplication modulo \(41\). All cliques are **vertex sets**, not ordered tuples or cliques identified up to automorphism. An exact \(r\)-exchange replaces precisely \(r\) vertices while keeping a maximum clique at every move; the two-exchange graph is not the ordinary token-jumping graph (which permits only one replacement). Graph distances count two-exchange moves. The claim concerns only this named finite Paley graph, not all Paley graphs.

## Proof

**1. Complete maximum-clique census.** The nonzero square set, computed by \(t\mapsto t^2\pmod{41}\), is

\[
Q=\{1,2,4,5,8,9,10,16,18,20,21,23,25,31,32,33,36,37,39,40\}.
\]

Run the deterministic sorted-clique recursion: start with the empty prefix and candidate list \(0,1,\ldots,40\); for each candidate \(v\) in ascending order, append \(v\) and keep only later candidates adjacent to \(v\); report a prefix upon reaching cardinality \(5\). Each five-clique has exactly one increasing ordering, so the recursion reports every five-clique once and only once. The accompanying standalone checker obtains \(205\) different five-cliques. For each of them, it explicitly checks that no outside vertex is adjacent to all five, ruling out six-cliques. The displayed \(B\) is a five-clique. Thus \(\omega(P_{41})=5\), and the maximum cliques are exactly the \(205\) enumerated five-sets. The second verifier independently checks all \(\binom{41}{5}=749398\) candidate sets and tests the nonextendibility of each five-clique.

**2. Regular affine action.** Every \(x\mapsto ax+b\), for \(a\in Q\) and \(b\in\mathbb F_{41}\), preserves the Paley edge relation because multiplication by a square preserves \(Q\). The subgroup \(H=\langle10\rangle\) has exactly the five multipliers displayed above; hence \(F=\mathbb F_{41}\rtimes H\) has order \(205\). Compute all \(205\) images \(aB+b\), indexed by \((b,a)\in F\); they are pairwise distinct and coincide with the complete five-clique census. Therefore this action is free and transitive. For comparison, all \(820\) square-affine transformations have the same orbit and exactly four stabilizers of \(B\): \((a,b)=(1,0),(9,33),(32,10),(40,2)\).

**3. Exact exchange generators.** Enumerating the intersection sizes of \(B\) with its \(205\) affine images gives cardinalities \(5,3,2,1,0\), occurring respectively \(1,8,16,64,116\) times. The intersection size \(4\) never occurs. The eight group elements attaining intersection size \(3\) are exactly \(\mathcal S\) as displayed. Since every affine transformation preserves intersection size, the two-exchange edge relation is the left-invariant Cayley relation \(g\sim gs\) for \(s\in\mathcal S\). The inverse of \((b,a)\) is \((-a^{-1}b,a^{-1})\); direct reduction modulo \(41\) shows \(\mathcal S^{-1}=\mathcal S\). The graph has \(205\cdot8/2=820\) undirected edges.

**4. Connectivity and exact diameter.** Use group multiplication

\[
(b,a)(d,c)=(b+ad,ac),
\]

with all arithmetic modulo \(41\), and start breadth-first search at the identity \((0,1)\), multiplying by the eight listed generators. The exact successive distance-shell counts are \(1,8,36,98,62\), summing to \(205\). The search visits every group element and reaches distance \(4\), but no greater distance. Left multiplication acts transitively and is distance preserving, so this profile holds from every vertex. Connectivity, radius \(4\) and sharp diameter \(4\) follow.

## Verification

Run `python3 verify.py`; independently compile `verify_alt.cpp` with a C++17 compiler and run the resulting executable. The first program enumerates five-cliques by increasing-neighbor recursion, checks the regular affine orbit, calculates the eight group generators and performs a Cayley-group breadth-first search. The second program iterates all \(749398\) five-subsets directly, builds the exchange graph from pairwise bitset intersections and performs breadth-first searches from **all** \(205\) vertices. Both certify \(205\) five-cliques, absence of six-cliques, zero one-swap edges, \(820\) two-swap edges and the same distance shells. All loops are finite and exhaustive.

## Relationship to prior work

Ito, Ono and Otachi (2014) introduced systematic clique reconfiguration under one-token rules and analyzed general reachability and algorithms. Their token-jumping move exchanges one vertex; our two-exchange rule differs and the stated numerical and Cayley classifications do not follow from their results. The published small-Paley-graph clique-number tables already record \(\omega(P_{41})=5\); the optimum cardinality is **not** claimed as new. The later study by Hoang (2026) concerns realizability of token-sliding and token-jumping reconfiguration graphs, without giving the two-exchange Paley-41 classification. A separate literature search did not identify a covering result, although an unindexed isomorphic Cayley-graph description could exist.

## Limitations

The theorem is finite and specific to \(P_{41}\); there is no all-prime Paley-family assertion. Reconfiguration is by simultaneous replacement of precisely two vertices, not a sequence of token slides through smaller cliques. Numerical assertions depend on exhaustive code provided with this result, rather than a fully handwritten closed-form proof of the enumeration. A search cannot establish historical novelty, and independent scholarly validation has not been performed.

## References

1. T. Ito, H. Ono and Y. Otachi, *Reconfiguration of Cliques in a Graph* (2014), arXiv:1412.3976v1, https://arxiv.org/abs/1412.3976.
2. S. D. Cohen, *Clique Numbers of Paley Graphs*, Quaestiones Mathematicae 11 (1988), 225–231, DOI:10.1080/16073606.1988.9631955 (known clique-size context).
3. Duc A. Hoang, *On Realizing Reconfiguration Graphs of Cliques* (2026), arXiv:2604.03567v2, https://arxiv.org/html/2604.03567v2 (distinct one-token realization problem).
4. *Clique Numbers for Small Paley Graphs*, https://cs.indstate.edu/ge/Paley/cliques.html (tabulation of baseline clique numbers).
