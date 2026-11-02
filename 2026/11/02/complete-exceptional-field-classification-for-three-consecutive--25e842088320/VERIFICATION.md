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

# Reproducible finite computation and proof limits

The attached `verify_ns3.py` is a standalone Python 3 program using only built-in exact arithmetic. Execute `python3 verify_ns3.py`. The observed output was:

```
VERIFY_OK primes=5037 extensions=77 exceptions=35 limit=105841
```

The code (i) sieves all primes below the analytic threshold; (ii) tests for a length-three NS3 witness for every prime of the required congruence class, exhausting all starts only for exceptions; (iii) independently enumerates all prime powers of the required congruence class below that threshold; (iv) checks each extension-field polynomial's irreducibility by finite-field factor criteria and confirms the listed multiplicative generator is primitive; (v) verifies explicit positive witnesses; and (vi) exhaustively scans negative extension fields using direct power tests. Exact integer field polynomial arithmetic is implemented inside the program. The certificate list and all algorithms are present; no third-party tables or packages need to be downloaded.

This finite program does not prove the infinite tail. That requires the sixth-order character expansion and the stated Weil estimate for complete character sums over finite fields. Conversely, the character estimate alone does not prove the 35 exceptional orders. Both parts are necessary.

The precise exception list and logical quantifiers are given in `RESULT.md`. Checks were completed before this package was finalized. This is a self-review only; independent audit has not been performed.
