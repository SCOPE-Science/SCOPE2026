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
# Reproducibility and current evidence

Use `python3 verify.py` with Python 3 and no external packages. The standalone script enumerates every unordered target pair, computes exact equal-distance vertex subsets from a distance table, and independently constructs all theorem-predicted maximal failure subsets. For each tested parameter, it verifies exact equality of the **entire families**, the predicted resolving number and the Laurent-coefficient maximum over all Hamming distances.

Tested parameter families: \(q=2\), \(d=1,2,3,4,5\); \(q=3\), \(d=1,2,3,4\); and \(q=4,5\), \(d=1,2,3\). All 15 cases passed in the supplied run. Some outputs are \(H(1,2): (\operatorname{res},\#\mathrm{failures})=(1,1)\), \(H(4,3):(28,48)\), \(H(3,4):(33,18)\), and \(H(3,5):(76,30)\).

Independent proof verification has not been performed. This finite enumeration is not evidence for untested dimensions; the quantified infinite conclusion follows from the coefficient count, convolution monotonicity and equality-case proof in `RESULT.md`. Priority searches are fallible and residual priority overlap is acknowledged in `REVIEW.md` and `AUDIT.json`.

