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

# Reproducibility and verification

Run `python3 verify.py` in the same directory as this document with Python 3 and SymPy. The program performs exact symbolic factorization of the conic, identity of the Fermat parametrization, expansion of the local smoothing equation, weighted base-change scaling, genus reconciliation, and the primitive-root characteristic polynomial. It checks the exponent identities at \(p=5,7,11,13,17,19\) and prints `VERIFY_OK` if all assertions pass. An actual execution of this exact packaged script produced that marker.

Mathematical scope: the finite script does not prove the general stable-model assertion for every prime; the local weighted stable-reduction argument and genus/monodromy calculation in RESULT.md address the infinite quantifier. The older 2017 general boundary paper could not be fully inspected and remains a literature-priority risk. No independent audit or validation has been performed.
