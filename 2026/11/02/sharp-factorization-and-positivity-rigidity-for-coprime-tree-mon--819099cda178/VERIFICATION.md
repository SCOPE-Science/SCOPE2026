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

The exact rational-arithmetic program `verify.py` computes the defining difference and compares it against the closed rational form at multiple rational points for exponents \(1\) through \(20\). It checks the \(r=1,2\) product identities, the top Laurent coefficient obstruction for \(3\le r\le20\), and exact signs over a finite grid of primitive indices and parameters. It also verifies a partial sum inequality for small \(q\) in selected cases.

Run `python3 verify.py`. It uses only the Python standard library and should report `VERIFY_OK`.

These tests are finite evidence for the identities and examples. They do not certify the infinite parameter assertions or rule out earlier literature. The general proof is in `RESULT.md`; independent mathematical audit has not been performed.
