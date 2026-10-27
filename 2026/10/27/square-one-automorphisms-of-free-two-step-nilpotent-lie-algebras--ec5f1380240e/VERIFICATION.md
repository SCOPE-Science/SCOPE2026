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

# Verification and reproducibility

Run `python3 verify_involutions.py` using an ordinary Python 3 installation; the script requires only the standard library and checks finite matrix identities without external services.

The odd-characteristic tests enumerate all square-one quotient matrices in dimensions two and three over the prime fields of orders three or five, verify the predicted dimension of the linear solution space in the central part, and compare the resulting exact totals. In dimension two, they additionally enumerate every central parameter, check the full block matrix square, and compute the fixed-space dimension. In characteristic two, tests over the field of order two exhaustively check every central parameter in dimensions two and three and verify linear-kernel counts for every square-one quotient matrix in dimension four.

Expected outputs include odd-field totals \(46\), \(176\), and \(57592\), and even-field totals \(10\), \(1184\), and \(19357696\), respectively. The final line is `FREE_TWO_STEP_ALL_CHARACTERISTICS_OK`.

The code enumerates small **prime** fields. The proof, not these finite tests, establishes the formulas over all prime-power fields and the conjugacy/fixed-space statements over arbitrary odd-characteristic fields. No independent audit has been performed.
