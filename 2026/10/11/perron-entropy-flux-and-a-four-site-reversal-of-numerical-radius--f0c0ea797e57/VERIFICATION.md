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

The proof derives the exact spatial numerical-radius variational formula for real and complex \(\ell_p\), invokes the simple Perron eigenvalue at \(p=2\), and differentiates the uniquely persistent local optimum. The explicit four-site eigenvector and characteristic identity give the two opposite limiting derivative signs, while the three-site calculation fixes the minimal dimension.

Run `python3 verify_entropy_flux.py` for high-precision example checks and independent power-iteration comparison. The expected output is `ENTROPY_FLUX_NUMERIC_CHECK_OK`. Finite tests cannot certify derivative limits or all positive weights; those are established by the stated analytic expansions. The recent general \(\ell_p\) numerical-range preprint was not fully inspected.
