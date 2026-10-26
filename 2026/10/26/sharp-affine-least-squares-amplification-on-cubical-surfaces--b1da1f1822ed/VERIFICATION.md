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

The included `verify.py` independently evaluates exact rational facet-surface and volume constants. It also integrates the facet convolution density with high-precision numerical quadrature and checks first-order asymptotic coefficients. Execute with Python 3.9 or newer and `mpmath` installed: `python verify.py`. In the prepared package, 60 assertions passed.

The all-dimensional theorem relies on the analytic derivation in RESULT.md; numerical tests cannot independently certify infinite asymptotics. The proofs use standard Fourier inversion and explicit error control for sums of independent bounded uniform random variables. No independently conducted audit has been performed.
