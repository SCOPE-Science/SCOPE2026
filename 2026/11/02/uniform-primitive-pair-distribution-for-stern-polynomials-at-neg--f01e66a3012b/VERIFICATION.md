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

The package includes `verify.py`, a standalone Python 3 standard-library program. Replay with `python3 verify.py`. It independently compares direct Stern recurrence values against binary digit matrix products for indices \(1\leq n\leq50000\). For \(36\) odd moduli it exhaustively enumerates the matrix orbit and compares it with the full primitive pair set and its exact Jordan-totient size, and separately checks marginal residue counts. The observed successful replay is `VERIFY_OK recurrence_indices=50000 moduli=36 primitive_states=84992`. These computations verify only the tested finite instances. The symbolic matrix identities, all-modulus transitivity argument and finite-chain convergence proof are documented in `RESULT.md`. Self-review passed; no independent mathematical audit was performed.
