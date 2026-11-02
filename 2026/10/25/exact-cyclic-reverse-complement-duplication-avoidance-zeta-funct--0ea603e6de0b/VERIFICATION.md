---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For complement a->3-a on four letters, forbidden windows have form (a,b,bar b,bar a). The 64-state order-three de Bruijn graph has allowed edges precisely when the length-four window is not forbidden. Labeled circular words of every n>=1, including periodic extension when n<4, biject with traced closed walks tr(A^n). Recomputed A independently and verified its entire degree-64 characteristic polynomial by exact integer symbolic factorization: x^36(x-1)^3(x+1)^3(x^2+1)^2 times the displayed cubic, squared quintic and companion quintic. Therefore det(I-zA)=Q(z) and formal determinant log gives exact zeta and all length traces. Burnside and Moebius give cyclic/primitive orbits; direct independent enumeration n=1..6 matches traces. The output does not claim physical duplication removal at n<4. Spectral dominance comes from isolated roots of the displayed polynomial; trace identity valid without numerical root approximations.

## originality

PASS

The relevant prior reverse-complement duplication research enumerates linear irreducibles and code capacities, not this explicit quaternary cyclic trace/zeta. Growth root from the cubic is known; the additional spectral factors and all labeled/necklace circular counts are the surviving claim. Equivalence to general transfer-matrix formalism acknowledged, not presented as novel.

## value

PASS

Periodic/necklace avoidance is a natural boundary-condition refinement of reverse-complement-duplication irreducibility for four-symbol DNA models. A fully explicit rational zeta polynomial, all lengths and primitive rotation classes are exact usable invariants that open-boundary growth formulas alone do not determine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
