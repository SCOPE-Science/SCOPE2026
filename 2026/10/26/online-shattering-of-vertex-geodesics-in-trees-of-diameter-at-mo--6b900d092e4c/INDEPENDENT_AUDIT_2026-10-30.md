# Independent mathematical audit

## correctness

PASS

The finite version-space recurrence Ldim(F)=max_x 1+min(Ldim(F_{x,0}),Ldim(F_{x,1})) for nonempty branches is used, not a VC-dimension substitution. On a diameter-four tree decomposed into center r, children c_i and their leaf clusters, paths containing a fixed leaf have Ldim<=2 by examining other leaves, its own child, other children and r; paths containing a fixed child c_i have rank<=3; paths avoiding the root have rank<=3. Thus each query of the unrestricted path class has a branch rank<=3, establishing Ldim<=4. If center degree is two, root-containing paths have rank<=2, child-negative paths have rank<=2, and leaf-positive paths rank<=2, giving Ldim<=3. The diameter<=3 cases follow analogous leaf/star reductions. Lower bounds use geodesically embedded path witnesses for D<=3 and D=4 with center degree two, plus the explicit six-vertex branching center-degree-three tree. Its depth-four complete mistake tree is stored in tree_geodesic_certificates.json; every one of its sixteen endpoint-pair histories was independently replayed against actual tree paths, with all five lower-bound certificates verified. Independent recurrence calculations also reproduced 51 canonical diameter-four shapes through 10 vertices; the frozen source verifier had tested 128 through 12. Only the written structural induction proves the unbounded family.

## originality

PASS

Ghazi–Golowich–Kumar–Manurangsi 2020/2021 prove generic closure bounds for Littlestone dimension under Boolean aggregation, with no exact diameter-four vertex-path family. Abraham–Delling–Fiat–Goldberg–Werneck prove VCdim<=2 for unique-shortest-path systems, which matches the static part but does not imply adaptive Ldim: the latter can be 3 or 4 with VCdim 2. Paths on chains and rooted descendant-cone concepts are narrower or different classes. The branching-sensitive center-degree threshold and exact small-diameter Ldim were not found as implications of inspected primary statements.

## value

PASS

This is an exact classification of online path-membership learning in the first four tree diameter layers, with a structural one-bit branching threshold and a six-vertex minimal witness. It answers a natural adaptive-versus-static contrast: Ldim can jump while known VCdim remains two, and the optimal realizable deterministic mistake bound stays <=4 regardless of tree order. This is a meaningful complete finite-diameter family classification, not a small enumerative curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
