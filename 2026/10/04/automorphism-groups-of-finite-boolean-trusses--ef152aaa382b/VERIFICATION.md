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

The proof was checked at the level of definitions and quantifiers for arbitrary finite Boolean trusses.

The published decomposition gives a commutative Boolean-ring part and two rectangular factors. Finiteness is used only to make the Boolean ring unital and hence isomorphic to a finite product of copies of \(\mathbb F_2\). The intrinsic leaf identities in the classification proof force a truss automorphism to preserve each coordinate family. This eliminates possible cross-factor shears.

On the commutative coordinate, multiplicativity forces preservation of the unique absorbing zero; heap preservation then becomes additivity, so the coordinate map is a Boolean-ring automorphism. On a left-zero or right-zero factor, multiplication adds no constraint beyond heap preservation. After choosing an origin, heap automorphisms are exactly affine maps \(x\mapsto\varphi(x)+c\).

The bundled `verify.py` independently enumerates permutations of five small models, checks the heap and multiplication tables exactly, and compares the resulting counts with the theorem. The saved output ends with `CHECK_OK`.

The finite enumeration is not an infinite proof. The arbitrary finite case rests on the symbolic factor-splitting argument above.
