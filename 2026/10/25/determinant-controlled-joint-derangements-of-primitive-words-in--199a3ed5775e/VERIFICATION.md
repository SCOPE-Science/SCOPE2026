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
# Verification

Run `python3 commuting_pair_checker.py` using Python 3 standard library. Expected signal: `COMMUTING_PRIMITIVE_EXCLUSION_OK 8903 30`.

The code checks all 8,903 ordered commuting pairs across nonempty labelled universes of size at most six. It computes joint fixed-point-free events for the primitive words \(v=(1,0)\), \(w=(1,d)\), \(d=1,2,3,4,5\), and compares exact rational exponential-function coefficients for all 30 size/determinant combinations. It also compares the single-word probability coefficient and the total commuting-pair count \(n!p(n)\). The proof, not these finite tests, supplies the unbounded-size enumeration and the asymptotic limits. Independent scientific audit not performed.
