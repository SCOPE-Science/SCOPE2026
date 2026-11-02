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

# Verification record

The analytic proof reconstructs the exact density of the last first-arrival time, the conditional winner distribution, the positive-truncated Poisson singleton probabilities, the size-biased Bernoulli sum, and the coordinatewise monotone likelihood-ratio lemma. The nonstandard step explicitly uses log-concavity of Bernoulli convolutions; the strict ordering is verified at the endpoints of the finite conditional support.

`python coupon_singletons_check.py` passed 16,538 assertions. The checks include random nonuniform vectors of 2 through 8 coupon types and an independent rational recursion for exact singleton distributions at four probability vectors, compared to separately integrated Poissonized densities. The integral quadrature is truncated at time 600; for the tested vectors the unintegrated completion tail is at most four times the exponential of minus 75, safely below the asserted absolute tolerance. The exact theorem does not rely on quadrature or simulated paths.

Limitations: the proof is for positive finite probability vectors, continuous completion times and ordinary iid coupon sampling. Numerical testing is not a proof beyond tested inputs. Literature priority has not been independently certified.
