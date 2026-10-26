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

Run `python3 verify.py` using the Python 3 standard library. The program checks exact rational covariance derivatives at 12,298 thresholds across \(2\le m\le14\), 810 exact rational bisection comparisons across \(2\le m\le19\), and four separate lattice-simplex Riemann-sum comparisons with specified error bounds; all 13,112 checks passed when tested. In particular \(C_3(1/3)=-1/27\), \(C_3(1/2)=1/24\), and \(C_4(1/4)=-25/512\).

The verifier does not enumerate every continuum sample and cannot establish all-dimensional sign uniqueness or asymptotics. Those follow from the conditional-maximum convexity and gamma concentration proof presented in `RESULT.md`. No independently executed verification or external audit is asserted.
