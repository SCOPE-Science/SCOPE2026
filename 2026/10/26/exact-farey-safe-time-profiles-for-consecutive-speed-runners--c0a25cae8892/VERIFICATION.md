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

# Verification details

Run `python3 verify.py` using Python 3 with the standard library. It evaluates every unsafe arc from the original speed list with exact `Fraction` endpoints, handles circular wrap by integer shifts, merges these arcs, and compares the uncovered length to a separate coprime-denominator-pair implementation. This is an independent computational encoding of the main formula (not an independent proof).

The execution returned `CERTIFICATE_OK sizes=20 exact_profile_points=480 kink_classifications=20`. It covers all integers \(2\le n\le21\) and 480 explicitly constructed rational thresholds, including reciprocal breakpoints, midpoints, zero, the union-bound threshold, and the critical endpoint. It independently enumerates attained denominator sums to check each parity breakpoint prediction, verifies the benchmark totient identity, and checks the reduced-residue harmonic formula for the final linear segment.

All comparisons use exact rational arithmetic with no numerical tolerances. Computational coverage is finite; the proof in `RESULT.md` establishes the result for arbitrary \(n\ge2\) and all real \(\delta\ge0\). The classical Farey-neighbor lemma and the totient-sum estimate are mathematical inputs, not separately machine-certified lemmas. Independent mathematical validation has not been performed.
