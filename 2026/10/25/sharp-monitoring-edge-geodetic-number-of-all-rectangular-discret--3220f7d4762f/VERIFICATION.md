---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

In C_m□C_n (5≤m≤n), every Cartesian-direction edge can be monitored only by a selected pair with identical other coordinate. Therefore all n column sections must be cycle MEG sets and require three selected vertices each: meg≥3n. The cycle criterion is exactly that consecutive selected cyclic gaps be ≤floor((r−1)/2); the balanced 3-offset construction with column shift floor(jm/n) controls every column and every row by B=ceil((ceil(m/3)−1)n/m)+1. Two-step induction in n proves B≤floor((n−1)/2) outside (5,6),(7,8). Explicit 5×6 and 7×8 binary placements handle exceptions. Independently verified section certificates on 1575 rectangles including both exceptions. The proof of unbounded n relies on the integer-gap induction; finite testing is not a proof.

## originality

PASS

Haslegrave (2023) gives the Cartesian section criterion, general product bounds and meg(C_m□C_m)=3m for squares; those results do not imply equality 3n in nonsquares. Foucaud–Pandey–Paul (2025 preprint, 2026 journal) classify distance-hereditary, P4-sparse, bipartite permutation and strongly chordal graphs, none containing every rectangular torus with induced long cycles. Their primary text mentions neither torus nor Cartesian products as a solved class. No covering exact formula found in product-network literature surveyed, though a separate product-networks journal work was not read in full.

## value

PASS

Exact all-aspect-ratio Cartesian torus monitoring-number classification closes the gap between known lower/upper bounds. The explicit optimal 3-per-column construction and exceptional templates solve a natural fault-detection placement problem beyond square tori.

The dated certificate retains the supplied scientific assessment, sources and limitations.
