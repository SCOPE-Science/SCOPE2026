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

The proof was checked directly from the source's printed resource states and Bell-measurement wiring. The exact resource factorizations are
\[
\lvert\Omega_1\rangle=\lvert\Phi^+\rangle_{m_1A_3}\otimes\lvert\Phi^+\rangle_{m_2A_2}\otimes\lvert\Phi^+\rangle_{m_3A_1},
\]
and
\[
\lvert\Omega_2\rangle=\lvert\Phi^+\rangle_{m_4B_1}\otimes\lvert\Phi^+\rangle_{m_5B_2}\otimes\lvert\Phi^+\rangle_{m_6B_3}.
\]
The mentor pairings therefore route \(B_1\) to \(A_3\) and \(B_2\) to \(A_2\). Direct Bell-bra contraction gives local Pauli maps on each route, and tensoring them yields the fixed SWAP on the source's named physical output order.

`artifacts/verify.py` was executed from the packaged path and returned `VERIFY_OK`. It uses only exact integer arithmetic. It checks every Bell-label combination for one chain, both resource factorizations, and the all-plus basis witness. Its finite checks corroborate the symbolic derivation rather than replace it.

Unproved limits: no statement is made about noisy dynamics, hardware fidelity, or whether an implementation silently interprets the logical output order as \(A_3,A_2\). The result is a correction of the ideal named-output recovery rule.
