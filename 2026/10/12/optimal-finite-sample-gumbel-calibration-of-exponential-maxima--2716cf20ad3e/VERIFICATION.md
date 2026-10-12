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

# Reproducibility and verification

Execute `python3 verify_gumbel.py` with a Python 3 standard-library interpreter in the same directory as the other packaged files. The script needs no third-party Python modules and makes no network requests. The expected confirmation line is `VERIFY_OK roots=100 moment_pairs=500 quadratures=4 asymptotic_points=3`.

The script brackets and bisects the derivative root for \(n=1,\ldots,100\), verifies root order and improvement, checks 500 beta-moment pairs for the transformed sample minimum, and independently integrates the original log-density ratio at sample sizes \(n=1,2,3,5\). Three large-sample calculations corroborate the constants. These are bounded numerical checks, with integration truncation and floating-point error; they are not exhaustive proofs of all sample sizes or asymptotic conclusions.

The mathematical verification is the beta-integral identity, exact KL reduction, strict scalar convexity, finite-harmonic derivative comparison and Taylor argument supplied in RESULT.md. Reverse KL is infinite owing to support mismatch. No independent audit has been performed.
