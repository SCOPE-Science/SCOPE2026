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
The companion `verify.py` uses Python's standard library to integrate the normalized Gaussian multiplier, check its finite moments, check the rational Milstein coefficient identity, and quantify the local small-step residual. It is an auxiliary numerical reproducibility check: the all-step, all-state and strong-convergence assertions rely on the mathematical proof in `RESULT.md`, not finite enumeration.

To replay: `python3 verify.py`. The generated `verification_output.txt` is its recorded output under standard double-precision arithmetic. The normalizer in the theorem means its *exact mathematical integral*; a finite-node quadrature approximation changes the scheme and need not preserve conditional mean exactly.
