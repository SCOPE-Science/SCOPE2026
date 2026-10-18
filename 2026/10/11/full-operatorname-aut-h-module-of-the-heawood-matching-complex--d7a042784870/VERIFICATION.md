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

Actual finite Fano incidence matching complex has 21 graph edges and exactly (21,168,644,1218,1050,336,24) faces. The package computes F2 boundary ranks (20,148,496,722,312,24); the rational ranks match because the F2 values are lower bounds and the chain-complex dimension upper bounds force equality, proving sole reduced H4 of rank16. Independent enumeration reproduced all 3461 faces and 336 graph automorphisms. The signed simplex Lefschetz character and separate edge-orbit inclusion/exclusion computation agree on all 336; character types preserve: (1,16),(2,0),(3,1),(4,0),(7,2), exchange: (2,4),(6,1),(8,0). Sylow-7 eight-point permutation character minus trivial gives irreducible 7d module; the residual 8d character has self-inner product one and zero cross inner products, yielding rational 1⊕7⊕8.

## originality

PASS

The separate previously published Heawood matching-complex calculation establishes 16 four-spheres, but no corresponding 336-element action. Li’s equivariant log-concavity describes graded permutation representations of matching sets, not the alternating boundary-quotient homology representation. Donovan–Scoville study different graph families. The new exact group character and irreducible splitting are not implied by the known nonequivariant topology. Best-of-knowledge with unindexed equivariant table risk.

## value

PASS

The Heawood/Fano incidence graph is a canonical small highly symmetric combinatorial object. Exact action on 16-dimensional top homology, one-dimensional invariant line and 7+8 irreducible decomposition are natural equivariant invariants; they distinguish geometrically meaningful symmetry information that the known Betti number misses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
