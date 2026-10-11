# Scientific review

## Correctness — PASS
For every \(m,n\ge3\), all open-neighborhood faces are in the union of the \(mn\) center simplices. A mixed face of at least three vertices identifies its center uniquely, so its containing simplex intersects the complete-edge, row/column boundary core along two disjoint simplices connected by the complete bipartite set of cross edges. This intersection is a graph-equivalent wedge of \((m-1)(n-1)-1\) circles. Cofiber and relative long exact sequence arguments yield the two-sphere quotient and integral homology isomorphism above degree two. Oriented boundary cycles prove the \(S_m\times S_n\) signs. The executable package independently checks eight small boards, face uniqueness, relative attaching structures, mod-two boundaries, and signed cycle actions; finite tests do not replace the uniform proof.

## Originality — PASS, with remaining uncertainty
The main same-object comparison is the **closed** neighborhood complex of rook graphs in Matsushita (2025), Example 3.5, which is a wedge of two-spheres. The present result concerns the **open** neighborhood complex and exhibits high-dimensional homology, so the closed result cannot imply it. Matsushita (2012/2017) analyzes open-neighborhood fundamental groups, not these higher homology modules; Shukla (2018) treats other graph classes; Antolín Camarena–Carnero Bravo (2023) treat categorical-product independence complexes used for the closed case. Searches for the graph aliases, row/column boundary cycles, equivariant lattice modules, and quotient decomposition, found no covering statement. A terminologically different or unindexed older open-neighborhood calculation remains a real risk, and search absence is not proof of uniqueness.

## Value — PASS
The canonical rook-graph family has two independent size parameters and a natural \(S_m\times S_n\) symmetry. The result explains exactly why every mixed high-dimensional face contributes only two-dimensional relative topology, making all higher integral homology computable in closed form, free, and symmetry-sensitive. It is a structural all-parameter theorem, not an arbitrary finite-sample rank, and clarifies why conclusions for closed neighborhoods cannot be transferred to open ones.

## Limitations
The first two homology groups, full homotopy type, and an equivariant cofiber splitting are not claimed; one prior exact-graph comparison concerns a distinct definition. Independent evaluation remains outstanding.

Same-model review: passed. Independent audit: not yet performed.
