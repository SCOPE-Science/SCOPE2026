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

Run `python3 verify_petersen_m2_s5.py` using Python 3 with its standard library. The script generates Petersen graph edges from the ten two-subsets of a five-element set, independently rebuilds all 32768 candidate edge sets and checks exactly 10870 admissible faces. It checks the complete f-vector, 5432 discrete-Morse pairs, the 63780 oriented nonempty face-cover relations and a complete acyclic topological ordering.

For each of the 120 ground-letter permutations it computes the exact alternating trace over admissible unions of edge orbits and checks equality to the number of fixed ground letters minus one. A second oriented-fixed-simplex trace implementation verifies all seven conjugacy-class representatives. All class counts and the irreducible character inner product are checked. Successful execution prints `PETERSEN_M2_S5_STANDARD_CHARACTER_VERIFIED`.

The argument computes the rational character of one finite complex; it does not address an integral \(S_5\)-lattice, a coherent equivariant homotopy equivalence or any other graph. The calculation is exhaustive for the stated object. Independent mathematical audit has not been performed.
