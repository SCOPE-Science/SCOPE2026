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

# Computational verification and proof boundaries

The included `verify_lunar_five.py` is a standalone Python 3 checker using only the standard library. It generates all positive factor exponents for one two-point and one three-point factor, computes the actual Minkowski sums as integer sets, deduplicates output supports, and compares the result against the closed formula for every degree \(4\le m\le130\). As a separate shape-completeness boundary test, it enumerates all nontrivial factor-support pairs of sizes two, three or four for degrees \(4\le m\le14\); the outputs coincide with the two-by-three census. Running the actual source produces:

`VERIFY_OK: 127 degrees m=4..130; independent 2-by-3 enumeration; all factor shapes m<=14; closed counts.`

The finite checks do not prove the all-degree result. The proof instead requires: (i) the sumset lower bound and equality case, (ii) classification of the single overlapping shifted element of a three-point set, (iii) injectivity and one arithmetic-progression overlap of the two families, and (iv) exact inclusion–exclusion. No symbolic or computational oracle is assumed in these universal steps.

No independent external audit or validation has been performed.
