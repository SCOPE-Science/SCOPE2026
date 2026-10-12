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

The proof is symbolic and complete within its three-prime-support domain. The arithmetic derivative formula and Euler product give \((24-7a-5b)r=35c+24\), and the proof checks every possible \((a,b)\) pair by congruence. The two Dirichlet progressions are coprime to \(35\), giving infinitude through a standard external theorem.

Run `python3 verify.py` with Python 3.8 or later; no third-party modules are required. It enumerates primes through \(9999\), exhausts positive \(a\le4\), \(b\le6\), and solves the linear equation for \(c\) exactly, comparing the result with both classification branches. It also checks the two displayed small cases by integer arithmetic. This tests arithmetic and boundary bookkeeping, not the infinitude conclusion.

The evidence consists of an explicitly supplied proof and reproducible finite tests. It is not an independently verified or independently audited result.
