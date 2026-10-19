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

# Verification of the rational matrix-exponential certificate

Execute `python3 verify_two_season.py` with Python 3. Only standard-library `fractions.Fraction` and `math.factorial` are used. The script reconstructs the shifted season matrices, computes \(S_{80}(TX/2)\) via rational matrix products, constructs rigorous entrywise exponential tail enclosures, uses three positive integer vectors to bound the corresponding spectral radii, and asserts all required strict integer comparisons, including the negative-growth certificate.

The common tail estimate follows from the max-row-sum norm for nonnegative matrices and a scalar geometric remainder bound. The Collatz–Wielandt inequalities hold because the monodromy is positive. All decisive checks are exact; printed floating-point approximations are explicitly not used to establish the result. The checker addresses the three stated periods and does not certify the full period-response profile, uniqueness of the maximizer, ecological persistence, or external originality. The proof in `RESULT.md` explains why the finite sequence of exact rational operations bounds the entire infinite exponential series.
