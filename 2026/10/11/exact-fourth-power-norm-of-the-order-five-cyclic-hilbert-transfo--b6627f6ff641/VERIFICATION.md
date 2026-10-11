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

The standalone `verify.py` file performs the following checks without external packages:

1. Exact integer-polynomial verification of
\[
N'(t)D(t)-N(t)D'(t)=-8t^2(3t^4-12t^2+8t-9),
\]
where \(R(t)=N(t)/D(t)\).
2. Exact polynomial verification that substituting \(R(t)\) into
\[
3185X^4-17948X^3+42750X^2-47500X+15625
\]
produces a polynomial divisible by \((3t^4-12t^2+8t-9)^2\).
3. Bisection of the unique positive root in \((1.85,1.86)\), followed by evaluation of \(R(t_*)\) and its fourth root.
4. Direct cyclic Fourier synthesis of a phase-aligned extremizer and comparison of its fourth-power ratio with the closed formula.
5. Deterministic regression checks comparing the derived two-phase moment formulas with direct five-point synthesis and confirming that sampled ratios do not exceed the claimed maximum.
6. A direct order-three regression confirming the expected \(L^4\)-isometry on real zero-mean data.

The exact polynomial identities and analytic sign argument establish the result. Finite numerical regressions do not stand in for proof, do not establish uniqueness by enumeration, and do not claim anything for cyclic orders other than five.
