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

Use \(\texttt{python3 verify.py}\) in a standard Python installation with no third-party dependencies. The script independently forms every two-excitation basis state, computes the action of each phase-free Hermitian Pauli string, and compares the exact integer-scaled magnitude with the theorem for \(n=4,5,6,7,8\). It also compares a separate combinatorial count for the fourth Pauli moment with the claimed rational form at every integer \(n\) from \(4\) through \(30\). The expected terminal marker is \(\texttt{VERIFY_OK}\).

The enumeration is finite and is not used to infer statements at arbitrarily large \(n\). The proof's asymptotic arguments require the sub-Gaussian uniform-integrability estimate, the central limit theorem for Rademacher sums, and the explicit three-sector scaling calculation. No independent external mathematical validation has been performed.
