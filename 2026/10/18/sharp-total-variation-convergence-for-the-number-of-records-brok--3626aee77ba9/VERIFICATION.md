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

# Verification protocol

The accompanying `verify.py` uses only the Python standard library. Execute it from the directory containing the supplied file with `python verify.py`. It constructs the finite-horizon law in two independent ways (conditioning on the number of past values below the arriving observation, and exhaustive relative-rank enumeration), performs exact generating-function and signed-law comparisons using `fractions.Fraction`, and evaluates the one-crossing total-variation expression numerically over increasing sample lengths.

The formula for the limiting rate is established analytically by an independent-record decomposition, log-concavity, and Fourier-inversion local central limit bounds. The finite checks do not provide an infinite proof. No external, independent audit has been conducted.
