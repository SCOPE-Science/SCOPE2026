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

The crown automorphisms are simultaneous permutations of matching indices and optional side swap. Properness restricts cross-side shared colors to unique diagonal pairs; distinct ordered color pairs eliminate all simultaneous-permutation stabilizers, and at least one nondiagonal pair removes side swap. Choosing t shared diagonal positions/colors, a and b exclusive palettes and injective onto placements in a-by-b cells gives precisely the U(a,b;n-t) inclusion-exclusion formula with no quotient by color labels. The optimal mixed threshold follows by maximizing t+floor((k-t)^2/4) for 1<=t<=k-2 and the known k=ceil(2sqrt(n)). Check n=3 separately. This is an all-n,q bijective argument, not an extrapolation from brute force.

## originality

PASS

The final claim was independently compared at statement/implication level against the identified closest original publications and targeted semantic finding searches. Specific prior components are credited and the remaining claimed addition is identified. Residual priority/access risks remain and this is best-of-knowledge, not universal certification. Exact proper distinguishing-coloring enumerator of crown graphs and the mixed-palette threshold.

## value

PASS

The entire labeled proper symmetry-breaking coloring polynomial and its mixed-color optimal stratum are natural exact combinatorial invariants of the crown family, beyond the previously determined minimum palette size. The shared-palette refinement is mathematically useful for exact symmetry-breaking enumeration; the onto-injective rectangle count and exceptional threshold are nontrivial, rather than mere renaming of chi_D.

The dated certificate retains the supplied scientific assessment, sources and limitations.
