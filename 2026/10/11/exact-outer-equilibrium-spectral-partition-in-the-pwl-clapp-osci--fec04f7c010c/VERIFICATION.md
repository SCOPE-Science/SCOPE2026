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

Run `python3 verify.py` in the same directory.

The checker is dependency-free and uses exact rational arithmetic. It verifies the following items:

1. The outer-equilibrium characteristic polynomial
\[
q_a(\lambda)=\lambda^4+\lambda^3+\left(3-\frac{a}{10}\right)\lambda^2+\left(a+\frac{21}{10}\right)\lambda-\frac{a}{10}.
\]
2. The discriminant identity \(\operatorname{disc}_\lambda(q_a)=P(a)/50000\) by exact Sylvester resultants at seven parameter values; the difference has degree at most six, so seven exact agreements establish the polynomial identity.
3. Exact Sturm counts showing that \(P\) has exactly two simple roots in \([-10,-1]\), one in each displayed narrow rational isolating interval.
4. The Routh-Hurwitz quantities \(\Delta_2=(9-11a)/10\) and \(\Delta_3=-(110a^2+131a-189)/100\), together with the unique negative crossing of \(\Delta_3\) in the source interval.
5. Exact Sturm real-root counts and Routh unstable-dimension counts at representative parameters \(a=-10,-4,-2,-1\), which determine the spectral type in each connected region between the three transition values.
6. The exact Hopf-frequency expression \(\omega^2=(331-\sqrt{100321})/220>0\).

The stored output was produced by the bundled checker and ends with `VERIFY_OK`. Decimal values in the report are rigorous enclosures or readability values derived after the exact algebra; they are not the proof.

This verification establishes only the local linear spectrum claimed in the finding. It does not verify nonlinear Hopf criticality, attractor existence, Lyapunov exponents, or a mechanism for chaos-hyperchaos transitions.
