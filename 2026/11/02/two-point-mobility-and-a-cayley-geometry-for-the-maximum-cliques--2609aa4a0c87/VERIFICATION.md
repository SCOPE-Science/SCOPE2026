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

`python3 verify.py` must print `FULL_CERTIFICATE_OK`; it enumerates every five-clique of the Paley graph on \(41\) residues, rules out six-cliques, checks the exact affine action, constructs the Cayley generators and confirms group-distance shells \((1,8,36,98,62)\).

Compile `verify_alt.cpp` with `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt` and run `./verify_alt`; it must print `INDEPENDENT_CERTIFICATE_OK`. This different code exhausts all \(inom{41}{5}=749398\) five-subsets, checks no larger clique, compares the \(205\) maximum cliques pairwise and computes shortest paths from every vertex. It establishes zero one-exchange edges and \(820\) two-exchange edges, degree \(8\), diameter \(4\) and constant distance-shell profile.

The numerical proof is exhaustive only for the specified finite graph, and does not imply an analogous statement for other prime powers. Self-review passed; independent scholarly audit has not been performed.
