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

# Computation and reproducibility

Run `python3 artifacts/verify.py` with Python 3 and SymPy. It constructs the four polynomial Euler-characteristic formulas from monomial enumeration in normal coordinates, checks the four coefficient pairs and the four exact discriminant identities, verifies coefficientwise strict positivity in \(b\) and \(u=a-b\), and compares polynomial results with direct integer monomial counts at test points. Passing output ends in `VERIFY_OK`.

The general conclusion for all integral \(a>b>0\) comes from the positive-coefficient algebraic identities displayed in `RESULT.md`, not from a finite census. Smoothness of anticanonical members and the root-location implication are justified geometrically and algebraically in the proof. No machine proof of historical priority, no external validation, and no characterization of intrinsic ample cones are asserted.
