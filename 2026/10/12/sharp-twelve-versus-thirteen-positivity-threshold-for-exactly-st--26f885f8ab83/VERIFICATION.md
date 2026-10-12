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

# Reproducibility

Execute `python3 verify.py` from the extracted directory with Python 3 and no third-party packages. The checker derives the three low-index scalar BDF2 formulas by exact arithmetic over rational coefficients of \(1\) and \(e^{-s}\), evaluates rigorous rational exponential Taylor intervals at seven rational arguments, and confirms the strict negative-diagonal witness for thirteen vertices without floating-point sign decisions. It also samples 30,000 positive stepsize values and 69 subsequent steps for supplementary stress testing (2,070,000 comparisons). Expected output begins `VERIFY_OK`.

The exact-rational tests provide a finite check on stated inequalities and symbolic formulas; the proof in `RESULT.md` separately covers every real positive stepsize and every natural time index. No independent audit or external certification has been performed.
