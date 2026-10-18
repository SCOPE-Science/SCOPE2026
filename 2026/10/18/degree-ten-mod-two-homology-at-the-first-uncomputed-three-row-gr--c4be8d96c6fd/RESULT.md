# Degree-ten mod-two homology at the first uncomputed three-row grid

## Finding
Let \(G=P_3\square P_{10}\) be the rectangular grid graph, and let \(M(G)\) be the simplicial complex whose simplices are sets of pairwise vertex-disjoint edges of \(G\). With coefficients in \(\mathbb F_2\), its **complete reduced homology** is
\[
\widetilde H_i(M(G);\mathbb F_2)\cong
\begin{cases}
(\mathbb F_2)^{273}, & i=9,\\
(\mathbb F_2)^2, & i=10,\\
0, & i\notin\{9,10\}.
\end{cases}
\]
In particular \(\widetilde H_{10}(M(G);\mathbb F_2)\ne0\), refuting the all-width sphere-wedge conjecture of Chauhan, Sharma and Shukla [1], whose proposed wedge dimension is \(n-1\), already at \(n=10\). The finding makes no assertion about integral torsion or the complete integral homotopy type.

## Assumptions and scope
The path \(P_m\) has \(m\) vertices. The graph \(G\) has \(30\) vertices and \(47\) edges, labeled by row-major vertex indices \(r\cdot10+c\), \(0\le r<3\), \(0\le c<10\). The edge order is row-major over each grid vertex, listing the downward edge (when present) before the rightward edge (when present). Each simplex is represented by the bit mask of its included edges. Coefficients throughout the finding and proof are \(\mathbb F_2\); reduced chains include the empty simplex in degree \(-1\).

## Proof
**1. Complete finite face complex.** Enumerate the \(47\) grid edges and recursively branch on excluding/including each edge, retaining an inclusion only when its endpoints are unoccupied. Every matching is produced exactly once; no nonmatching can be produced. The resulting augmented face set has precisely \(47{,}177{,}097\) members (including the empty face). The complete recursion is supplied in `verify_grid10.cpp`.

**2. An acyclic partial matching.** Process edge-vertices in either increasing or decreasing order. At stage \(e\), among faces left unmatched by previous stages, pair every face \(F\) that does not contain \(e\) with \(F\cup\{e\}\), whenever both faces remain. Delete each pair and continue. This is a matching of consecutive dimensions in the face poset. It is acyclic: in a hypothetical closed alternating gradient path, choose the earliest edge-vertex \(e\) (in the chosen processing order) used in one of its matched upward steps. An upward step at \(e\) inserts \(e\); eventually a downward step must remove \(e\). The upper and lower faces of that downward step are both paired at stage \(e\) or later and hence were both still present when stage \(e\) was processed. Since they differ exactly by \(e\), the procedure must have paired them at stage \(e\), contradicting their use as an unmatched downward step. This argument applies to all dimensions, including the augmented empty face.

For increasing order, the matching leaves exactly \(393\) critical dimension-\(9\) faces and \(122\) critical dimension-\(10\) faces, with none in any other degree. For decreasing order, it leaves \(301\) critical dimension-\(9\) faces and \(30\) critical dimension-\(10\) faces. The noncritical pairs total \(23{,}588{,}291\) and \(23{,}588{,}383\), respectively. The initial empty simplex is paired, so these are reduced Morse chain complexes.

**3. Complete Morse differential and exact ranks.** Over \(\mathbb F_2\), a critical \(10\)-cell has ordinary simplicial boundary given by its eleven \(9\)-dimensional facets. To calculate its Morse boundary, project each facet \(F\) recursively: a critical \(9\)-face maps to its own basis vector; a \(9\)-face paired *upward* with a \(10\)-face \(U\) maps to the sum of the projections of the other ten facets of \(U\); and a \(9\)-face paired *downward* with a dimension-\(8\) face maps to zero. These are precisely the unit-pivot elementary chain-cancellation equations. They terminate because of the acyclicity proved above. All transitions and basis coefficients are computed directly from the generated matchings, not from predicted homology ranks.

The increasing-order critical Morse boundary is a binary matrix of size \(122\times393\) with exact \(\mathbb F_2\)-rank \(120\). The decreasing-order matrix is \(30\times301\) with exact rank \(28\). The two complete, independently generated matrices are included in `certificates/ascending_mod2.txt` and `certificates/descending_mod2.txt`. The script `verify_matrices.py` independently checks the dimensions and ranks using exact integer-bitset row elimination; `verify_grid10.cpp` regenerates both matrices from the complete \(47{,}177{,}097\)-face complex. Because there are no other critical degrees, the increasing-order complex gives
\[
\dim_{\mathbb F_2}\widetilde H_{10}=122-120=2,\qquad
\dim_{\mathbb F_2}\widetilde H_9=393-120=273.
\]
The independent decreasing-order complex gives \(30-28=2\) and \(301-28=273\). Standard algebraic discrete Morse reduction preserves homology. This proves the claim.

## Verification
Compile with a C++17 compiler, run `./checker ascending certificates/ascending_mod2_replayed.txt` and `./checker descending certificates/descending_mod2_replayed.txt`, then compare these outputs byte-for-byte with the provided respective certificates. The compile command is `g++ -std=c++17 -O3 verify_grid10.cpp -o checker`. Running `python3 verify_matrices.py` checks both stored matrices independently. The full calculation was actually executed in both directions and both replayed matrices matched the included certificates exactly; the rank checker returned \(120\) and \(28\). Peak memory for the complete computation is about one gigabyte. The result is an exhaustive finite proof, not a statistical or truncated experiment.

## Relationship to prior work
Chauhan–Sharma–Shukla [1], first posted September 23, 2026, establish sharp connectivity for \(M(P_3\square P_n)\), report integral homology for \(1\le n\le9\), and explicitly conjecture that for **all** \(n\) the complex is a wedge of spheres solely in dimension \(n-1\) (Conjecture 4.1, page 22). Their Table 1 stops at \(n=9\). The present computation is the first subsequent width and yields two nonzero mod-two classes one dimension above their proposed range. The earlier proposed all-width classification of Goyal–Shukla–Singh [2] was withdrawn in 2025 because of a proof gap. Published formulas for grid matching-complex reflection Lefschetz numbers [3,4] concern alternating character sums and do not imply the individual degree-ten Betti number; they are not reclassified here.

## Limitations
This is a single finite-grid computation at width ten, not a formula for all widths. It computes homology only over \(\mathbb F_2\), so the two degree-ten classes could reflect integral free classes or torsion in degree nine; neither possibility is asserted. The rank certificates rely on a complete finite enumeration and an explicit algebraic Morse differential; their source is included for independent replay. Novelty is asserted relative to the examined published and indexed literature, not as a proof that no unindexed equivalent work exists. Independent external scientific validation has not been performed.

## References
[1] P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1 (posted 2026-09-23), especially Theorems 1.2–1.3, Table 1 and Conjecture 4.1.

[2] S. Goyal, S. Shukla, A. Singh, *Matching complexes of \(3\times n\) grid graphs*, arXiv:2106.09915 (2021; withdrawn version dated 2025-11-26 explicitly identifies a proof gap).

[3] *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes*, public mathematical research archive, 2026-10-11.

[4] *Half-turn Lefschetz characters and full symmetry quotients of \(3\times n\) grid matching complexes*, public mathematical research archive, 2026-10-11.
