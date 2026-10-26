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

The proof in `RESULT.md` is valid for every integer \(n\ge1\); the accompanying computations are deliberately finite sanity checks. Run `python3 verify.py` in the directory containing these files. The script uses integer bit shifts and Python standard-library `fractions.Fraction` for exact computations. `verification_output.txt` is its captured output.

The script reconstructs the digital line from the bit-linear floor formula and separately computes the fixed-slope positive maximum using the binary state recurrence. It checks the bit-reversed maximizing column for every slope with \(1\le n\le11\), exhaustively checks all columns for \(1\le n\le7\), and checks the claimed global rational closed form for \(1\le n\le11\). The final output line is a check marker, not an independent proof of all \(n\).

The key noncomputational checks are: (i) the coefficient-sign identity \(e_i=(b_i-x_i)/2\); (ii) the telescoping relation \(\sum_i e_i=s/2^n\); (iii) the Bellman candidate difference \((1-u_{m-1})(1/2-x)\); (iv) the solved scalar recurrences and attained lower bound. These are documented with definitions, quantifiers and boundary cases in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
