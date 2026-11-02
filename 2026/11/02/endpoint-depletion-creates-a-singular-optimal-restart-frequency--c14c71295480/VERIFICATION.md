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

# Verification and scope

The accompanying `verify.py` was executed against its packaged content with the dependencies recorded in `requirements.txt` and printed `PASS: 103 finite assertions; analytic theorem not inferred from numerical samples.` The checks independently evaluate the discounted exit boundary solution by quadrature and special functions, the critical exact hyperbolic expression, the low-rate exit-moment derivative, six representative endpoint exponents at three high rates, and a spatially discretized absorbing Brownian generator with complete resetting.

The discrete Markov approximation tests convergence consistency on several finite meshes and rates; they do not prove continuum identities. Numerical minimization only illustrates \(\varepsilon k_\varepsilon\to2\) for selected positive values of \(\varepsilon\). The continuous-range, global-minimizer and singular-asymptotic statements are established analytically in the proof; no finite experiment or log is used as an infinite certificate.

The available primary literature covers general renewal formulas and frequent-reset asymptotics. The exact beta-law optimizer asymptotic remains a qualified originality assessment, because a plausible 2026 source on circular resetting could not be compared through complete full text. No independent audit or independent validation is asserted.
