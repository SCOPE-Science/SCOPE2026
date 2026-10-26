# Four-tuple orbit counts distinguish all eleven reducts of the generic digraph

## Finding

Let \(\mathcal D\) be the countable generic oriented graph: between two distinct vertices there is one directed edge in either direction, or no edge, but never a two-cycle. Agarwal classified its eleven closed automorphism supergroups (equivalently, its reducts up to interdefinability). For each such group \(G\), let \(a_G(n)\) be the number of \(G\)-orbits on **injective, ordered** \(n\)-tuples, where coordinate places are fixed (not permuted). The following gives \(a_G(n)\) for every integer \(n\ge1\).

Put \(m=\binom n2\), \(q=\binom{n-1}{2}\), and
\[
S_n=\frac1{2^n}\sum_{k=0}^n\binom nk3^{\binom k2+\binom{n-k}{2}},\qquad
R_n=\frac1{2^n}\sum_{k=0}^n\binom nk3^{k(n-k)}.
\]
Here \(S_n\) and \(R_n\) are integers, and \(S_n+R_n\) is even. Name the groups as follows: \(G_E=\operatorname{Aut}(\mathcal D)\); \(G_-\) also permits global reversal of all arcs; \(G_{\mathrm{sw}}\) also permits switching the directions of all arcs crossing a vertex cut; \(G_{\mathrm{sw},-}\) permits both; \(G_{\mathrm{rot}}\) permits cyclic rotation of the three adjacency states at any vertex; and \(G_{\mathrm{rot},-}\) also permits global arc reversal. Let \(G_\Gamma\) be the automorphism group of the random undirected graph obtained by forgetting arc directions, let \(G_{\Gamma,-}\) additionally complement every undirected adjacency, let \(G_{\Gamma,\mathrm{sw}}\) additionally complement the adjacencies crossing arbitrary cuts, and let \(G_{\Gamma,\mathrm{sw},-}\) permit both graph operations. The final group is the full symmetric group \(G_\ast\).

| Group | Exact injective orbit profile \(a_G(n)\) |
|---|---|
| \(G_E\) | \(3^m\) |
| \(G_-\) | \((3^m+1)/2\) |
| \(G_{\mathrm{sw}}\) | \(S_n\) |
| \(G_{\mathrm{sw},-}\) | \((S_n+R_n)/2\) |
| \(G_{\mathrm{rot}}\) | \(3^q\) |
| \(G_{\mathrm{rot},-}\) | \((3^q+1)/2\) |
| \(G_\Gamma\) | \(2^m\) |
| \(G_{\Gamma,-}\) | \(1\) if \(n=1\); otherwise \(2^{m-1}\) |
| \(G_{\Gamma,\mathrm{sw}}\) | \(2^q\) |
| \(G_{\Gamma,\mathrm{sw},-}\) | \(1\) if \(n\le2\); otherwise \(2^{m-n}\) |
| \(G_\ast\) | \(1\) |

**Sharp distinguishing arity.** The eleven values at \(n=4\), in the above order, are respectively
\[
729,\ 365,\ 108,\ 76,\ 27,\ 14,\ 64,\ 32,\ 8,\ 4,\ 1,
\]
and are pairwise distinct. At \(n=3\) there are collisions: \(a_{G_{\mathrm{sw},-}}(3)=a_{G_\Gamma}(3)=8\), \(a_{G_{\mathrm{rot},-}}(3)=a_{G_{\Gamma,\mathrm{sw}}}(3)=2\), and \(a_{G_{\Gamma,\mathrm{sw},-}}(3)=a_{G_\ast}(3)=1\). Hence **four is the smallest tuple arity at which a single orbit count distinguishes all eleven reducts**.

The numbers \(b_G(n)\) of orbits on all ordered tuples, now allowing repeated coordinates, are also completely determined:
\[
b_G(0)=1,\qquad b_G(n)=\sum_{k=1}^n\left\{\begin{matrix}n\\k\end{matrix}\right\}a_G(k)\quad(n\ge1),
\]
where braces denote Stirling numbers of the second kind. In the same group order, the eleven counts on **all ordered four-tuples** are
\[
913,\ 464,\ 177,\ 139,\ 53,\ 34,\ 127,\ 64,\ 28,\ 18,\ 15.
\]
These are also pairwise distinct, while the corresponding three-tuple counts collide. Thus the sharp arity conclusion holds with or without the injectivity requirement.

## Assumptions and scope

The groups are precisely the eleven closed supergroups listed in Agarwal's classification of reducts of the generic digraph [1], and no arbitrary groups outside that lattice are asserted to be classified. The tuple positions are labelled and fixed; counting nonisomorphic unlabelled finite digraphs or counting groups up to abstract isomorphism is a different problem. All formulas hold for every \(n\ge1\), including the low-arity exceptions displayed for graph complementation. The general tuple formulas have no finite-size cutoff.

The two finite-edge states \(\pm1\) in the switching argument mean opposite orientations, while \(0\) represents nonadjacency. In the rotation argument the three states instead form \(\mathbf F_3\), with \(0\) nonadjacency and \(1,2\) the two opposite directions. The distinct encodings are intentional.

## Proof

**1. Finite labelled configurations are the relevant orbit objects.** By homogeneity and the extension property, every assignment of the three possibilities to each pair of \(n\) named distinct vertices occurs as an induced subdigraph, and two such tuples are in the same \(G_E\)-orbit precisely when their assignments agree. Thus there are \(3^m\) basic injective orbits. Agarwal's description of the remaining reduct groups [1, §§2–3] says that their action on such configurations is generated exactly by the indicated global reversal, vertex switching, vertex rotation, and/or the operations on the underlying random graph. It is therefore sufficient to count orbits of the explicit finite edge-state actions below; no assumption that vertex positions may themselves be permuted is used.

**2. Arc reversal.** On the \(m\) ternary edge states, global reversal fixes only the all-nonedge configuration for \(n\ge2\), and at \(n=1\) fixes the unique empty configuration. Burnside's lemma gives \((3^m+1)/2\), valid also at \(n=1\).

**3. Arc switching.** Choose a sign \(s_i\in\{+1,-1\}\) at each labelled vertex. A nonzero oriented edge state between vertices \(i,j\) changes to \(s_is_j\) times that state, while zero remains zero. All \(2^n\) sign vectors may be included in Burnside's average, even though the all-negative vector acts trivially. If exactly \(k\) signs are positive, each of the \(k(n-k)\) crossing pairs must be nonadjacent in a fixed configuration; every other pair may carry any of three states. The fixed-point number is \(3^{\binom k2+\binom{n-k}2}\). This proves the formula for \(S_n\).

Compose a sign action with global arc reversal. Now a crossing pair receives two reversals, so can have any of three states, while a within-sign pair must be nonadjacent. The fixed count is \(3^{k(n-k)}\). Averaging the two cosets gives \((S_n+R_n)/2\), simultaneously proving its integrality.

**4. Arc rotation.** Order the tuple positions \(1<\cdots<n\). Encode each pair \(i<j\) by \(x_{ij}\in\mathbf F_3\), using labels \(0\) for no arc, \(1\) for \(i\to j\), and \(2\) for \(j\to i\). Independently rotating the three adjacency states at the vertices acts as
\[
x_{ij}\longmapsto x_{ij}+t_i-t_j\pmod3\qquad(t_i\in\mathbf F_3).
\]
The kernel of the potential map is the one-dimensional space of constant potentials because every pair is present in the complete array of possible adjacency slots. Thus the image has dimension \(n-1\), and its translation action on \(\mathbf F_3^m\) is free. The quotient has \(3^{m-(n-1)}=3^q\) classes. A complete invariant is the collection of triangular sums \(x_{1i}+x_{ij}-x_{1j}\) for \(2\le i<j\le n\), after sign conventions consistent with \(x_{ij}\). These \(q\) values can be independently prescribed.

Global arc reversal sends \(x_{ij}\) to \(-x_{ij}\) and descends to negation on the quotient vector space \(\mathbf F_3^q\). Over an odd-characteristic field, negation has exactly one fixed class, the zero class. Another Burnside average yields \((3^q+1)/2\).

**5. Underlying-graph reducts.** Forgetting directions leaves one binary adjacency bit per pair, hence \(2^m\) labelled graphs. Complementation fixes no bit assignment if \(m>0\), giving \(2^{m-1}\) when \(n\ge2\); at \(n=1\) it is the identity. Vertex-cut switching adds the coboundary \(u_i+u_j\in\mathbf F_2\) to each binary adjacency bit. Its rank is \(n-1\), producing exactly \(2^{m-n+1}=2^q\) orbits. For \(n\ge3\), the all-one edge vector for global complementation does not lie in this coboundary space: summing its labels around any triangle gives \(1\), while the sum of every coboundary around a triangle is \(0\). It therefore doubles the translation subgroup, leaving \(2^{m-n}\) orbits. At \(n=2\), complementation is already a vertex switch; at \(n=1\), both operations act trivially. The full symmetric group is transitive on injective \(n\)-tuples.

**6. Four-point separation and repetitions.** Substituting \(n=4\) into the proven formulas gives the eleven distinct values stated above. Substituting \(n=3\) yields the three explicit collisions, so no smaller single arity distinguishes them. For tuples with equality, the kernel partition of the map from coordinate positions to distinct vertices is invariant under each group. For a fixed partition into \(k\) blocks, ordered by first occurrence, the induced orbit problem is exactly the injective \(k\)-tuple problem. Summing over the \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) partitions proves the Stirling transform, and the numerical evaluations show the same sharp four-arity threshold for unrestricted tuples.

## Verification

Run `python verify_orbit_profiles.py` using an ordinary Python 3 interpreter. It constructs all labelled three-state or two-state pair configurations through \(n=5\), independently generates orbits by the appropriate elementary state transformations, and compares the resulting orbit numbers with the formulas. It explicitly tests all eleven groups and the exceptional small values. The recorded output is `verification_output.txt` and terminates with `ALL_DIRECT_ORBITS_PASS`. This finite enumeration checks the low-arity sharpness claim and formula instances; the algebraic and Burnside arguments above establish the unrestricted result for all \(n\).

## Relationship to prior work

Agarwal [1] establishes the eleven-group reduct lattice and the finite switching/rotation descriptions needed here, but the specific closed orbit-count profiles and the arity-four separation statement are not asserted to be results of that paper. The result here applies enumeration and finite-field quotient methods to that established classification. McKay and Schweitzer [2] analyze vertex switching from the separate perspective of reconstruction, not the complete orbit profiles of the reduct lattice. Related orbit-profile investigations for reducts of random bipartite graphs and random partial orders concern different structures and are not implications of these eleven formulas [3,4]. The standard Burnside principle and cut/cycle-space identities are established tools rather than novel ingredients.

## Limitations

The distinguishing statement concerns orbit **numbers**, not a complete invariants-based logical interpretation of every reduct. It relies on Agarwal's exhaustive classification; it does not independently reprove that classification or address nonclosed supergroups. The claim is not an unlabeled enumeration result. The literature comparisons do not eliminate the possibility that these elementary finite orbit calculations appeared previously in specialized, unpublished, or poorly indexed discussions. Independent validation has not been performed.

## References

[1] L. Agarwal, *Reducts of the Generic Digraph*, arXiv:1411.4820 (first submitted 2014-11-18); subsequently *Annals of Pure and Applied Logic* **167** (2016), 370–391. https://arxiv.org/abs/1411.4820 . Accepted manuscript: https://eprints.whiterose.ac.uk/id/eprint/92912/1/Reducts_of_the_Generic_Digraph.pdf .

[2] B. D. McKay and P. Schweitzer, *Switching Reconstruction of Digraphs*, arXiv:1308.0675 (2013); *Journal of Graph Theory* **76** (2014), 279–296. https://arxiv.org/abs/1308.0675 .

[3] *Exact ordered-tuple orbit profiles of the side-preserving random bipartite reducts*, published research record, 2026-09-30. https://github.com/Resultary/2026/tree/main/2026/9/30/SCOPE-exact-ordered-tuple-orbit-profiles-of-the-side-preserving-random--f8b9342567cf .

[4] *Exact ordered-tuple orbit profiles of the five random-poset reduct groups*, published research record, 2026-09-30. https://github.com/Resultary/2026/tree/main/2026/9/30/SCOPE-exact-ordered-tuple-orbit-profiles-of-the-five-random-poset-redu--635ca0d5aff9 .
