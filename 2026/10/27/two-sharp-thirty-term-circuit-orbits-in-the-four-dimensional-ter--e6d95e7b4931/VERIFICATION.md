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

# Certificate replay

Compile the self-contained `verify_fourcube.cpp` with a C++17 compiler using `c++ -O2 -std=c++17 verify_fourcube.cpp -o verify_fourcube`, then execute `./verify_fourcube`. The checker exhaustively tests all 6,010,004 rooted supports using integer fraction-free determinants, verifies the asserted best length and root counts, and computes the two order-384 signed-coordinate-permutation orbits. Expected single-line output:

```text
CERTIFICATE_OK tested=6010004 positive=120560 max=30 rooted_max=156 orbit_count=2 orbit_sizes=384,384 distinct_maximizers=768
```

The verification has been executed from the source included here. A separate cofactor-Laplace implementation and independent exact symbolic computation of both representatives agree. The rank-four algebraic reduction is proved in `RESULT.md`; finite enumeration is exhaustive for that explicitly restricted domain. It is not evidence of an unrestricted five-support optimum.
