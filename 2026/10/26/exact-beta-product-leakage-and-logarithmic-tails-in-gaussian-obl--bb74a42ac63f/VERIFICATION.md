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

The mathematical proof in `RESULT.md` reduces the actual canonical lifted tangent projector to two scalar Gaussian slopes, identifies two independent beta ratios, and proves the leading tail coefficient using a one-dimensional convolution. It is valid for all stated dimensions and all independent real Gaussian sketches, not just the finite tested cases.

Run the included standalone program with `python verify_beta_leakage.py` in an environment containing NumPy and SciPy. This was executed from its actual complete package source, yielding `PASS 3221 checks`. It checks actual matrix projectors against the claimed \(2\times2\) block, verifies the reciprocal-beta expectation formula, compares four exact tail-integral evaluations with independent beta-product samples, and checks the asymptotic prefactor across three sketch sizes and large thresholds. It uses a fixed seed for reproducibility.

Finite simulations are diagnostics and cannot prove the Gaussian distribution or asymptotics. The source theorem concerns an instantaneous unit normal forcing and independent Gaussian sketches: it does not imply an infinite expected global integration error for any implementation, nor does it cover sketches conditioned on acceptable embeddings or finite precision. An independent audit has not been performed.
