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

# Finite verification and scope

The two programs were executed in their source directory with their declared commands. `verify.py` uses the cyclic \((7,3,1)\) difference-set Fano representation, and `verify_alt.cpp` uses the seven nonzero vectors of \(\mathbb F_2^3\) and triples whose vector XOR is zero. Both algorithms form all admissible induced three-edge matchings and recursively cover all 21 graph edges exactly once by seven triples. Complete pair comparisons establish the two- and three-class trade graphs, and complete BFS from each vertex establishes the graph diameter. The Python run additionally checks all graph automorphism actions, six symmetry orbits, the fourteen ambiguous six-edge unions, and six distance-shell types. Each program verifies its actual computed values by executable assertions; neither assumes precomputed certificates.

`python3 verify.py` concludes with `FULL_VERIFY_OK` after reporting 84 induced triples, 416 optimal partitions, zero legal two-class trades, 1568 three-class edges, radius and diameter 6, and six orbit sizes 8,16,56,112,112,112.

`c++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt` concludes with `INDEPENDENT_VERIFY_OK` after independently reporting the same optimal partition count, 0/1568 two-/three-class edges, and connected radius and diameter 6. This second verifier does not rely on the cyclic incidence labels or the first program's saved output.

The theoretical upper bound of three edges per induced matching is proved by a Fano tangent-line argument. The exact finite programme checks the exhaustive classification; no infinite-family or conventional Kempe-chain result is claimed. The programs are computational crosschecks, not an independent scholarly assessment. The self-review has passed; no external audit was performed.
