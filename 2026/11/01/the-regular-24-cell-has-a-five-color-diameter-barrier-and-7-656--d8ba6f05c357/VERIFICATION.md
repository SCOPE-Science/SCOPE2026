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

# Reproduction and finite-certificate limits

Run the standalone artifact with a Python 3.9+ standard library interpreter:

```sh
python3 verify.py
```

The program reconstructs the 24 signed roots and their exact integer Gram matrix, enumerates all \(134596\) six-root subsets for nonnegative pairwise inner products, checks the 24 identified six-sets for seventh-point extensions, establishes no disjoint four-tuple, checks a five-facet cover for all 16 sign vectors, constructs an explicit eight-class cover, and enumerates every one of the 96 positive triples. The dynamic-programming exact-cover recurrence visits 12,367 used-vertex states and returns the exact integer coefficient vector \((8,0,0,0,2848,0,4480,0,320)\); its entries sum to 7,656.

All coordinate operations are integer and all counting operations exact. There is no floating-point comparison, randomized search, external computation service, or reliance on a previously produced log. Finite checking covers only the finite root configuration. The independent-audit channel remains unperformed; self-review does not substitute for an external mathematical check.
