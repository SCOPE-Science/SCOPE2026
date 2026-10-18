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
# Verification

The mathematical proof reconstructs the conditioned Crofton measure and yields an exact edge-pair overlap formula for each dimension \(n\ge3\). The squared-mean subtraction is explicit. The binomial mismatch count and normalization limits, including negligibility of exponentially small mismatch counts, establish the claimed constant; no extrapolation is used.

Run `python checks/verify.py` in an environment with NumPy. It samples the width-biased normal directly using a size-biased half-normal coordinate, checks the known means in dimensions three through five, and tests the independent random-edge overlap representation up to dimension 512. A fixed pseudorandom seed makes simulations reproducible. Tests are supplementary and statistical, not formal proof certificates. No independent audit or external validation has been performed.
