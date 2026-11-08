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

# Exact finite verification

The accompanying `verify.py` uses Python standard-library integers and `fractions.Fraction`, not floating-point arithmetic. It constructs the actual tube simplices of each star with two through six leaves, exposes a vertex for every generic total coordinate order, removes duplicates, computes the exact uniform-vertex covariance matrix, and checks the two eigenvalues and barycenter against the closed expressions. It additionally evaluates the spectral gap exactly in dimensions two through 64. Invocation: `python verify.py`.

Recorded output:

`STELLOHEDRON_VERTEX_COVARIANCE_CHECKS_PASSED dimensions=5 vertices= 2369 spectral_tests=63`

The finite enumeration tests only dimensions two through six. The rigorous general proof consists of the exposed-vertex parametrization, exact reciprocal-factorial moment identities, symmetry decomposition, and uniform inequalities establishing the transition in every larger dimension. It does not rely on numerical inference about arbitrarily large dimensions. The manuscript and checker concern *distinct vertices* with equal probabilities, not generic total orders with equal probabilities. Independent audit remains unperformed.
