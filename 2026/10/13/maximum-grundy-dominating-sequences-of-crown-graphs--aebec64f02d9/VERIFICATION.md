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

The package includes `verify.py`, which constructs each crown graph directly from the deleted-matching definition and independently recomputes closed neighborhoods. For each \(n\in\{5,6,7\}\), it performs two checks.

First, a global dynamic program over covered and used vertices computes the maximum length of a legal closed-neighborhood sequence and confirms that it equals \(n\).

Second, every \(n\)-vertex subset is examined. A dynamic program over internal orderings counts exactly how many legal dominating orders that fixed set has. The result is compared with the four structural types in RESULT.md, including the forced versus two-way terminal order in the two-light-side cases. Aggregate maximum-set and maximum-sequence counts are then checked against
\[
2+n(n-1)(2n-1)
\]
and
\[
4n\,n!.
\]

A successful replay prints `VERIFY_OK n_range=5..7 maximum_sets=1062 maximum_sequences=160800 max_order=14`.

The finite replay does not certify the theorem for arbitrary \(n\); the proof in RESULT.md establishes the general statement.
