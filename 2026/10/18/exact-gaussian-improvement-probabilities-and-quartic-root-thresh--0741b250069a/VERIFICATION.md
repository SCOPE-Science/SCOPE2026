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

Run `python verify.py` with NumPy and SciPy installed. The program constructs the actual Nyström matrices and their symmetric inverse square roots, then compares exact numerical spectral condition numbers with the derived rational formula. It also computes regularized incomplete-beta tails, simulates independent Gaussian sketches, and checks critical-window approximations. A successful run prints `PASS: 1108 finite numerical/distribution checks`. Universal claims are established in the written mathematical proof; finite checks do not certify them. No external independent audit or infinite-dimensional theorem is asserted.
