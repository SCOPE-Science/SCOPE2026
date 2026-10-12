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

Execute `python3 verify.py` using Python 3.9 or later; no third-party dependencies are needed. The verifier was executed from the same packaged source and returned `VERIFY_OK 210 analytic normalizations, piecewise densities, transport, modal signs, and independently sampled stationary laws`.

The source independently samples the explicit stationary-age mixture rather than directly sampling the proposed magnetization density, numerically integrates density contributions in the log-magnetization variable, tests the closed-form transport formula via quadrature, and checks derivative signs on parameter points below, at, and above the stated boundary. Its numerical tolerances are specified in the code. The exact generator identity, renewal-age limit, all-parameter modal classification, and optimality of the transport coupling are justified in `RESULT.md`; simulations alone would not prove them.

Self-review has passed for the stated conditional-mean theorem. No independent audit has been performed.
