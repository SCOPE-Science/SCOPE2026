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

# Verification record

The included `verify.py` was executed with the active Python interpreter using only the standard library and returned `CHECK_OK`. Its Decimal arithmetic (150 significant digits) checked six cases: confidence parameters \(\delta=1.2,2,3.5\) and steepness \(\gamma=30,40\). For each case it reconstructed the exact equilibrium function from sigmoid weights, bracketed the two positive roots, checked analytic derivative signs and alternating drift directions, and compared the leading separator and outer-attractor asymptotics. It does not exhaust the continuum of model parameters or replace the proof.

The proof in `RESULT.md` is responsible for the all-sufficiently-large classification. Its nonstandard steps are the uniform derivative bound before the confidence boundary, strictly positive second derivative inside the interior layer, and strict negative derivative inside the final exponentially thin boundary layer. The asymptotic expressions are obtained from the exact scalar equilibrium equation. All model hypotheses and excluded cases are stated in `RESULT.md`.

Self-review passed. Independent scientific audit not performed.
