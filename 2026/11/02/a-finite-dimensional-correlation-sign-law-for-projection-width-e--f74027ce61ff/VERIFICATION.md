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

# Verification record

The supplied `verify.py` can be executed with `python verify.py`. It uses only the Python standard library (in particular `math` and `random`). The observed deterministic output from the package's current verifier was:

`VERIFY_OK 1478 checks (Dirichlet exact moment and independent spherical tests)`

The tests cover five positive symmetric-Dirichlet concentration parameters, dimensions two through eight, four even benchmark exponents, nine first exponents, two independent exact mixed-moment formula implementations, the specialized fourth-power identity, independent circular midpoint quadrature, and seeded independent Gaussian-direction sampling.

The key universal mathematical check is analytic: the identity
\[
z\left(\frac{(z+a)_m}{(z)_m}-1\right)=a\sum_{k=0}^{m-1}\frac{(z+a)_k}{(z+1)_k}
\]
follows by telescoping. For \(m\ge2\) the summand with \(k=1\) is strictly monotone in \(z\) except at \(a=1\), and every other nonconstant summand has the same monotonicity. This proves the claimed sign in all dimensions and exponents, independently of finite testing.

Finite quadrature and pseudo-random sampling do not constitute a proof of an infinite assertion. Floating-point computations are checked with explicit tolerances, and do not purport to certify historical priority or independent validation. The sign theorem does not cover two arbitrary non-even benchmark exponents.
