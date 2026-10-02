# Independent mathematical audit — 2026-10-01

Audited at: 2026-10-01T04:47:00Z

## Final claim

Non-displaceability and Newton-polytope rigidity of the k>2 toric-mutated monotone torus in CP^n

## Correctness — PASS

PASS. Starting from the displayed Pascaleff-Tonkonog potential W'=sum_{i=k}^n y_i^{-1}+P Q^k, direct symbolic differentiation gives a critical local system with y_1,...,y_k=1/k and the remaining variables 1, critical value n+1. Expanding PQ^k gives the stated simplex vertices. Exact determinant reduction yields normalized volume k^(k-1)(n+1); gcds of edge vectors give a complete K_k of affine-length-k edges on C,P^(1),...,P^(k-1), with every other edge primitive. For k>3 this long-edge incidence cannot occur in a lifted Vianna simplex, whose non-unit edges lie in one triangular face; for k=3 the long triangle has lengths (3,3,3), not a Markov triple. The critical-point Floer criterion then gives non-displaceability. Independent symbolic checks through 3<=k<=n<=7 agreed with the uniform algebraic proof.

## Originality — PASS

PASS. Pascaleff-Tonkonog provides the higher mutation/wall-crossing input and Chanda-Hirschi-Wang provides the lifted-Vianna Newton-simplex classification, but neither inspected source states the cross-family exclusion for the k>2 one-step Pascaleff-Tonkonog torus. The audited result combines the explicit PT potential with a new simplex volume/long-edge incidence calculation and compares it against the later Markov-triangle classification. Searches found no exact prior comparison or table.

### Equivalent formulations
PASS. Pascaleff-Tonkonog provides the higher mutation/wall-crossing input and Chanda-Hirschi-Wang provides the lifted-Vianna Newton-simplex classification, but neither inspected source states the cross-family exclusion for the k>2 one-step Pascaleff-Tonkonog torus. The audited result combines the explicit PT potential with a new simplex volume/long-edge incidence calculation and compares it against the later Markov-triangle classification. Searches found no exact prior comparison or table.

### Broader coverage
PASS. Pascaleff-Tonkonog provides the higher mutation/wall-crossing input and Chanda-Hirschi-Wang provides the lifted-Vianna Newton-simplex classification, but neither inspected source states the cross-family exclusion for the k>2 one-step Pascaleff-Tonkonog torus. The audited result combines the explicit PT potential with a new simplex volume/long-edge incidence calculation and compares it against the later Markov-triangle classification. Searches found no exact prior comparison or table.

### Exact database or table
No exact database/table coverage was identified; this is supporting best-knowledge evidence only, not proof by failed search.

### Claim versus prior implication
PASS. Pascaleff-Tonkonog provides the higher mutation/wall-crossing input and Chanda-Hirschi-Wang provides the lifted-Vianna Newton-simplex classification, but neither inspected source states the cross-family exclusion for the k>2 one-step Pascaleff-Tonkonog torus. The audited result combines the explicit PT potential with a new simplex volume/long-edge incidence calculation and compares it against the later Markov-triangle classification. Searches found no exact prior comparison or table.

## Scientific value — PASS

PASS. Distinguishing natural monotone Lagrangian tori up to symplectomorphism and proving non-displaceability are central structural questions in this area. The Newton-polytope incidence obstruction separates two established mutation families uniformly in n and k.

## Sources inspected

- **James Pascaleff and Dmitry Tonkonog, The wall-crossing formula and Lagrangian mutations** (https://arxiv.org/abs/1711.03209): INPUT_THEORY_NOT_CROSS_FAMILY_COVERAGE. PT supplies the mutation and wall-crossing machinery; no inspected statement gives the audited Newton-volume/long-edge exclusion from all lifted Vianna simplices.
- **Soham Chanda, Amanda Hirschi and Luya Wang, Infinitely many exotic Lagrangian tori in higher projective spaces** (https://doi.org/10.1007/s11784-024-01137-4): CLOSEST_COMPARATOR_NOT_COVERING. Theorem 1.1 says a lifted Vianna Newton simplex has one triangular face with Markov edge lengths a,b,c and all other edges affine length one; it does not state the audited PT k>2 family or its exclusion.

## Residual risks

- The argument takes existence/monotonicity and the displayed PT wall-crossing potential as prior inputs; those geometric constructions were not reproved.
- The symbolic artifact checks only n<=7, but the determinant and edge-gcd proof audited here is uniform.

## Disposition

**passed**
