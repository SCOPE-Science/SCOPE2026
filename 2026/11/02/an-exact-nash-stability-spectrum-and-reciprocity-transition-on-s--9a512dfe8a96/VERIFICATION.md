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

# Reproduction and limits

Run `python verify.py` using Python 3.9 or later and only the standard library. The program enumerates all signed hub–leaf valuation profiles for zero through five leaves, and independently tests every coalition partition under direct strict unilateral Nash deviations. It compares the observed Nash partition count with the independent labeled-block recurrence, and the observed existence with the derived exact criterion. In one full run: 1,365 profiles, 222,233 profile/partition comparisons, all assertions passed.

The supplementary exact-rational checks independently weight all profiles for one through six leaves at reciprocity values \(0,1/4,1/2,3/4,1\). They compare the exact probabilities at zero and full reciprocity, plus the complete critical even/odd parity law, for 30 parameter pairs. All assertions passed.

The deterministic proof covers all finite signed stars, and the stochastic proof separately invokes concentration, the triangular-array central limit theorem, sign-reversal symmetry, and Vandermonde's identity. The finite enumeration is not an exhaustive verification for arbitrarily many leaves; the code cannot independently establish the limiting probability law or publication priority. No independent audit has been performed.
