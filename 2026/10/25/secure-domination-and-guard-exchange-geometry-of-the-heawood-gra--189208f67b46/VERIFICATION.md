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

# Reproduction and limits

`fano_secure_enum.py` uses the dot-product definition of the Fano plane and exactly enumerates all \(2^{14}=16384\) vertex subsets. It verifies the ordinary and secure domination minima, the exact characterization of every secure six-set, every exchange edge, each shortest-path eccentricity, and the size \(84\) orbit under all \(168\) binary invertible linear maps. The raw recorded output is `fano_secure_enum.out`.

`secure_fano_crosscheck.cpp` independently uses the cyclic \(\{0,1,3\}\) Fano difference set and performs domination and defense checks with separate point- and line-side loops, then independently constructs the optimal exchange graph and checks all shortest paths. Compile with `c++ -std=c++17 -O2 secure_fano_crosscheck.cpp -o secure_fano_crosscheck` and execute `./secure_fano_crosscheck`; its raw recorded output is `secure_fano_crosscheck.out`.

The independently implemented programs both report a secure optimum of \(6\), exactly \(84\) optimum placements, exchange degree \(4\), \(168\) exchange edges, and radius and diameter \(7\). Their shared cardinality and distance profiles match. The mathematical proof also counts the placements geometrically and proves transitivity. Nothing here establishes a theorem for larger projective planes or independently certifies novelty; independent external audit remains unperformed.
