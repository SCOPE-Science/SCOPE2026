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

# Reproducibility and limitations

All included programs are complete source files. To reproduce from an extracted folder, run `python3 lower_bound.py`, `python3 witness.py`, and `python3 six_point_census.py`. Compile the independent implementation with `c++ -O2 -std=c++17 full_pairs.cpp -o full_pairs` and execute `./full_pairs`. Compare output against the corresponding `.out` file, which records the already-obtained execution.

The lower-bound program covers all \((n!)^2\) ordered pairs of permutations for each nonempty cardinality \(n\le5\). Its key is the multiset of vertex-level five-bit atomic-two-type count histograms, which is invariant under two-variable logic with counting. The explicit six-point witness checks commute status, composition disagreement, and identical one-cell equitable partitions. The canonical six-point program covers eleven possible first-permutation cycle types, each with 720 second permutations; reducing by the first permutation's centralizer yields 901 simultaneous-conjugacy classes. It also jointly refines pairs of mixed representatives, checking full \(C^2\) indistinguishability. The independent C++ program visits all \((6!)^2=518400\) labelled pairs and corroborates exactly three mixed stable signatures.

No external program, data table or proprietary library is required. A finite verification cannot by itself establish claims about larger cardinalities, and this package does not make any larger-cardinality census claim. The finite-exhaustive argument has a stated mathematical completeness proof and uses the standard equivalence of counting logic and colour refinement for binary structures. There has been no independent scientific audit or formal proof-assistant certification.
