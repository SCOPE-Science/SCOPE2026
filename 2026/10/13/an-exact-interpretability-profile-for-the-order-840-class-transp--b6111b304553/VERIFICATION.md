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

`verify.py` reconstructs the eight-letter alphabet, the source transition relation, the map from letters to pairs of residue classes, and the four numerical residue-class parameters of the sharp pair. For every structurally admissible word of lengths \(1\) through \(7\), it solves the chained linear Diophantine system exactly by repeated gcd congruence reduction. It then checks the same-parity distinctness criterion symbolically on the resulting affine one-parameter family.

The output verifies the exact triples \((n,	ext{total},	ext{integer},	ext{exact})\): \((1,8,8,8)\), \((2,16,8,8)\), \((3,32,8,8)\), \((4,64,6,6)\), \((5,128,4,4)\), \((6,256,2,2)\), and \((7,512,0,0)\). It also identifies the two length-\(6\) survivors, evaluates the four displayed integer cycles directly, and checks the least-common-multiple and certificate-minimality assertions.

The calculation is finite and exact. The implication from zero exact length-\(7\) interpretations to finite order, and the divisor \(840\) upper bound for finite order, are cited from Theorems 6.4 and 7.1 of arXiv:2610.01793v1 rather than inferred computationally.
