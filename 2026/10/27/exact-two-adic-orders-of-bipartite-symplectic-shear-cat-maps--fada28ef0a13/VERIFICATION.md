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

Running `python3 verify.py` with a standard Python 3 interpreter produced:

```
VERIFY_OK: 476 exact matrix-order comparisons; base valuation and lifting comparisons for 64 bipartitions
```

The program uses integer modular multiplication and exponentiation and compares the asserted global order with its proper prime-divisor exponents. It verifies all bipartitions \(1\le a,b\le8\), moduli \(2^s\) for \(1\le s\le7\), and several larger bipartitions. It also checks exact base and first lifting valuations. The all-size theorem relies on the algebraic proof, not on extrapolation from the enumerated cases. No independent audit has been performed.
