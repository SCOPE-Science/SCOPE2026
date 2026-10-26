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

# Reproducible checks

Execute `python verify_random_contractions.py` from the package directory with standard Python 3. The verifier uses only the standard library and reconstructs maps as value tuples, not as a citation to any external artifact. It tests the binary normal form, exact biased and endpoint Bernoulli convolution on all maps through \(n=6\), all uniform product fibers and rank strata for \(n\leq6\) through three factors, and four factors for \(n\leq5\). It additionally tests exact rational rank sums for \(n=10,50,100\) and several factor lengths. Expected terminal string: `VERIFY_OK_BERNOULLI_CONVOLUTION_CONTRACTIONS`.

The finite enumeration does not establish the theorem for unbounded \(n\) or unbounded factor lengths. Those are proved by the conditional multivariate probability-generating-function identity in the accompanying result. No independent mathematical audit has been performed.
