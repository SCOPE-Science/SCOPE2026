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

# Reproduction and boundaries of verification

The proof is complete in `RESULT.md` and uses no numerical inference for assertions quantified over arbitrary probabilities or parameters. The standalone `verify.py` script uses only standard Python and can be run as `python verify.py` in the directory containing this file and `RESULT.md`.

The script asserts the exact rational integral \(q\int_{-1/(2q)}^{1/(2q)}|t|^p\,dt=1/((p+1)(2q)^p)\) for twenty integer parameter pairs, checks numerical midpoint approximations of those integrals, and verifies the displayed conversion from the \(p\)-th moment to the metric radius. It printed `PASS: 20 exact rational moment identities and finite ring checks` in the tested environment.

The infinite-dimensional assertions—classification of all invariant Borel probabilities, station/core connectivity and transport isometry for every real \(p\ge1\) including \(p=\infty\)—follow from the complete disintegration and transport-coupling proof. They are not certified by the script, nor has an independent scientific audit been performed.
