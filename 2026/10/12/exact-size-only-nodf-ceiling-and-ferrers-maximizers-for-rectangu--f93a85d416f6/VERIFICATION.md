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
For binary matrices with both guild sizes at least two and with no zero row or column, the classical NODF definition assigns to a pair with unequal degrees the neighborhood-overlap fraction relative to the smaller degree, and assigns zero to an equal-degree pair.

The proved upper bound counts all such equal-degree pairs in the larger guild. If
\[
b=qa+r,\qquad 0\le r<a,
\]
then the unavoidable number of degree ties is
\[
(a-r)\binom q2+r\binom{q+1}2.
\]

The proof constructs Ferrers matrices attaining the upper bound, characterizes all equality cases and counts their distinct degree histograms.

The embedded `verify_shape_only_nodf.py` exhaustively checks all admissible labeled binary matrices for the ten shapes
\[
(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),
\]
amounting to
\[
176554
\]
matrices. For each it computes NODF by integer-scaled overlap fractions. It confirms the exact optimum, checks every maximizing incidence matrix for nested row neighborhoods, and verifies the predicted number of optimizing degree-frequency types.

It also checks explicit extremal constructions over a larger parameter grid. Those finite checks are independent corroboration and not substitutes for the all-dimensions mathematical proof.

Run:

`python3 verify_shape_only_nodf.py`

The first output line is `VERIFY_OK` only after every assertion passes. The source requires no external Python packages.
