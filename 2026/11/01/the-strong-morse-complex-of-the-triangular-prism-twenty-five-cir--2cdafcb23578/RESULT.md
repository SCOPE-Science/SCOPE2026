# The strong Morse complex of the triangular prism: twenty-five circles and a prism-symmetry character

## Finding
Let \(P\) be the **unfilled one-dimensional** triangular-prism graph \(C_3\square K_2\), with vertices \(0,1,2\) on the upper triangle, \(3,4,5\) on the lower triangle, and edges
\[
01,12,20,34,45,53,03,14,25.
\]
Let \(X=\mathcal{SM}(P)\) be the **full**, rather than pure, complex of strong discrete Morse matchings in the sense of Knudson and Owens–White. The graph is regarded as a one-dimensional simplicial complex: the two triangular cycles are **not** filled by two-simplices.

Then \(X\) simplicially collapses to a connected graph having \(18\) vertices and \(42\) edges. In particular,
\[
\boxed{|X|\simeq\bigvee^{25}S^1,\qquad H_1(X;\mathbb Z)\cong\mathbb Z^{25}.}
\]
All reduced integral homology groups other than degree one vanish, and \(\pi_1(X)\) is free of rank \(25\).

The full graph-automorphism group \(G\cong S_3\times C_2\) permutes the three positions and independently swaps the two triangle layers. Write \(\varepsilon\) for the one-dimensional rational character \((\pi,s)\mapsto\operatorname{sgn}(\pi)\), trivial on the layer swap. There is an isomorphism of rational \(G\)-representations
\[
\boxed{H_1(X;\mathbb Q)\cong\mathbb Q[G]^{\oplus2}\oplus\mathbb Q_\varepsilon.}
\]
Equivalently, the layer-exchange involution has rational \(+1\) and \(-1\) eigenspaces of dimensions \(13\) and \(12\), respectively.

## Assumptions and scope
An oriented arc \(u\to v\) represents the primitive Morse pair consisting of vertex \(u\) and its incident graph edge \(\{u,v\}\). The \(18\) arcs are the vertices of \(X\). A strong gradient is obtained from a total ordering of the six original graph vertices. At the introduction of \(u\), its descending link is the discrete set of neighbors that precede \(u\). Since the input is **one-dimensional**, this link is a simplicial cone exactly when it contains one vertex \(v\); then the strong gradient contains \(u\to v\). A vertex with zero or at least two earlier neighbors contributes no pair. The faces of \(X\) are exactly the subsets of all strong gradients so obtained; this downward closure is essential because an arbitrary subset of a strong gradient need not itself be a strong gradient.

No two-dimensional simplex is filled in \(P\), no general graph with cycles is classified here, and the rational module statement does not assert an integral direct-sum decomposition of the \(G\)-lattice.

## Proof
**1. Exhaustive facet classification with three symmetry orbits.** Enumerate the \(6!=720\) total orders \(\tau=(v_0,\ldots,v_5)\). Starting from an empty set \(B\), process vertices in order and insert the single arc \(v_j\to w\) precisely when \(w\) is the unique neighbor of \(v_j\) among \(v_0,\ldots,v_{j-1}\). Take the downward closure of the resulting arc sets. Every step is dictated by the definition above, so this procedure generates all and only the simplices of \(X\).

There are \(85\) distinct order-generated arc sets, and exactly \(36\) inclusion-maximal ones. The maximal simplices decompose into the following \(G\)-orbits; an entry lists one representative as a set of arcs and the size of its orbit:

| Cardinality | Representative | Orbit size |
|---|---|---:|
| \(2\) | \(\{1\to2,\ 3\to0\}\) | \(12\) |
| \(3\) | \(\{0\to3,\ 2\to0,\ 3\to4\}\) | \(12\) |
| \(3\) | \(\{1\to4,\ 2\to1,\ 3\to4\}\) | \(12\) |

The exact finite-order enumeration and a *second reconstruction* of all facets from these three symmetry orbits are implemented independently in `verify.py`. Equality of the two sets is asserted, not inferred from matching totals. The resulting counts of nonempty simplices by dimension are
\[
(f_0,f_1,f_2)=(18,66,24),
\]
and no higher-dimensional simplices exist.

**2. Explicit simplicial collapses.** In the first three-arc orbit, the edge \(\{2\to0,3\to4\}\) belongs to exactly one triangular face. In the second three-arc orbit, the edge \(\{1\to4,3\to4\}\) also belongs to exactly one triangular face. Each orbit of triangular facets has trivial stabilizer, so transporting the indicated free edge through the twelve symmetries gives **one distinct free edge for each of the twenty-four triangles**. (Distinctness follows because an edge in exactly one triangle cannot serve two different triangles.) Thus twenty-four elementary \((1,2)\)-collapses can be made, in any order, removing all triangles and exactly twenty-four edges. The remaining graph has \(18\) vertices and \(66-24=42\) edges.

An exact breadth-first search over the remaining graph reaches all eighteen vertices; `verify.py` constructs this graph from the verified face set and checks the free-face condition at each collapse. Its connectedness and the graph-spine formula give
\[
\operatorname{rank}H_1(X;\mathbb Z)=42-18+1=25.
\]
A connected finite graph is a wedge of that many circles. This is an **integral homotopy conclusion**, not merely a field-Betti calculation.

**3. Automorphism character.** For \(g=(\pi,s)\in S_3\times C_2\), its action on arcs is induced by its permutation of the original prism vertices. For each simplicial chain group \(C_j(X;\mathbb Q)\), a \(g\)-fixed simplex contributes the sign of the induced permutation of its ordered arc vertices. Exhaustive signed fixed-face enumeration gives the following exact chain traces (the row labeled transposition or three-cycle is independent of the chosen element within that class):

| \(S_3\) type | Layer swap \(s\) | \(\operatorname{tr}C_0\) | \(\operatorname{tr}C_1\) | \(\operatorname{tr}C_2\) |
|---|---:|---:|---:|---:|
| identity | \(0\) | \(18\) | \(66\) | \(24\) |
| transposition | \(0\) | \(2\) | \(0\) | \(0\) |
| three-cycle | \(0\) | \(0\) | \(0\) | \(0\) |
| identity | \(1\) | \(0\) | \(0\) | \(0\) |
| transposition | \(1\) | \(0\) | \(-2\) | \(0\) |
| three-cycle | \(1\) | \(0\) | \(0\) | \(0\) |

Since \(X\) is connected and has no reduced homology outside degree one, the Lefschetz alternating-trace identity yields
\[
\operatorname{tr}(g\mid H_1)=1-\operatorname{tr}(g\mid C_0)+\operatorname{tr}(g\mid C_1)-\operatorname{tr}(g\mid C_2)
=24\,\mathbf1_{g=e}+\operatorname{sgn}(\pi).
\]
The regular character of the order-twelve group \(G\) is \(12\) at the identity and zero elsewhere. Over \(\mathbb Q\), representations of finite groups are semisimple, so equality of rational characters gives \(H_1(X;\mathbb Q)\cong2\mathbb Q[G]\oplus\mathbb Q_\varepsilon\). The trace of the layer swap is \(1\), and its \(\pm1\) multiplicities are \((25\pm1)/2=(13,12)\).

## Verification
Run `python3 verify.py` beside this file. The code uses only the Python standard library; it enumerates all \(720\) orders, independently regenerates the maximal facets as three automorphism orbits, validates all face counts, checks the twenty-four actual simplicial free-face collapses and connectivity, and computes signed fixed-face chain traces for all twelve automorphisms. It asserts the precise wedge rank and complete rational character. The terminal output consists of three `VERIFY_OK` lines. All loops are over finite explicit sets; no randomized search, numerical approximation, or external package is involved.

## Relationship to prior work
Knudson and Owens–White introduced the full and pure strong discrete-Morse matching complexes, provided their construction from vertex filtrations, and classified them for paths, cycles (partially for the full complex), stars, and simplices and their boundaries [1]. Their primary result also establishes that these complexes differ from ordinary discrete-Morse matching complexes. The triangular prism graph and its full strong-complex homotopy and symmetry representation do not appear among their stated classifications.

A published indexed finding [3] concerns the **ordinary** Morse complex \(\mathcal M(P)\) for the same prism, whose reduced degree-four mod-two Betti number is \(64\). This does not imply our theorem for the proper subcomplex \(\mathcal{SM}(P)\): the face rule and resulting topology are different. The present calculation shows how sharply the strict strong-gradient condition can change topology on a minimal three-regular prism graph. Fernández's strong discrete Morse theory [2] provides the underlying strong-gradient construction, not this graph-complex calculation.

## Limitations
The theorem is exact for the one-dimensional triangular-prism graph alone; it is not a classification of all prism graphs, polyhedral graph complexes, or pure strong complexes. The rational representation is not asserted to split integrally, and no homotopy-equivariant wedge decomposition is claimed. The finite proof is complete for this graph, but independent validation and an exhaustive survey of unindexed literature have not been performed; mathematically equivalent prior work remains a possible originality risk.

## References
1. Kevin P. Knudson and Abigail Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, publicly submitted 2026-09-06; Definition 4.2 and Sections 3–4, 6–10. https://arxiv.org/abs/2609.06844
2. Ximena L. Fernández, *Strong discrete Morse theory*, arXiv:2504.15729v1, first publicly submitted 2025-04-22. https://arxiv.org/abs/2504.15729
3. *Mod-\(2\) homology of the triangular-prism Morse complex*, public mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-triangular-prism-morse-complex--4af8059de6d1 .
