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

Run `python3 verify_coxeter_character.py` using only the Python standard library. It constructs both Coxeter graph presentations, matches the 28 vertices by the explicit `ISO` bijection, and checks all 378 adjacency pairs. Its recursive enumeration covers all 196,009 independent subsets including the empty subset. An exhaustive Hasse topological sort verifies that 98,001 face pairs give an acyclic discrete-Morse matching with precisely seven critical six-faces.

It enumerates all 336 invertible projective matrices over \(\mathbb F_7\), checks the induced graph automorphisms, computes fixed-orbit alternating sums and compares traces to the quadratic-determinant-twisted augmentation character. An independent signed fixed-face evaluation checks a representative of every one of the eight cycle types. The supplied output is from this program. The finite verification does not investigate integral equivariant lattice structure or establish absolute bibliographic uniqueness.
