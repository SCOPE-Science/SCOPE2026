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

# Computational checks and limits

The standalone standard-library program `verify.py` directly builds the specified row/column equivalence frame and bidiagonal marking. It checks the exact finite-depth type formula for every \(n\) from \(3\) through \(70\), including the full-distinction threshold, and checks that ordinary type refinement stabilizes at two types.

To avoid relying only on the same recursive signature calculation, a second finite algorithm constructs pairwise counting-bisimulation relations by iterated back-and-forth using explicit perfect matching between the successor lists, and constructs ordinary back-and-forth through existential matching. It verifies identical terminal partitions for both logics on \(n=2,3,4,5,6,7\).

A third algorithm independently enumerates definable Boolean subsets with direct graded-counting semantics for each threshold and both modalities, closes them under Boolean operations, and compares the actual depth filtration on \(n=2,3,4\) to the predicted type counts.

**Executed command:** `python verify.py`

**Observed output:**

`VERIFY_OK 68 grid_sizes  2482 graded_levels  12 independent_pair_games  3 direct_boolean_semantics`

**Boundaries:** \(n=2\) is intentionally outside the separation theorem, but is included in computational consistency checks. \(n=3\) is the smallest admitted value. Direct Boolean-set enumeration scales exponentially and was only performed for \(n\le4\). The proof for all \(n\ge3\) is analytic, not a statistical extrapolation. An independent mathematical audit has not been performed.
