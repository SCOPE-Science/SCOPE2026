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

# Verification

The mathematical claim is established by the case-decomposition and fixed-pair coupling proofs in `RESULT.md`. To replay finite exact-rational checks, run:

```sh
python verify_involution_filtration.py
```

Observed result: `PASS: 675381 exact assertions; enumerated all involutions for n=2..10`.

The Python 3 script requires no external packages. It enumerates every involution on \(n=2,\ldots,10\), checks exact class cardinalities and expected inversion counts, checks every ordered position pair's inversion probability in each class, verifies the odd increment identity for every possible pair of fixed points, and confirms each possible target receives exactly \(k+1\) preimages. Further rational calculations for \(n=3,\ldots,120\) check the spatial slope, global sum, and strict increase between adjacent classes.

No finite enumeration is used to infer that an infinite-range assertion holds. The proof of the spatial formula and strict monotone coupling applies to all integer parameters in the stated domain. Exhaustive checks are limited to the specified finite sizes. Broader historical priority and independent mathematical validation remain open.
