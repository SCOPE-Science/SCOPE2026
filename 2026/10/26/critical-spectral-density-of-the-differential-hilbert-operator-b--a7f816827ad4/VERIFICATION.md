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

# Verification information

The proof in `RESULT.md` explicitly derives the coefficient matrix, a uniform Hilbert–Schmidt reduction, trace moments of every positive integral order, the weighted spectral measure and the two concluding distribution formulas. The proof uses no unperformed external certification.

Run `python3 verify.py` with Python's standard library. The checker compares exact Mellin moments at \(s=1/4\), numerically integrates the analytic Fourier transform at three frequencies, and verifies Gamma-ratio approximation error scaling over a finite \(80\times80\) matrix sample. It prints the exact \(15\pi/8\) and \(225\pi^2/16\) constants. These finite checks validate arithmetic and numerical consistency only; the infinite theorem is justified by the written analytic proof.

The spectral comparison requires fixed \(\alpha\in(-1,0)\), sufficiently small positive \(\delta\), fixed threshold \(t>0\), and fixed real \(p\ge2\). No independent external mathematical audit is represented.
