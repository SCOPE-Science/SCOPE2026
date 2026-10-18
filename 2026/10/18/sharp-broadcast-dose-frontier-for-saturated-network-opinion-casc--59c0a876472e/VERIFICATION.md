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

# Verification and reproducibility

Run `python verify.py` with the dependencies listed in `requirements.txt`. The script checks symbolically that the asserted primitive has derivative \(1+g(s)/(1-s)\) and that the claimed pointwise calibration gap is an exact algebraic identity. It numerically computes the sharp shaped-dose infimum and the constant-pulse minimizing amplitude, checks the sign of its derivative and comparison with selected amplitudes, and verifies the crossing-time prediction in a three-node directed cycle for five amplitudes immediately below and above the threshold duration.

The program also integrates a shaped input intended to follow \(s(t)=1-e^{-t}\) up to \(t_0=-\log(1-q)\). The numerical discrepancy at the switching surface was smaller than \(3\times10^{-9}\); its test tolerance is \(10^{-7}\). The exact statement is proved by directly substituting that trajectory into the scalar ODE. The proof's universal graph and input quantifiers, uniqueness assertion, and nonattainment of successful boundary dose are derived analytically, not from these numerical checks.

The computations were replayed with `scipy` 1.17.0, `numpy` 2.3.5 (transitive dependency), and `sympy` 1.14.0. No external solver or inaccessible file is necessary. The printed decimal values are numerical approximations; exact mathematical quantities are defined by integrals, equations, and logarithms in `RESULT.md`.
