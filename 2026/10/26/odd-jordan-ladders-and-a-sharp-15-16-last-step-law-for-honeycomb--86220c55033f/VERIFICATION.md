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

# Reproducibility and verification

The proof is algebraic for every nonnegative integer exponent. For the finite tests, compile the included `verification/verify.cpp` with a conforming C++17 compiler and execute it; no third-party libraries are needed. The test reconstructs all edges independently from their modular-coordinate definition, verifies symmetry and absence of loops, generates successive adjacency powers by applying the three-neighbour rule to their columns, and obtains matrix ranks by binary elimination. It checks `k=1,2,4,8`, including the maximum required step and one extra step. For `k=1` the test enumerates every one of the 262144 labelled inputs and checks the distinct image size.

The retained output is `verification/verify.out`. All rank lines matched the symbolic predictions and the run ended with `HONEYCOMB_VERIFY_OK`. Finite verification supports, but cannot replace, the all-size decomposition in `RESULT.md`. Primitive cycle lengths and arbitrary honeycomb torus parameters were not verified or claimed.
