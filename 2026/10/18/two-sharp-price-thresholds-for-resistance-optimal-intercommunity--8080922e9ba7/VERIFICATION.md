---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A connected feasible design exists (uniform cross edges), and tr(L restricted to the mean-zero space)^(-1) diverges on approach to a disconnected design. The trace-inverse Hessian in any nonzero symmetric direction is twice a squared Frobenius norm; off-diagonals recover independently chosen weights, so the global solution is unique and invariant under within-part permutations. The weighted spectral branches are U=px+qz, V=qy+pz and Nz with multiplicities p−1,q−1,1. At x=y=0 the larger part's per-budget marginal test binds first, at t_on=2p/(qH). For y=0, equality of the larger internal and cross marginals gives (U/z)^2=2D1/(tH_q); x>0 requires U/z>q, and the smaller part's inactive marginal requires U/z≤p. These crossings are t_on and t_fill; hence y is still zero at t_fill. With both parts active, U=V and (U/z)^2=2ND2/t, feasible precisely for U/z>p. Substitution in the budget gives the conductances; reciprocal minimization under a linear budget by Cauchy–Schwarz gives the stated total-resistance values, including the factor N. The matching spectral ratios at boundaries imply continuity, p=q merges the crossings, and leading powers give the fixed-q limits. The frozen exact-rational script was inspected, not executed, and is ancillary to the universal argument.

## originality

PASS

The supported distinct result is the unequal-size full phase diagram, in particular the larger-part-only interval with its second threshold. The exact equal-size specialization is separately covered and is not credited as distinct. Foundational convex allocation and general linear-budget optimality also are not claimed as new.

## value

PASS

For a natural design model, two explicit marginal transitions decide which edges can be dropped without sacrificing the global optimum. The unequal-size interval is not a guessed symmetric design: strict convexity certifies that asymmetric competitors cannot tie. The support law and exact weights are more useful than a generic convex program or the already covered balanced case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
