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

# Reproducibility and limits

Execute `python3 VERIFY.py` with Python 3. The file is standalone, uses only the standard library, and printed `PASS: 1150 finite and high-precision diagnostics; the proof supplies the infinite statement.` It reconstructs the two hole cylinders for 2≤m≤9 by exact rational map iteration, exhaustively compares allowed binary words through length 13 against the renewal recurrence, and checks small-root high-precision estimates at 8≤m≤25.

The complete mathematical proof is in `RESULT.md`: cylinder-to-defect coding, last-one decomposition, Perron entropy/dimension argument, Bernoulli finite-time probabilities and a uniform Taylor expansion. Finite checks do not prove the infinite recurrence, Hausdorff dimension, uniqueness of the Perron root, or the asymptotic error term. Bibliographic originality is supported by the specified primary literature comparisons but has not been independently established.
