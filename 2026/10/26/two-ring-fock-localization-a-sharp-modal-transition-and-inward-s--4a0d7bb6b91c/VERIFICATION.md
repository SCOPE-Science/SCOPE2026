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

With Python 3.10 or newer and SciPy 1.8 or newer, run `python verify.py`. The test integrates each of the two finite squared-radius intervals using the normalized gamma density, then counts discrete modal sign changes for 21 parameter pairs and checks the direction and approximate asymptotic coefficient of the two-peak gap. It also tests the odd correction formula at six Gaussian critical points. The captured console output is in `verification_output.txt`.

The actual infinite-parameter arguments are analytical: exact radial Toeplitz diagonalization, a four-term exponential-polynomial zero bound, differentiated uniform Stirling expansion, strict Gaussian-mixture critical-point classification, and a parity-breaking cubic correction. Numerical agreement does not establish an asymptotic remainder bound, uniqueness of continuous roots outside a tested range, or historical novelty.
