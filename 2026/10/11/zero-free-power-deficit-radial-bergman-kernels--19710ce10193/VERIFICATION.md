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

# Verification of the power-deficit radial Bergman kernel theorem

The proof independently derives the complete coefficient sequence \(c_n\), the probability-mixture identity for \(0\le q<1\), and the rational closed form for \(q=1\). The decisive infinite certificate is the pointwise inequality
\[
0\le u\left|\frac{1-s}{1-us}\right|^2\le\frac{4u}{(1+u)^2}<1
\]
for real \(0<u<1\) and complex \(|s|<1\), proved on the boundary and extended by maximum modulus. Integrating this inequality against the exact probability measure proves the strict disk and half-plane bounds. The endpoint is checked separately by the Cayley right-half-plane identity.

Run `python power_weight_verify.py` with the Python standard library. The executed script passed 4,200 exact rational coefficient equalities, a finite pointwise contraction sample, and finite-series consistency tests on parameter and complex-input grids. Finite tests do not prove the universal theorem; the analytic proof does. All inputs, statements and conventions are recorded explicitly and no external certificate or independent validation is claimed.
