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

# Reproduction checks and limits

Use Python 3, NumPy 1.24 or later and run `python verify.py` in the directory containing both this file and `verify.py`.

The executable constructs normalized full graph-state amplitudes, forms the two-terminal partial trace, diagonalizes its partial transpose, compares the predicted full spectrum and negativity, and tests \(1\le c\le7\) at ten phases. It independently checks the odd-binomial identity at \(1\le c\le40\), the finite upper bound, the exact \(c=1\) maximizer, and large-\(c\) numerical behavior. Expected completion line: `VERIFY_OK 8211 checks`.

The finite checks do not certify the all-integer identity or the asymptotic exponent. Those assertions are proved with analytic orthogonality/partial trace, positivity, and uniform expansions in `RESULT.md`. External independent audit has not been performed.
