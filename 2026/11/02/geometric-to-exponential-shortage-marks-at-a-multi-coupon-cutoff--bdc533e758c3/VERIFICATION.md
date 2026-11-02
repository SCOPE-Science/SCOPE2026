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

# Reproduction

Run `python verify.py` in an environment with NumPy and SciPy. See `verification_output.txt` for the actual deterministic run output. The checker tests Gamma-versus-Poisson lower tails, exact finite multinomial occupancies on tiny cases, the conditional factorial ratio for shortage depths, numerical cutoff windows, and selected scalar identities.

The mathematical proof is in `RESULT.md`. Finite experiments and floating-point comparisons are not proofs of any infinite weak convergence. The crucial analytic checks are the Gamma-quantile asymptotic \(b_nh_n^2\asymp\log n\), the falling-factorial approximation on the \(1/h_n\) mark scale, and the Poisson-clock sandwich for monotone tail counts. Quantities outside the stated asymptotic regimes are not covered.

No independent audit or independent experimental validation has been performed.
