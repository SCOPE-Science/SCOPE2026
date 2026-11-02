---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Replay
Extract `verify_rooted_entropy.py`, `rooted_census.tsv` and `rooted_checks.txt`. In a fresh directory run `python verify_rooted_entropy.py` using Python 3 standard library only. Compare generated `rooted_census.tsv` and the seven printed lines with the embedded artifacts. The process exhaustively traverses all Prüfer-labeled trees up to order six and all distinguished roots; an independent recursive-parent generator finds the same 37 rooted isomorphism types. The first solver uses exact max–min values, the second searches for complete binary trees at successive depths. Both agree on every case.

## Symbolic checks
The two exceptional six-vertex shapes have order-ideal counts 16 and 19. Their lower-bound product subfamilies have dimension three. For the first, no root-query splitting is balanced eight/eight; for the second the only cardinality-plausible first query has a positive branch with dimension two. The common-root construction satisfies the stated product count and one-added-concept bound for every positive integer parameter.

## Limits
No exact dimension for the connected extension is asserted beyond its two-sided bound; no historical-priority certification or independent audit is claimed.
