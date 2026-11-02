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

`verify_symbolic.py` exactly checks the three coefficient-extraction identities in the full polynomial ring, the quadratic leading coefficient, and the non-square discriminant specialization. It reports `EXACT_POLYNOMIAL_IDENTITIES_AND_NONSQUARE_DISCRIMINANT_OK`.

`verify_universal.py` enumerates all 3125 monic quintics over the prime field, tests separability with Euclidean gcd, computes the coefficients of the cubic power, the rank of Cartier, and stable iterates. It reports exactly 625 singular models; smooth strata counts are 1800 for \((f_5,a)=(2,2)\), 680 for \((0,2)\), and 20 for \((0,4)\). The final line is `CHAR5_UNIVERSAL_EXACT_OK`.

`verify_extension.py` uses an independent custom implementation of \(\mathbb F_{25}\) and its fifth-power inverse Frobenius, directly iterating the semilinear Cartier map. A seeded sample of 6000 coefficient choices contained 5764 smooth curves, including 5507 with \((f_5,a)=(2,2)\) and 257 with \((0,2)\). The final line is `GF25_SEMILINEAR_CARTIER_OK`.

The proof, not the finite tests, establishes all geometric statements. The absolute irreducibility proof is the exact polynomial discriminant argument in `RESULT.md`; the relevant specialization is \(4t^2+3\), which is non-square over any algebraic closure in characteristic five. A smooth member of the rank-drop divisor has coefficients \((c_0,c_1,c_2,c_3,c_4)=(0,1,0,1,1)\), quintic discriminant \(2\), and nonzero gradient component \(\partial\mathcal P/\partial c_0=2\). A smooth point off the divisor is \((0,1,0,1,0)\), with quintic discriminant \(4\) and \(\mathcal P=2\). A smooth superspecial representative is \((0,1,0,0,0)\).

No independent external audit or validation has occurred. The priority comparison with the full 2025 Sohn paper remains limited by text access.
