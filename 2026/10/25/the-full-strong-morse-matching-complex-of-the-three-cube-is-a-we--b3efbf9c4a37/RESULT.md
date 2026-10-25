# The full strong Morse matching complex of the three-cube is a wedge of 31 two-spheres

## Finding
For the three-dimensional cube graph \(Q_3\), regarded as a one-dimensional simplicial complex with eight binary-string vertices, the **full** strong discrete Morse matching complex satisfies
\[\mathcal{SM}(Q_3)\simeq\bigvee^{31}S^2.\]
The complex has 24 vertices and face vector \((f_0,f_1,f_2,f_3)=(24,168,392,216)\). All 216 three-simplices admit elementary collapses, yielding a two-dimensional simplicial complex with 24 vertices, 168 edges, and 176 triangles. This remaining complex is simply connected and has reduced integral second homology \(\mathbb{Z}^{31}\).

## Assumptions and scope
Let \(Q_3\) have vertex set \(\{0,1\}^3\), with adjacent bitstrings differing in exactly one coordinate. For a total order on its eight vertices, the descending link of a vertex is the set of its earlier graph neighbors. Since \(Q_3\) has no triangles, this descending link is a simplicial cone precisely if it consists of exactly one earlier neighbor. Such a vertex contributes the strong discrete Morse pair consisting of that vertex and the edge to its unique earlier neighbor; otherwise it contributes no pair. For graphs, no higher-dimensional simplex pairs occur. Following Definition 4.2 of Knudson–Owens-White, \(\mathcal{SM}(Q_3)\) is the **downward closure** of all such complete gradient sets from all vertex orders. It is not the ordinary Morse complex, the ordinary graph matching complex, or merely the pure strong subcomplex.

## Proof
**Exact construction.** Label the eight graph vertices by integers from 0 to 7 with binary expansion. Index the 24 ordered incidences \((v,u)\) satisfying \({\rm popcount}(v\mathbin{\mathrm{xor}}u)=1\). There are \(8!=40320\) total vertex orders, and for each order the descending-link rule above selects a deterministic subset of the incidence labels. Exhaustive integer-bitmask generation gives 584 distinct nonempty gradients. Its inclusion-maximal subsets are exactly 216 four-element sets. Enumerating their downward closure gives 24 singleton faces, 168 two-element faces, 392 three-element faces, and 216 four-element faces, with Euler characteristic
\[\chi=24-168+392-216=32.\]
The standalone script verifies these assertions without any random sampling.

**Elementary collapses.** Build the incidence map from every triangular face of a maximal tetrahedron to its containing tetrahedra. Repeatedly choose lexicographically the smallest triangular face contained in exactly one remaining tetrahedron, remove that free triangle and its unique tetrahedron, and update the incidence map. The exact calculation succeeds 216 times, eliminating every tetrahedron. Each step is an elementary simplicial collapse: the triangle lies in exactly one maximal coface, so deleting the free pair preserves homotopy type. The resulting subcomplex has 24 vertices, 168 edges, and 176 triangles; no higher-dimensional simplices remain.

**Fundamental group.** For that two-complex, choose the deterministic breadth-first spanning tree rooted at incidence vertex 0, with lexicographically ordered neighbors. The tree has 23 edges. A standard cellular presentation of its fundamental group has one generator for each of the 145 edges outside this tree and a relation for each triangular two-cell. Repeatedly choose a triangle with two edges already known to represent the identity (tree edges or edges eliminated by previous relations); its triangular attaching relation then forces the third edge to represent the identity. The script records 145 such triangular eliminations and verifies that every edge is eliminated. Hence the fundamental group is trivial. This is stronger than the vanishing of first homology.

**Homotopy conclusion.** Since the remaining complex is connected, simply connected, and two-dimensional, its second cellular homology is a free abelian group, and Euler characteristic 32 gives \(H_2\cong\mathbb{Z}^{31}\). Hurewicz supplies 31 spherical representatives, giving a map from \(\bigvee^{31} S^2\) inducing an integral homology isomorphism. The homology Whitehead theorem for simply connected CW complexes makes this a homotopy equivalence. The elementary collapses transfer it to \(\mathcal{SM}(Q_3)\).

## Verification
Run `python3 verify_cube_strong.py` under Python 3.10 or later. The standalone standard-library script exhausts every vertex ordering, checks the 216 free triangle–tetrahedron pairs, constructs the spanning tree and 145 fundamental-group-eliminating triangle relations, and independently computes mod-two boundary ranks \((23,145,216)\) in dimensions one through three. The rank check yields \(\widetilde\beta_2=31\) and no other reduced mod-two homology. The proof of simple connectivity and the two-dimensional reduction, rather than the mod-two calculation, establish the claimed integral homotopy type. Every set used in the proof is reconstructed from the explicit binary-label model.

## Relationship to prior work
Knudson and Owens–White introduce the full strong matching complex and compute it for paths, stars, simplices and their boundaries, as well as pure-cycle cases; they do not give the present cube calculation. Fernández develops the underlying strong discrete Morse construction. Existing computations of the **ordinary** discrete Morse complex of the cube (with homology in degrees five and six), and of the ordinary cube edge-matching complex (four two-spheres), concern distinct constructions: the former allows all acyclic face-poset matchings and the latter uses unoriented disjoint graph edges. Neither statement determines the homotopy type here.

## Limitations
This result concerns only the eight-vertex three-dimensional cube and the full strong matching complex. No extension to higher cubes or to other graph families is asserted. The computer calculation is exhaustive and its derivation is described above; its correctness depends on the stated combinatorial interpretation of descending domination, and the published sources cited below provide that definition. Prior-literature searches cannot establish absolute absence of an equivalent derivation.

## References
1. Kevin P. Knudson and Abigail Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first public September 6, 2026. https://arxiv.org/html/2609.06844v1 (especially §§3–4, 6–10).
2. Ximena Fernández, *Strong discrete Morse theory*, arXiv:2504.15729v1, first public April 22, 2025. https://arxiv.org/html/2504.15729v1.
