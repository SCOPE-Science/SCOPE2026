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

A standalone Python 3 standard-library script `verify.py` recomputes the edge list of \(P_n^2\) from scratch, builds the third-edge conflict relation directly, and enumerates all binary subsets of edges for \(0\le n\le11\). This direct check never invokes the tile characterization. It compares the complete coefficient dictionary with two independent analytic descriptions: a tile-start recursion and the binomial formula.

For \(12\le n\le50\), the tile recursion is compared against the binomial expression and the six-case optimum/maximum-multiplicity formulas. These latter checks do use the structural model and are not independent infinite certificates. The exact replay command is `python3 verify.py`; the output from the packaged source is `verify_output.txt`.

The general claim is proved by the unique tile decomposition, formal-series summation, vertex-budget bound and slack enumeration in `RESULT.md`. Finite verification neither substitutes for those arguments nor establishes priority. Independent audit status is not performed.
