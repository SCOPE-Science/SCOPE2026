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

The analytic proof is self-contained. `verify.py` reconstructs the two-sample joint distribution from the four atom probabilities, confirms the closed forms for \(\delta\), \(\operatorname{Var}(L)\), and \(\rho(\theta)\), and checks the exact polynomial factorization of the deficit. It also evaluates a rational grid as a supplemental stress test.

The finite grid is not used to infer the universal inequality. Universality follows from the exact identity
\[
\frac5{11}-\rho(\theta)=
\frac{4(2\theta-1)^2(1+12\theta-4\theta^2)}{11(3+24\theta-12\theta^2+16\theta^3-4\theta^4)}
\]
and the positivity of the non-square factors for \(0\le\theta\le1\). No assertion is made for nonsymmetric four-point masses.
