# Sharp eighth-moment frustration threshold for the signed Heawood Ising model

## Finding
For every signing of the fourteen-vertex Heawood graph, the first eight raw moments of its zero-field signed Ising energy density of states determine the frustration index exactly; moments of orders zero through seven do not. Indeed, the pair \( (M_6,M_8) \) identifies the entire energy density of states among the seven types realized by all signings. The bound eight is sharp: two signings have equal \(M_k\) for every integer \(0\le k\le7\) but different frustration indices, respectively two and three. These are exact noiseless-identifiability statements on this fixed graph, not general statements about other graphs.

## Assumptions and scope
Let \(G\) be the bipartite incidence graph of the Fano plane with points \(0,\ldots,6\), lines \(7,\ldots,13\), and the seven lines on points
\[
\{0,1,3\},\ \{0,2,5\},\ \{0,4,6\},\ \{1,2,4\},\ \{1,5,6\},\ \{2,3,6\},\ \{3,4,5\}.
\]
There are \(14\) vertices and \(21\) edges. Give every edge \(e=uv\) a sign \(\sigma_e\in\{-1,1\}\). With the commuting Pauli operators \(Z_u\), define the zero-field Hamiltonian, normalized energy moments, and switching-invariant frustration index by
\[
H_\sigma=-\sum_{uv\in E(G)}\sigma_{uv}Z_uZ_v,\qquad
M_k(\sigma)=2^{-14}\operatorname{tr}(H_\sigma^k),\qquad
L(\sigma)=\min_{s\in\{-1,1\}^{14}}\bigl|\{uv:\sigma_{uv}s_us_v=-1\}\bigr|.
\]
Thus the spectrum consists of energies \(2f-21\) where \(f\) is the number of unsatisfied edges; the ground energy is \(2L-21\). A vertex switching changes signs of incident edges and induces a spin relabeling, preserving the moments, the density of states, and \(L\). The graph is fixed throughout, and only edge signs vary.

Write \(c_6(\sigma)\) and \(c_8(\sigma)\) for the sum of sign products around all simple cycles of lengths six and eight, respectively. The exact moment identities are
\[
M_0=1,\quad M_2=21,\quad M_4=1281,\quad
M_6=126021+720c_6,\quad
M_8=16784481+20160(17c_6+2c_8),
\]
with \(M_1=M_3=M_5=M_7=0\). Consequently \((M_6,M_8)\) uniquely recovers \((c_6,c_8)\).

The following table exhausts all \(256\) signings after fixing all spanning-tree edge signs positive. The multiplicities count switching representatives with a fixed underlying labeled Heawood graph; they do **not** count switching-isomorphism classes.

| \(c_6\) | \(c_8\) | \(L\) | Representatives | \(M_6\) | \(M_8\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| -8 | 9 | 3 | 28 | 120261 | 14405601 |
| -4 | -3 | 3 | 56 | 123141 | 15292641 |
| 0 | -7 | 3 | 24 | 126021 | 16502241 |
| 0 | 1 | 2 | 84 | 126021 | 16824801 |
| 4 | -3 | 2 | 42 | 128901 | 18034401 |
| 12 | 5 | 1 | 21 | 134661 | 21098721 |
| 28 | 21 | 0 | 1 | 146181 | 27227361 |

Each row has one distinct complete energy frequency vector, so the two specified raw moments determine the whole density of states, not merely the frustration index. In contrast, the two rows with \(c_6=0\) share every moment of degree at most seven but have different ground energies.

## Proof
**Reduction to finitely many signings.** The connected graph has cycle-space dimension \(21-14+1=8\). Choose a breadth-first spanning tree rooted at vertex zero. Vertex switching makes its thirteen tree-edge signs positive, uniquely up to global sign flip. Each of the eight chords can independently have either sign, yielding exactly \(2^8=256\) tree-normalized representatives. Likewise fix the spin at vertex zero to eliminate the twofold global spin-flip degeneracy: all \(2^{13}=8192\) spin choices then occur exactly once.

**Moment identities.** Expanding \(H_\sigma^k\) in the computational basis, the normalized trace of any selected product of edge terms vanishes unless every vertex occurs to even degree, equivalently the set of edges used an odd number of times is an even-degree subgraph. The Heawood graph is bipartite with girth six. Up through degree eight the only nonempty possibilities are one simple six-cycle or one simple eight-cycle. Odd moments vanish additionally because flipping all spins on one bipartition reverses every energy. In degree six, each six-cycle contributes \(6!=720\) orderings. In degree eight, an eight-cycle contributes \(8!=40320\), and a six-cycle together with two additional appearances of an edge contributes
\[
15\frac{8!}{2!}+6\frac{8!}{3!}=342720=17\cdot20160.
\]
The sign-independent terms (all edges appearing an even number of times) contribute \(126021\) in degree six and \(16784481\) in degree eight, as follows directly by multinomial enumeration of partitions of six or eight into even positive multiplicities across 21 edges. This proves the displayed formulas; order four similarly yields \(21+6\binom{21}{2}=1281\). The formulas recover \(c_6\) from \(M_6\) and then \(c_8\) from \(M_8\).

**Complete exact finite certificate.** The accompanying self-contained Python program generates the Fano incidence graph from the seven displayed lines and verifies its basic incidence axioms. Its eight fundamental cycles generate all \(256\) even-degree edge masks, with weight distribution \(1,28,21,84,98,24\) at weights \(0,6,8,10,12,14\). For each of the \(256\) tree-normalized edge signings it enumerates all \(8192\) distinct vertex cuts and computes the complete histogram \(N_f\) of unsatisfied-edge counts. As a mathematically independent check of each histogram, the same code computes the signed even-subgraph enumerator and reconstructs the histogram via the exact cut-code MacWilliams/Krawtchouk transform:
\[
N_f=\frac1{256}\sum_{w}\left(\sum_{\substack{F\ \mathrm{even}\\|F|=w}}\prod_{e\in F}\sigma_e\right)
\sum_j(-1)^j\binom wj\binom{21-w}{f-j}.
\]
The two integer calculations coincide for all \(22\) frequency entries in every signing. The computed table exhausts the full set of \(256\) normalized signings; its row multiplicities total \(256\), and the seven cycle-signature pairs correspond to seven pairwise different complete frequency vectors. All assertions are exact integer equalities.

**Sharpness.** In the table, \(c_6=0\) occurs with \(c_8=-7\), giving \(L=3\), and also with \(c_8=1\), giving \(L=2\). Both share \(M_0\) through \(M_7\), because only \(M_6\) can depend on signs below degree eight; they have different \(M_8\). Therefore no function of the moments through order seven can determine \(L\) on all Heawood signings, whereas the pair \((M_6,M_8)\) does determine it, proving optimality.

## Verification
Run `python3 verify_heawood.py` using Python 3.10 or newer; no third-party packages are required. The program recomputes all \(256\) switched-normalized signings, \(8192\) spin-cut representatives, \(256\) even-cycle subgraphs, all two-route frequency histograms, seven distinct density-of-states types, the table, and the moment identities. Its success marker is `VERIFY_OK 256_signatures 8192_spin_cuts 256_even_subgraphs 7_DOS_types cutoff_8`. The finite search is exhaustive **because** the spanning-tree reduction and cycle-space basis are proved above, not merely because the script terminates.

## Relationship to prior work
Scali and Kyriienko (2026) formulate spectral-moment features for signed Ising graph Hamiltonians and use them to predict frustration, including moments up to order six; their work motivates the precise finite feature-identifiability question. Their general moment-counting and switching-invariance principles are taken as established, not claimed here. Sivaraman (2012, Chapter 4) already classifies seven switching-isomorphism types of signed Heawood graphs and records their frustration indices and counts of negative six-cycles. That prior classification is likewise **not** a new contribution here. The specific new comparison is the all-signings Ising moment order threshold, the eighth-moment cycle-signature refinement, and its exact full-density-of-states identification. The latter statement was not identified in the inspected relevant primary work; implicit prior derivations remain possible.

## Limitations
The result is finite and graph-specific. It concerns exact, noiseless, zero-field moments and does not give finite-shot distinguishability bounds, a robust learning method, a computational speedup, an extension to variable graphs, or an analogous statement for nonzero transverse fields. Complete density-of-states identification on this graph does not imply that the same pair of moments identifies arbitrary signed Ising models. The exhaustive program provides a transparent finite certificate but is not an independent external audit or a proof of general infinite-family claims. Literature-priority uncertainty remains despite targeted comparisons.

## References
1. S. Scali and O. Kyriienko, *Learning structural balance of graphs from quantum spectral features*, arXiv:2609.11736v1 (first publicly posted 10 September 2026), https://arxiv.org/abs/2609.11736.
2. V. Sivaraman, *Some Topics concerning Graphs, Signed Graphs and Matroids*, Ph.D. dissertation, The Ohio State University (2012), Chapter 4, https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1354645035&disposition=inline.
3. A. Solé and T. Zaslavsky, *A Coding Approach to Signed Graphs*, Discrete Applied Mathematics 1994, general coding-theoretic background on signed graphs and switching.
