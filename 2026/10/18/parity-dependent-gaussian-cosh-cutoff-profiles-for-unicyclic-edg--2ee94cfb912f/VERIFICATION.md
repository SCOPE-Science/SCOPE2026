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
# Reproducibility and limitations

`python3 verify.py` completes exact-rational finite-state checks for every feasible simple unicyclic example from three to eight vertices, including all cycle lengths and discrete times zero through four. It reports 2,757 exact checks. All graph kernels, the edge-coordinate cube push-forward, and the explicit Fourier chi-square formula are checked. This computation is finite and cannot certify the asymptotic claims; the proof in RESULT.md uses an independent analytic \(L^2\) Fourier argument, conditional Gaussian limits, and direct Gaussian moment calculations. The reference law in the even-cycle case is necessarily the currently reachable periodic class. No independent audit has been performed.
