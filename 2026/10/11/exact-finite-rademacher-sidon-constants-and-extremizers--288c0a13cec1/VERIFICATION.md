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

For coefficients a∈ℂ^n, signed-sum convex hull equals zonogon Z=Σ[-a_j,a_j] with circumradius M and perimeter 4Σ|a_j|. If there are d nonparallel generator directions modulo sign, Z has m=2d≤2n sides. Every convex m-gon inside the centered radius-M disk has perimeter ≤2mM sin(π/m) by moving genuine maximizing vertices to the circle then Jensen on central-angle gaps, equality iff regular. Since m sin(π/m) grows strictly for m≥2, Σ|a_j|/M≤n sin(π/(2n)). Equal modulus and evenly spaced directions modulo sign give regular 2n-gon and attain equality. Conversely, equality forces m=2n, all generators nonzero/nonparallel, regularity, hence precisely equal modulus and those directions. The n≥5 theorem follows without extrapolating finite tests.

## originality

PASS

Best-of-knowledge implication-level comparison of the complete final claim with the identified primary literature. Prior ingredients and asymptotic/general tools are explicitly credited; no inspected publication entails the complete exact conclusion. Any incomplete access is preserved below as a named residual risk, not incorrectly counted as negative science.

## value

PASS

A natural finite-dimensional Sidon constant has exact sharp dependence on n and a complete extremizer classification. The result quantifies the gap below Seigner’s infinite π/2 constant and identifies uniquely regular-zonogon rigidity; exact constants for finite coordinate systems are useful even if the limiting constant is classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
