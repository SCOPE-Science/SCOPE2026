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

Every algebra automorphism is parametrized by (A,u)∈GL₂(q)×(F_q²)* with φ(v)=Av+u(v)z, φ(z)=det(A)z. Radical fixed points solve (A−I)v=0 and u(v)+(det A−1)t=0; the whole fixed space gains scalar line 1. Split determinant!=1 (a 1-eigenvector iff conjugate diag(1,det A)), A=I, nonidentity unipotent det1, and remaining SL₂(q) with no 1-eigenvectors; all disjoint and exhaustive. Counts yield N1=q³(q+1)(q−2)², N2=2q⁵−q⁴−4q³−q²+q, N3=(q+1)(q²−1), N4=1, summing q²|GL₂(q)|. Radical orbits: zero, nonzero socle, nonzero linear part; independently enumerated every (A,u) for q=3 and q=5, yielding {1:108,2:291,3:32,4:1} and {1:6750,2:5105,3:144,4:1}, verifying formulas and Burnside 3q. Field-independence of counts proves extension fields, not prime-only finite checks.

## originality

PASS

Best-of-knowledge priority for the precisely delimited contribution. Known subfamilies, classical inputs, and plausible stronger derivations separately documented; searches alone are not treated as a novelty proof.

## value

PASS

A complete fixed-point-dimension distribution of all automorphisms and the precise Burnside orbit count are natural finite representation invariants of the fundamental smallest nontrivial exterior algebra. Unlike the group-size formula alone, the four fibers provide exact statistics usable in invariant theory and enumerative algebra; mathematically motivated albeit narrow, not a generalization to higher-rank exterior algebras.

The dated certificate retains the supplied scientific assessment, sources and limitations.
