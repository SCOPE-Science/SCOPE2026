# Exact cross-join graph distances among binary order-five de Bruijn cycles

## Finding

Let \(G_5\) be the undirected cross-join graph whose vertices are all binary de Bruijn cycles of order five, identified modulo cyclic rotation. Two vertices are adjacent precisely when one cycle can be obtained from the other by a *single* cross-join operation (two conjugate-successor switches that preserve a single cycle). There are exactly \(2048\) vertices and \(38704\) edges. Its graph-theoretic diameter is exactly \(7\) and its radius is exactly \(5\).

For \(d\in\{1,2,3,4,5,6,7\}\), the numbers of **unordered distinct vertex pairs** at graph distance \(d\), in increasing order, are

\[
(38704,305376,758800,710976,254800,27104,368).
\]

The numbers of vertices with eccentricity \(5,6,7\), respectively, are

\[
(48,1264,736).
\]

Consequently any two order-five binary de Bruijn cycles can be interconverted in at most seven cross-join operations, and seven operations are necessary for exactly \(368\) unordered pairs. The mean cross-join distance between distinct cycles is exactly \(7040/2047\). These statements concern shortest paths through valid intermediate de Bruijn cycles; they do not concern cyclic index span or longest common subsequences.

## Assumptions and scope

An order-five binary de Bruijn cycle has period \(32\) and contains each five-bit word exactly once as a cyclic factor. Label its length-five states by integers \(0,\ldots,31\) in ordinary binary notation. For a state \(s\), put \(v=s\bmod16\), and define

\[
\Phi_m(s)=2v+b_m(s),\qquad
b_m(s)=\begin{cases}
(m\gg v)\mathbin{\&}1,&0\le s<16,\\
1-((m\gg v)\mathbin{\&}1),&16\le s<32,
\end{cases}
\]

where \(m\in\{0,\ldots,65535\}\), \(\gg\) means a right bit shift, and \(\&\) denotes bitwise AND. Thus \(m\) is the sixteen-entry Boolean feedback table for the final four state bits. The conjugate states are \(v\) and \(16+v\).

Call \(m\) *valid* precisely when the permutation \(\Phi_m\) consists of a single directed cycle of length \(32\). A cross-join edge connects two valid masks that differ in exactly two distinct bit positions. The proof below shows why this exactly matches the conventional cross-join operation; merely changing two arbitrary feedback bits without maintaining a Hamiltonian cycle is not an edge. Graph distance counts edges, not vertices, on a shortest path.

## Proof

**1. Exhaustive and nonredundant encoding.** A de Bruijn cycle assigns each of the \(32\) five-bit states exactly one successor, obtained by deleting its leading bit and appending one new bit. For each fixed four-bit suffix \(v\), the only possible destinations from its two conjugate predecessors \(v\) and \(16+v\) are \(2v\) and \(2v+1\). Since a Hamiltonian cycle is also a permutation, the two chosen appended bits must be opposite. Exactly one Boolean choice therefore remains for each of the \(16\) suffixes, giving precisely the masks above. Conversely, each such mask gives a permutation of all \(32\) states; it corresponds to a de Bruijn cycle if and only if its permutation is one full cycle. The cycle can uniquely be rooted at state zero, so two valid masks cannot encode the same cyclic word.

The verifier iterates **every** integer \(0\le m<65536\). For each it starts at state zero, follows \(\Phi_m\) for exactly \(32\) steps and accepts precisely when no state repeats early and the final state is zero. This is equivalent to being one \(32\)-cycle, and yields exactly \(2048\) valid masks. The number independently agrees with the classical count \(2^{2^4-5}=2048\).

**2. Exact edge criterion.** Toggling feedback bit \(i\) interchanges successors of the conjugate states \(i\) and \(16+i\). Starting with one directed cycle, this first switch splits it into two cycles. Toggling another distinct bit \(j\) rejoins those cycles exactly when the two states of the second conjugate pair lie in different cycles after the first switch. Equivalently, the four conjugate states occur in alternating pairs along the original cycle. Thus two distinct valid masks are cross-join adjacent if and only if their XOR is \(2^i+2^j\) for two different \(i,j\in\{0,\ldots,15\}\). This is an equivalence, not merely a sufficient construction.

The verifier checks the equivalent alternating-position predicate for **each valid mask and all \(\binom{16}{2}=120\) pairs of different bit positions**, and asserts equality with membership of the doubly toggled mask among the valid masks. It also checks adjacency symmetry. The resulting graph has \(38704\) undirected edges. As an external cross-check, its complete vertex-degree distribution equals the previously published order-five cross-join-neighbor table of Alhakim (2018); that degree distribution is not claimed as new.

**3. Complete shortest-path calculation.** For each of the \(2048\) vertices in increasing mask order, the verifier runs ordinary unweighted breadth-first search on this complete adjacency list. Induction on breadth-first layers proves that the first assigned label of every reached vertex is exactly its shortest-path distance; disconnected vertices would have label \(-1\) and are explicitly rejected. All searches reach every vertex. For each search, the maximum distance is recorded as the source eccentricity. For each unordered vertex pair, the distance is recorded exactly once by counting target indices strictly larger than the source index. The resulting distance histogram and eccentricity histogram are precisely the two arrays in the Finding. The pair histogram sums to \(2048\cdot2047/2=2096128\) and the eccentricity histogram sums to \(2048\), independently confirming the count boundaries.

**4. Extremal and mean values.** Since the only eccentricities are \(5,6,7\), the radius is \(5\) and the diameter is \(7\). An explicit pair at distance \(7\) has masks \(32943\) and \(65361\); one shortest mask path is

\[
32943,33005,33017,33521,33745,35665,44881,65361.
\]

Every consecutive pair differs at two mask bits and is a valid cross-join edge. The all-pairs breadth-first calculation excludes a path of length less than seven between the endpoints. Finally, the sum of pairwise distances is \(7208960\); division by \(2096128\) gives \(7040/2047\).

Each step is finite and exact, and every possible mask, prospective edge, source, and target is covered. The calculation is therefore an exhaustive proof of these order-five facts, not a sampled or asymptotic experiment.

## Verification

Run `python3 crossjoin_verify.py` from the directory containing the supplied standalone file; the script uses only the Python standard library. It reconstructs all \(65536\) feedback masks, validates the full \(32\)-state orbits, verifies the alternating conjugate-pair edge criterion, reproduces Alhakim's earlier degree table as a non-novel checksum, and independently calculates all graph distances by breadth-first search.

The checked output is:

```
NODES 2048
EDGES 38704
DIAMETER 7
RADIUS 5
UNORDERED_DISTANCE_COUNTS {1: 38704, 2: 305376, 3: 758800, 4: 710976, 5: 254800, 6: 27104, 7: 368}
ECCENTRICITY_COUNTS {5: 48, 6: 1264, 7: 736}
DISTANCE_SEVEN_PAIR 32943 65361
VERIFY_OK
```

All integer predicates, loops, and assertions are visible in the file; no external dataset or precomputed adjacency matrix is assumed.

## Relationship to prior work

Mykkeltveit and Szmidt (2013) defined the two-switch feedback formulation and proved global reachability by repeated cross-joins, but not the minimum number required for the complete order-five graph. Alhakim (2018) proved connectivity and a Hamiltonian path for more general cross-join graphs, and published the exact order-five **degree** histogram; this is a strong independent check on graph construction, not a statement of shortest-path distances. In particular, Alhakim expressly distinguishes the longest-common-prefix quantity used in the connectivity proof from graph shortest-path distance. Jiang and Lin (2020) discuss the *diameter of a cross-join pair* in the sense of positions or common-subsequence span, which is not the diameter of the graph of all cycles. Later algorithmic cross-join generation treatments provide context but do not, in the accessible material, give the distance/eccentricity census here.

The novel statement assessed here is the exact **all-pairs graph metric** of the order-five binary cross-join graph, not the classical count \(2048\), connectivity, Hamiltonicity, a clique number, or the published degree distribution. Historical uniqueness is not independently certified.

## Limitations

The theorem is an exact finite classification for binary order five only. It supplies no general formula or bound of seven for arbitrary orders, no claim about computational security, and no spectral or random-walk mixing theorem. Graph distance depends on the definition of a single cross-join edge; other nonlinear feedback transformations may have different costs. One highly related 2020 article was accessible only in abstract/preview form and a 2026 study in excerpts, so independent historical-priority checking remains appropriate.

## References

1. Johannes Mykkeltveit and Janusz Szmidt, *On cross joining de Bruijn sequences*, Cryptology ePrint Archive 2013/760 (initial record 2013-11-21), https://eprint.iacr.org/2013/760 . See the full text, especially Sections 2–4, for the cross-join definition and connectedness theorem.
2. Abbas Alhakim, *Hamiltonicity of the Cross-Join Graph of de Bruijn Sequences*, arXiv:1805.12059 (2018-05-30), https://arxiv.org/abs/1805.12059 . See Table 1 for the order-five degree census, Section 4 for the distinct prefix-distance metric, and Section 6 for the scope of the graph results.
3. Yupeng Jiang and Dongdai Lin, *Longest subsequences shared by two de Bruijn sequences*, Designs, Codes and Cryptography 88 (2020), 1463–1475, https://doi.org/10.1007/s10623-020-00759-2 . Preview/abstract inspected.
4. Przemysław Dąbrowski, Tomasz Rachwalik and Janusz Szmidt, *The Cross-Joint Method and Generation of De Bruijn Sequences*, Mathematics 14 (2026), 1424, https://doi.org/10.3390/math14091424 . Accessible extract/abstract inspected.
