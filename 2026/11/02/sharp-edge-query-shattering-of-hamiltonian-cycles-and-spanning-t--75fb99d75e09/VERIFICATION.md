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

All two-factors have degree exactly two and n edges. A shattered support with >=n-1 edges gives contradictions: any n-edge all-positive support exhausts a factor; any n-1-edge all-positive subset is a factor with one removed edge, hence a path plus cycles, and requiring all but an endpoint path edge forces that forbidden edge by exact degree deficits. Thus VC<=n-2. A path of n-2 queried edges on n-1 vertices plus one extra vertex is shattered by explicit Hamiltonian cycle block reorderings (k=1,2,3,>=4 cases), proving VC=n-2 for all n>=5 in both families. For n=3..7 exact integer edge masks exhaust 2-factors and Hamilton cycles; independent permutation-cycle generation and fiber-refinement VC counts agree, finite game recursion and complete tree witnesses prove Littlestone pairs (0,0),(1,1),(3,3),(4,5),(5,6). At n=7 all edges symmetric; the entire positive-first-edge version space fails depth6, so LD<7; depth6 witnesses exist. Independently reconstructed n=7 465/360 families, support polynomials [1,21,210,1190,3780,2520]/[1,21,210,1155,3465,2520], positive-branch upper failure; n<=6 corroboration. Finite n<=7 not extrapolated to higher n Littlestone.

## originality

PASS

Best-of-knowledge after actual Resultary search, direct primary theorem comparison and mathematical equivalence tests. None of the inspected statements logically dominates the complete final claim; sources and access risks below qualify historical-priority uncertainty.

## value

PASS

Hamiltonian cycles and spanning two-factors are canonical combinatorial concept classes for edge membership queries. Exact all-order static dimension, a concrete optimal shattered path support, the first strict static/adaptive gap, and fully classified small-order shattering profiles are mathematically natural reusable learning-complexity invariants. The nontrivial finite n=7 cutoff and differing support polynomials justify specific computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
