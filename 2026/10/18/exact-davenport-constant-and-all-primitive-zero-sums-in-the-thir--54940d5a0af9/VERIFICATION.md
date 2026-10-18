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

# Reproducibility and limits

Run `python3 verify_ball2.py` from the package directory. The checker is standalone and uses the Python standard library only; its expected status begins `CERTIFICATE_OK`.

The checker confirms 13 lattice points of squared norm at most four, and 21 lattice points of squared norm at most five. The latter bound uses the established planar Euclidean Steinitz theorem; it is not inferred by computation. It inspects all \(64\binom{25}{4}=809600\) bounded four-dimensional free-multiplicity choices for length at most 21. Each candidate is solved by an exact two-pivot determinant calculation, and primitive zero sums are retained by increasing-degree antichain elimination. The checker independently scans all direct six-variable multiplicity assignments up to length nine, checks every reported primitive multiset against every proper submultiset, and classifies maximal multisets by eight square isometries.

Expected outputs: 40 primitive nontrivial-pair multisets (12 of length three, 16 of length four, 12 of length five); together with the zero singleton and six opposite pairs, 47 in total. The maximal length is five; there are twelve maxima, in orbits of sizes four and eight with respective support sizes five and three.

Exact arithmetic is used throughout. Exhaustive finite checking becomes a proof of the infinite-length exclusion only in conjunction with the proven length-21 upper bound. No external formal verification or independent review has been performed. Remaining risks include subtle implementation mistakes and undiscovered earlier equivalent claims.
