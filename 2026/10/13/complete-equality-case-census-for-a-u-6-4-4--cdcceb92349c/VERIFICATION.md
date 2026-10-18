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

Ulam d=6−LCS is invariant under common symbol relabeling. Fix identity among codewords; exactly132 other S6 permutations have d≥4, with 612 compatible edges among these 132. Independent exact LCS dynamic-programming enumeration gave 298 compatibility triangles and zero extendable triangles (so maximum4, no size5). Every triangle yields normalized four-word maximum, hence exactly 298*720/4=53640 labeled maxima; independently built and deduplicated all 53640. Each such maximum has all six distances exactly4. Independently enumerated 1440-group orbits using just transposition, cycle relabeling and position reversal generators; obtained 57 orbits (seven360, twenty-nine720, twenty-one1440). Checked every normalized maximum lacks subgroup closure, excluding left subgroup cosets. All counts are exhaustive finite calculations for S6, not extrapolation.

## originality

PASS

Göloğlu–Lember–Riet–Skachek give exact optimum A_U(6,4)=4 in their Table I, not number of optimal sets or their 57-orbit/coset/equidistance structure. Resultary older published complete Ulam census concerns (n,d)=(5,3), a different parameter cell and does not imply (6,4) equality classes. Metric, LCS bounds and sphere-volume formulas do not settle the extremizer classification.

## value

PASS

For a canonical small Ulam coding-theory boundary with known maximum size, the full 53640 count and 57 symmetry-orbit decomposition determine genuinely finer geometry; equidistance/no-subgroup constraints inform constructions and symmetry reductions, not an arbitrary restatement of known A_U(6,4)=4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
