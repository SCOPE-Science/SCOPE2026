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

`verify.py` uses exact fractions to reconstruct the physical Pauli-channel weights, five rational instances of the exceptional-point Bloch matrix and their first fifteen powers. It checks equality with the rank-one power formula, the known optimal-step ties and numerical convergence to \(2s e^{-s}\) for four scaling parameters. The command `python verify.py` prints `PASS: 75 rational Bloch-power identities; Pauli CP checks; sharp-time ties; critical-scale limits.` when successful.

**Mathematical reach.** The exact unbounded-ancilla supremum is established by the trace-norm-duality proof and a matching pure-state lower bound in `RESULT.md`. Finite matrices alone cannot certify the supremum over ancillas or the asymptotic limit. The two channels are compared after uninterleaved repeated uses, not arbitrary adaptive interleavings. No independent audit is represented by this verification document.
