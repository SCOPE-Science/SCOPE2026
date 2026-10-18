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

Run \(\texttt{python3 verify.py}\) using Python 3.8 or later. The script uses only the Python standard library. It has been executed on the supplied file and printed:

`VERIFY_OK: exact 4x4 determinant/resolvent, rational derivatives, binary enumeration and exact moments (L=0..9)`

The checker constructs integer polynomials in three indeterminates, evaluates both four-by-four determinants exactly via the Leibniz formula, and verifies three rational derivative identities by symbolic polynomial cross multiplication. It then compares the carry-state enumerators against separate binary-digit calculations and direct binomial-valuation computations for finite lengths. All finite moment comparisons use exact fractions. Polynomial determinant and derivative calculations are identities in formal variables and do not rely on sampling.

The derivation of the finite-length covariance formula uses formal coefficient extraction of those exact rational generating functions. The direct enumeration through \(L=9\) is corroboration and does not alone constitute a proof for arbitrary length. No independent mathematical audit has been performed.
