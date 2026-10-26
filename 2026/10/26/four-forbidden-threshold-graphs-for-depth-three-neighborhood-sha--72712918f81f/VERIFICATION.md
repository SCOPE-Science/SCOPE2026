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

# Reproduction and finite certificates

The proof has two logically separate components: a mathematical reduction from an arbitrary threshold graph to an induced witness on at most fifteen vertices, and an exhaustive calculation of the minimal positive creation words in that finite range. Both are necessary. The reproduction scripts execute only standard finite integer and bitset operations; no floating-point arithmetic is used.

Run:

```sh
g++ -O3 -std=c++17 exhaustive_threshold.cpp -o threshold_enum
./threshold_enum
python3 independent_threshold_check.py
python3 witness_checker.py
```

The first two programs enumerate all \(32767\) creation strings of orders one through fifteen, apply the exact rank-three splitting criterion to deduplicated neighborhood rows, and test every one-vertex deletion of positive graphs. Their order-by-order results are supplied in `cpp_enumeration.out` and `python_enumeration.out`. The independently coded Python enumeration explicitly asserts the expected complete count vector and the four minimal words.

`witnesses.json` contains four complete depth-three binary trees. `witness_checker.py` generates the same trees and checks the neighbor relation along each of eight root-to-leaf paths per graph; all eight witnessing centers per graph are distinct. The four degree sequences in RESULT.md can be reconstructed directly from the provided creation words.

The one-vertex-deletion property is sufficient for induced minimality because deleting more vertices cannot increase the depth of a shattered tree. Conversely, the full fifteen-vertex theorem follows from retaining exactly the queried vertices and one realizing center per leaf of any depth-three witness. Thus the computation is exhaustive for the proof's finite domain, but is not presented as a direct enumeration of arbitrarily large graphs.

Limitations: This verifies the stated mathematical and computational argument as self-review only; no external independent scientific audit or historical-priority certification has been conducted.
