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

# Reproducible verification

The included `artifacts/verify.py` uses the character vectors \(\chi_h(x)=\exp(2\pi i\langle h,x\rangle/q)\) with the complete constant-plus-one-coordinate frequency set. It builds the Hermitian concentration Gram matrix by summing only over words with exactly \(k\) nonzero entries. Its eigenvalues are compared with the four exact spectral sectors, each repeated by its claimed multiplicity. Small instances include composite \(q=4\), confirming that a prime-power assumption is unnecessary.

The second experiment evaluates \(R,U,T\) as exact Python fractions and compares their triple-equality condition against the integer congruence, for all \(3\le q\le15\), \(2\le n\le79\), and \(1\le k\le n-1\). No tolerance or floating-point threshold is involved in this check. The finite Fourier tests use the eigensolver tolerance \(10^{-10}\). Run from the package directory with `python artifacts/verify.py`; it needs NumPy. The analytic result is proved in `RESULT.md`, independently of these bounded calculations.

Scientific limitations: higher Fourier degrees, unions of shells, and degenerate shells are excluded. An equivalent earlier formulation in association-scheme literature remains an originality risk. This report is not an independent audit.
