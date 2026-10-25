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
The supplied `verify.py` uses only Python's standard library. Execute `python verify.py` in the extracted directory. Exhaustive cases: one coordinate on four values, two coordinates on two and three values, three coordinates on two values, and four coordinates on two values. Every subteam of every finite ambient grid is classified directly against all coordinate-cover choices; all minimal obstruction sizes are compared with the theorem. For each minimal obstruction the program finds the covering hyperplanes after each deletion, checks an invertible diagonal polynomial-evaluation matrix, expands the polynomial coefficients in the complete multilinear monomial basis, and checks the full Boolean-cube sharpness construction.

The finalized checker must print `CONSTANCY_COHERENCE_BOUND_OK 60`; that output was obtained by running the supplied file. The finite calculations do not establish the general theorem for arbitrary cardinalities; Step 1 and Step 2 in RESULT.md do so. No independent audit has been performed.
