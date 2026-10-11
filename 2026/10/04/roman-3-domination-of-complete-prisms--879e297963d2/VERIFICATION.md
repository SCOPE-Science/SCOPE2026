---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For G_n=K_n square K_2, if a_i has label 0 or 1 its Roman-{3} constraint is exactly alpha+f(b_i) at least 3, with the symmetric condition beta+f(a_i) at least 3. If a feasible labeling has total weight at most 5, one layer has sum at most 2; sums 0 and 1 are immediately impossible for n at least 4, and sum 2 forces at least n-1 opposite-layer entries to be at least 1. This gives the sharp lower bounds 5 for n=4 and 6 for n at least 5. Tightness analysis gives exactly the eight n=4 minima, the 1225 balanced plus ten exceptional n=5 minima, and for n at least 6 forces both layer sums to equal 3, giving binomial(n+2,3)^2 minima. A fresh direct brute-force replay independently checked all 4^(2n) labelings for n=4 and n=5 and reproduced (5,8) and (6,1235); the package verifier additionally uses an independent aggregate dynamic program through n=60.

## originality

PASS

The inspected Roman-{3}/double-Italian literature gives general degree bounds, extremal-value classifications, and tree results, but no Cartesian-product or complete-prism formula was located. The n>=4 prism values 5/6 lie outside the small/near-order extremal classifications, and the complete minimum-function counts are strictly finer than the domination number. A targeted Resultary search returned related Roman variants on complete multipartite graphs but no exact Roman-{3} complete-prism theorem. Thus the all-n value and minimizer classification survive best-of-knowledge originality.

## value

PASS

Complete prisms are a canonical Cartesian-product family, and the result gives both the exact Roman-{3} domination number and a complete minimum-function census with two sharp small-size transitions. That is a natural exact classification of a standard graph family, not an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
