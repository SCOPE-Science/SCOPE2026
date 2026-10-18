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

# Reproducibility and limits
Run `python3 verify.py` with standard Python 3 and no third-party packages. The program independently generates the modal Boolean subalgebra by closure under the concrete finite forward-box operation and also iterates finite successor-type partitions. It exhaustively checks all 510 binary valuations on chains of lengths 1 through 8; it also checks 92 alternating chains of lengths 9 through 100. The expected terminal output is `VERIFY_OK: 510 exhaustive finite colored-chain cases (n<=8), 92 longer alternating chains.`

Finite chains are not a substitute for the infinite theorem. The infinite case is proved in `RESULT.md` using closure of the four-element algebra in the two-cofinal-colors case, a bounded morphism to the finite run quotient in the eventually constant case, and an induction giving exact depth-type counts. There is no independent mathematical audit.
