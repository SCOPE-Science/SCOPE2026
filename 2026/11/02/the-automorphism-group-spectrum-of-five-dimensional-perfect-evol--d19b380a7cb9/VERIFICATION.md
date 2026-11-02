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

# Verification procedure

Execute `python3 verify.py` with standard Python 3. The code builds \(S_5\) literally as all permutations of five indices, enumerates its 156 subgroups by adjoining generators and closure, computes every subgroup's orbits on the 25 matrix-entry positions, and checks nonsingularity of every orbital-constant binary matrix by exact row operations. For the trivial subgroup, the 9,999,360 invertible matrices are counted by the finite-field general linear group product, not iterated individually. Descending subgroup-poset inversion finds all exact stabilizer fibers and counts orbits of each abstract stabilizer group type.

The code asserts nonnegative exact-stabilizer counts, all listed 16 isomorphism-type class counts, a total of 85,411 classes, 9,999,360 labeled invertible matrices, and a separate Burnside aggregate of 10,249,320 fixed-point incidences. It verifies the seven cyclic-subgroup centralizer counts directly from orbitals, then checks dimension-three and dimension-four counts of 33 and 908 by an independent direct matrix/permutation enumeration. On success it prints `VERIFY_OK` followed by the class-count spectrum.

# Limits

This finite verification is exhaustive for the stated binary dimension-five family. The logical reduction of algebra isomorphism to permutation similarity invokes the published natural-basis rigidity theorem for perfect evolution algebras. The code does not prove that theorem separately and does not establish global bibliographic priority. No independent mathematical audit was carried out.
