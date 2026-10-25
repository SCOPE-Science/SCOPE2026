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

The standalone `check_hamming_three_cut.py` builds the Alexander dual simplices from their proposed line-and-square classification, then independently tests **every triple and quadruple** using induced connectivity of the Cartesian graph. With coordinates of size at most four, it also checks all five-element candidates where relevant. Across `(2,2,2)`, `(2,3)`, `(2,3,3)`, `(3,3,3)`, `(2,2,2,2)`, `(2,3,4)`, and `(3,3,4)`, it computes all simplicial boundary ranks in characteristics two, three, and five and compares the full resulting Betti vector to the theorem. All seven cases passed.

For the first new mixed-alphabet example `(2,2,3)`, the theorem predicts \(N=12\), \(a=12\), \(b=6\), so the nonzero reduced homology of the ordinary three-cut complex is \(\mathbb Z^6\) in degree \(7\) and \(\mathbb Z^{12}\) in degree \(8\). The code verifies the corresponding dual Betti vector \((1,12,6)\) in each tested characteristic. The checker does not and cannot establish the infinite quantifier or integral torsion-freeness; those follow from the direct geometric proof and integral long exact sequence. There is no independent audit or externally certified proof.
