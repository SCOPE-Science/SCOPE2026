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

# Reproduction and limits

Execute `python verify.py` with NumPy and SymPy installed. The checker reconstructs the *actual* full kernel and source-defined block preconditioner matrices, compares the symmetric generalized spectrum with the derived three-value formula across 1,392 parameter settings, establishes one rational symbolic spectrum exactly, and performs exact-rational CG with and without the block inverse. It prints two `PASS` summaries on success. No external data, internet service, or third-party paper is needed to rerun the checks.

The universal spectral identity, strict ordering, and optimality of the local obstruction rest on the exact proofs in `RESULT.md`; finite numerical cases are supplementary. The CG-step statement is exact-arithmetic and generic-right-hand-side, not a finite-precision runtime guarantee. The validity of a source preconditioner on other kernel families has not been established. No independent review has been performed.
