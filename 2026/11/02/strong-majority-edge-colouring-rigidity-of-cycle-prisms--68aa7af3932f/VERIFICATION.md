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
# Computation and proof boundary

A standalone \(\texttt{verify.cpp}\) uses the actual edge-incidence lists of \(P_n\) (rather than the proof's sum equations) and checks every edge-neighborhood frequency directly. Under \(\texttt{g++ -std=c++17 -O2}\), execution reports the following exact counts:

```
BRUTE 3 0/512
BRUTE 4 8/4096
BRUTE 5 0/32768
BRUTE 6 0/262144
BRUTE 7 0/2097152
VERIFY_OK brute_labels_n=3..7 cubic_prism_n=3..44 proper_three_edge_coloring=all exactly_eight_n_multiple_4=all
```

The quantified proof for every \(n\ge3\) appears in RESULT.md, based on an exact local equation classification plus an explicit Hamiltonian-cycle 3-edge-coloring. The finite brute force is a separate boundary check and is not claimed to prove the infinite theorem. Both edge-neighborhood adjacency and named-color conventions are explicit. Independent assessment has not been performed.
