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

# Reproducibility

From this directory, using only a C++17 compiler and the included files:

```sh
c++ -std=c++17 -O2 verify.cpp -o verify
./verify > verify_output.txt
c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck
./crosscheck > crosscheck_output.txt
```

`verify.cpp` constructs exactly \(7\binom{8}{2}6!=141120\) normalized rank-seven maps, computes every subset transition and shortest path by complete breadth-first search, and prints the complete `threshold,classes` distribution. It also counts the congruence-preserving classes, checks the exact 1856 zero class, and prints selected high-threshold representatives.

`crosscheck.cpp` iterates independently over the full \(8^8=16777216\) arrays, retains all and only those with output image \(\{1,\ldots,7\}\), and performs an independent BFS on subsets using a per-state transition loop. Its entire 32-row result was compared to the first program's `threshold,classes` block and to `spectrum.csv`; all agree exactly. Both executions finished with `VERIFY_OK` and `CROSSCHECK_OK`, respectively.

The CSV `spectrum.csv` lists all 32 nonzero histogram entries including nonsynchronizability as threshold zero; `rare_witnesses.csv` records representative tuples for each threshold at least 30. The runtime checks cover the entire finite domain, not a random experiment. All these checks are for reproducibility, not external mathematical certification.

**Limits:** The proof is specific to eight states, the specified eight-cycle and a rank-seven second map. No claim about higher state counts or other transformation ranks is supported. The congruence criterion has an established literature route through the primitive/defect-one theorem and is not presented as a new result. Independent scientific validation has not been performed.
