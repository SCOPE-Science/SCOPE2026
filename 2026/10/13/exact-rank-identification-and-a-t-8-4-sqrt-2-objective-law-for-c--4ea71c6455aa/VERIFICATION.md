---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Conditional on the primary method's Algorithm1 thresholding/radius definition quoted in the inspected source package, f(X)=||X−I/2||_F²/2 has L=mu=1, optimum X*=I/2, initial lower bound B0=f*=0 and scalar diagonal coordinate f=s². With eta1=1, eta2=2/3 and opposite rank-one oracle, s1=−sgn(s0)/2, s2=sgn(s0)/6. Since d2=sqrt2/6 < smallest eigenvalue(X2)=1/3, the thresholding and efficient ranks both become full 2 at t=3; for |s|<=1/6 inequality 1/2−|s|−sqrt2|s|>0 is invariant. Full oracle maps s to −(1+sqrt2)s, giving recurrence s_t=(t−3−2sqrt2)/(t+1)s_{t−1}, t>=3, and exact gamma product with objective exponent 8+4sqrt2. Exact line search from any nonzero diagonal start reaches I/2 at t=1. Independent symbolic gamma-product iterations through t=24 confirmed the recurrence and invariant range. The full primary ERSO-FW article could not be read, so matching the source algorithm's quoted normalization remains an explicit correctness-documentation risk, not silently independently certified.

## originality

PASS

Best-of-knowledge, with substantive documented primary access gap: 2026 ERSO-FW establishes general eventual rank identification, while checked 2020 spectral FW and 2025 simplex precursor do not determine this exact centered trajectory, t=3 optimal-rank event, gamma-product exponent or one-step line-search contrast.

## value

PASS

Rank identification is the central stated design goal of the new optimization method. A solvable isotropic full-rank benchmark provides a meaningful exact finite identification time (3 vs generic sufficient 290), reveals unusual gamma exponent 8+4sqrt2 for simple steps, and demonstrates the one-step contrast with exact line search. This motivated algorithm-specific structural calculation is not just a tiny numerical gain or normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
