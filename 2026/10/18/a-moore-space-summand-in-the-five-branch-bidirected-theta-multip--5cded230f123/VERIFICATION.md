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

# Reproduction and limits

Execute `python VERIFY.py` followed by `python REDUCTION.py` in a directory containing both scripts. Python 3.10+ and SymPy 1.12+ suffice. Their recorded output is in `REPLAY_OUTPUT.txt`. Every face is generated from scratch; the first enumeration tests all arc sets of at most four arcs, and a second, structurally independent path-union enumeration matches it exactly. The four-arc bound is a graph-theoretic bound, not a computational cutoff.

There are 710 nonempty faces, 2180 covering incidences, and 297 matched pairs. A complete Kahn topological sort checks the acyclic matching. The projected integral boundary matrices have shapes 1x1, 1x42 and 42x72 and Smith forms `(0)`, `(1)`, and `(1 repeated 40 times, 2, 0)`, respectively. The integer chain condition is checked exactly. The last matrix digest is `26dee90726943f7c3d97fb478986efdeaa598fe9e1ab7a78c2d3c1226e6f6dd9`. An independent integer unit-pivot reduction produces 40 unit factors and a residual row of gcd 2.

The elementary-CW argument in `RESULT.md` uses the critical cells to show simple connectivity before invoking Hurewicz and identifying the three-cell attaching maps. It is a finite mathematical proof conditional on the stated, completely replayable enumeration and matrix calculations. No claim for larger graph parameters or independent validation is made.
