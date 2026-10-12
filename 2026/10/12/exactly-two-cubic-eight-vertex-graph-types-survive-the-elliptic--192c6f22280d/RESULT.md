# Exactly two cubic eight-vertex graph types survive the elliptic Arf edge transform

## Finding

Let \(V=\{0,1,\ldots,7\}\) and let \(G\) be a simple \(3\)-regular graph on \(V\). Define the binary quadratic form associated with each spanning edge-subgraph \(H\) by
\[
Q_H(x)=\sum_{\{i,j\}\in E(H)}x_i x_j\quad\text{in }\mathbb F_2,\qquad x\in\mathbb F_2^8.
\]
Let \(P(H)\) equal one precisely when the adjacency matrix of \(H\) is nonsingular over \(\mathbb F_2\) and \(Q_H\) has Arf invariant one, and zero otherwise. The Boolean edge Möbius transform is
\[
T(G)=\sum_{H:\,E(H)\subseteq E(G)}P(H)\pmod 2,
\]
with all eight vertices retained even when some become isolated.

**Classification.** Among the six isomorphism types of simple cubic graphs on eight vertices, exactly two satisfy \(T(G)=1\). Both are connected. The complete class table, with numbering fixed by the code's explicit edge representatives, is:

| Class | Labeled graphs | Triangles | Elliptic spanning edge-subgraphs | \(T(G)\) |
| --- | ---: | ---: | ---: | ---: |
| 0 | 35 | 8 | 54 | 0 |
| 1 | 2520 | 4 | 26 | 0 |
| 2 | 10080 | 2 | 17 | 1 |
| 3 | 3360 | 1 | 6 | 0 |
| 4 | 840 | 0 | 0 | 0 |
| 5 | 2520 | 0 | 5 | 1 |

All but class 0 are connected. The two affirmative representatives have the following edges, with vertex labels fixed as above:

**Class 2:** \(\{01,02,03,12,14,25,34,36,47,56,57,67\}\).

**Class 5:** \(\{01,02,03,14,15,24,26,35,37,47,56,67\}\). This is an eight-vertex Möbius ladder (also called the Wagner graph).

The assertion classifies the intersection of the transform's support with the cubic eight-vertex graph class; it does not classify the transform on every eight-vertex graph.

## Assumptions and scope

All graphs are finite, simple, undirected, with exactly eight labeled vertices for the transform. A spanning edge-subgraph is specified by a subset of the original edges and retains isolated vertices. Cubic means every vertex has degree exactly three. Graph classes are taken up to arbitrary vertex permutation. All computations use exact integers and bit operations; there is no floating-point tolerance.

The named transform corresponds to the inversion of the parity representation of \(P\). Indeed, over \(\mathbb F_2\), if \(T(G)=\sum_{H\subseteq G}P(H)\), then
\[
\sum_{H\subseteq G}T(H)=\sum_{J\subseteq G}2^{|E(G)\setminus E(J)|}P(J)=P(G),
\]
so the unique edge-subgraph parity representation described in the motivating source is recovered.

## Proof

**Step 1: exact elliptic test.** Write
\[
S(H)=\sum_{x\in\mathbb F_2^8}(-1)^{Q_H(x)}.
\]
The polar alternating bilinear form of \(Q_H\) is the adjacency matrix over \(\mathbb F_2\). If the quadratic form is nonzero on its polar radical, translation by a radical vector reverses every summand and \(S(H)=0\). Otherwise, if the polar rank is the even number \(r\), the form descends to a nonsingular quadratic form in dimension \(r\), and standard symplectic-pair elimination gives \(S(H)=\pm2^{8-r/2}\). Thus, for eight vertices, the equality
\[
P(H)=1\quad\Longleftrightarrow\quad S(H)=-16
\]
holds: a singular polar form of rank at most six cannot have Gauss sum of magnitude sixteen, and the negative nonsingular sign is exactly Arf invariant one.

**Step 2: complete cubic graph enumeration.** The included stand-alone program enumerates labeled cubic graphs by repeatedly choosing the least unsaturated vertex, then joining it to every admissible set of higher-index unsaturated neighbors sufficient to bring its degree to three. Earlier vertices have already been saturated, so no edge to an earlier vertex is missing. Each simple labeled cubic graph has exactly one such sequence of choices, and no generated graph can violate the degree condition. This gives exactly \(19355\) distinct labeled graphs. Independently, all eight-vertex vertex permutations are applied to each of the six explicit representative edge sets. The resulting six disjoint orbits have cardinalities \(35,2520,10080,3360,840,2520\), and their union agrees exactly, edge mask by edge mask, with the direct exhaustive enumeration. Hence these are exactly the six cubic isomorphism classes.

**Step 3: finite exact elliptic sums.** Every cubic eight-vertex graph has precisely twelve edges, hence \(2^{12}=4096\) spanning edge-subgraphs. For each representative, the program computes all Gauss sums exactly by evaluating the quadratic form at all \(2^8=256\) vectors for every edge-subgraph. It also recomputes the same \(4096\) Gauss sums by an independent Walsh--Hadamard transform on the edge-incidence signature of all \(256\) vectors. The two calculations agree exactly and give the successive elliptic counts
\[
(54,26,17,6,0,5).
\]
Their parities are \((0,0,1,0,0,1)\). Graph isomorphism preserves the underlying quadratic form under coordinate permutation and permutes the spanning edge-subgraphs, so these parities hold throughout the six orbits. The classification follows.

## Verification

Run `python3 verify_cubic8.py` using Python 3.8 or later, with no third-party packages. The checker independently reconstructs all \(19355\) labeled cubic graphs, partitions them by the exact vertex-permutation orbits, tests all six elliptic counts with two independent algorithms, and reproduces the source's six-vertex transform as a normalization regression. It prints `VERIFY_OK` only if every asserted equality holds. The six-vertex regression recovers \(345\) labeled support graphs with edge-count profile \(105\) (seven edges), \(180\) (eight edges) and \(60\) (nine edges), all of maximum degree at most three.

## Relationship to prior work

Raza and collaborators, *The Quantum States of a Graph* (2023), Section 7, introduce the elliptic/non-singular Arf property and cite the unique Boolean edge-subgraph transform. They report the six-vertex transform as four subcubic graph types and discuss a conjecture that its support is always subcubic. They do not state the exact eight-vertex cubic restriction or its six elliptic-subgraph counts. The present result computes this natural first unreported even-order cubic boundary; it neither proves nor disproves the conjecture. The underlying inversion and quadratic-form Gauss-sum classification are standard ingredients and not asserted as new.

The unpublished 2019 draft cited by the source could contain additional computations not publicly accessible here. A later graph-state paper by Czech and collaborators (2026) addresses Arf phases and amplitudes, but its full text was not available for detailed comparison. These represent residual originality risks, not evidence of independent novelty verification.

## Limitations

This is an exact **finite** classification, not a general statement for arbitrary graph order, for noncubic eight-vertex graphs, or for general graph-state equivalence classes. The exhaustive result is conditional only on the explicit definitions above and finite deterministic enumeration; it does not infer an infinite theorem from sampled data. Equivalent previously unpublished or differently indexed computations may exist. No independent audit has been performed.

## References

1. M. A. Raza, A. N. Alahmadi, W. Basaffar, D. G. Glynn, M. K. Gupta, J. W. P. Hirschfeld, A. N. Khan, H. Shoaib, and P. Solé, “The Quantum States of a Graph,” *Mathematics* **11** (2023), 2310, Section 7. DOI: `10.3390/math11102310`. First publicly dated 16 May 2023; primary MSC `81P45`.
2. A. N. Alahmadi, A. N. Alkenani, R. A. Hijazi, N. M. Muthana, and D. G. Glynn, “A transform of graph properties,” unpublished draft (2019), cited as reference 9 in [1]; complete text not independently obtained.
3. B. Czech, Y. Feng, X. Wu, and M. Xie, “Fun with Graph States: Nonlocal Bell Pairs and the Arf Invariant,” arXiv:`2606.06582` (2026); abstract inspected, complete text inaccessible.
