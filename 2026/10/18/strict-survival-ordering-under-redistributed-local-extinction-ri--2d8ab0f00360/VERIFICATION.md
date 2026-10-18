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

The standalone `verify.py` reconstructs the stated transient generator and uses exact symbolic algebra to check the determinant, survival Laplace transform, all three resolvent cofactors, the product sensitivity identity, and the exact mean and mean derivative. It checks the displayed rational example, then compares survival probabilities from finite matrix exponentials across 216 positive-time rate allocations.

The Python verification command is `python verify.py`; dependencies are SymPy, NumPy, and SciPy. The script's finite grid is not exhaustive for all admissible real parameters or continuous times. The universal strict sign follows from the explicitly proved convolution of positive transient kernels, not from testing. At zero recolonization the separate triple-exponential kernel proof is required. The corresponding cited 2001 conservation study remained inaccessible in full, so possible earlier equivalent work is an originality limitation; no independent assessment is claimed.
