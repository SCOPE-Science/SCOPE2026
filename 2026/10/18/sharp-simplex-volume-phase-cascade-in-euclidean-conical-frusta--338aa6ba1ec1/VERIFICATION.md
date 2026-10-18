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

Place `check_frustum.py` beside `RESULT.md` and run `python3 check_frustum.py` with Python 3 (standard library only). The expected final line is:

`PASS: 486 constructed layer configurations, 5400 random contained simplices, 9 dimension phase lists, and high-dimensional consistency checks.`

The source file constructs centered regular-simplex vertices in orthogonal subspaces, reconstructs their determinant in dimensions \(2\) through \(10\), samples general feasible frustum vertices in dimensions \(2\) through \(6\), and checks the exact adjacent-score transition ordering. The analytic correctness of all dimensions and the continuous radius range depends on Proof Steps 1–5 in `RESULT.md`, not on these finite trials.

The closest archival mathematical source is Lassak (2011), DOI 10.1007/s13366-011-0026-x; another important related theorem is Horváth and Lángi (2014), arXiv:1402.6496. McKinney (1974), DOI 10.1112/S0025579300005763, could not be inspected in full, and independent mathematical and historical-priority checking remains outstanding. No Lean, external certification, or independent audit is claimed.
