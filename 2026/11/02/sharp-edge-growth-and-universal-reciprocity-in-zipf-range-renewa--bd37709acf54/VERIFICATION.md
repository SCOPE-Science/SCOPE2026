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

# Verification of the Zipf edge and reciprocity theorem

The complete proof is supplied in `RESULT.md`. The standalone standard-library `verify.py` independently enumerates small discrete words and checks both ordered and unordered pattern-avoidance recurrences against their exact expected edge statistics. Actual checker replay: `PASS 7030 finite exact and supplementary numerical assertions`. The script was run from the newly produced package content. The final package replay must match this output. The checker additionally tests divisor multiplicity and numeric values of the integral in the proof.

The finite assertions cannot verify the infinite-dimensional Poisson approximation, the weighted divisor limit or the almost-sure convergence; those are established analytically in the proof. They also cannot certify the novelty of the result against all existing literature. No independent audit has been performed.
