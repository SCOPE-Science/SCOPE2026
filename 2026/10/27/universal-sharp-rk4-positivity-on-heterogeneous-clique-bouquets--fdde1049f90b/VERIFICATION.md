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

The proof is analytical and is not inferred from a finite census. Run `python verify.py` in this package with the pinned dependencies in `requirements.txt`; the script verifies algebraic reflection, scalar RK4 positivity, the across-petal quadratic certificate, exact rational polynomial transition identities against independently assembled graph Laplacians, and high-precision boundary probes. No internet access or external datasets are used.

The polynomial reflection identity is valid because \(\rho^3-4\rho^2+12\rho-24=0\). The proof of spectral stability uses the exact eigenvalue \(n\), not numerical estimates. The high-precision checks at steps immediately past \(\rho/n\) show the predicted hub transition sign but do not certify the theorem for infinitely many graphs. No independent audit was performed.
