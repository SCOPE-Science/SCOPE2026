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

The companion `verify.py` computes divisor sums independently for odd primes below 50 and positive exponents \(a\le20\), \(b\le4\), compares both GCDs against the modular-order/LTE criterion, and enumerates exponent-square counts for selected fixed primes at \(N=30,100,1000\). It uses only the Python standard library. Run `python3 verify.py` from the extraction directory. Finite computations test cases and boundaries; the infinite proof is given in RESULT.md. The primary source's relevant complete arXiv HTML was inspected. A closely related squarefree-support result was compared via its accessible summary, not its inaccessible complete proof. No independent audit has been performed.
