---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For nearest-neighbor symmetric walk with observations S0…Sn sorted with ties, minimum multiplicity R_n yields states (0,0),(0,1),(1,1) except the unique-next-level endpoint event (1,2). Decomposing at min visits yields formal generating functions A(z)^2 E(z)^(r−1), A=(1+(1+z)/sqrt(1−z²))/2, E=(1−sqrt(1−z²))/2; R=2 has mass 1/4. Unique minimum and adjacent level at an endpoint has c_n=binom(n−2,floor((n−2)/2))/2^(n−1), so the four exact joint masses follow. Their TV distance to (1/4,1/4,1/2,0) is exactly c_n. Independently enumerated all 8188 paths over 2≤n≤12 with exact rational matches. Proof is the generating-function argument for all n≥2, not enumeration.

## originality

PASS

Pitman–Tang proves joint limiting lower order statistics and TV convergence, and Kirschenhofer–Prodinger develops Catalan minimum/return path counts; neither inspected material gives the exact finite n four-atom two-gap law or exact c_n TV rate. The older Aneja–Sen (1972) paper has an extremely plausible rank-order-statistics title but full text unavailable after lawful attempts; no whole-document noncoverage assertion, explicit residual risk.

## value

PASS

An exact finite-horizon two-dimensional lower-order-statistic law and sharp total-variation profile refine a published limit theorem and yield a reusable finite-sample quantitative benchmark; endpoint parity matters. Exact self-contained law is mathematically natural, not just a finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
