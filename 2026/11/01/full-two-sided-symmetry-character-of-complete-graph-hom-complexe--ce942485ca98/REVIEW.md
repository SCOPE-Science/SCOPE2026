# Scientific review: complete-graph Hom-complex symmetry

## Correctness — PASS

The final claim concerns the rational top homology of \(\operatorname{Hom}(K_m,K_n)\) for every \(2\le m<n\) and every simultaneous source/target permutation. Its proof uses the published complete-graph wedge theorem to concentrate homology in degree \(n-m\), then derives an exact signed fixed-cell formula for *arbitrary* group elements. The essential orientation determinant is obtained by subtracting the blockwise constant summand of the permutation module on used colors. Inclusion–exclusion enforces nonempty blocks, with an explicit divisibility rule for cycles of the source and target permutations. The Hopf trace formula removes exactly one connected-component trace. Ordinary and signed cycle-index evaluations give the two quotient homology statements, with no reliance on extrapolating numerical experiments. The hypotheses, the strict \(n>m\) boundary, the rational coefficients, and the ordinary-orbit-space interpretation are all explicit.

The supplied standalone program enumerates exact signed cellular boundaries and verifies their compositions over the integers for four nontrivial cases. Its independent signed fixed-cell traces match the closed formula on all 3,792 actions of the joint groups. Six full color-symmetry averages, including two additional larger cases, match the invariant dimensions. These checks corroborate the algebra but are not substituted for the universal proof.

## Originality — PASS, subject to bibliographic residual risk

The closest **equivalent underlying object** is the ordered nonempty disjoint-subset poset \(\widehat{\mathcal B}_{n,m}^{o}\) in Babson–Kozlov (1997). Its face-poset identification and its ordinary homotopy theorem are acknowledged without claiming them as new. Its unordered-block quotient concerns the **source** \(S_m\)-action rather than the separately calculated quotient by even versus all **target-color** permutations. Babson–Kozlov (2003) also proves the wedge-of-spheres theorem and enumerates the Betti number. Neither inspected text states a character formula for every \((\sigma,\pi)\in S_m\times S_n\), nor the \(A_n\) quotient multiplicities. Pfeifle's geometric description and Dochtermann's graph-homotopy functoriality likewise do not imply the explicit joint character in their inspected material. Thus the claimed novelty is carefully confined to the simultaneous character and its target-color quotient consequences; known nonequivariant statements are excluded. Equivalent unindexed work, especially in older deleted-product literature, remains a real residual priority risk.

## Value — PASS

The complete-graph Hom complexes are basic and historically important in topological combinatorics and graph-coloring obstructions. Their ordinary sphere counts do not specify the source/target symmetry representation. The new formula determines every joint group element's character for two independent symmetric-group actions and proves a sharp qualitative distinction between full and alternating color-quotients: one is rationally acyclic whereas the other has \(\binom{n-2}{m-2}\) independent top-dimensional classes. The result therefore has natural meaning independent of its verification code, does not depend on arbitrary isolated numerical parameters, and applies to a full two-parameter family.

## Limitations and literature

Only rational homology representations and ordinary geometric quotients are classified. Integral representation lattices, quotient homotopy types, Borel-equivariant groups and arbitrary graph pairs are not determined. The prior underlying poset, ordinary wedge theorem and nonequivariant Betti numbers were already established. The key primary references are Babson–Kozlov (1997, arXiv:math/9704227, Definition 6.1 and Theorem 6.2) and Babson–Kozlov (2003, arXiv:math/0310056, Definition 1.2 and Propositions 4.5–4.6). Pfeifle (arXiv:math/0512529) and Dochtermann (DOI:10.1016/j.ejc.2008.04.009) were also compared. This self-review is not independent peer review and does not establish publication priority definitively.

Self-review: passed. Independent audit: not yet performed.
