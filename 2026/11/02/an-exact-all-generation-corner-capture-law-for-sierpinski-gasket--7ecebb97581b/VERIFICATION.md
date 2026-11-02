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

# Reproducible checks

Run `python3 check_sierpinski.py` with a standard Python 3 interpreter. No external libraries or downloaded datasets are needed. The script constructs all six finite graphs directly from the recursive triangle geometry, checks their vertex/edge counts and degrees, then computes the span of successive adjacency powers applied to the three corner vectors using two distinct prime fields. The independently calculated ranks are \(3,6,11,21,41,81\) for levels \(0,1,2,3,4,5\). In addition, for levels zero through two it computes exact rational resolvent entries by solving the full matrices at \(z=10\) and compares them with the two-channel decimation formula.

The entire family is not certified by checking six levels. Its proof is the general midpoint-elimination identity, the reduced rational-polynomial degree induction, the spectral residue rank identity, and the finite-dimensional absorption argument in `RESULT.md`. Modular agreement does not establish equality over the rationals in general; the independent exact rational checks address the low-level starting equations. Only the stated finite checks have been executed; no independent external audit or physical experiment has been performed.
