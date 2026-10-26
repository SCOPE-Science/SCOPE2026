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
# Verification record

The attached standard-library script `verify_hn.py` was executed and returned `VERIFY_OK: degree, strict HN gaps and determinant checks for g=3..10003`. It verifies the polynomial identities \(4g+4\), \(2g+6\), \(g+8\), the strict differences and \(\deg N=7g+18\), and the determinant exponents. No external CAS, package dependency or remote certificate is needed.

The finite loop cannot verify the infinite theorem or the exactness of geometric sequences. Those are proved directly: balanced direct image of the hyperelliptic pencil; normal sequence of the cubic scroll; locally free resolution of its normal bundle; complete evaluation and snake-lemma exact sequence; and HN uniqueness from three stable rank-one factors of strictly descending degree. Characteristic-zero and general-polarization scope are essential. The work has not undergone independent audit.
