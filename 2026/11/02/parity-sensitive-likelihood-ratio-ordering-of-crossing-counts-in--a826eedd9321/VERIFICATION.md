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

# Reproducibility

Run `python verify.py` using Python 3 and no third-party modules. It exhaustively enumerates the \( (m-1)!! \) residual matchings for each even \(m\le12\), compares exact histograms, and checks rational-arithmetic normalization, means, two upper-tail inequalities, and two-step likelihood-ratio formulas for residual sizes through 40. The source code raises an assertion on failure. These finite checks are not an infinite proof; the counting, nested-cut transition, and likelihood-ratio algebra in `RESULT.md` provide the general proof.

No independent external audit has been performed.
