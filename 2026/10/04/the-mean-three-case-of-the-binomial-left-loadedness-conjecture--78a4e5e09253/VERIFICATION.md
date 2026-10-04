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

The theorem is analytic. For \(n=6\), binomial symmetry gives \(\alpha_i=0\) for all three indices. For \(n>6\), the literature-verified Simmons inequality gives \(\alpha_1>0\). The remaining new calculation is the exact identity
\[
\frac{\Pr(X=6)}{\Pr(X=0)}-1
=\frac{(x-3)(x^4+246x^3+333x^2-216x-324)}{80x^5},
\qquad x=n-3.
\]
For \(x\ge4\), the quartic equals
\[
x^4+246x^3+333(x-4)^2+2448(x-4)+4140,
\]
which is strictly positive. Hence \(\alpha_3<0\), and the three-term sign-change argument proves \(L_1\).

The bundled checker replays the polynomial identities using integer arithmetic and evaluates small cases exactly as a stress test. Those finite evaluations are not an exhaustive proof and are not used to infer the result for all \(n\).

Scientific limit: no claim is made for means other than \(3\). Originality searches can miss a result expressed under different terminology; that risk is recorded in the review.
