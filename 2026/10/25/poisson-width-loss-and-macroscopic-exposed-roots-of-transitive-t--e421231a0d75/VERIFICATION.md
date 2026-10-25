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

# Reproducible verification

Run `python3 verify.py` from the directory containing this file. The script uses only the Python standard library and prints a `VERIFY_OK` line or raises an error. It checks exact support maximization, spherical normalization, the global-extrema ordering identity, and independently implements Poisson ordered-pair optimization by both a linear scan and exhaustive pair search. It also prints seed-fixed numerical distributional diagnostics for finite Gaussian samples and truncated Poisson point processes.

The experiments are finite and do not prove the Poisson point-process convergence, asymptotic uniform integrability, or any statement quantified over infinitely many dimensions. These are established by the analytic steps in the accompanying mathematical text. The Poisson simulation omits marks below a stated finite cutoff, whereas the theorem uses the full limiting process. No independent mathematical audit has been performed.
