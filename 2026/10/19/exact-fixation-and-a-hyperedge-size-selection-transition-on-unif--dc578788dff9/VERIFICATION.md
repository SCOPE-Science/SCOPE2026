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

# Verification guide

The theorem is analytically proved in `RESULT.md`. These programs check its main transition identities and finite Markov chains without claiming to certify the infinite-parameter result computationally.

Run `python verify_exact.py` with Python 3. The program evaluates 22,400 identities/inequalities using standard-library exact `Fraction` arithmetic, including the reduced-chain first-step identities, boundary conditions, the single-peripheral-mutant first-change identity, uniform initialization, neutrality, and the strict center/periphery comparison for multiple petals.

Run `OPENBLAS_NUM_THREADS=1 python check_general.py` with Python 3 and NumPy installed. It independently assembles (i) full \(2^{sm+1}\)-state binary chains for small populations and (ii) permutation-aggregated chains for larger petal families, then compares their absorption probabilities against the formulas. It reports 13,677 comparisons and consistency checks. Matrix solutions and inequalities in this program use floating-point arithmetic and a tolerance of \(10^{-10}\); they are numerical diagnostics, not exact global certificates.

Exact state count, residual equations, and their derivations are printed in `RESULT.md`. The tests do not establish an all-fitness amplifier/suppressor ordering, do not cover every infinite configuration, and do not establish publication priority. Their purpose is to check implementation and catch finite algebraic errors independently of the analytical argument.
