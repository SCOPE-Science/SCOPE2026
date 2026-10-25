# A duality-sign twist between Heawood perfect and ordinary matching homology

## Finding
Let \(H\) be the Heawood graph (the point-line incidence graph of the Fano plane), \(G=\operatorname{Aut}(H)\), and \(\varepsilon:G\to\{\pm1\}\) the character that is \(+1\) on automorphisms preserving the two vertex classes and \(-1\) on automorphisms exchanging them. Write \(\mathcal P(H)\) for the perfect-matching complex: its vertices are edges of \(H\), and its simplices are **edge sets extendible to a perfect matching**. Write \(\mathcal M(H)\) for the ordinary matching complex of all vertex-disjoint edge sets.

**Theorem.** The entire rational homology representations, in their unique nonvanishing reduced degrees, are related by
\[
\boxed{\widetilde H_2(\mathcal P(H);\mathbb Q)\ \cong_G\ \varepsilon\otimes \widetilde H_4(\mathcal M(H);\mathbb Q).}
\]
Both vector spaces have dimension \(16\). The complete characters are:

| Vertex-class action | Order of automorphism | Number | Trace on \(\widetilde H_2(\mathcal P(H);\mathbb Q)\) | Trace on \(\widetilde H_4(\mathcal M(H);\mathbb Q)\) |
| --- | ---: | ---: | ---: | ---: |
| Preserves | 1 | 1 | 16 | 16 |
| Preserves | 2 | 21 | 0 | 0 |
| Preserves | 3 | 56 | 1 | 1 |
| Preserves | 4 | 42 | 0 | 0 |
| Preserves | 7 | 48 | 2 | 2 |
| Exchanges | 2 | 28 | -4 | 4 |
| Exchanges | 6 | 56 | -1 | 1 |
| Exchanges | 8 | 84 | 0 | 0 |

Rows group automorphisms by bipartition behavior and order; the order-seven row may combine distinct conjugacy classes having equal traces. The unique \(\operatorname{GL}_3(\mathbb F_2)\)-fixed line in perfect-matching homology is **duality-odd**, so \(\widetilde H_2(\mathcal P(H);\mathbb Q)^G=0\), whereas \(\dim\widetilde H_4(\mathcal M(H);\mathbb Q)^G=1\). In particular the elementary point-line polarity has trace \(-4\) on the former, with \(+1\)- and \(-1\)-eigenspace dimensions \(6\) and \(10\), versus trace \(+4\) and eigenspace dimensions \(10\) and \(6\) on the latter.

## Assumptions and scope
Identify the seven points and seven lines with the nonzero vectors \(p,\ell\in\mathbb F_2^3\); point \(p\) is incident with line \(\ell\) precisely when \(p\cdot\ell=0\) over \(\mathbb F_2\). This presents \(H\) as a connected bipartite cubic graph with \(14\) vertices and \(21\) edges. Fix graph-edge order by lexicographically listing all pairs \((p,\ell)\) with binary integer labels \(1\) through \(7\) and zero dot product.

The side-preserving subgroup \(B\) consists of the \(168\) invertible binary linear transformations \(A\): \(p\mapsto Ap\), \(\ell\mapsto A^{-T}\ell\). Point-line duality \(\tau:(p,\ell)\mapsto(\ell,p)\) exchanges sides, and \(G=B\sqcup\tau B\) has order \(336\). Equivariance is over \(\mathbb Q\); the theorem makes no claim of isomorphic integral \(G\)-lattices or of an equivariant homotopy equivalence.

## Proof
**1. The homology degrees and their dimensions.** Enumerate each bijection of the seven point labels to the seven line labels and retain those respecting incidence. Exactly \(24\) are perfect matchings. Taking all nonempty subsets of these matching facets yields \(2201\) perfect-complex simplices, with face numbers in dimensions \(0\) through \(6\)
\[
(21,168,560,756,504,168,24).
\]
Independently generate every ordinary matching by testing disjointness on the \(21\) graph edges; this gives \(3461\) nonempty simplices.

For both complexes construct a discrete-Morse pairing in the nonempty face poset by successive edge toggles. At each edge \(e\) of a specified priority list, pair every still-unpaired face \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever both are still unpaired. Use the following zero-based edge-index priority lists (in the lexical order above):

- Perfect complex: `4,16,8,6,13,2,7,17,15,10,12,1,20,19,14,3,11,9,0,18,5`.
- Ordinary complex: `6,17,9,11,7,4,5,3,15,20,16,10,18,14,8,2,0,1,19,13,12`.

The provided verifier constructs the complete directed Hasse graph for each matching, directing matched incidences upward and all other codimension-one incidences downward. It topologically sorts every node of each graph, proving acyclicity: all \(8736\) perfect-complex and \(14574\) ordinary-complex incidences are included. The perfect-complex matching has \(1092\) pairs and exactly one critical vertex plus \(16\) critical two-cells; the ordinary-complex matching has \(1722\) pairs and exactly one critical vertex plus \(16\) critical four-cells. Forman's theorem and the absence of intermediate CW cells give
\[
\mathcal P(H)\simeq\bigvee^{16}S^2,
\qquad
\mathcal M(H)\simeq\bigvee^{16}S^4.
\]
This is a complete finite proof by explicitly checkable face-poset operations, not an inference from experimental Betti numbers. It establishes that the only nonzero reduced rational homology groups occur in the degrees stated in the theorem.

**2. The whole automorphism group.** An automorphism preserving the two sides is a Fano-plane collineation. Its action is determined by the ordered images of any independent triple, giving \(7\cdot6\cdot4=168\) choices. Every such choice defines a binary invertible linear map, with the dual action on lines. Connectedness makes the unordered bipartition intrinsic. The explicit polarity \(\tau\) exchanges its sides, hence the displayed \(336\) maps exhaust all graph automorphisms. The verifier constructs their pairwise distinct permutations on the \(21\) edges.

**3. Signed Lefschetz enumeration.** Let \(K\) be either complex and \(g\in G\). Because reduced rational homology is concentrated in one even degree, the trace on that homology is exactly the reduced Lefschetz number
\[
\chi_K(g)=-1+\sum_{\substack{\varnothing\ne\sigma\in K\\g\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
The checker enumerates every face fixed setwise by each of the \(336\) edge permutations, computes the sign of the induced permutation of its ordered vertices, and sums the integer contributions. An **independent second evaluation** decomposes each edge permutation into disjoint cycles and selects precisely those collections of cycles whose union is a valid face. For a fixed face containing \(c\) entire edge cycles, its contribution is \((-1)^{c+1}\). Including the empty cycle collection gives the equivalent exact formula
\[
\chi_K(g)=-\sum_{\substack{J\text{ a collection of edge cycles}\\\bigcup J\in K}}(-1)^{|J|}.
\]
The two algorithms agree separately on **all \(336\) elements of \(G\)** for both complexes, producing the eight rows above.

**4. The representation consequence.** Inspection of every character row shows \(\chi_{\mathcal P}(g)=\varepsilon(g)\chi_{\mathcal M}(g)\) for every \(g\in G\). Maschke's theorem and equality of characters of finite-group representations over characteristic zero yield the claimed rational \(G\)-module isomorphism. Averaging the exact traces over \(G\) gives zero invariants for the perfect complex but one for the ordinary complex. Averaging only over \(B\) gives one invariant line in each; the polarity acts by opposite signs on these lines.

## Verification
Run `python3 verify_heawood_equivariant.py` using Python 3's standard library. The program independently enumerates all perfect and ordinary matching faces, builds the two toggle matchings and their **complete** Hasse digraphs, checks the full acyclicity condition, enumerates all \(336\) automorphisms, calculates their orders, and compares the signed-face trace to the independently implemented edge-cycle feasibility trace for both complexes. It verifies the exact character multiplicities and invariants. The machine-readable reference output `heawood_equivariant_check.json` is included; rerun the checker and compare its output to that file. No randomly sampled elements, external solver, or unproved infinite extrapolation is involved.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega introduced and classified perfect-matching complexes for several honeycomb graph families. Their exact definition applies here, but their honeycomb classifications do not determine the Fano incidence graph's symmetry representation. The previously published *Perfect Morse reduction of the Heawood perfect-matching complex* establishes the degree-two sixteen-sphere homotopy type, without an automorphism character. The distinct published result *Full automorphism module of the Heawood matching complex* calculates the ordinary matching complex's degree-four character and module decomposition; it contains no matching subcomplex action and does not imply the duality-sign relation. The present result independently computes both characters in a common labeling, thereby relating two distinct known nonequivariant homotopy types by a previously unestablished \(G\)-module sign twist. Li's equivariant log-concavity theorem concerns graded permutation modules of matchings rather than these homology representations.

In the notation of the preceding ordinary-complex module decomposition \(\mathbf1\oplus T\oplus W\), the theorem equivalently identifies perfect-matching homology with \(\varepsilon\oplus(\varepsilon\otimes T)\oplus(\varepsilon\otimes W)\). This is a rational statement only.

## Limitations
The result is specific to the Heawood graph, and the exact class counts are established by a finite executable certificate rather than a short closed-form character calculation. It does not assert that a topologically natural map realizes the rational module isomorphism or that the integral representation lattices are isomorphic. Indexed searches and comparisons cannot prove universal historical novelty; unindexed equivalent work remains possible. The scientific verification is self-review only, with no independent mathematical audit.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first public 2022-09-06, especially Definition 1 and the honeycomb classification; *Electron. J. Combin.* 30(2) (2023), #P2.45.
2. *Perfect Morse reduction of the Heawood perfect-matching complex*, public research record `0994476b8c0d`, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d/RESULT.md.
3. *Full automorphism module of the Heawood matching complex*, public research record `d7a042784870`, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-full-operatorname-aut-h-module-of-the-heawood-matching-complex--d7a042784870/RESULT.md.
4. S. Li, *Equivariant log-concavity of graph matchings*, arXiv:2202.08828v1, first public 2022-02-17.
5. R. Forman, *Morse theory for cell complexes*, *Adv. Math.* 134 (1998), 90–145.
