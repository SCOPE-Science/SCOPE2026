# Review: Chromatic repair radii of friendship graphs

## Correctness — PASS

For \(F_m=K_1\vee(mK_2)\), fixing the repaired hub color makes the edit distance an independent sum of two-orientation peripheral-edge costs. The sum of its three hub costs gives the unrestricted upper bound; the explicit three-block monochromatic source attains it. The feasible profile \((1,m,m)\) pins the ordinary target hub color to the unique singleton; the supplied even/odd sources meet the resulting \(m+1\) upper bound. The weak exceptional values at \(m=2,3\) follow by a complete parity case split. Finally, cyclic color relabeling of an unrestricted extremizer over three components creates a feasible combined profile and proves the disjoint-union equality. All quantifiers and small cases appear in RESULT.md. The independent exhaustive implementation reproduces all maxima for \(1\le m\le6\) and both extremal constructions through \(m=100\). Computations check the algebra but do not establish the unbounded theorem.

## Originality — PASS (bounded literature comparison)

Jiang et al., *Exact and extremal values of chromatic villainy* (arXiv:2610.13580v1), develops the color-profile framework, odd-cycle and complete-multipartite formulas and order-chromatic extremal bounds. Jiang et al., *Disjoint unions and fixed-parameter algorithms for chromatic villainy* (arXiv:2610.13556v1), establishes the general \(k\)-fold unrestricted fixing identity, which is credited. The inspected relevant text of these papers contains no friendship-graph formula and neither the single-copy ordinary/weak exceptional transition nor the exact unrestricted friendship fixing radius follows directly from their general numerical statements. The original Clark et al. chromatic-villainy paper was compared for family and parameter coverage; no equivalent was identified. The earlier Garnero et al. fixing-number paper could be assessed from an abstract but its full text was not lawfully accessible; its possible hidden family-specific theorem is a residual historical-priority risk. Unsearched alternative descriptions also remain possible.

## Mathematical value — PASS

The sharp formulas answer three naturally coupled repair questions on a fundamental block-graph family and establish a genuine size-growing difference between worst unrestricted assignments and feasible-profile disturbances. The two low-order exceptions expose a concrete boundary, while the explicit three-copy gap grows as \(3\lfloor(m-1)/3\rfloor\), giving a transparent combinatorial realization of a recently characterized repetition phenomenon; the general repetition theorem itself is not claimed as new.

## Remaining limits

No independent assessment or exhaustive historical-priority proof. The formulas are for three named colors, vertex-Hamming changes, friendship graphs, and three disjoint copies. The existing abstract-only older source remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
