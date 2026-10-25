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

# Reproduction and limits

Run `python3 fimex_radau3_verifier.py` with the Python 3 standard library. The verifier checks the exact method (the two implicit stage equations from the primary publication) against the displayed rational block matrix, the three Jury-polynomial identities, selected endpoint ordering, and the defective stiff limit. Its deterministic finite tests cannot prove all-parametric inequalities; the full algebraic argument is in `RESULT.md`.

For a source-level independent check, substitute \(f^{\mathrm{imp}}=-ay\) and \(f^{\mathrm{exp}}=-by\) directly into Buvoli–Southworth equation (45), using \(s=ra\), \(t=rb\), \(h=2r\), and invert the resulting \(2\times2\) linear system. Compare its characteristic coefficients to `RESULT.md`. The separate square-root threshold and Jordan-limit arguments are symbolic, not extrapolations of the numerical checks.

Publication-priority searches cannot rule out unindexed equivalent results. Independent scientific audit has not been performed.
