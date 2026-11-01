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

# Reproducibility and scope

The mathematical assertion is proved for all integers \(n\ge2\); finite enumerations check examples and code independently, not infinite completeness. Two standalone programs implement the update map with distinct data structures.

From the directory containing this file, run:

```sh
python3 checks/path_exhaustive.py
g++ -std=c++17 -O2 checks/path_exhaustive.cpp -o /tmp/path_exhaustive_check
/tmp/path_exhaustive_check
```

The Python program directly updates Boolean arrays, checks \(A(F_n(x))=\{j-1:j\in A(x),j>1\}\), and compares actual hitting times and exact shell populations for every configuration with \(2\le n\le15\): **65,532** complete initial orbits. The independent C++ program uses bitwise local neighborhood updates and tests the complete hitting time/histogram for every configuration with \(2\le n\le20\): **2,097,148** complete initial orbits. Original reproduced output is in `checks/python_output.txt` and `checks/cpp_output.txt`.

These checks cannot rule out a subtle proof failure at untested larger sizes. The proof instead rests on the direct recurrence, zero-propagation lemma, ascent equivalence and rightmost-ascent combinatorial count, independently of code. The all-zeros state has hitting time zero, nonzero ascent-free states have time one, and no persistence-threshold clipping at path endpoints is allowed. Any change in endpoint convention or update schedule changes the model.
