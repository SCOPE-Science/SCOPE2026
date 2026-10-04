---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The symbolic proof classifies supports by cube-face adjacency and counts tile positions that do not touch a cube edge leading to an empty face. The accompanying exact script enumerates all nonempty proper subsets of the six cube faces and verifies the formulas for every integer \(n\) with \(2\le n\le100\).

Expected successful replay output begins with:

`VERIFY_OK n=2..100; all 62 nonempty proper face supports enumerated per n; formulas B1..B5 exact as positional capacities`

The finite replay is a consistency check, not an infinite proof. The extension to all \(n\ge2\) follows from the case-by-case symbolic counts in `RESULT.md`. The six-face term \(6n^2-3n+1\) is taken from the cited primary source and is not reproved by the script.
