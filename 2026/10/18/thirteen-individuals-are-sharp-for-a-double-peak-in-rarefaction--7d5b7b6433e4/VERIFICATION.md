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
# Reproducibility

Run `python3 verify_rarefaction_peaks.py` with Python 3 standard library. The execution returns exit code zero and prints census counts for each total \(3\le N\le13\), the unique qualifying profile, every exact variance, and a success statement. It checks both (i) the absent-species indicator covariance formula and (ii) a separate integer-coefficient multivariate-hypergeometric convolution for *all* classified census profiles. These yield exact rational moments; no Monte Carlo, floating-point threshold, random seeds, or external databases enter the correctness certificate.

The partition-recursion induction guarantees exhaustiveness of all positive-integer species abundance vectors up to relabelling, with counts \(3,5,7,11,15,22,30,42,56,77,101\) for census sizes \(3,\dots,13\). Censuses of size 1 or 2 cannot have two interior strict peaks because there are fewer than two interior positions. Source comparisons, interpretive ecological implications, and unknown larger-size behavior are not certified by the finite verifier. Independent scientific audit has not been performed.
