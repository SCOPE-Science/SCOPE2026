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
Compile the standalone `verify.cpp` with a C++17 compiler, for example `c++ -std=c++17 -O2 verify.cpp -o verify`, and run `./verify`.

The checker builds each \(C_3\square C_n\) adjacency list, marks \(N[S]\) for every initial set \(S\), and repeatedly applies the unique-unmonitored-neighbor rule. It exhaustively computes the maximum size of unsuccessful initial sets at \(n=3,4,5,6,7\), giving respectively \(1,2,2,3,3\), and counts the extremal failed sets as \(9,18,30,24,63\). It checks the alternating stalled witness through \(n=20\) and local two-column forcing assertions for cyclic gaps of one, two, or three through \(n=13\). The expected terminal line is `VERIFY_OK`.

These computational checks independently corroborate the case analysis at small finite sizes. The general cyclic-gap argument and stalled construction are the proof for all \(n\ge3\). No third-party or independent mathematical audit has been performed.
