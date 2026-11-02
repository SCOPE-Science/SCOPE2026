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

# Reproducibility and verification

Run `python3 check_identifiability.py` using Python 3's standard library. No network, compiler, or external packages are required. The completed program reported `PASS: 802 independent numerical assertions`.

The verifier independently evolves first-, second-, and third-degree moments of integrated diffusivity using the forward Markov-generator hierarchy; it does not evolve the conditional-correlation integrals used in the proof. It checks 75 positive random parameter cases, the analytic second/fourth/sixth cumulants, and exact-data reconstruction at randomly selected two positive observation times. An additional multi-model test holds the mean, diffusivity variance, and correlation decay fixed while changing the stationary occupation probability, thereby checking agreement of all second/fourth observations and separation by sixth. Numerical evaluations also check the strictly positive hyperbolic-cosine expression from the monotonicity proof.

The analytical proof in `RESULT.md` is the infinite-parameter justification. A finite numerical grid cannot establish positivity or uniqueness globally. The theorem does not prove sample-size guarantees, robustness to measurement errors, or arbitrary non-Markov hidden dynamics. Review is confined to the supplied mathematics and program; no independent audit has been performed.
