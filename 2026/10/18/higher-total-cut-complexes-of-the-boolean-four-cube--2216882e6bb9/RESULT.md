# Higher total-cut complexes of the Boolean four-cube

## Finding
Let \(Q_4\) be the four-dimensional cube graph with sixteen vertices, and let \(\Delta_k^t(Q_4)\) be its total \(k\)-cut complex. For **every integer** \(4\le k\le8\), the complete integral homotopy type is

\[
\begin{array}{c|c|c}
k&\Delta_k^t(Q_4)&\text{number of sphere summands}\\\hline
4&\bigvee^{529}S^8&529\\
5&\bigvee^{937}S^6&937\\
6&\bigvee^{441}S^4&441\\
7&\bigvee^{49}S^2&49\\
8&S^0&1.
\end{array}
\]

All reduced homology groups are therefore torsion-free and vanish outside the indicated dimension. This gives the entire higher-parameter end of the total-cut filtration on the Boolean four-cube. In particular, these are **homotopy** equivalences, not merely homology computations.

## Assumptions and scope
The simple graph \(Q_4\) has vertices the four-bit strings, identified with the integers \(0,\ldots,15\); two vertices are adjacent exactly when their bitwise XOR has one nonzero bit. A subset \(I\) is independent if no two of its vertices are adjacent. By definition, the facets of \(\Delta_k^t(Q_4)\) are precisely the complements \(V(Q_4)\setminus I\) of the independent \(k\)-sets \(I\). A set \(\sigma\) is a simplex if and only if its complement contains an independent \(k\)-set. Only \(k\in\{4,5,6,7,8\}\) is asserted as a new classification. The independence number of \(Q_4\) is \(8\), so this range reaches the final nonvoid level. No claim is made for arbitrary-dimensional cubes.

## Proof
**1. Exact face membership.** Represent a subset of the sixteen vertices by its sixteen-bit mask. For a vertex subset \(S\), let \(\alpha(S)\) denote the independence number of the induced graph \(Q_4[S]\). With \(v\) any vertex of nonempty \(S\), the elementary include/exclude recurrence is

\[
\alpha(S)=\max\{\alpha(S\setminus\{v\}),\ 1+\alpha(S\setminus N[v])\},\qquad \alpha(\varnothing)=0.
\]

Here \(N[v]\) is the closed graph neighborhood of \(v\), interpreted inside \(S\). Computing this recurrence on all \(2^{16}\) masks gives an exact simplex-membership test: \(\sigma\in\Delta_k^t(Q_4)\) precisely when \(\alpha(V\setminus\sigma)\ge k\). As an independently implemented cross-check, enumerate all independent \(k\)-sets from vertex combinations, form their complementary facets, and enumerate every nonempty subface. The two resulting face sets agree **as sets**, not just in cardinality.

**2. Explicit acyclic matchings.** For each \(k=4,5,6,7,8\) separately, start with the finite poset of all **nonempty** faces of \(\Delta_k^t(Q_4)\). Process the vertices in the fixed order \(0,1,\ldots,15\). At vertex \(v\), simultaneously match every pair of still-unmatched faces \((\sigma,\sigma\cup\{v\})\) for which \(v\notin\sigma\) and both faces remain. Remove both faces from later matching stages. These are sequential element matchings; the standard element-matching lemma proves their union acyclic. Independently, the supplied verifier orients every Hasse cover upward if matched and downward if unmatched, then performs an **exhaustive topological sort** of the entire directed graph. Every face is visited, so directed cycles do not occur.

The exact integer counts from these complete computations are:

| \(k\) | Independent \(k\)-sets | Nonempty simplices | Matched face pairs | Hasse covers checked | Unmatched critical cells |
|---|---:|---:|---:|---:|---|
| \(4\) | 228 | 58,670 | 29,070 | 447,600 | One \(0\)-cell; 529 \(8\)-cells |
| \(5\) | 128 | 39,958 | 19,510 | 274,624 | One \(0\)-cell; 937 \(6\)-cells |
| \(6\) | 56 | 17,574 | 8,566 | 103,792 | One \(0\)-cell; 441 \(4\)-cells |
| \(7\) | 16 | 4,526 | 2,238 | 22,368 | One \(0\)-cell; 49 \(2\)-cells |
| \(8\) | 2 | 510 | 254 | 2,032 | Two \(0\)-cells |

These counts, the sorted integer masks of **every** critical simplex, and the SHA-256 digest of each complete matched-pair list are in `certificate_q4_totalcut.json`. The self-contained source `verify_q4_totalcut.py` recomputes and checks that certificate and every Hasse orientation; thus the finite computation is exhaustive, not sampling.

**3. Conclude the integral homotopy types.** The acyclic discrete-Morse theorem produces a CW complex with one cell for each critical face. For \(k=4,5,6,7\), there is exactly one \(0\)-cell and all remaining cells have the single positive dimension \(16-2k\). There are no intermediate cells, hence every attaching map is constant to the \(0\)-skeleton. The CW complex is precisely a wedge of the indicated many spheres. For \(k=8\), the matching has just two critical vertices, hence the complex is homotopy equivalent to two points, or \(S^0\). In fact \(Q_4\) is connected, bipartite, and \(4\)-regular, so any independent set of size eight determines a bipartition; the only two maximum independent sets are the even- and odd-parity classes. The two complementary facets consequently form two disjoint simplices, giving a direct check of the last case.

## Verification
Run `python3 verify_q4_totalcut.py certificate_q4_totalcut.json` with Python 3. The standard-library-only program separately constructs faces by independent-set facets and by the induction recurrence for graph independence numbers, checks set equality at every level, executes the matching, examines **every** Hasse cover, topologically sorts the reversed-matching digraph, and compares the resulting critical cells and pair digests with the accompanying certificate. The proof uses the complete finite universe of all \(65,536\) vertex subsets, not a finite sample standing in for an infinite theorem. The reproduced critical cells and the discrete-Morse theorem provide the integral homotopy assertion without relying on field-specific homology calculations.

## Relationship to prior work
Bayer et al. introduced total cut complexes and proved the sequential-element-matching theorem used here; their classifications treat other families and lower stages, not these four-cube higher stages. Carnero Bravo's 2026 analysis explicitly asks for the higher total-cut homotopy types of Cartesian products of complete graphs (Question 53), of which \(Q_4=K_2\square K_2\square K_2\square K_2\) is a natural first four-factor binary case. The already known four-cube total \(3\)-cut homotopy classification and the known general total \(2\)-cut results are **not** presented as new. The rectangular \(4\times4\) grid \(P_4\square P_4\) is not \(Q_4\): the former has 24 edges, while the latter has 32. Filakovský's square-sequence graph and rectangular grid theorems therefore do not imply this five-level result; a square-sequence construction on sixteen vertices has at most 28 edges.

## Limitations
This is an exact finite, graph-specific computation for one natural graph at five complete parameter levels; it neither proves a general-dimensional hypercube formula nor computes equivariant characters or attaching maps for other graphs. The homotopy types follow from fully verified acyclic matchings, but no independent external mathematical audit has been performed. An unindexed equivalent treatment of this exact higher cut tower cannot be ruled out by literature search alone.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503v1 (first posted September 27, 2022); see Definition 2.3 and Theorem 7.5 in v2.
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427v3 (2026), Section 5.4, especially Question 53.
3. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365v4 (2026), Theorem 1 and Corollary 4.
4. P. Chauhan, S. Shukla, K. Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486 (2025), Theorems 1.4 and 1.5.
5. *The total 3-cut complex of the 4-cube: a 129-sphere wedge and its hyperoctahedral character*, publicly indexed mathematical note (2026); claims only the separate \(k=3\) level.
