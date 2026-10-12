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

# Verification and limits

The reproducibility code `verify.py` is standard-library Python 3. Run `python3 verify.py` in the extracted file directory. It exhaustively checks the maximal-subset-product ratio bound for 8,063 finite integer-log configurations, including ties, varying dimensions and all face sizes in its enumerated ranges. The checker was executed against the very file included here and returned `PASS: 8063 exact winner-gap and subset-product comparisons`.

The mathematical verification is principally analytic: the joint CLT with identical limiting Gaussian variances yields the strictly positive random order-statistic gap; the prefix/suffix construction makes the winner selector asymptotically prefix-measurable; a nonresonant independent suffix kills each fixed nonzero integer Fourier coefficient; the finite-label Fourier characterization forces label–phase independence; and an exact deterministic product-ratio inequality makes the maximum asymptotically dominate the face sum.

The verifier does not exhaust infinitely many lengths, distributions, base values or frequencies. It does not check that a given application satisfies independence, equal logarithmic moments or nonresonance. No machine-formal or independent external proof audit has been performed. Possible equivalent coverage outside inspected literature remains a scientific priority risk.
