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

The exact-fraction checker `check.py` was executed with a standard Python interpreter and returned `Rational certificate PASS`. It independently recomputes the two integrated coverage polynomials, the lower bound \(29716847/62914560\), the antipodal upper bound \(181/384\), the strict atomic-law gap \(61807/62914560\), and the strict full-support gap \(15727/62914560\).

The remaining critical premises are established analytically in `RESULT.md`: independent thinning of Poisson arrivals, the union-length formula for two radius-\(r\) arcs, exact antipodal hitting geometry, the nonnegative signed Taylor remainders, and the full-support coupling. Code verifies algebra, not these infinite/probabilistic assertions. Neither a simulation nor an independent mathematical audit is claimed. The proof does not identify the globally optimal seed law or the exact Haar mean.
