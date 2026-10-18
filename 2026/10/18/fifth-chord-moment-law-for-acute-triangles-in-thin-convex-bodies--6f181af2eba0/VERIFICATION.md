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

The proof's exact fiber calculation is equivalent to \(\int_0^1\int_0^1 u\min(u,v)\,dv\,du=5/24\); multiplying by the two extremal vertical-order cases and \(\int_0^w r^4dr=w^5/5\) gives \(w^5/12\). The exact rational calculations in `check_acute.py` test this identity, the moments for the rectangle, triangle and trapezoid, and sharp bound attainment.

The standalone script uses seeded Sobol integration of the **complete three-angle inequalities** in the logarithmically conditioned gap variables, so it samples otherwise exceptionally rare acute configurations efficiently. It compares \(\varepsilon=10^{-3}\) and \(\varepsilon=10^{-7}\) to the limiting coefficient. These are nonexhaustive tests with acceptance tolerances; only the mathematical argument proves the continuum limit.

Run `python check_acute.py` with NumPy and SciPy. Specific printed numbers depend deterministically on the included seeds and numerical library versions. This is not independent formal verification or peer review.
