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

The included `ehrenfest_endpoint_checker.py` uses Python's standard library and constructs transition probabilities by Poisson uniformization of the exact finite birth–death generator. It then computes the induced \(\ell^1\) semigroup norm, the \(\ell^\infty\) derivative norm and the central-column derivative. Across 36 combinations of dimension and time, it checks these independently computed quantities against the binomial and integral identities. Additional finite large-size checks compare the logarithmic-time derivative with its predicted limit. Running the included checker produced **427 passed finite comparisons**.

Execute `python3 ehrenfest_endpoint_checker.py` from the folder containing this file. Its path is relative and it requires no package installation or network access.

The mathematical proof, not the checker, establishes the strict maximizing-column order, universal exact finite-time formula, strict monotonicity, uniform optimizing-time asymptotic and logarithmic derivative lower bound. Finite calculations do not prove the asymptotic theorem. The result does not assert a sharp \(\ell^1\) derivative coefficient, odd-dimensional analogue, independent mathematical review or exhaustive historical originality certification.
