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

The package's `artifacts/verify.py` reconstructs the complete face set for the six labeled graph vertices and calculates all chain boundaries in the lexicographically ordered graph-edge basis. Its exact integer elimination has only unit pivots and certifies boundary ranks \((14,91,364,821,711,180)\); the nonzero reduced rational Betti numbers are \(115\) in degree four and \(24\) in degree five. The code checks \(\partial^2=0\), equivariance of the oriented chain action on a transposition and a six-cycle generating \(S_6\), and the eleven-class character calculation.

The coefficient-extraction computation of the degree-five kernel character, subtraction of the injective degree-six chain module, the equivariant Euler identity in degree four, and the Murnaghan–Nakayama multiplicity calculations all use exact integers. Specht character orthogonality and integral nonnegative multiplicities are checked. Run `python3 artifacts/verify.py`; expect `D63_S6_CHARACTER_VERIFY_OK` at the end.

This verifies a finite rational representation theorem only. It does not establish any claim about integral \(\mathbb Z[S_6]\)-lattices, modular representations, larger graphs, or global novelty. Independent audit is not performed.
