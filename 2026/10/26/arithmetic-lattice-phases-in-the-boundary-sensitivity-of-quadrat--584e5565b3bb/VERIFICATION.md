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

# Verification

The self-contained script `quadratic_boundary_verify.py` uses only the Python standard library. Execute `python quadratic_boundary_verify.py` to verify 1,175 exact rational coefficients from independent Gram inversion and 248 finite-sample Bernoulli identities to 60 digits. Every finite test passed when run on the embedded script source.

The infinite root-sign statement follows by factoring the explicit kernel, and the quadratic sum identity follows from exact endpoint-truncated Euler–Maclaurin. The second-order liminf and limsup require Weyl equidistribution for \((6-\sqrt6)/10\) along the residue class \(m\equiv3\pmod5\), not just numerical experimentation.

Limits: No finite test establishes the infinite phase law; no full \(\ell^\infty\)-operator-norm statement for the whole fitted-value matrix or off-grid evaluation is asserted. Independent scientific audit remains unperformed.
