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

# Reproducible finite checks

`verify.py` is a standalone Python 3 script using only the standard library. In the same directory run `python3 verify.py`. For each site count from 3 through 6 it enumerates every permutation update order; for each site count from 7 through 9 it tests 101 deterministic update orders. It compares all states against the predicted number fixed by every power from 1 through twice the site count plus one, checks that the claimed global order fixes every basis state and that no prime-factor quotient is the identity, and checks direct primitive-cycle counts for a subset of orders.

Verified output terminates with:

```
VERIFY_OK fixed_comparisons 16089 map_order_comparisons 1173 primitive_period_comparisons 904
```

Finite computations neither establish the unrestricted theorem nor independently verify historical originality. The theorem's universal proof uses wall transpositions, a two-cycle split, two binary parity constraints, and a minimal-order argument. Independent scientific audit is not yet performed.
