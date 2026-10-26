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

# Exact finite verification

With Python \(3.8\) or later, execute:

`python3 verify.py`

Expected terminal record: `ALL_VERIFY_OK`. The script first enumerates all \(\sum_{k=0}^{6}\binom{16}{k}\) subsets and tests \(120\) explicit nonendpoint-witness requirements for each. The exact optimum count histogram is `0,0,0,0,0,0,1600`. It independently retests each minimum set using all endpoint pairs and individual witnesses, checks the complementary distance-two and antipodal filters, enumerates all \(384\) cube automorphisms, and constructs all one-vertex exchanges. The printed final structural line is `EXCHANGE_OK connected=1600 vertices=1600 edges=17088 degrees=[(12, 384), (22, 576), (26, 576), (30, 64)]`.

For a separate implementation of all subset and exchange-count computations (C++17 compiler required), run:

`g++ -O3 -std=c++17 -o checker independent.cpp && ./checker`

It must output the exact cardinality histogram and degree frequencies, including `edges:17088`. This implementation scans all \(2^{16}\) bitmasks directly and recomputes resolving masks using compiler integer popcount operations; it does not import the Python answer. The orbit and BFS connectivity checks are performed by the Python script and are not claimed to have been independently duplicated by the C++ code.

## Limits

The searches are exhaustive only over the finite cube. Computation time varies by machine; there are no randomized branches and all checks use exact integer operations. Neither verifier proves a formula for larger-dimensional cubes, nor does this self-review amount to independent external validation.
