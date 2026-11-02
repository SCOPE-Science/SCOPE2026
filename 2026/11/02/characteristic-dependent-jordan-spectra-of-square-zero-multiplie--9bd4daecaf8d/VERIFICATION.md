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

Execute `python3 verify_square_zero_multiplication.py`. The program has no external dependencies and builds the multiplication maps directly in the monomial basis, checks \(f^2=0\) coefficientwise, independently computes \(\operatorname{rank}(m_f)\) by Gaussian elimination, and compares every cumulative rank histogram with the proved formulas.

Completed output: `SQUARE_ZERO_MULTIPLICATION_JORDAN_CENSUS_OK 18 6244`.

Fields tested: \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), with 18 total small truncation configurations. Boundary \(n=1\) is tested by the code as an additional consistency case but is not in the stated theorem. The exact 6,244 figure counts square-zero test elements, not all input elements examined. The characteristic-two and odd-characteristic branches and each predicted rank multiplicity were verified independently for the enumerated cases. Exhaustive small finite computations do not prove a universal theorem; the general argument uses the valuation and invariant-factor steps in the written proof. The reduced-geometry assertion is proved algebraically, not computationally certified.
