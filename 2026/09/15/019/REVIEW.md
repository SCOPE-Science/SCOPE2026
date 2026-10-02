# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. Starting from the displayed Pascaleff-Tonkonog potential W'=sum_{i=k}^n y_i^{-1}+P Q^k, direct symbolic differentiation gives a critical local system with y_1,...,y_k=1/k and the remaining variables 1, critical value n+1. Expanding PQ^k gives the stated simplex vertices. Exact determinant reduction yields normalized volume k^(k-1)(n+1); gcds of edge vectors give a complete K_k of affine-length-k edges on C,P^(1),...,P^(k-1), with every other edge primitive. For k>3 this long-edge incidence cannot occur in a lifted Vianna simplex, whose non-unit edges lie in one triangular face; for k=3 the long triangle has lengths (3,3,3), not a Markov triple. The critical-point Floer criterion then gives non-displaceability. Independent symbolic checks through 3<=k<=n<=7 agreed with the uniform algebraic proof.

Originality: PASS. Pascaleff-Tonkonog provides the higher mutation/wall-crossing input and Chanda-Hirschi-Wang provides the lifted-Vianna Newton-simplex classification, but neither inspected source states the cross-family exclusion for the k>2 one-step Pascaleff-Tonkonog torus. The audited result combines the explicit PT potential with a new simplex volume/long-edge incidence calculation and compares it against the later Markov-triangle classification. Searches found no exact prior comparison or table.

Scientific value: PASS. Distinguishing natural monotone Lagrangian tori up to symplectomorphism and proving non-displaceability are central structural questions in this area. The Newton-polytope incidence obstruction separates two established mutation families uniformly in n and k.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
