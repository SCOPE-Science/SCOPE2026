# Optimal pebbling on the Heawood graph: four orbit types and fragmented one-pebble transfers

## Finding

Let \(H\) be the point–line incidence graph of the seven-point Fano plane. In the usual graph-pebbling model, a move replaces two pebbles at one vertex by one pebble at an adjacent vertex. A distribution is *solvable* when **each** graph vertex can be reached by some legal sequence starting from the original distribution; the sequences for different targets may differ. Then the optimal pebbling number is
\[
\pi_{\mathrm{opt}}(H)=6.
\]
There are exactly **161** solvable distributions of total size six. They are precisely the following three geometric families, comprising four orbits under the full automorphism group of \(H\):

1. **Opposite-side pair (98 distributions).** Put four pebbles at a vertex \(u\) and two at a vertex \(v\) in the opposite bipartition class. There are \(42\) incident and \(56\) nonincident ordered choices of \((u,v)\), with four-pebble and two-pebble roles distinguished.
2. **Incident triple-pair (21 distributions).** Put three pebbles at each endpoint of an incidence edge.
3. **Marked Fano triple (42 distributions).** Put four pebbles at one member and one pebble at each of the other two members of either a three-point line or a triple of concurrent line-vertices. The member carrying four pebbles is distinguished.

Define \(\mathcal R(H)\) to have the 161 optimal distributions as vertices; two are adjacent when **one pebble is relocated across an edge** of \(H\) and the resulting six-pebble distribution is also solvable. Then
\[
\mathcal R(H)\cong 21P_3\;\sqcup\;98K_1.
\]
The same reconfiguration graph is obtained even if the one relocated pebble may jump between arbitrary distinct vertices. The 21 three-vertex paths correspond to the 21 point–line flags; 56 isolated distributions arise from nonincident opposite-side pairs, and 42 from marked Fano triples. The four full-automorphism orbit sizes are \(21,42,42,56\).

## Assumptions and scope

The underlying graph is fixed and finite. One explicit model has points \(p_i\) and lines \(\ell_j\), for \(i,j\in\mathbb Z/7\mathbb Z\), with
\[
p_i\sim\ell_j\quad\Longleftrightarrow\quad i-j\in\{0,1,3\}\pmod 7.
\]
Every line contains three points, every point belongs to three lines, and the graph has fourteen vertices and twenty-one edges. A nonincident point–line pair is at graph distance three. A triple of line-vertices is *concurrent* if the represented Fano lines share a point.

A distribution is a function \(D:V(H)\to\mathbb Z_{\ge0}\), with total weight \(|D|=\sum_{v\in V(H)}D(v)\). A legal pebbling move \(u\to v\), for \(uv\in E(H)\) and \(D(u)\ge2\), changes it to \(D-2\mathbf e_u+\mathbf e_v\). Reachability of different targets is tested from the **same initial distribution**, but not necessarily in the same run. The reconfiguration relocation of one pebble is a **different** move: it replaces \(D\) by \(D-\mathbf e_u+\mathbf e_v\) without discarding a pebble, and both endpoints must be optimal solvable configurations.

## Proof

**Exact reachability recurrence.** For each nonnegative integer vector \(D\), let \(R(D)\) be the set of vertices reachable by ordinary, lossy pebbling moves. The recurrence
\[
R(D)=\{v:D(v)>0\}\;\cup\!
\bigcup_{\substack{uv\in E(H)\\D(u)\ge2}}
R(D-2\mathbf e_u+\mathbf e_v)
\]
is exact: a successful route either starts with a pebble already at its target or has a first legal move, after which the remaining route is a route from the successor state. Conversely every successor route can be prefixed by its legal first move. Each move reduces \(|D|\) by exactly one, so the recurrence terminates and is inductively valid.

For \(0\le k\le6\), the number of fourteen-coordinate distributions of weight \(k\) is \(\binom{13+k}{k}\). Exhaustively evaluating the recurrence yields:

| Weight \(k\) | All distributions | Solvable distributions |
|---:|---:|---:|
| 0 | 1 | 0 |
| 1 | 14 | 0 |
| 2 | 105 | 0 |
| 3 | 560 | 0 |
| 4 | 2,380 | 0 |
| 5 | 8,568 | 0 |
| 6 | 27,132 | 161 |

In total \(38{,}760\) distinct states of weight at most six are covered, including intermediate states after pebbling moves. Every reachability mask appears in `reachability_states.tsv`; the deterministic recurrence-checking program regenerates all of them. An independent direct breadth-first search over pebbling states, using the nonzero binary vectors and their line triples as a second construction of the Fano plane, produces the same table of total and solvable counts. Hence six is both attainable and minimal.

**Geometric completeness.** The exact list in `optimal_distributions.tsv` is checked against a predicate for the three families above, in both directions. In the Fano plane, there are \(14\cdot7=98\) opposite-class assignments to the distinguished four- and two-pebble locations, of which \(2\cdot21=42\) are incident. There are 21 incidence edges, giving the \((3,3)\) class. There are seven three-point Fano lines and seven concurrent triples of Fano lines; each has three choices for the four-pebble position, giving \(2\cdot7\cdot3=42\) marked Fano triples. Thus the geometric classes are pairwise disjoint and together have \(98+21+42=161\) members. Since the exact reachability computation finds 161 solvable configurations and verifies that each falls into one of these classes (and, separately, that every described configuration is solvable), these are all the optima.

**Symmetry and exchange structure.** All invertible linear transformations of \(\mathbb F_2^3\) and an incidence-swapping duality act on the Fano incidence graph. The standalone symmetry checker constructs and checks all \(336\) permutations in the full group, and obtains four orbits of sizes \(21,42,42,56\). Independently, the geometric incidence action gives the same partition: flags, marked flags, anti-flags, and marked Fano triples.

A one-pebble relocation between two classified optima can only be the conversion
\[
(3\text{ at }u,3\text{ at }v)
\longleftrightarrow
(4\text{ at }u,2\text{ at }v)
\quad\text{or}\quad
(2\text{ at }u,4\text{ at }v),
\]
where \(uv\) is an incidence edge. In particular, the two \((4,2)\) assignments at an incidence edge and their \((3,3)\) midpoint form one \(P_3\). A nonincident \((4,2)\) assignment cannot exchange with a \((3,3)\) optimum, and any single relocation from a marked Fano triple either changes its weight partition or destroys the required Fano triple. These cases exhaust all possibilities, including nonlocal relocation. Different incidence edges give disjoint triples; all remaining configurations are isolated. Hence \(\mathcal R(H)\cong21P_3\sqcup98K_1\).

## Verification

The package includes all dependencies required for three fully deterministic finite checks:

- `verify_dp.cpp` builds the cyclic-difference-set incidence graph, evaluates the acyclic reachability recurrence in C++, classifies all weight-six optima, and recomputes the exchange components. Compile with `c++ -O2 -std=c++17 verify_dp.cpp -o verify_dp`, then run `./verify_dp`.
- `verify_bfs.py` builds a separate binary-XOR model of the Fano plane, explicitly explores all legal pebbling successors by breadth-first search, exhausts all distributions of weights zero through six, and checks geometric completeness and both exchange rules. Run `python3 verify_bfs.py`.
- `verify_symmetry.py` constructs the \(336\) automorphisms from invertible binary-linear maps and a duality, verifies graph adjacency, and checks the optimum-orbit partition. Run `python3 verify_symmetry.py` alongside `verify_bfs.py`.
- `certificate.py --verify` regenerates and compares `reachability_states.tsv`, `optimal_distributions.tsv`, and `exchange_edges.tsv` byte-for-byte. `certificate.py --write` can regenerate the three data files from the documented graph model.

The reachability certificate encodes each distribution as fourteen digits in cyclic-graph vertex order \(p_0,\dots,p_6,\ell_0,\dots,\ell_6\), followed by a four-digit hexadecimal mask whose \(i\)-th bit is set precisely when vertex \(i\) is reachable. The other two certificates use that same ordering. Recorded stdout outputs for all verification programs are included. This is a complete finite computation, not a sample or an extrapolation to larger graphs.

## Relationship to prior work

Bunde, Chambers, Cranston, Milans, and West developed fundamental tools and general bounds for optimal graph pebbling, including methods that depend on minimum degree and girth. Their 2005 preprint and author-posted revised text do not supply the six-pebble Heawood optimum classification or the one-pebble relocation structure established here. Belford and Sieben studied *rubbling*, which additionally allows two pebbles at two different neighbors to merge into one: their optimum values concern a different move system and do not imply this ordinary-pebbling theorem. Their complete open preprint likewise does not establish these Heawood-specific counts. The full geometric classification and the disconnected transfer graph are the claimed contribution, not the general definition of pebbling or any result for paths, cycles, or Petersen graphs.

## Limitations

The conclusions apply only to the fourteen-vertex Heawood graph, to ordinary two-for-one pebbling for solvability, and to the explicitly defined fixed-weight relocation operations for reconfiguration. Reachability is target-by-target, not a simultaneous all-vertices covering objective. The result does not determine arbitrary graph pebbling numbers, robust pebbling, rubbling optima, or an infinite-family formula. An independent external mathematical review has not been performed. Searches of indexed literature cannot rule out all unindexed calculations or unpublished supplementary tables.

## References

1. D. P. Bunde, E. W. Chambers, D. Cranston, K. Milans, and D. B. West, *Pebbling and Optimal Pebbling in Graphs*, arXiv:math/0510621, first posted 2005-10-28, revised 2007-01-11; later *Journal of Graph Theory* 57 (2008), 215–238. https://arxiv.org/abs/math/0510621 ; https://dwest.web.illinois.edu/pubs/pebbl.pdf
2. C. Belford and N. Sieben, *Rubbling and Optimal Rubbling of Graphs*, arXiv:0707.4256, first posted 2007-07-28; later *Discrete Mathematics* 309 (2009), 3436–3446. https://arxiv.org/abs/0707.4256
