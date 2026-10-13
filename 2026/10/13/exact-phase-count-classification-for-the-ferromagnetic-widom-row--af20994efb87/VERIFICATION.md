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

The theorem is verified analytically by four exact steps: (1) direct monotonicity of the symmetric scalar branch, (2) reversible elimination of every nonsymmetric solution to a ratio equation, (3) an exact hyperbolic parameterization and domain condition, and (4) strict monotonicity of the resulting activity map from convexity of \(s\coth(st)-\coth t\).

The standalone `verify.py` is a corroborative replay. It samples several tree orders and ferromagnetic parameters, reconstructs \((u,v)\) from the hyperbolic parameter, substitutes them into both original boundary-law equations, checks strict sampled growth of the activity map, and checks its critical limit. The replay output is:

`VERIFY_OK cases=112 max_residual=1.998e-15`

No finite grid, numerical residual, or sampled monotonicity check is used as proof of the all-order statement. The proof covers every integer \(k\ge4\) and every parameter in the stated continuous ranges. The theorem does not address non-translation-invariant Gibbs measures or extremality.
