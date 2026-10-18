# Optimal threshold-three activation and exchange geometry of two strongly regular graphs

## Finding
Let \(R=K_4\square K_4\) be the sixteen-vertex rook graph and \(S\) be the sixteen-vertex Shrikhande graph. Both are strongly regular with parameters \((16,6,2,2)\). Under synchronous irreversible three-neighbour bootstrap activation, both have minimum percolating-seed cardinality four. The exact families of minimum percolating sets, however, differ:

| Invariant | \(R\) | \(S\) |
| --- | ---: | ---: |
| Minimum percolating sets | 864 | 720 |
| Orbits under an explicit graph-automorphism action | 2 | 6 |
| Activation within three rounds | 0 | 144 |
| Activation in exactly four rounds | 864 | 576 |
| Token-jumping exchange edges | 11,520 | 8,640 |
| Token-jumping connected components | 1 | 1 |
| Token-jumping radius/diameter | 4 / 4 | 4 / 5 |
| Token-sliding exchange edges | 5,472 | 3,936 |
| Token-sliding connected components | 1 | 1 |
| Token-sliding radius/diameter | 5 / 6 | 5 / 6 |

In particular, **two graphs with identical strongly regular parameters have different numbers and orbit types of optimal contagious sets and different token-jumping diameters**. The rook optimum-exchange graph is self-centered under jumping, while the Shrikhande one is not.

For jumping, the eccentricity distributions are \(\{4:864\}\) for \(R\) and \(\{4:432,5:288\}\) for \(S\). For sliding they are \(\{5:288,6:576\}\) and \(\{5:240,6:480\}\), respectively. The rook case of the minimum-cardinality statement was already known and is not claimed new [2].

## Assumptions and scope
The graphs are finite, simple, undirected and labeled on \(V=\{0,\dots,15\}\), using coordinates \(v=4x+y\) for \(x,y\in\mathbb Z/4\mathbb Z\). In \(R\), two distinct vertices are adjacent iff their first or second coordinates agree. In \(S\), two vertices are adjacent iff their coordinate difference belongs to
\[
D=\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\]

For any initial seed set \(A_0\subseteq V\), define in parallel
\[
A_{t+1}=A_t\cup\{v\in V:\ |N(v)\cap A_t|\ge3\}.
\]
A seed set *percolates* when some \(A_t=V\), and is minimum if no smaller percolating set exists. Let \(\mathcal P(G)\) be the family of minimum percolating sets of \(G\). In the token-jumping graph \(J(G)\), two members \(A,B\in\mathcal P(G)\) are adjacent precisely when \(|A\setminus B|=|B\setminus A|=1\). In the token-sliding graph \(T(G)\), such an exchange is permitted only if the unique removed and inserted vertices are adjacent in \(G\). Distances, radii and diameters refer to shortest paths in these *configuration graphs*, not in the original graphs. The finding is limited to these two graphs, to threshold exactly three, and to fixed-cardinality optimal configurations.

## Proof
Both adjacency descriptions produce a simple six-regular graph on sixteen vertices; the supplied verification checks directly that every two distinct vertices have exactly two common neighbours. They are nonisomorphic: a vertex-neighborhood subgraph of \(R\) is the disjoint union of two triangles, whereas a vertex-neighborhood subgraph of \(S\) is a six-cycle.

**Exact minimum.** For every possible three-element initial set, exhaustive closure computation reaches at most five vertices in \(R\) and at most seven in \(S\), so no three-set percolates. Monotonicity rules out any smaller set. Exhaustive inspection of all \(\binom{16}{4}=1820\) four-sets yields exactly 864 percolating sets for \(R\), and 720 for \(S\). The listed seed families are therefore all and only the minima. As an independent formulation, the inactive vertices at threshold three on a six-regular graph undergo successive deletion whenever they have at most three still-inactive neighbours; percolation is equivalent to disappearance of the residual four-core. The separate implementation checks the full enumeration under this equivalent peeling rule rather than forward infection.

**Orbits.** For \(R\), independently permuting its four rows and columns, together with optionally interchanging the coordinates, gives 1,152 explicit automorphisms. For \(S\), take all sixteen translations and the twelve invertible linear maps over \(\mathbb Z/4\mathbb Z\) that preserve \(D\). These give 192 explicit automorphisms. For each displayed orbit representative below, its image set under the relevant automorphisms lies inside the percolating minima; these image sets are pairwise disjoint and their sizes sum to the complete enumerations 864 and 720, establishing exhaustive classifications. The tuples are vertex labels \(4x+y\):

| Graph | Representative | Orbit size | Infection rounds | Jumping degree/eccentricity | Sliding degree/eccentricity |
| --- | --- | ---: | ---: | --- | --- |
| \(R\) | (0,2,5,8) | 576 | 4 | 24 / 4 | 12 / 6 |
| \(R\) | (2,3,5,8) | 288 | 4 | 32 / 4 | 14 / 5 |
| \(S\) | (0,1,3,8) | 96 | 4 | 20 / 5 | 8 / 6 |
| \(S\) | (1,2,4,8) | 96 | 4 | 20 / 5 | 10 / 6 |
| \(S\) | (1,3,4,8) | 192 | 4 | 22 / 4 | 9 / 6 |
| \(S\) | (0,2,5,8) | 96 | 3 | 24 / 5 | 10 / 6 |
| \(S\) | (1,3,5,8) | 192 | 4 | 29 / 4 | 14 / 5 |
| \(S\) | (3,5,6,8) | 48 | 3 | 28 / 4 | 16 / 5 |

**Configuration geometry.** Exhaustively exchanging each of the four selected vertices against each of the twelve unselected vertices, retaining the replacement precisely when it appears in the certified minimum family, constructs every jumping edge. For sliding, additionally require adjacency of the exchanged vertices in the underlying graph. The resulting undirected edge lists contain exactly the counts above. Breadth-first search from *each* configuration exhausts the exact graph-distance metric; in each case it reaches all configurations. Taking the minimum and maximum eccentricities produces the displayed radii, diameters and distributions. Every number in this proof is re-derived by the two stand-alone algorithms, and the certificate contains the complete labeled states, edge lists, symmetry-orbit representatives and diameter-attaining paths.

## Verification
The included `verify_forward.py` enumerates all candidates using parallel activation, constructs both exchange graphs, independently computes all-pairs distances, checks explicit automorphisms, and reproduces `certificate.json`. It requires only Python's standard library. Run `python3 verify_forward.py replay_certificate.json`, compare `forward_output.txt`, and check `cmp certificate.json replay_certificate.json`.

Independently, compile `verify_peeling.cpp` with `g++ -std=c++17 -O2 verify_peeling.cpp -o verify_peeling`, then run `./verify_peeling` and compare `peeling_output.txt`. The latter reconstructs the graph by direct coordinate arithmetic, uses the complement's four-core peeling condition instead of forward activation, and independently constructs and explores all configuration graphs. These are finite exhaustive proofs of the exact enumerated statements, not numerical estimates or evidence about arbitrary graphs. The certificate contains explicit diameter witnesses and full edge lists to allow replay without reconstructing the presentation.

## Relationship to prior work
Guggiola and Semerjian [1] study minimum contagious sets in random regular graphs, explain the activation/induced-core duality, and motivate exact time-dependent optimization. Their scope does not include labeled exact counts or exchange graphs for these two specific strongly regular graphs. Bidgoli, Mohammadian and Tayfeh-Rezaie [2, Theorem 2.1] establish the previously known minimum \(m(K_4\square K_4,3)=4\) as part of a general exact formula for two-dimensional Hamming graphs. The present claim does **not** assert that this cardinality or the general bootstrap process is new; it supplies the optimal-family enumerations, symmetry types and exchange metrics, as well as the parallel comparison with the Shrikhande graph.

The token-sliding terminology follows the general combinatorial reconfiguration literature [3], but independent-set-specific results there do not imply reconfiguration of contagious seed sets. Studies of strongly regular graphs' topology, spectral data or independence complexes also do not determine the threshold-three closure families or their exchange distances. A targeted literature and mathematical-record search did not find stronger exact coverage of these quantities; absence from a search is not proof of global novelty.

## Limitations
This is a finite theorem for two sixteen-vertex graphs; neither a general strongly regular graph theorem nor a higher-order Hamming-graph exchange classification is claimed. The proof of the full census relies on transparent, exhaustive combinatorial algorithms rather than a short symbolic classification of all minima. Published or unindexed supplementary computations could overlap the exact finite tables, and no independent external review has been performed. The two algorithms use the same mathematical graph definitions but genuinely different activation tests; agreement does not constitute independent human certification.

## References
[1] A. Guggiola and G. Semerjian, *Minimal contagious sets in random regular graphs*, arXiv:1407.7361 (first posted 2014-07-28), Sections II and V, https://arxiv.org/abs/1407.7361.

[2] M. R. Bidgoli, A. Mohammadian and B. Tayfeh-Rezaie, *Percolating sets in bootstrap percolation on the Hamming graphs*, arXiv:1905.01942 (first posted 2019-05-06), Section 2 and Theorem 2.1, https://arxiv.org/abs/1905.01942.

[3] E. D. Demaine et al., *Linear-time algorithm for sliding tokens on trees*, Theoretical Computer Science **600** (2015), 132–142, DOI:10.1016/j.tcs.2015.07.037; terminology only.
