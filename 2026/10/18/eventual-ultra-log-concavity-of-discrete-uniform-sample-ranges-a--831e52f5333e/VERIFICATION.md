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

# Verification of the range-law theorem

Running `python3 check.py` performs exact integer comparisons for six-face sample sizes \(2\le n\le24\). For each size, a direct minimum/maximum-state recursion is compared with the closed counting formula, and all four possible interior ULC determinants are evaluated. Trial sizes \(2\) and \(3\) have negative determinant at \(k=2\), while every integer \(4\le n\le24\) has four strictly positive determinants. The proof in `RESULT.md` independently covers all \(n\ge25\) for six faces and all \(n\ge m^2\) for arbitrary finite uniform alphabets.

Additional finite-alphabet arithmetic tests are supplementary checks only. The executable makes no inference from sampled numerical points to an infinite parameter domain. No independent audit or external certification was performed.
