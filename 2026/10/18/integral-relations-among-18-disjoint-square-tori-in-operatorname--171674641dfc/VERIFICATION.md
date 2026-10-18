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

# Reproducibility of the finite integer proof

Execute `python3 verify_k44_torus.py` with any ordinary Python 3 interpreter supporting integer modular inverses (Python 3.8 or newer). The verifier has no external dependencies, no input files, and performs only exact integer and finite-field computations.

The program builds the full 96-by-72 signed cubical boundary \(B\) and checks that every one of the eighteen torus two-chains is a cycle. It constructs six proposed relation columns and checks each exactly. The rank calculation over \(\mathbb F_3\) gives 60 and, in conjunction with twelve independent kernel columns, determines the **rational** boundary rank. A 12-by-12 integer torus coefficient minor has determinant +1, establishing **integral** saturation; a 6-by-6 integer relation coefficient minor has determinant -1, establishing a full primitive relation lattice. These determinant checks supply information not obtainable from modular ranks alone.

The successful verification output terminates with `VERIFY_OK_K44_UNORDERED_TWO_PARTICLE_PRODUCT_TORUS_PRESENTATION`. The computation has been run on the exact standalone program included here. The proof relies on complete finite chain enumeration, not on a probabilistic or truncated search.

Limits: Only this finite graph and ordinary unordered collision-free two-particle model are examined. This check does not assess future applications, external novelty priority, or independent mathematical verification.
