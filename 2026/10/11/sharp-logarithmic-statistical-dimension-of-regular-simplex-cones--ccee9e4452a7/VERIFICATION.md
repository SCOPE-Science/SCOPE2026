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

The rigorous proof derives the exact Gaussian projection equation, identifies its pooled-leaf count with the conic intrinsic-volume index, obtains \(u_m^2\sim2\log m\) by Mills-ratio estimates, and proves both a probability limit and uniform integrability with a Gaussian/Chernoff exceptional-set bound.

Run `python3 verify.py` using only the Python standard library. In the current supplementary run the checker produced `VERIFY_OK checks= 8267`, including two independent finite projection implementations, angular checks in dimension two, and Gaussian threshold statistics. These finite tests check implementation and signs but cannot prove the limit.

The pre-existing all-dimensional **finite** conic intrinsic-volume formula is Theorem 2.4 of Kabluchko–Seidel (arXiv:2006.09492). Only the sharp asymptotic leading logarithmic behavior is assessed here. No independent audit has been performed.
