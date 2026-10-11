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
# Reproducibility and limits

The exact proof is in `RESULT.md`. No external certificate or independent examination is claimed.

From a directory containing the packaged standalone files, execute `python3 verify.py` with the standard Python library. Its actual run printed:

`VERIFY_OK exact_parameters=1152 direct_rows=20 gaussian_n=10000 gaussian_q=4 ratio=0.483931970541 target=0.483941449038 poisson_first_regime=4 sparse_crossover=4`

The verifier recomputes, in exact rational arithmetic, the degree-two Hamming kernel's absolute binomial sum and the four-boundary expression for each of 1152 parameter pairs. It separately enumerates 20 small complete Hamming rows. Floating-point checks on larger finite parameters corroborate but cannot establish the asymptotic Gaussian and Poisson theorems; those require the analytic limiting arguments and uniform integrability in the proof. The cusp formula is derived from the unique second-Charlier sign change and locally uniformly differentiable Poisson tails.

The only dependencies are Python's standard library. All required definitions, conventions, domain restrictions and formulae are self-contained in this package.
