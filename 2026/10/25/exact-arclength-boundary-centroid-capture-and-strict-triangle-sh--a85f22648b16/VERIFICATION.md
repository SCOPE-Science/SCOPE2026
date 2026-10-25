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

# Verification procedures and limits

The proof in `RESULT.md` derives all conditional geometric inequalities and evaluates the two necessary integrals without relying on sample computation. `verify.py` (Python 3 standard library) re-evaluates the integrals with deterministic midpoint quadrature, checks algebraic identities at nontrivial side-weight vectors, and independently simulates centroid-in-triangle events using physical Cartesian coordinates for five non-similar triangles. Re-run with `python3 verify.py`; it prints per-check expected values and standard-error deviations. These numerical tests only corroborate, rather than establish, the exact identities and infinite-quantifier statements. No independent external scientific audit is claimed. Source date is anchored to arXiv:0906.0309's verified UTC first public posting of 2009-06-01; Prékopa (1972) and Wendel (1962) are earlier historical sources with no reliably established exact first-public calendar day in the inspected records.