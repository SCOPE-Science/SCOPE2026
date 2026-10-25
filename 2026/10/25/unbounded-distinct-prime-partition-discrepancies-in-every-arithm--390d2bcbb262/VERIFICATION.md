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

# Reproducibility checks

Run `python3 verify.py` using the Python standard library. A successful run prints `VERIFY_OK` and a summary. The script tests the residue-class formula exhaustively over 120 moduli, finite CRT divisibility/coprimality for each unit class modulo at most 13 and small gaps, and the factorial inequality over 99 integers. These are necessary finite checks of the algebra, not an exhaustive proof of infinitely many primes.

Infinite existence follows from the specified applications of Dirichlet's theorem, the distinct-three-prime consequence of Vinogradov's theorem, and the exact deductions in `RESULT.md`. No claims of independent replication, external certification, or computational proof of the prime-existence theorems are made.
