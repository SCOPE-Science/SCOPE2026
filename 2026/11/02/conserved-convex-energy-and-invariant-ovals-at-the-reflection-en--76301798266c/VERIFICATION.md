---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

From ω=2 Sinkhorn ratio updates U+=g_c(V)^2/U and V+=g_c(U+)^2/V, where g_c(t)=(ct+1)/(t+c). Both maps are global involutions, determinant -1 in log-odds; composition determinant +1. The rational first integral J=(UV+c(U+V)+1)/sqrt(UV) is invariant because the first reflection exchanges the numerator summands after writing J linear in sqrt(U), and likewise for V. In log coordinates J=2cosh((X+Y)/2)+2c cosh((X-Y)/2) has positive-definite Hessian (det=c cosh((X+Y)/2)cosh((X-Y)/2)>0), proper compact strictly convex level ovals and unique minimum at origin. |φ_c'(y)|≤|1-c|/(1+c)<1 excludes other fixed points. Exact preservation of area and H forces commutation with the nonzero Hamiltonian field; on every oval this is a rigid time shift, so periodic or dense, recurrent and never convergent to origin. Independent symbolic checks verified both involution invariants and Hessian determinant for arbitrary positive symbols; c=1 degeneracy remains a valid half-turn map.

## originality

PASS

Best-of-knowledge PASS for identifying the exact ω=2 2x2 symmetric Sinkhorn endpoint with a globally proper strictly convex first integral and all-oval rotation/nonconvergence classification. A general QRT symplectic-first-integral principle is prior, and ω<2 convergence theory is prior, but neither inspected primary source identifies this specific Sinkhorn map plus its entire real positive energy-level geometry. Possible prior QRT embedding is explicit residual risk.

## value

PASS

The relaxation boundary excluded from standard convergence theorems has a qualitatively different global dynamical regime: every nonfixed scaling remains on a compact invariant oval rather than converging. The explicit global Hamiltonian and rotation dichotomy are structurally useful for understanding numerical parameter choice, not merely a local stability computation or renaming of an abstract QRT map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
