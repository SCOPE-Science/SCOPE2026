# The sharp six-vertex obstruction census for strict zero-or-two-neighbor public-goods equilibria

## Finding
Let every vertex of a finite simple undirected graph choose either activity (1) or inactivity (0), with unique best response 1 exactly when it has zero or two active neighbors. Every graph of order at most five admits a pure equilibrium. Among all six-vertex graphs, exactly 300 of the \(2^{15}=32768\) labeled graphs have no pure equilibrium. They form precisely two isomorphism classes: an eight-edge class with 180 labeled realizations and a nine-edge class with 120 labeled realizations. Hence six is the exact smallest possible order of a graph with no pure equilibrium, and eight is the minimum edge count among the six-vertex obstructions. The nine-edge obstruction is the previously published 3-sun; the contribution here is the sharp completeness and second, sparser class, not the existence of the 3-sun obstruction.

Represent the eight-edge graph \(G_8\) on vertices \(0,1,2,3,4,5\) by the edge list

\[
\{01,02,04,05,12,23,25,34\}.
\]

Represent the nine-edge graph \(G_9\) by

\[
\{01,02,04,05,12,13,14,34,45\}.
\]

Here \(ij\) denotes the unordered edge with endpoints \(i,j\). Their degree multisets are respectively \((4,4,2,2,2,2)\) and \((4,4,4,2,2,2)\), so they are nonisomorphic. Both are connected.

## Assumptions and scope
The graph is finite, undirected, simple, unweighted, and has no loops. Every player follows the same *strict* response pattern \(T(k)=1\) if and only if \(k\in\{0,2\}\) for nonnegative integer \(k\). A pure equilibrium is a binary vector \(s\) with \(s_i=T(\sum_{j:\,ij\in E}s_j)\) at every vertex. The theorem classifies *existence* through order six, without claiming a result for larger graphs, weighted edges, heterogeneous preferences or mixed equilibria. Because \(T(0)=1\), the all-zero strategy cannot be an equilibrium of a nonempty graph; thus every pure equilibrium is automatically nontrivial.

## Proof
**Local witness calculations.** At a degree-two vertex \(u\) whose neighbors are \(v,w\), the rule is equivalent to the parity identity \(s_u+s_v+s_w\equiv1\pmod2\), because its permitted neighbor counts are zero and two.

For \(G_8\), vertices \(1,3,4,5\) have degree two. Their parity identities imply \(s_0=s_2\), \(s_1=s_5=1\), and \(s_3+s_4\equiv1+s_0\pmod2\). If \(s_0=s_2=1\), vertex 0 has at least three active neighbors (1,2,5), and cannot best respond with activity 1. If \(s_0=s_2=0\), vertex 0 must have three active neighbors to remain inactive, which forces \(s_4=1\), while vertex 2 similarly forces \(s_3=1\). This contradicts \(s_3+s_4\equiv1\pmod2\). Hence \(G_8\) has no pure equilibrium.

For \(G_9\), the degree-four vertices \(0,1,4\) form a triangle, with each pair of these joined to exactly one of the degree-two vertices \(2,3,5\). Let \(r\) count the active triangle vertices. The degree-two parity identities make their states 1 exactly when their two triangle neighbors agree. If \(r=0\), all three degree-two vertices are active, and every inactive triangle vertex sees two active neighbors and must be active. If \(r=3\), all degree-two vertices are active, and every triangle vertex sees four active neighbors and must be inactive. If \(r=1\), the two inactive triangle vertices each see two active neighbors (the active triangle vertex plus the pendant vertex joining the inactive pair), contradicting their inactivity. If \(r=2\), the single inactive triangle vertex sees its two active triangle neighbors and neither adjacent pendant vertex active, again contradicting inactivity. No value of \(r\) is possible. This is the familiar six-vertex 3-sun obstruction, already exhibited in the earlier literature.

**Exhaustive sharpness and completeness.** There are \(\binom n2\) possible edges on labeled vertices \(0,\ldots,n-1\). A mask with \(\binom n2\) bits enumerates each possible simple graph exactly once, and an \(n\)-bit mask enumerates each possible strategy exactly once. For any pair of masks, the bit-count identity \(\operatorname{popcount}(\mathrm{adj}[i]\mathbin{\&}s)=\sum_{j:\,ij\in E}s_j\) makes the test in `verify.py` *equivalent*, vertex by vertex, to the stated equilibrium definition. The program checks all graphs for every \(1\le n\le6\), without isomorphism filtering or random sampling. Its exact number of equilibrium-free graphs, by increasing order, is

\[
0,\ 0,\ 0,\ 0,\ 0,\ 300.
\]

For completeness of the isomorphism classification, the same program enumerates all \(6!=720\) vertex permutations of each displayed witness. It obtains orbits of sizes 180 and 120, which are disjoint (indeed, the graphs have distinct edge counts), and verifies **set equality** between their union and all 300 equilibrium-free labeled six-vertex graphs. Thus there is no third isomorphism type. The respective automorphism-group orders are \(720/180=4\) and \(720/120=6\). Since the only six-vertex classes have eight or nine edges, the first-obstruction edge minimum is eight. This is a finite exhaustive proof rather than an extrapolation beyond six vertices.

## Verification
Run `python3 verify.py` with any Python 3 interpreter supporting integer `bit_count` (Python 3.8 or later may require replacing that primitive; Python 3.10+ supports it). The checker needs only the Python standard library and emits `CERTIFICATE_OK` after comparing all 300 exceptions with the disjoint labeled orbits. Its printed order-by-order census is `1: 0/1; 2: 0/2; 3: 0/8; 4: 0/64; 5: 0/1024; 6: 300/32768`, where the numerator counts graphs without an equilibrium. As an additional cross-check, the program independently tallies active neighbors edge by edge for 10,816 graph-state probes and compares those answers with the bit-mask implementation. The two displayed examples also have the direct structural proofs above. No external precomputed graph catalog is required.

## Relationship to prior work
Gilboa and Nisan (2022) formalize strict homogeneous binary network public-goods responses and pose the zero-or-two-neighbor complexity problem. Gilboa (2023) establishes NP-completeness for this pattern and exhibits an equilibrium-free chain of four triangles on nine vertices. Klimm and Stahlberg (2023, Section 5.1, Figure 1a and Lemma 5.3) already exhibit the six-vertex 3-sun as an equilibrium-free graph; its known nonexistence is **not** a novelty claim here. The result above adds the exact smallest-order certification, the other nonisomorphic six-vertex obstruction, the full six-vertex census and its minimal-edge distinction. NP-completeness and the existence of isolated obstruction examples do not themselves imply this classification. Broad finite-graph enumeration algorithms were already known; the point here is this model-specific equilibrium obstruction profile, not an improved enumeration algorithm.

## Limitations
The classification is exact only for graphs of order at most six. The absence of a matching result in searched sources is not a proof of publication priority. A separately published equilibrium census under another description may cover the classification. The checks concern pure strategies only. The six-vertex minimum and its two isomorphism classes say nothing about practical network behavior, approximate equilibria or strategic dynamics.

## References
1. M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238v1, first submitted 2022-07-09, https://arxiv.org/abs/2207.04238.
2. M. Gilboa, *A Characterization of Complexity in Public Goods Games*, arXiv:2301.11580v1, first submitted 2023-01-27, https://arxiv.org/abs/2301.11580; see Section 3, Figure 4.
3. M. Klimm and M. J. Stahlberg, *Complexity of Equilibria in Binary Public Goods Games on Undirected Graphs*, arXiv:2301.11849v1, first submitted 2023-01-27, https://arxiv.org/abs/2301.11849; see Figure 1a and Lemma 5.3.
