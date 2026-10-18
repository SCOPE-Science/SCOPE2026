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

The self-contained `verify_python.py` enumerates all induced matchings using increasing-edge compatibility bitsets, independently enumerates edge-disjoint maximum-matching families, tests that every clique smaller than four extends, verifies the \(26\)-regular disjointness graph and the seven-color partition, and enumerates all \(168\) point permutations preserving Fano lines. It writes `certificate.json`, whose complete \(84\) hexadecimal maximum-matching masks are compared with those output by the separately structured C++17 verifier.

The self-contained `verify_cpp.cpp` rebuilds adjacency and recomputes every induced-matching extension by directly testing candidate edges against previously chosen edges. It independently checks disjointness packings, purity, degree, and the color classes. It has no external libraries beyond the C++17 standard library. It outputs every extremal mask in ascending hexadecimal order. Both programs were run and their recorded results are in `python_output.txt` and `cpp_output.txt`.

To replay in the directory containing these files:

```sh
python3 verify_python.py > python_replay.txt
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_cpp.cpp -o verifier
./verifier > cpp_replay.txt
```

The exact expected matching histogram is \((1,42,609,3808,10374,11172,4242,84,0)\), the exact packing histogram is \((1,84,1092,3528,2478,0)\), the only clique size of maximal disjoint families is four, the graph is regular of degree \(26\), and the \(168\) collineations produce an orbit of size \(84\).

**Limits:** These programs certify the stated finite identities, not any infinite-family claim, bibliographic priority, or external independent validation. The numerical strong chromatic index seven was already known; the new contribution concerns the extremal matching geometry explaining it.
