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

The proof reduces the worst-case failure probability to the exact stopping-time tail
\[
\Pr\!\left(\sum_{r=1}^n G_r>T\right),
\qquad
G_r\sim\operatorname{Geom}\!\left(\frac{1-2^{-r}}2\right).
\]
For the bulk \(r\ge2\), the normalized log moment generating function converges to
\[
\Lambda(\theta)=\log\!\left(\frac{e^\theta}{2-e^\theta}\right).
\]
The saddle \(\theta_x=\log(2(x-1)/x)\) reaches the domain boundary imposed by \(G_1\) exactly at \(x=3\). Matching upper and lower bounds then give the two displayed branches of the rate function.

The accompanying checker verifies the algebraic branch matching and computes representative exact finite stopping-time tails by dynamic programming. These finite checks are corroborative only; they do not certify the asymptotic theorem by enumeration. The theorem does not assert protocol optimality or a converse for other adaptive learners.
