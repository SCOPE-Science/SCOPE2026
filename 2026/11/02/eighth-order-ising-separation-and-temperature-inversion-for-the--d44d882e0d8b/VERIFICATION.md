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

The accompanying `verify.cpp` constructs both graphs from explicit Latin squares. It tests the Latin conditions, shared strongly regular parameters, nonisomorphism via the \(K_4\) counts, and sharp lower bounds for all subset sizes. Independent Gray-code bitset and row-wise occupancy recursions each exhaust all \(2^{25}\) subsets for each graph and compare the complete pair of integer induced-edge histograms. Integer binomial moments verify the sixth- and seventh-order symbolic factorizations, the eighth-order total moment \(-24576\), and direct physical eighth-order energy-moment identities at four test fields. The field-general theorem is algebraic, not inferred from those four tests. All stated low-temperature multiplicities are exactly enumerated.

Compile and run:

```sh
c++ -std=c++17 -O3 verify.cpp -o verify
./verify
```

Required final output includes `MOMENTS_OK` and `VERIFY_OK`. The source is standalone and does not require precomputed data or an online service. A failed assertion invalidates the indicated check. The guarantee applies to the enumerated finite graphs; no arbitrary-order or thermodynamic result is asserted. Independent audit has not been performed.
