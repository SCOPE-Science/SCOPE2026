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

# Verification record

Run `python check.py` with Python 3, SymPy and NumPy. The script proves the named finite polynomial identities by symbolic simplification, and separately conducts numerical regime sanity checks. `check_output.txt` records its actual console output.

The verified exact identities are: the squared-pole rational reduction at two exact test parameters; the polynomial discriminant for arbitrary symbolic parameters; the quadratic-in-weight discriminant; the unique critical radical factorization; the nonzero transversality Jacobian; a third-order zero derivative test; and distinct double-root boundary checks at an exact rational spacing.

The four floating-point root regimes are finite diagnostics and do not prove the complete parameter classification. The analytical argument in `RESULT.md` supplies the signs, quantifiers, multiplicities and all boundary cases. The checker depends only on the public `check.py` and the packages in `requirements.txt`; it does not use any earlier research files or external execution logs. No independent mathematical audit has been performed.
