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

The finite classification is rebuilt from first principles by `verify_bgs_s4_counts.py`.

* Vertex set: the sixteen four-bit vectors, encoded by integers \(0,\ldots,15\).
* Matching enumeration: repeatedly pair the least unused vertex with each possible partner. This is bijective with unordered perfect matchings and returns \(2{,}027{,}025=15!!\).
* Profile extraction: each edge contributes the nonzero XOR of its endpoints; each matching profile is sorted canonically.
* Independent domain enumeration: every nondecreasing eight-tuple over \(1,\ldots,15\) is generated exactly once and retained exactly when its XOR is zero. The result is \(20{,}295\) admissible profiles.
* Exhaustiveness: the admissible-profile set equals the set produced by the matching census exactly.
* Counts: the verifier checks the complete sixteen-row multiplicity histogram, its total profile count, and the multiplicity-weighted total of all perfect matchings.
* Boundary characterization: exactly fifteen profiles have one realization, all are constant; every nonconstant profile has realization count at least four.

The verifier stores no list of matchings or accepted profiles, so the central table is recomputed rather than merely compared against a packaged certificate. A separate optimized C++ implementation of the same canonical matching recursion was run during review and independently produced the same totals and histogram.

Unproved limits: no higher-dimensional extrapolation, orbit classification, or closed formula for \(R(M)\) is claimed. Literature search is evidence for originality, not a proof of novelty.
