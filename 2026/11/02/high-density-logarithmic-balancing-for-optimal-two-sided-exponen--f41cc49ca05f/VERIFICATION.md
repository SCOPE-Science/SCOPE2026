---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: The exact prior A and B sharp frame bounds for the normalized two-sided exponential were checked directly against Faulhuber–Shafkulovska Eq.(8.1), and uniqueness/localization against Theorem 2.7. Algebraic factorization κ=cosh(x)coth²(η/2)(1+u/b)/(1-u/a) with x=η/q is correct. On the known η~log q optimizer interval, uniform elementary expansions give logκ=η²/(2q²)+4(1+η)e^-η+controlled smaller terms and derivative η/q²−4ηe^-η+smaller terms. Solving the exact stationarity equation gives e^-η=(4q²)^−1(1+O(log²q/q²)), hence the claimed position and three coefficients. Independently optimized exact analytic formulas for q up to 2048 corroborate the rate. Finite numerical tests do not prove uniform remainders; that follows from the stated controlled elementary expansions.

## originality

PASS

PASS best-of-knowledge: Faulhuber–Shafkulovska 2023 already provide the exact finite-redundancy sharp bounds, unique condition-number optimizer and coarse interval; these are acknowledged. Their relevant two-sided exponential section and theorem do not state the moving-optimizer asymptotic ηq=2log(2q)+o(1) and the three logarithmic condition-excess terms in inspected text. The high-redundancy expansion is not an automatic fixed-η substitution; controlling the derivative is needed. Earlier Janssen and unindexed follow-up analyses may contain equivalent expansions.

## value

PASS

PASS: Optimal frame stability at high redundancy is a natural nontrivial quantity for a standard totally positive window. The logarithmic displacement of the optimal rectangular sampling lattice and its sharp excess condition number quantify conditioning and distinguish optimal from naive choices; they are stronger than simply recomputing known finite-q formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
