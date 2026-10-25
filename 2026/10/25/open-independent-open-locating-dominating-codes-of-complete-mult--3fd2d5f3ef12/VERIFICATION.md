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

# Verification record

The standalone program `VERIFY.py` checks open-neighborhood signatures directly in line graphs, separate from the structural proof. It exhaustively evaluates each possible selected-edge subset with a permitted number of disjoint two-edge-path pairs, and separately calculates predicted code counts using exact rational polynomial coefficients of the stated cubic exponential and using a recursive enumeration of triple blocks. Every multipartite integer-partition profile of total order 3–8 and at least two nonempty parts was included (57 profiles); all comparisons passed. The exact triangular-graph counts at 3 and 6 vertices, and the one-unused-vertex examples with part profiles (5,2) and (5,1,1), were checked separately. The displayed observations are not substitutes for the proof at arbitrary part sizes.

Run with Python 3: `python3 VERIFY.py`. The script uses only the standard library. The case distinctions in the proof apply to finite simple complete multipartite graphs with at least two positive part sizes. No computer-assisted inference is used to justify an unbounded quantifier. External independent mathematical validation has not been performed.
