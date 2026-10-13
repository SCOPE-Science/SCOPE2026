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
# Reproducible checks

Run `python3 verify.py` with Python 3.10 or newer; the file uses only the standard library. Its actual successful output is:

```
VERIFY_OK transfer_states=16 arcs=49 exact_determinant_newton_orders=1..16 cycle_parity_identity_n=3..60 cycle_closed_formula=3..120 brute_n=3..10 masks=1398080 all_coefficients=equal published_ungraded=3..12 published_minima=3..60
```

The verifier constructs the local transfer from its defining Boolean constraints; compares all coefficients against direct exhaustive enumeration of all 1,398,080 vertex subsets for graph orders 3 through 10; verifies all 16 coefficients of the exact integer-polynomial determinant through Newton identities; checks the parity formula through order 60; checks the cycle gap expression through cycle length 120; and matches published ungraded/minimum scalar data. The universal theorem relies on the parity-preserving bijections and cyclic gap count, not on the bounded enumeration. A successful local replay is not independent mathematical audit or an external certification.
