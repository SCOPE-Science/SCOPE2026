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

# Verification of fixed-phase entrance law

The stand-alone `check_eos_entry.py` was executed from the complete package and passed 88 finite checks using the Python standard library. It evaluates exact smooth-map iterates for coprime pairs \((n,k)=(2,1),(3,1),(5,2),(7,3)\), parameters \(a=24n,30n\), both sides of the half-grid, three positive scaled times, one threshold time, and fixed-bin period-return displacements. Assertions compare the observations to the claimed universal signed logarithmic-coth profile and hyperbolic-tangent hitting clock with stated numerical tolerances.

The proof is not numerical. Its crucial quantified claims are the uniform return displacement on each fixed \([d,1/n-d]\), monotone trapping around its unique fixed point, a uniform Euler residual \(o(1)\) for the bounded transformed coordinate, and compact-time discrete-Gronwall convergence. These steps justify the limiting wave and threshold law, while finite checker runs only test consistency.

No uniform claim is made as \(n\to\infty\), for moving starting phases, or at scaled time zero. Bibliographic priority and correctness have not been independently audited.
