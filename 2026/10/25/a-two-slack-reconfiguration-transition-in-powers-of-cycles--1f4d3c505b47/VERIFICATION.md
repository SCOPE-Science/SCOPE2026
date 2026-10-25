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

# Computational verification

The scripts use only the Python 3 standard library and construct their inputs from their own parameters. Commands run:

```sh
python3 verify_bruteforce.py > verify_bruteforce.out
python3 verify_gaps.py > verify_gaps.out
```

The first output begins `BRUTE_FORCE_OK 36` and the second begins `GAP_CHECK_OK 162`. Each line gives the cycle-power parameter pair, surplus, circumference, number of optimum configurations, exchange edges, components, and triangles. Both programs check all asserted finite-case formulas and adjacency constraints. The direct adjacency enumeration also checks that no admissible maximum-cardinality token jump exceeds cyclic distance two.

The direct enumeration covers \(2\le r\le5\), \(2\le m\le4\), \(s\in\{0,1,2\}\). The separate gap enumeration covers \(2\le r\le7\), \(2\le m\le10\), \(s\in\{0,1,2\}\). Each program was rerun from its packaged location. Tests do not replace the cyclic-gap proof for all \(r,m\).

The original published independence numbers and general maximum-set token-swap equivalence are background, not independently certified discoveries. No external independent audit has been undertaken.
