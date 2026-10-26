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

Run `python3 verify.py` with Python 3 (standard library only). The exact checker returns `VERIFY_OK` after checking six smooth toric vertex charts, all nine minors of the universal Hasse-jet residual block, the coefficient-\(2\) characteristic split, and representative fiber ranks in characteristics \(2,3,5,7,11\). The proof in RESULT.md shows why these universal integer-polynomial identities imply the full statements in arbitrary characteristic; finite-field test points alone would not certify an infinite classification.

The determinantal scheme is defined by \(5\times5\) and \(4\times4\) minors of the rank-six second principal-parts map, respectively. The local ideals are obtained by reducing to \(B\), not by searching a finite list of points. No independent audit has been performed.
