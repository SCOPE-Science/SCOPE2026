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

# Executable finite verification

Run `python3 verify_heawood_filtration.py` with Python 3.10 or newer. The program uses only the standard library and checks the following assertions from graph definitions rather than reading precomputed logs:

1. The fourteen vertices form the point-line incidence graph of the Fano plane; each of seven lines has three points, and each pair of lines intersects in exactly one point.
2. For component bounds 2 through 6, exhaustive subset-component traversal agrees **on every subset** with independent avoidance of all connected induced subsets of the forbidden size. The five nonempty face counts are 2256, 4622, 6190, 7870, 9683, and the five Euler characteristics are -12, 2, 2, 2, -19.
3. For the third stage, 2310 disjoint codimension-one matching pairs exhaust the 4622 nonempty faces except one vertex (bitmask 256) and one six-simplex (bitmask 10454). The complete oriented Hasse graph, comprising 23884 cover incidences, is acyclic.
4. The 1568 relative faces in the fourth stage are paired into 784 pairs; the 1680 relative faces in the fifth stage are paired into 840 pairs. Both oriented relative Hasse graphs are acyclic.
5. Starting from the **full** fourth and fifth complexes, the program verifies and performs exactly 784 and 840 legal elementary simplicial collapses, respectively, leaving exactly the preceding subcomplex at each step.

The core topological inputs are the discrete-Morse theorem (one critical zero-cell and one critical six-cell imply a six-sphere) and the fact that elementary simplicial collapses preserve simple-homotopy type. No infinite-family extrapolation or independent review is claimed.
