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

The self-contained `verify.py` script uses only the Python standard library. Run `python3 verify.py` in the same directory. The completed checks included all nonzero binary projective vectors for \(n=4,8\), exact linear-algebra dimensions of the gradient ideal through degrees \(n\), local double-point compatibility for \(n=4,8,12,16\), and the binomial component counts. The observed terminal line was `VERIFY_OK`.

The script is a finite cross-check. It does not prove all field-valued zeros have only two distinct coordinates, that the gradient quadrics form a regular sequence for every \(n\), or the general ideal equality. Those points are established in the mathematical proof.
