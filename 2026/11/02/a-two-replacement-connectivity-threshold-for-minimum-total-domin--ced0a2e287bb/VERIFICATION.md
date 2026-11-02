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
# Reproducibility and limits

The package contains `verify_clebsch.py` and `verify_direct.cpp`. Execute the former with `python3 verify_clebsch.py`, and the latter with `g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` on a C++17 compiler. No external package, downloaded dataset, network access, or numerical floating-point computation is required.

The Python program enumerates all 1820 four-subsets of one parity half, verifies that exactly 40 cover the other half, matches the list exactly to the forty \(C_4\) subgraphs of the distance-four Clebsch graph, checks an independent 10+30 symbolic square construction, all 780 unordered square pairs, the \(H\)-adjacency degrees and every distance profile, and computes the Cartesian-product profile. Its success marker is `CLEBSCH_SQUARE_CLASSIFICATION_AND_METRIC_PASS`.

The C++ program constructs the original 32-vertex hypercube directly. It enumerates all \(\binom{32}{8}=10{,}518{,}300\) subsets, finds exactly 1600 total dominating sets, exhausts all one- and two-replacement neighbors, and computes an all-source breadth-first distance histogram on the 1600 optimal configurations. Its success marker is `DIRECT_Q5_ALL_8_SUBSETS_ALL_REPLACEMENTS_PASS`.

The conclusion that no set of fewer than eight vertices can total dominate is proved mathematically by the parity-side neighborhood bound. The 780-pair incidence lemma is verified by exact finite exhaustive loops rather than a printed pair-by-pair certificate. Two independent implementations support, but do not constitute an independent scholarly audit of, the stated proof. No results about higher-dimensional hypercubes are asserted.
