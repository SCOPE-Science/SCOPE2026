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

# Reproduction and limits

Compile `propagating_cycle_spectrum_verifier.cpp` using a C++17 compiler without disabling assertions:

```sh
c++ -O3 -std=c++17 propagating_cycle_spectrum_verifier.cpp -o verify
./verify
```

The program first enumerates each eligible integer state in every base from 2 through 1230 using a three-color traversal. Its separate indegree-peeling implementation independently enumerates all directed cycles in the same graphs. It asserts equality of their first-occurrence tables and equality with the stated list, and then prints `VERIFIED`. In the executed check both methods passed. The integer bound \(1230^2\) is small enough for 32-bit signed integer arithmetic, including squared-digit successors. The attached TSV lists directly checked cycles realizing each first base.

The complete enumeration proves only the nineteen finite minima, not an asymptotic polynomial bound. Independent audit and independent validation have not been performed.
