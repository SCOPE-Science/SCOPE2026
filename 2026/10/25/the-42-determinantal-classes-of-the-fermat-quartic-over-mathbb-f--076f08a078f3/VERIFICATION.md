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
Run `python3 verify.py`. It performs exhaustive coefficient-field arithmetic over \(\mathbb F_5\), \(\mathbb F_{25}\), \(\mathbb F_{125}\); checks the Hasse–Weil numerator and Jacobian order; checks the 22 effective degree-two and 42 non-effective arithmetic totals; verifies sixteen bitangent line-square identities; and gives an explicit finite six-dimensional quadratic symplectic consistency model with sixteen fixed odd and sixteen fixed even characteristics. The geometric 28-bitangent correspondence, theta parity, nonhyperellipticity and determinantal sheaf correspondence are invoked as standard theorems, not formalized as code. Exact output must end with `VERIFY_OK`. No independent audit was performed.
