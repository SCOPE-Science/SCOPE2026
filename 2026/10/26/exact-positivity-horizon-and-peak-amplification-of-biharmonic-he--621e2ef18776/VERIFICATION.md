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
# Reproducibility of sharp rook-graph formulas

Run `python verify_rook_biharmonic.py` with Python 3.9 or later, NumPy, and SciPy. The script constructs \(L=a(I-J_a/a)\otimes I_b+bI_a\otimes(I-J_b/b)\), forms \(\exp(-tL^2)\) independently using matrix exponentiation, and compares its entries against the proposed four-type kernel and maximum-row-sum identity for all pairs \(2\le a,b\le7\). It also tests the uniqueness-regime signs, critical times, balanced exact constants, and numerical convergence of the thin-board asymptotic statements.

Actual execution result: `PASS: 6465 finite-matrix identities and asymptotic consistency assertions`.

The numerical cases and floating-point comparisons do not prove the theorem for untested integers or limiting regimes. The proof in RESULT.md establishes all quantifiers; the checker is a consistency and transcription safeguard. Independent scientific review and priority verification have not been performed.
