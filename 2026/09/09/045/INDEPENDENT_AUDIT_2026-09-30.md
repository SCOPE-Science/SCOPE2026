# Independent audit — 2026-09-30

**Record:** `2026/09/09/045`  
**Audited source tree:** `b287807cb30ad055d03419b9b91b14d019404a56`

## Correctness — PASS

A fresh exhaustive check of the two displayed witnesses found 99 distinct covered pairs in each, no five pairwise disjoint triples among all 237336 five-subsets, and respectively 269 and 266 disjoint four-subsets. The degree multisets are exactly [5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7] and [4,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7], proving non-isomorphism. The elementary point-degree bound gives at most floor(16*7/3)=37 blocks. Thus the claimed interval [33,37] and PPC=4 witnesses are fully established; no exact value above 33 is claimed.

## Originality — PASS

Stinson's published construction theorem gives, at rho=4 and v=16, the earlier lower bound 25; the full-text theorem was inspected. The maximum-PSTS(16) enumeration literature describes automorphism, Pasch, mitre and Fano data, but the inspected material does not provide a maximum-PPC classification or a beta(4,16) lower bound of 33. Exact beta(4,16) searches found the present record rather than an earlier 33-block construction. The new statement is therefore the explicit 33-block PPC-four construction and resulting improved interval, not the standard upper bound 37.

The comparison explicitly checked equivalent formulations, broader coverage, exact tables/databases, and whether prior results logically imply the final claim.

## Scientific value — PASS

beta(4,16) is a natural extremal parameter, and increasing the constructive lower bound from 25 to 33 closes most of the previously cited gap while providing two structurally distinct witnesses. Even though 34-37 remain unresolved and the upper bound is elementary, a large certified improvement for a named extremal function is mathematically useful and not merely a code-validation exercise.

## Source inspections

- **Stinson — On partial parallel classes in partial Steiner triple systems** — Full conference-slide text for definitions and Theorem 2, including the general construction lower bound; theorem page visually inspected. At rho=4, v=16 the theorem gives lower bound 25, so it does not cover the 33-block witnesses. https://arxiv.org/abs/2007.11033
- **Demirkale, Donovan, Grannell — Enumerations of maximum partial triple systems on 16 and 17 points** — Abstract and stated structural-invariant scope. Enumerates maximum PSTS(16) and reports automorphism/Pasch/mitre/Fano data; the inspected material does not provide beta(4,16) or maximum-PPC data. https://arxiv.org/abs/1708.07646

## Residual risks

- The exact value beta(4,16) remains open within 34–37; there is no upper-bound improvement here.
- The 33-block witnesses are computational constructions without a structural characterization of all extremals.
- Published maximum-PSTS(16) system files were not exhaustively reclassified by PPC during this audit.

## Disposition

**PASS.** The final claim passes correctness, originality, and scientific value without changing `RESULT.md` or `SLOGAN.txt`.
