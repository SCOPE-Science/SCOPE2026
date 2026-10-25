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

The analytical proof establishes the distribution, integrability cutoff, and sharp minimax negative-risk bound for all admissible real symmetric positive-definite matrices and all finite sketch dimensions. The supplied `verify.py` reconstructs the generalized pencil directly and checks Gaussian risk frequencies against the Student distribution for five row counts and three two-eigenvalue spectra, without extrapolating the finite experiments to an infinite proof.

The critical equality is the exact endpoint coefficient-of-variation identity. Its simulated validation uses a fixed seed and explicit tolerance. Input and output scale do not affect the negative-value event. Numerical tests can miss the rare extreme tails where moments diverge: the rigorous density-at-zero proof establishes those tails.

Reproduction: install the packages in `requirements.txt`, then execute `python verify.py`. No external datasets or files are required.
