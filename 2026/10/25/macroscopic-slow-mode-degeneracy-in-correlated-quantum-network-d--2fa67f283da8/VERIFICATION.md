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

# Reproducibility and verification

The analytic argument proves the full claim for all even network sizes at the specified parameter values; numerical samples alone cannot prove the theorem. The standalone script `artifacts/verify.py` reconstructs all edge exchange matrices, the community collective jump, and the coherent commutator independently from the stated definitions. It checks complete superoperator spectra for 9 combinations: \(N=4,6,8\) and \(\kappa=0,1/2,9/10\). Each combination checks the unique stationary eigenvalue, the exact slow decay rate, the predicted multiplicity, independent linear constraint-rank, the independent-edge spectrum and the explicit witness eigenoperator. All 63 assertions passed on the stated code. Use Python 3 with `numpy` and `scipy` as listed in `artifacts/requirements.txt`.

The primary mathematical evidence is the direct four-subspace decomposition of the edge dissipator, Hilbert–Schmidt dissipation bound, equality conditions, and exact unsigned-incidence rank computation in `RESULT.md`. Floating-point eigenvalue thresholds of \(10^{-8}\) are numerical checks, not proof of an infinite or exact parameter statement. The exact finite switching channel and \(\kappa=1\) are not covered; independent audit remains not performed.
