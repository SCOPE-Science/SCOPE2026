---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Vertices with a fixed coordinate support form false-twin classes, so any resolving set must contain all but at most one vertex of every nonempty proper support class, giving the base term \(N-(2^n-2)\). For a binary coordinate, the class of support \([n]\setminus\{i\}\) is a singleton whose sole neighbor class of support \(\{i\}\) is also singleton; domination therefore forces exactly one additional landmark for each binary factor, and these forced pairs are disjoint for \(n\ge3\). The matching upper construction chooses all but one per support class and includes the required binary singleton vertices; coordinate singleton landmarks then separate every pair of omitted vertices. Fresh exhaustive searches for \((2,2,3)\) and \((2,3,3)\) independently returned the formula values \(5\) and \(8\). The frozen verifier was read and checks a wider bounded grid.

## originality

PASS

The 2023 primary full text was read. Its resolving-domination theorems split into two homogeneous regimes: all field orders two give \(\gamma_r=n\), while all field orders at least three give \(\gamma_r=N-(2^n-2)\). It does not state the mixed-order formula. The later dominant-metric paper studies other rings and general bounds; the 2026 semisimple-ring work treats determining number and metric dimension, not resolving domination. Fresh Resultary search returned the audited record as the exact mixed-product hit.

## value

PASS

The formula completes the natural mixed regime left between two published endpoint theorems and identifies exactly why \(\mathbf F_2\) is exceptional: each binary coordinate creates one unavoidable domination surcharge beyond the twin-class resolving bound. That structural explanation is reusable for related support-class graph invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
