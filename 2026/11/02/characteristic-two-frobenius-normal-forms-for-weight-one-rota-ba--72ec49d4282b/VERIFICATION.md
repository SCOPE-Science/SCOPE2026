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

Run `python verify.py` using the standard Python library. The executable directly constructs all candidate matrices from their first images in \(\mathbb F_q^n\) for \(q=2,4,8\), tests the original weight-one Rota–Baxter identity on every basis pair, and computes linear ranks by elimination with independently implemented field arithmetic. It checks the exact predicted rank histograms for \(2\le n\le8\) at \(q=2\), \(2\le n\le6\) at \(q=4\), and \(2\le n\le5\) at \(q=8\). The program completed with `VERIFY_OK`.

The direct enumerations do not establish the result for untested orders or all dimensions. The symbolic proof in RESULT.md establishes the field-general normal form and derives the rank enumeration. There is no independent mathematical audit, proof-assistant formalization, or external certificate.
