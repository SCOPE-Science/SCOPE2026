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

The script `verify.py` was run from the extracted scientific package with `python3 verify.py` and printed `VERIFY_OK`. It uses exact rational arithmetic for Schur-complement determinant/rank identities for \(3\le m\le7\), the canonical residual-matrix rank criteria for \(1\le t\le8\), and a nonsingular dense-chart witness at \(m=5\). These tests check formulas and small instances only. The proof for all \(m\ge3\) is the symbolic block-rank and boundary-codimension argument together with the published general radicality/unmixedness theorem. The general theorem's published text has been inspected; it is not re-proved by the script. The all-parameter primality and novelty have not undergone independent validation.
