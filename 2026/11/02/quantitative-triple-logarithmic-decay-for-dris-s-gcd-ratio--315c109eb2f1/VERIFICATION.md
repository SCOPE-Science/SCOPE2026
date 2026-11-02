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

# Verification scope

Run `python3 verify.py` using Python's standard library. The recorded result is:

```
VERIFY_OK gcdn_counts=100000 source_cutoffs=5 witness_primes=5 crt_residues=196
```

The verifier tests \(100000\) GCD identities, matches five earlier tabulated counts, and checks the local cyclotomic obstruction for five primes and a small CRT probability exactly. Its finite computations do not prove the asymptotic triple-logarithmic rate. That proof invokes Turán–Kubilius with a uniform constant, the Siegel–Walfisz estimate for growing small moduli, and the Mertens theorem in one residue class. No independent scientific audit has been performed; the asymptotic constant may be ineffective.
