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

The included `verify.py` is a pure-Python, no-dependency, exact-rational checker. Invoke it with `python3 verify.py`. It independently enumerates all rank permutations and their associated conditional moments (not a simulation) and compares them against the record/maximum covariance formula for \(n=2,3,4,5,6,7\) and both coordinate-quantile exponents in \(\{1,2,3\}\). There are 54 exact permutation/kernel comparisons and 98 further harmonic checks over sample sizes 2 through 99, all passing in the recorded replay. The checker assumes explicitly stated power-law quantiles for those finite experiments; it does not exhaust all continuous marginal laws or all \(n\).

The general theorem is established by the proof in `RESULT.md`: independence of the sorted first coordinate and the reordered second-coordinate sample, relative-rank independence, conditional future-record probability, and the strict covariance identity for monotone functions of one nondegenerate random variable. Uniform specialization uses exact Beta moments, not numerical fitting. No external proof certification or independent scientific audit has been performed. Possible implicit historical coverage in broader record-process results remains a scientific limitation.
