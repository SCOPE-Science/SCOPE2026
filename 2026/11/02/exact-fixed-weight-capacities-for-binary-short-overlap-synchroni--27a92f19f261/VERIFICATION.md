---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The 1-overlap constraint makes every nonempty code choose a common first bit and opposite final bit; complement reduces to starting 0/ending 1. The four eligible 3-prefixes 000,001,010,011 have nested 3-suffix neighborhoods of sizes 4,3,2,1. Any code is contained in the rectangle for its largest occurring prefix, all rectangles valid for disjoint boundaries n>=6, and a weight-w slice contains coefficient of (1+z)^(n-6) H_j(z) yielding the four binomial expressions. Complement swaps orientations; coefficient asymptotics and exact adjacent crossings give all three density transitions. Independent code enumerated all 255 nonempty subsets of three-bit prefixes at 132 (n,w) pairs n=6..16 and matched the formula; logical nesting proof applies at every n>=6.

## originality

PASS

Best-of-knowledge qualified originality after exact statement/implication comparisons; primary work covers key ingredients, but the final parameter-specific classification is not established in inspected prior results. Residual risks explicitly retained.

## value

PASS

Constant-composition capacity under short forbidden overlaps is a natural coding problem, distinct from unrestricted code size. Exact four-term capacity and sharp golden-ratio changes in optimal word-boundary structure are mathematically meaningful nontrivial combinatorial classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
