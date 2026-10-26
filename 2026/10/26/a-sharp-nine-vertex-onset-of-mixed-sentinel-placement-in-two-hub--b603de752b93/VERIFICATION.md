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

Exact reproducibility: with Python 3 standard library, execute `python verify.py` in this directory and compare its single JSON output line to `verification_output.json`. The verifier enumerates all edge states and source components for the finite specified tests, checks the symbolic cancellation coefficients and the positive Bernstein certificates, and checks the two witness regimes with rational arithmetic. The proof in `RESULT.md` supplies the all-parameter analysis. Independent external verification has not been carried out.
