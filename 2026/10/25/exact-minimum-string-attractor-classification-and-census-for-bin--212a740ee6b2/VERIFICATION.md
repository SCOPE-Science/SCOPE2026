---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every positive a,b,c,d the factor-occurrence definition forces γ≥2; an explicit three-position universal witness covers all factors. The proof partitions the complement of (a>c and d>b) or (c>=a+2 and b>=d+2) into four exhaustive size-two witness cases; constant-run factors plus the 10 boundary prove three distinct forced positions in the two exceptional regimes. Direct independent exhaustive factor-occurrence computation checked all 625 quadruples with 1≤a,b,c,d≤5; independent integer compositions reproduced exact generating-function coefficients for n=4..24. The all-positive parameter result follows from proof cases, not the bounded experiment. Counting both starting symbols yields 2(z^6+z^8)/((1-z)^2(1-z^2)^2) and limiting density 1/2.

## originality

PASS

A new all-positive-four-run parameter classification is not implied by the general string-attractor definition/bounds or the inspected morphic-word results. The disjoint exact obstruction inequalities and complete indexed census sharpen generic finite-word bounds. Equivalent/synonymous literature may be unindexed, so this is qualified priority only.

## value

PASS

A four-run binary word is a minimal natural test family for compact substring-index coverage with three transitions; the result provides a complete nontrivial threshold (two different obstructions), a constructive decision procedure for every four-tuple, and the exact proportion of exceptional indexed words. This is not merely a fixed-length brute-force table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
