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

# Verification of the scalar normalization theorem

The public `artifacts/verify.py` uses Python 3.9+ standard library only. Execute with `python3 artifacts/verify.py` from the extracted package root. It prints `PASS: 3970 finite exact-rational and numerical assertions` on successful completion.

The verifier uses exact rational arithmetic to check that the cubic example has precisely the proposed two radii and two-step multipliers. It evaluates the original normalized-gradient formula, compares its parameter threshold with the unique critical point of the scalar denominator on randomly selected real exponents, numerically solves both sides of the two-cycle level equation, checks each orbit and local stability, and probes the predicted square-root coalescence. It also checks strict contraction at sampled subcritical points and the algebraic relaxation constant on selected nonterminating trajectories.

The proof of universal convergence is not by sampling. It follows from the exact minimization of a strictly convex radial denominator. The uniqueness of each cycle branch follows from strict derivative signs on each side of its critical point, the stability classification from exact Jacobian substitution, and the asymptotic from a limiting reciprocal-power increment. Finite tests do not prove absence of other periodic orbits, finite-precision robustness, global basin geometry, or historical priority. External independent validation remains unperformed.
