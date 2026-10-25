---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Let T be the k 2-labeled rook cells, a covered rows and b covered columns. Every cell outside these rows/columns is forced 1, so weight>=2k+(m-a)(n-b); forced ones cannot neighbor any 2 and thus do not support them. For k<=m-3 weight>2m; k=m-2 equality forces isolated 2s and fails support. For k=m-1, inspect n>=m+2 and n=m,m+1, with support forcing weight>2m except small squares 2x2 and 3x3. For k=m all-zero remaining configuration requires covering all rows (or all columns in square boards) and every occupied column/row having >=2 defender 2s. Row maps with no singleton fibers count F_m(n)=m![u^m](e^u-u)^n. The exceptional boards contribute +9 at 2x2 and +54 at 3x3; totals 13 and 60. Brute independently checked all weight<=2m labelings for boards (2,2),(2,3),(2,5),(3,3),(3,4),(4,4): minima 2m and optimum counts 13,3,5,60,4,80. Source bundled verifier separately checks larger complete defender-map classes. This is a symbolic all m<=n >=2 classification supported, not proved solely by samples.

## originality

PASS

Compared this final statement and its strict logical implications against the actual pinned source proof and the named primary prior results. Gives full equality structure and labeled optimizer count for quasi-total Roman domination on a standard Cartesian product family, refining coarse general bounds and ordinary rook domination polynomial. Handles genuine exceptional square cases and captures occupancy-fiber combinatorics, a natural exact extremal classification.

## value

PASS

Gives full equality structure and labeled optimizer count for quasi-total Roman domination on a standard Cartesian product family, refining coarse general bounds and ordinary rook domination polynomial. Handles genuine exceptional square cases and captures occupancy-fiber combinatorics, a natural exact extremal classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
