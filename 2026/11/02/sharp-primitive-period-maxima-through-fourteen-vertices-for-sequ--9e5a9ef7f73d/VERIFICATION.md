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

# Reproduction and verified boundaries

The package contains two distinct state-cycle search methods: a Python functional-graph indegree-pruning implementation (`verify.py`) and a C++17 visit-marker implementation (`scan_cpp.cpp`). The latter reads every tree in `tree_catalog.txt`, whose construction is independently checkable by `gen_trees.py` using leaf augmentation and AHU center codes. The documented observed final message of the complete C++ scan is `CPP_VERIFY_OK: 5447 unlabelled trees n=1..14`. The Python implementation independently established the table through order \(12\); an additional Python enumeration of order \(13\) and an independent nonisomorphic-tree generator comparison at order \(14\) agreed with the C++ search. The witness file is independently replayed by `witness14.py`, which outputs `WITNESS14_OK: 106 distinct states, exact return at time 106`.

In a directory with all embedded files, reproduce with:
```
python3 gen_trees.py
g++ -std=c++17 -O3 scan_cpp.cpp -o scan_cpp
./scan_cpp
python3 witness14.py
```

The `cpp_certificate.txt` is an observed transcript of the bounded exhaustive search, not a replacement for executable proof reproduction. The file `witness14_trace.txt` records the exact sequence of \(106\) pairwise distinct state masks followed by a return to the first. The finite-state cycle algorithm is exhaustive for the stated tree orders; nothing is asserted for larger graphs or non-permutation time-varying scan orders. Order-independence depends on the published cycle-equivalence theorem for graph dynamical systems.
