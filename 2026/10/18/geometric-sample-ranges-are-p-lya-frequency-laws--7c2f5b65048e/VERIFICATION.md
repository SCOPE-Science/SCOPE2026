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

The proof derives the distribution generating function for arbitrary finite sample size by a tie-broken sorting bijection, then invokes the published real-rootedness theorem for the exact same descent/comajor polynomial. A normalized product of independent Bernoulli and geometric generating functions follows. Total positivity is proved by nonnegative Toeplitz factors and Cauchy–Binet, not by enumeration.

The standalone `geometric_range_check.py` file was run with Python standard library arithmetic and returned `PASS 288 exact coefficient/normalization checks; counterexample discriminant -15`. It computes the probability of ranges independently by subtracting exact CDF values and checks the numerator using direct permutation enumeration for every integer sample size from two through seven at four rational parameters. The counterexample uses an exact polynomial with nonreal zeros. These tests do not cover arbitrary sample sizes or continuum parameters and are not a replacement for the proof.

The primary literature comparison includes accessible indexed portions of the original 2023 discrete-order-statistic result and the original §5.1 proof of the q-Eulerian real-rootedness theorem; an explicit older range formulation may have escaped indexing. Independent audit remains unperformed.
