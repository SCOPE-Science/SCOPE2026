---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

At rho=1/10 the three full-rank source cone matrices have q=(1,1) interior, all A_rho send w=(1,1) strictly positive, and tau=1/5 dilation excludes f(0)-f(t) from the domination cone for all t!=0. Thus f(0) is Ch-quasi-proper non-dominated under the printed conditions, with affine f and strictly feasible g=-1. At t>0 both original row scalarizations of f(s)=(s,-s) are s; both subgradients are {1}, h derivative zero, all constraints inactive, so Theorem 4.1(a) requires 0=lambda1+lambda2 with positive multipliers, contradiction. xi=(1/2,1/2) has negative coefficient -1/2 in pointwise A_rho row basis; polar of common intersection cannot imply all pointwise polar memberships. Exact rational independent matrix checks confirm all sign inequalities.

## originality

PASS

The published theorem itself is contradicted; Theorem 4.1(a) and its proof on pp.12–13 of the full primary text are read. Fixed cone 2023 predecessor does not infer point-dependent polar decompositions. Targeted searches found no same counterexample/correction. Best-of-knowledge original for this model and theorem.

## value

PASS

A structural counterexample under every stated hypothesis invalidates a necessary multiplier theorem in a newly published variable-polyhedral-order result, directly identifying the polar-intersection-to-pointwise-polar mistake. This is a consequential counterexample, not a generic negative normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
