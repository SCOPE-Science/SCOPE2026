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

# Verification of the all-excitation Dicke damping formula

Run `python verify.py` from this directory with NumPy installed (`requirements.txt`). The verifier independently applies local Kraus loss masks in the computational basis and computes the full symmetric-logarithmic-derivative spectral sum for 75 combinations with \(3\le N\le7\), \(2\le k<N\), and \(p\in\{0,0.2,0.53,0.9,1\}\). It also compares 95 independently constructed Boolean-lattice inclusion Gram spectra against the proposed exact eigenvalues, checks both endpoint identities for 230 cases with \(4\le N<24\), and checks the analytical first-order late-loss slope in four separate examples. The observed maximum full-matrix Fisher discrepancy is \(3.2\times10^{-14}\), within the stated numerical tolerance \(10^{-9}\).

Expected terminal line: `VERIFY_OK dense_qfi=75 inclusion_spectra=95 endpoints=230 late_slope=4 max_error=3.2e-14` (small variations in the last floating figure depend on the BLAS implementation). No finite enumeration is presented as an all-size proof; the raising/lowering argument establishes that proof in `RESULT.md`.

For the boundary expansion, the proof explicitly computes the zeroth and first damping-order eigenvalues and shows all omitted Fisher terms are second order. This includes transitions to zero-eigenvalue sectors. No independent audit, external certification, or experimental validation is claimed.
