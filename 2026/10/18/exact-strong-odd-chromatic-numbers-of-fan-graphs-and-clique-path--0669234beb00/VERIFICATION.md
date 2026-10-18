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

# Computational and analytical verification

The mathematical proof in RESULT.md is self-contained and applies to every positive integer clique order and path length. This file records supplementary finite checks, not independent validation.

Running `python verification.py` from the same directory completes three tests without dependencies beyond the Python standard library:

1. For each \(1\le n\le200\), verify the explicit seed construction has the asserted number of symbols, proper distance-two separation, and odd count for every nonempty symbol class.
2. For each \(1\le n\le80\), run a dynamic program over the final two colors and the parity mask of all color counts; check the least feasible palette equals the proposed formula.
3. For each \(1\le n\le12\), exhaust unlabelled color partitions of the path and evaluate the actual star-join graph directly. Test all graph edges for properness and every color on every open neighborhood for oddness. The resulting minimum numbers of path colors are \(1,2,3,4,5,6,5,4,3,4,5,4\), respectively. These computations do not appeal to the path-word characterization.

The direct search is exhaustive only for the specified finite lengths; the parity DP is also finite. Neither establishes an all-integers assertion. No external audit or validation has been performed.
