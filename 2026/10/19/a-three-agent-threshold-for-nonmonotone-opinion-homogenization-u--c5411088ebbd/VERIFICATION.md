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

# Verification and limits

The code `verify.py` in this package uses exact symbolic arithmetic to test the proposed closed-form fixed point against the original linear update, calculate the population mean-centered variance, differentiate it, substitute the proposed unique minimizer, and verify both endpoint gaps. It independently solves the general two-agent fixed point to compare its opinion-gap coefficient with the formula used in the minimality proof.

The example at \(b=3/4\) and \(z=4/5\) is evaluated as exact rational numbers, including the positive endpoint variance increase \(1/1274\). Finite rational parameter checks test algebraic consistency. The proof in `RESULT.md` supplies the necessary continuum sign arguments and contraction/uniqueness justifications; no claim of formal theorem-prover certification or independent audit is made.

To rerun: install the Python dependencies in `requirements.txt` and execute `python verify.py` from this directory. Only public mathematical source references, not private operational artifacts, are needed.
