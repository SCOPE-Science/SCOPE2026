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

# Reproduction and verification

Run `python3 verify.py` in the directory containing `verify.py` and `classification.json`. It depends only on the Python standard library. The checker exactly enumerates every labeled simple cubic graph on four, six and eight vertices using a vertex-by-vertex degree recursion; it then constructs all relabeling orbits of the supplied representatives and checks that they are disjoint and collectively exhaustive. Each adjacency characteristic polynomial is recomputed using integer trace/Newton identities, and each expected factorization is multiplied back to the integer polynomial. The explicit two-edge swap, triangle counts, and certified rational intervals for each algebraic coexistence threshold are checked.

Observed output:

```
ORDER_4_OK total=1 connected=1 classes=1
ORDER_6_OK total=70 connected=70 classes=2
ORDER_8_OK total=19355 connected=19320 classes=5
SPECTRA_EXACT_OK; one swap creates one triangle and lowers coexistence threshold
MINIMALITY_OK: unique strict inversion at order 8 (certified rational root intervals)
VERIFICATION_OK
```

The proof gives the exact ecological reduction from the adjacency spectrum and the Lyapunov convergence statement. These are mathematical arguments rather than inferences from finite numerical simulation. The checks do not establish any broader statement for graphs of differing degrees, directed interactions, or stochastic ecology. Independent scientific validation has not been performed.
