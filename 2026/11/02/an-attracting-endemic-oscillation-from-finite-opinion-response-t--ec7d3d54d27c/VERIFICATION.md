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

# Verification of the local NOD-SIS Hopf calculation

The standalone `verification/check_hopf.py` file requires Python 3 and SymPy, as documented in `verification/requirements.txt`. Run `python verification/check_hopf.py` from the package root. The program was executed against the packaged copy and returned its explicit PASS line.

Its exact symbolic operations reconstruct all second- and third-order derivatives of the original prevalence/opinion equations at \((1/2,-1/2)\), transform the derivative tensors to canonical \((X,Y)\) coordinates, evaluate the planar first Lyapunov formula, and assert equality to the displayed closed coefficient. It also asserts vanishing trace, the exact determinant/frequency relation, transversality, and admissible parameter inequalities. A finite positive-term representation of \(\log 3\) together with a rational tail bound proves \(1.0986<\log3<1.0987\), then exact rational algebra certifies positivity of the quartic numerator.

The executed checker reports the coefficient approximately \(-1.40432205624407547028425\). Floating-point values are diagnostic only; all existence, parameter-bound, and criticality conclusions come from analytic identities and exact rational inequalities coupled with the local Hopf theorem. The program does not certify global cycles or an explicit neighborhood width, and no independent audit was performed.
