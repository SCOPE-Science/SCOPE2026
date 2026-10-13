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

Run `python3 verify.py` with the Python standard library. The script constructs the proposed and alternative length-eight codebooks from explicit five-component column vectors, independently computes every output's ML likelihood, and verifies the complete success-polynomial coefficient vectors.

A first exact method enumerates all \(256\) possible received words and expands each maximizing probability as an integer polynomial in the Z-channel flip parameter. A second method computes the maximum of five exact `Fraction` likelihoods separately for six rational flip probabilities. Both reproduce the two analytic formulas. An exact fraction comparison at \(p=9/10\) yields a strict improvement in average correct-decoding probability of \(1044981/250000000\), with no floating-point step.

The polynomial argument in `RESULT.md`, not numerical testing, establishes the interval of strict improvement for all \(\rho<p<1\). The verifier only corroborates the finite polynomial calculations. No codebook global-optimality search or independent external audit is claimed.
