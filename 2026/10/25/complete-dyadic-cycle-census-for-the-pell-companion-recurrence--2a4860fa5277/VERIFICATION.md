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

Run `python3 verify.py` with Python 3 standard library. It traces every state under \(T_k\) for \(1\le k\le8\), independently measures actual orbit length, compares every state to the claimed norm-valuation period, and compares the resulting cycle counts with the complete formula. Total independently traced starting states: \(87{,}380\). Each trace terminates at the starting state because the recurrence matrix has determinant \(-1\), invertible modulo \(2^k\).

This is a finite replay, not proof for unbounded \(k\). The universal result follows from the explicit \(\sqrt2\)-adic valuation identities and shell counts in `RESULT.md`. All mathematical limits and scope restrictions are stated there. No external validation has been performed.
