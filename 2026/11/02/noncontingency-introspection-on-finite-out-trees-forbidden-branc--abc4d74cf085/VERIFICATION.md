---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS: Δφ means truth constant over the immediate children, including 0/1-child vacuity. If a parent v and child u both branch, assigning p constant on children of v but differing on two grandchildren under u makes Δp(v)=true and ΔΔp(v)=false. If no such edge, a vertex or all its children are nonbranching, forcing ΔΔp everywhere. The correct labeled species split A=z(1+T) for nonbranching root, B=z(exp(A)−1−A) for branching root gives T=A+B and counts [1,2,9,64,565,6036,77749,1176736]. Smooth implicit-function transfer yields t_n/n^(n−1)~(c/sqrt 2)(e rho)^(-n) with rho≈0.446602824618744, c≈4.6404518492014, base≈0.8237284247. Independently reconstructed recurrence through n=8 and high-precision characteristic solution; finite enumeration does not replace asymptotic schema.

## originality

PASS

PASS (best of knowledge): Classical frame correspondence and general sequent calculi for noncontingency do not directly enumerate finite labeled rooted immediate-successor trees with no adjacent branching. The specific species equation and exponential density decay were not located in the inspected primary sources and semantically related Resultary records.

## value

PASS

PASS: A clean forbidden-local-structure characterization of a natural modal introspection axiom, paired with exact labelled counts, first failure, and rigorous asymptotics. It connects noncontingency frame semantics with a well-motivated species enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
