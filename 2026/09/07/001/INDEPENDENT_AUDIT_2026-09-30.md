# Independent audit — 2026-09-30

## Final claim assessed

Among 4-subsets of an 8-point ground set with no two distinct members intersecting in exactly one point, the maximum family size is 17, and the equality families are exactly the radius-one Hamming balls defined by intersection at least three with a fixed 4-set.

## Correctness — PASS

The lower-bound ball has 17 members and is visibly 1-free. An independent exact maximum-clique computation on all 70 four-subsets found clique number 17 and exactly 70 maximum cliques; those 70 cliques are exactly the 70 balls. This independently verifies both the sharp bound and uniqueness. The explicit counterexample to preservation under a Frankl shift is also correct.

Evidence inspected:
- RESULT.md
- artifacts/final_verify.py
- artifacts/enumerate17.py
- independent exact compatibility-graph enumeration over all 70 four-subsets

Residual risks:
- The published proof is computer-assisted rather than a fully human case analysis, although the independent exhaustive check is small and exact.

## Originality — PASS

The exact small parameter case is not implied by the main asymptotic forbidden-intersection results inspected. Frankl's 1977 singleton-intersection paper is a sufficiently-large-n theorem. Frankl's 1983 Steiner-system bound has a hypothesis that fails for k=4,t=1. Ellis-Keller-Lifshitz explicitly leave the near-half-density window containing n=8,k=4 for forbidden intersection one. Searches of published mathematical records and the web found no prior statement with the same exact 17-and-unique-ball conclusion.

Sources inspected:
- Peter Frankl, Bull. Austral. Math. Soc. 17 (1977), DOI 10.1017/S0004972700025521
- Peter Frankl, Combinatorica 3 (1983), DOI 10.1007/BF02579293
- Ellis-Keller-Lifshitz, JEMS 26 (2024), arXiv:1604.06135

Residual risks:
- The 1977 publisher page exposed the abstract but not article HTML; an obscure small-parameter table or thesis could still duplicate the exact value.

## Scientific value — PASS

This is a sharp finite extremal classification at a natural boundary case where the standard asymptotic theory does not apply, with an explicit correction of a plausible but false 15-element guess and a concrete warning that ordinary shifting fails. That is a motivated structural fact rather than an arbitrary computation.

Context checked:
- forbidden-intersection literature above
- RESULT.md

Residual risks:
- The result is narrow and does not extend the asymptotic theory.

## Outcome

All three acceptance axes pass for the final claim as stated. Conjectures, heuristic search observations, and explicitly excluded broader regimes remain outside the accepted claim.
