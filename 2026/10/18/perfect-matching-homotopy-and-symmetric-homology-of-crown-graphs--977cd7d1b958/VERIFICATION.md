---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For two or more unmatched rows, every leftover column has at most one forbidden row, so any set of at least two rows sees every leftover column, and a singleton sees at least one. Hall therefore proves the claimed extension criterion; a lone unmatched row and column must have different labels. Independently regenerated all nonempty faces for n=4,5,6,7 (99, 734, 6335, 61984), applied the specified toggle orders and topologically sorted each entire directed Hasse graph (228, 2320, 25290, 298788 incidences). It left exactly one vertex and 4, 33, 256, 2175 critical cells in degrees 1, 2, 3, 4 respectively. Discrete Morse theory then gives the wedges, since the only lower-dimensional skeleton is a point. In the reduced Lefschetz trace a setwise invariant k-element face with c vertex cycles contributes (-1)^(k-1) times (-1)^(k-c), with empty contribution -1. The independent oriented-simplex computation matched all 30 entries, both character averages 1, and transpose eigenspace dimensions 1045 and 1130. Replay: python3 /workspace/branches/3cca69d2-2b25-4196-8b52-dd76a6087e1e/crown_independent.py 4 5 6 7; the same directory contains crown_independent_n4.json and crown_independent_n5_n7.json. This is exhaustive only for the finite claimed cases; no homotopy formula for larger n or formal certification is assessed.

## originality

PASS

Best-of-knowledge pass for the joint finite homotopy classification and the n=7 equivariant calculation, not a claim that each constituent fact is exclusive. A later-dated indexed record states the identical n=5 wedge and a finer n=5 character calculation; the overlap is real regardless of priority. Neither that statement nor the inspected general or same-day statements cover the four-case result and the n=7 table.

## value

PASS

These are the first four positive-dimensional homotopy types in a natural family distinguished from ordinary chessboard complexes. Explicit integral wedge types are useful benchmarks for further crown complexes, and the seven-label character gives invariants of the natural symmetry action, including the nontrivial difference between the transpose eigenspaces that ranks alone cannot detect. The value rests on these exact structural results, not merely the computation or the overlapping n=5 subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
