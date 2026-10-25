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

# Verification and reproduction

Run `python3 check.py` in the directory containing the included standalone script. No external packages, internet access or downloaded datasets are needed. The script constructs the difference-set design on \(11\) points using quadratic residues modulo \(11\), the point–hyperplane design on the \(15\) nonzero vectors of \(\mathbb F_2^4\), and the complementary designs.

For each design, it independently checks the symmetric \(2\)-design axioms, builds its incidence graph, grounds one graph vertex, inverts the grounded Laplacian using exact `fractions.Fraction` Gaussian elimination, computes every dipole current column, and compares the resulting cut and cycle absolute-current sums to the two rational formulas. It makes no appeal to the explicit seven-class potential formulas in the proof.

The four independently constructed design parameters and norm pairs are \((11,5,2):(159/55,172/55)\), \((11,6,3):(31/11,35/11)\), \((15,7,3):(107/35,368/105)\), and \((15,8,4):(179/60,7/2)\). The checker covers \(55+66+105+120=346\) complete edge columns. Its final line must be:

`SYMMETRIC_DESIGN_ENDPOINT_EXACT_OK designs=4 columns=346`

The unrestricted mathematical claim is proven analytically from the incidence-matrix identity, the exact Laplacian dipole solution, the seven signed edge classes and the complementary-projection identity. Finite numerical or rational tests are not used to infer universal existence, uniqueness or the operator-norm formulas for untested designs. The verification is not an independent audit or external certification.
