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
# Reproduction and limits

Run `python3 verify.py` with Python 3 and no third-party libraries. The exact-rational checker verifies the balanced binary maximizers for \(2\le m\le16\), the two-point centered minimizers, all nonconstant ternary coordinate configurations through \(m=8\), and an exact pairwise variance identity, returning `EQUILATERAL_EUCLIDEAN_EXACT_OK 9966`.

The general statement is established by the analytic argument in RESULT.md: invariant-form averaging plus the two sharp extremum calculations and duality. The rational finite checks are not an exhaustive search of all vectors or Euclidean ellipsoids, and do not certify novelty or provide independent mathematical review. Complex scalar spaces and non-equilateral metrics are not covered.
