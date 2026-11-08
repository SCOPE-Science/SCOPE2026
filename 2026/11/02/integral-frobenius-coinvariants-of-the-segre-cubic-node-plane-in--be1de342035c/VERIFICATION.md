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

Node labels are unordered partitions of six coordinates into triples and plane labels perfect matchings; a node lies on a plane when each matched pair crosses the triple. The resulting 10×15 incidence has each row sum 6, column sum 4, II^T=4I+2J, rank mod2 5 and an explicit determinant-64 maximal minor. Combined with the degree map to Z/4, these force Smith nontrivial factors (2,2,2,2,4). The mod2 node-indicator construction identifies Q/2Q as F2^6/<ones> with its natural S6 action; quotienting by permutation gives c(σ)-δ(σ) mod2 generators, while the preserved degree map forces exactly one order-4 factor. Independently built the incidence via matchings and obtained the exact same Smith invariants and determinant 64; the source verifier checks all 720 S6 actions and eleven Frobenius types. The result concerns incidence coinvariants, not geometric Picard/Brauer groups.

## originality

PASS

Classical Segre accounts give ten nodes, fifteen planes and S6 action, and forms classification, but the inspected statements do not compute this integral incidence cokernel and full Frobenius-coinvariant family. Best-of-knowledge PASS with a real residual risk from classical combinatorial design Smith-form tables.

## value

PASS

Integral incidence torsion and Frobenius coinvariants are natural arithmetic refinements of the classical node–plane design, including a uniform order-four obstruction across all eleven forms. This is an exact structural invariant not implied by point counts or rational permutation representations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
