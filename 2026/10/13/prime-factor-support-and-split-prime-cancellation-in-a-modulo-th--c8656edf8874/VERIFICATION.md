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
# Verification notes

The `verify.py` program is a standalone, Python-standard-library finite check. It independently calculates the defining bounded-multiplicity partition numbers modulo \(3\) up through \(n=1200\), enumerates every Gaussian representation with the required congruences, and compares the absolute signed sums with the stated prime-factor formula through \(n=9999\). It verifies a nontrivial zero from split-prime cancellation at \(N=629\).

These calculations establish correctness only for the stated finite ranges. The theorem for unbounded indices follows from the formal theta identity, the invertible norm parametrization, unique factorization in \(\mathbb Z[i]\), and a local orientation-parity proof. No external certification or independent audit was performed.
