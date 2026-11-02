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

# Exact verification and boundaries

Execute `python verify_weierstrass.py` from the folder containing the standalone checker. The script requires Python 3 and SymPy. It verifies the defining quartic identity, the root discriminant identity, the exact quadratic--quartic resultant, and all four root formulas by reducing in the quotient algebra defined by \(i^2+1=0\), \(s^2-(t^2+1)=0\).

It also performs finite-field enumeration of all parameters satisfying the explicitly stated nonvanishing condition in the prime fields of orders \(3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59\) and the quadratic extensions of the first four. It checks direct six-degree-polynomial root counts against the quadratic-character formulas in \(488\) admissible cases; it independently compares the full paired curve point counts in the same \(488\) cases, including points at infinity; and for four eligible prime-field parameters it checks that every one of the six roots lies in the quadratic extension and verifies their Frobenius fixed points.

The expected terminal marker is `WEIERSTRASS_AND_JACOBIAN_COMPATIBILITY_PASS parameter_cases=488 pair_point_counts=488 quadratic_splitting_cases=4`. These checks were executed successfully on the exact accompanying script.

The infinite-field results are established in the proof by factorization, nonvanishing, explicit inversion of root differences, and sign characters. Finite enumeration is not used as an infinite proof. The isomorphism of the two unpolarized Jacobians is the cited theorem of Abdellatif (arXiv:2410.03664v1); its proof is not supplied as part of this certificate. No independent external mathematical audit has been conducted.
