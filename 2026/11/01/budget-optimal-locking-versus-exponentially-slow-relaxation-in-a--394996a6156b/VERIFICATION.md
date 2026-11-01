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

# Reproducible checks and limits

Run `python verify.py` from the directory containing that standalone script, using Python 3 with SymPy, NumPy and SciPy. The code verifies the symbolic Jacobian eigenbasis and alternative-branch trace, solves 400 sample attracting-lock equations and compares direct Jacobian eigenvalues, then checks numerical onset monotonicity and large-exponent asymptotic behavior. The program completed successfully in the preparation environment. These finite tests do **not** establish exhaustive coverage of continuous parameters: the proof in `RESULT.md` supplies the global statements.

The theorem holds only for a three-site positive-reciprocal Kuramoto network with frequencies symmetric about zero, a fixed budget over off-diagonal links, and finite weighting exponent. All stability and decay claims are relative to the neutral common-phase direction. The limit of infinite exponent disconnects the middle oscillator; it must not be interpreted as a linearly stable finite-exponent system. No independent external validation has been performed.
