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
# Verification

The integral in the proof is the even-index, zero-order specialization of the standard Macdonald integral and Theorem 16 in arXiv:2610.31368v1. Critical derivatives and the unique-saddle equation are explicitly differentiated and displayed in RESULT.md. The Gaussian expansion is analytical; it does not use extrapolation from numerical tests. There are no external certificates or independence assertions.

Run the self-contained diagnostic `python check_saddle.py` with the Python dependencies from `requirements.txt`; it checks twelve centered quadratures at positive arguments \(1/4,1,3,10\) and even orders \(60,200,600\). All twelve checks passed in the current package, with absolute rescaled residual below \(0.08\). These finite tests support computation consistency only and do not prove the asymptotic statement. The exact remainder is established by the localization and integrated expansion in RESULT.md.

Limitations: fixed real positive argument only; even differentiation index at zero order only. Independent audit is not performed.
