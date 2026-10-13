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

# Reproducibility of the local threshold calculation

Run `python verify.py` with Python and SymPy. The checker constructs the infected-compartment transfer matrix and new-infection matrix, tests the complete symbolic three-by-three reduced reproduction matrix, then substitutes the published-model parameter witness as exact rational numbers. Successful observed output included `VERIFY_OK`, the exact matrix entries, corrected reproduction number approximately \(1.95814334397992\), and the printed comparison value \(7/8\).

The checker validates symbolic linear algebra and exact arithmetic, not an experimental dataset, an undisclosed simulation, or the general next-generation spectral theorem. The proof uses that established theorem to infer the strict disease-free local stability and instability cases. The equality case, global dynamics, empirical implications, and any corrected biological mechanism are not proved.
