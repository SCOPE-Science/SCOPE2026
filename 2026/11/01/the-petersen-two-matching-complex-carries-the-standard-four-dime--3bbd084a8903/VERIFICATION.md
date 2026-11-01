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

# Reproduce the exact finite verification

From the directory containing the embedded `verify.py`, run `python3 verify.py` using Python 3.10 or newer. No external package, network connection, stored table, or separate certificate is required. Success terminates with `ALL_VERIFY_OK`.

The program constructs \(P=\mathrm{KG}(5,2)\) and all face subsets of its degree-two bounded-edge complex. It verifies the full face-count vector, 5,432 ordinary discrete-Morse pairs, one critical zero-cell and four critical seven-cells, and checks acyclicity by topologically sorting all 10,869 nonempty faces against the full 63,780-edge oriented Hasse diagram. Thus it establishes the already known nonequivariant rational homology concentration without depending on earlier calculations.

Every element of \(S_5\) is then tested twice. First, the program lists its edge orbits and sums the signs of each valid orbit union; second, it directly enumerates every fixed face and calculates its orientation permutation sign. Both must match the exact five-point fixed-label count minus one. They must agree on every one of the 120 permutations, yielding conjugacy-class traces \((4,2,0,1,-1,0,-1)\) in cycle-type order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\).

Only integer arithmetic and finite exhaustive enumeration are used. This establishes the rational character and does not produce an integral \(S_5\)-lattice isomorphism or a canonical equivariant topological equivalence. The program independently reruns the mathematical checks but does not substitute for independent human review.
