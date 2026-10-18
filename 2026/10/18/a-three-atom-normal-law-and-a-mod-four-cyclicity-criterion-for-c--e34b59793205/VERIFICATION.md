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

## Reproduction
Run `python3 hexagon_normal_checker.py` using Python 3 and its standard library only. Expected final line begins `CYCLIC_HEXAGON_NORMAL_CHECK_OK`. Tests include five cyclic shapes with a total of 250,000 sampled interior points, plus a noncyclic obtuse case with 40,000 sampled points. Results depend only on deterministic seeds. The exact regular \(\nu=1/3\) identity and the nonregular \(\nu=8\sqrt2-11\) example are proved geometrically in `RESULT.md`; the checker numerically verifies the regular area ratio and the nonregular distribution.

## Limits
Monte Carlo and finite pointwise tests neither prove universal quantifiers nor settle originality. Rigorous reasoning and explicit use of the prior expectation theorem are provided in `RESULT.md`. No independent audit has been performed.
