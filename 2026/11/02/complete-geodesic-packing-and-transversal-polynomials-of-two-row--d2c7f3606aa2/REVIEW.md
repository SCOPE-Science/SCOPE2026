# Review of complete geodesic-packing and transversal polynomials

## Correctness — PASS

The decisive structural observation is that every maximal geodesic in \(K_2\square K_n\) has a unique complete two-vertex column and one further cell from another column. Vertex-disjoint packing is therefore equivalent, in both directions, to choosing \(k\) complete columns, \(k\) distinct cells outside them and a bijection. This proves every packing coefficient, the exact maximum and its residue-class multiplicity. The strict log-concavity proof compares positive successive coefficient ratios and has no experimental premise. A geodesic-free vertex subset is either a partial transversal of the columns or a single full column; complementing these sets proves the complete transversal polynomial and minimum and inclusion-minimal statements. Separate graph-distance and exhaustive vertex-subset checks confirmed the formulas for \(2\le n\le8\); additional exact arithmetic checks covered \(2\le n\le150\). The proof, not the finite search, establishes all \(n\ge2\).

## Originality — PASS, with publication-priority risk

The most relevant primary text is Manuel–Brešar–Klavžar, arXiv:2210.15325, particularly its introduction, §2 and conclusion. It defines the packing problem, gives generic bounds, and treats geodesic transversals of *square* rook graphs. Its separate exact value for the *complete bipartite graph* does not concern the Cartesian product studied here. These results supply the upper bound and definitions, not the enumerators, constructive sharpness, log-concavity or minimum-transversal census. Wild, arXiv:2409.16955, enumerates single geodesics algorithmically, not packings of disjoint maximal geodesics. Searches included the equivalent induced-three-vertex-path packing and two-clique-plus-perfect-matching descriptions. None of the accessed results directly supplied the joint polynomial theorem. Residual risk: an earlier combinatorial counting formula might exist under one of these equivalent descriptions; unindexed research has not been excluded.

## Mathematical value — PASS

The original geodesic-packing work explicitly motivates studying graph products and the packing–transversal relationship. The two-row rook graph is the smallest noncomplete Cartesian product of cliques and is structurally different from the complete bipartite graph sometimes confused with it. Rather than merely deriving an isolated scalar from the generic packing bound, the theorem determines both entire size distributions, establishes strict log-concavity of the packing distribution, counts every maximum configuration, and identifies every inclusion-minimal dual transversal. The unique-full-column matching model also gives a reproducible baseline for the genuinely more complex multirow problem. Nothing is asserted for that unsolved extension.

## Limits and closest literature

The closest full primary work is *Geodesic packing in graphs* (Manuel, Brešar, Klavžar, 2022 preprint/2023 publication); an additional related full-text HTML source is Wild's *Enumerating all geodesics* (2024). The former's general vertex-count bound is known, and the latter's individual-path enumeration does not imply a closed collection enumerator. Equivalence to disjoint induced-path packings creates residual priority uncertainty. Verification is self-contained but not independent validation.

Self-review: passed. Independent audit: not yet performed.
