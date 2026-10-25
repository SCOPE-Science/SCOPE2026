# The full \(S_4\times C_2\) symmetry module of cube matching homology

## Finding
Let \(Q_3\) be the three-dimensional cube graph and \(X=\mathcal M(Q_3)\) its **ordinary matching complex**. Its full graph automorphism group is \(G\cong S_4\times C_2\). Let \(\mathcal D\) be the four unordered antipodal vertex pairs of \(Q_3\), and let \(\pi_g\in S_4\) be the induced permutation of \(\mathcal D\). Each automorphism can be written uniquely as \(g_{\sigma,b}:v\mapsto\sigma v+b\), for \(\sigma\in S_3\) and \(b\in\mathbb F_2^3\). Define the character \(\varepsilon(g_{\sigma,b})=(-1)^{|b|}\), where \(|b|\) is the Hamming weight of \(b\).

As a rational representation of **all** \(48\) cube automorphisms,
\[
\boxed{\widetilde H_2(X;\mathbb Q)\cong
\mathbb Q_{\varepsilon}\oplus
\operatorname{Inf}_{S_4}^{G} S^{(2,1,1)},}
\]
where \(S^{(2,1,1)}\) is the three-dimensional irreducible rational Specht module and inflation uses the action on \(\mathcal D\). Every other reduced rational homology group is zero. Equivalently, for every \(g\in G\),
\[
\boxed{\operatorname{tr}(g\mid\widetilde H_2(X;\mathbb Q))=
\varepsilon(g)+\operatorname{sgn}(\pi_g)
\bigl(\#\operatorname{Fix}_{\mathcal D}(g)-1\bigr).}
\]
The antipodal involution has trace \(2\), hence its \(+1\) and \(-1\) eigenspaces have dimensions \(3\) and \(1\). The full orbit space \(X/G\) is rationally acyclic; the quotient by the index-two even-coordinate-flip subgroup has exactly one reduced rational degree-two homology class.

## Assumptions and scope
The cube vertices are binary triples. Two triples form a graph edge if and only if they differ in exactly one coordinate. A simplex of \(X\) is a set of pairwise vertex-disjoint **graph edges**, not a set of disjoint cube faces or a discrete Morse vector field. All oriented simplicial chains use the lexicographic order of the twelve undirected cube edges. Statements about equivariant homology are over \(\mathbb Q\), not integral module classifications.

The affine signed-coordinate maps form all automorphisms: an automorphism is determined by the image of \((0,0,0)\) and a permutation of its three neighbors. Each such map preserves adjacency, giving exactly \(8\cdot6=48\) elements. Its action on the four body diagonals has kernel consisting of the identity and central inversion. Central inversion has \(\varepsilon=-1\), so \(g\mapsto(\pi_g,\varepsilon(g))\) identifies \(G\) with \(S_4\times C_2\). The index-two subgroup in the quotient statement is \(\ker\varepsilon\), not necessarily the orientation-preserving Euclidean symmetry subgroup.

## Proof
**1. Exact homology concentration.** Enumerating the matching subsets of the twelve cube edges gives the augmented face counts \((1,12,42,44,9)\) in cardinalities \(0,1,2,3,4\). The ranks of the augmented simplicial boundary maps over \(\mathbb F_2\), starting with \(\partial_0\), are \((1,11,31,9)\). The included verifier reconstructs these matrices directly and checks all integer \(\partial^2=0\) cancellations.

A matrix over \(\mathbb Z\) has rational rank at least its rank modulo two. On the other hand, \(\partial_0\) has one row, \(\partial_0\partial_1=0\), \(\partial_1\partial_2=0\), and \(\partial_3\) has nine columns. In succession, these constraints give the rational rank upper bounds \((1,11,31,9)\) as well. All four rational ranks therefore equal the displayed values. Subtracting boundary and coboundary ranks from each chain dimension yields reduced rational Betti numbers \((0,0,4,0)\) in degrees \(0,1,2,3\). The empty-simplex contribution is used only to compute reduced homology.

**2. Full signed Lefschetz computation.** For a cube automorphism \(g\), a matching \(s\) of \(r\) edges contributes to the trace on oriented \((r-1)\)-chains only when \(g(s)=s\). In that case its contribution is the sign of the permutation induced by \(g\) on the \(r\) **ordered graph edges**. Because the only nonzero reduced rational homology lies in degree two, the equivariant Euler–Poincaré identity gives
\[
\operatorname{tr}(g\mid\widetilde H_2(X;\mathbb Q))
=\sum_{s\in X}(-1)^{|s|-1}
\mathbf1_{g(s)=s}\operatorname{sgn}(g\mid s),
\]
where the empty matching contributes \(-1\). There are only \(108\) matching faces including the empty face. Enumerating all of them and all \(48\) affine automorphisms gives the following complete character table, with each row indexed by the cycle type \(\lambda\) of \(\pi_g\). The middle column is the class size for **each** specified sign of \(\varepsilon\).

| \(\lambda\) | Size for each \(\varepsilon\) | Trace if \(\varepsilon=+1\) | Trace if \(\varepsilon=-1\) |
| --- | ---: | ---: | ---: |
| \((1,1,1,1)\) | 1 | 4 | 2 |
| \((2,1,1)\) | 6 | 0 | -2 |
| \((2,2)\) | 3 | 0 | -2 |
| \((3,1)\) | 8 | 1 | -1 |
| \((4)\) | 6 | 2 | 0 |

Every one of these values equals \(\varepsilon(g)+\operatorname{sgn}(\pi_g)(\#\operatorname{Fix}_{\mathcal D}(g)-1)\). This is a **complete** list of all ten conjugacy classes, rather than a sample of group elements.

**3. Irreducible identification.** The natural permutation representation of \(S_4\) on four body diagonals splits into the trivial line and the three-dimensional standard module \(S^{(3,1)}\). Tensoring that standard module with the sign character gives \(S^{(2,1,1)}\), whose character is \(\operatorname{sgn}(\pi)(\#\operatorname{Fix}(\pi)-1)\). The remaining one-dimensional character is precisely \(\varepsilon\). Thus the observed character is the displayed direct sum. Semisimplicity of rational representations of finite groups makes equality of characters an isomorphism. The checker also verifies all ten irreducible inner products independently.

**4. Quotients.** Taking the average of the character over all \(48\) automorphisms gives zero; over the \(24\)-element kernel of \(\varepsilon\) it gives one. For a finite simplicial group action, barycentric subdivision makes the action without simplex inversions; rational chains of the quotient identify with group coinvariants, which are isomorphic to invariants in characteristic zero. Consequently the two orbit spaces have the stated rational homology. No freeness of the action is assumed.

## Verification
Execute `python3 verify_cube_matching.py` using Python 3 and only its standard library. It generates the cube edge set and all matching faces, checks the augmented boundary ranks over \(\mathbb F_2\), verifies signed boundary cancellation, checks that every one of the \(48\) automorphisms preserves the complex, evaluates all \(48\) signed Lefschetz traces, tests their closed formula, and computes all ten irreducible-character inner products. The expected final marker is `ALL_CUBE_MATCHING_SYMMETRY_CHECKS_PASSED`.

## Relationship to prior work
Matsushita's planar small-grid matching-complex theorem concerns two-row rectangular grids, not the three-direction cube. Donovan and Scoville compute matching-complex homotopy types for paths, cycles and Dutch windmills, not this full cube action. A publicly accessible cube-matching calculation (mathematical record `79d70fe8b67e`) already establishes \(\mathcal M(Q_3)\simeq\bigvee^4 S^2\); its homotopy classification is **not** claimed here. That nonequivariant result fixes the dimension four, not the displayed character or its quotient consequences. The published equivariant matching calculation for the **octahedral graph** (record `c700eceb52bb`) involves a different graph and an eleven-dimensional first homology module. An equivariant three-cut computation for the cube (record `7e5f41a11a8d`) involves a different simplicial complex and homological degrees, and does not imply this ordinary matching-complex representation.

## Limitations
The calculation classifies the rational homology module only for the three-dimensional cube. It does not classify the integral \(\mathbb Z[G]\)-lattice, the higher-cube matching complexes, or the equivariant homotopy type. The finite computation is exhaustive for this complex but is not an infinite-family argument. Priority is assessed relative to the cited full texts, the accessible mathematical record and targeted searches; an unindexed equivalent representation calculation remains possible.

## References
1. T. Matsushita, *Matching complexes of small grids*, arXiv:1812.11000, first submitted 2018-12-28, sections 1–4.
2. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, first submitted 2022-07-27.
3. *The cube matching complex is \(\bigvee^4 S^2\)*, public mathematical result record `79d70fe8b67e` (2026).
4. *The full octahedral symmetry representation of the matching complex*, public mathematical result record `c700eceb52bb` (2026).
5. *Automorphism-module structure of the cube three-cut complex*, public mathematical result record `7e5f41a11a8d` (2026).
