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
The universal argument is analytic.

For each eigenvalue \(\lambda\), zero-velocity Heavy-Ball gives
\[
p_1(\lambda)=1-\alpha\lambda,
\]
\[
p_2(\lambda)=(1-\alpha\lambda)^2-\beta\alpha\lambda.
\]
With
\[
\rho=\frac{\sqrt\kappa-1}{\sqrt\kappa+1},
\]
one has
\[
\alpha\mu=(1-\rho)^2,
\qquad
\alpha L=(1+\rho)^2,
\qquad
\beta=\rho^2.
\]
This yields the endpoint ratios
\[
g_\mu=\frac{\rho(3-2\rho)}{2-\rho},
\qquad
 g_L=\frac{\rho(3+2\rho)}{2+\rho}.
\]
The latter is larger and equals
\[
\frac{(\sqrt\kappa-1)(5\sqrt\kappa+1)}{(\sqrt\kappa+1)(3\sqrt\kappa+1)}.
\]
The condition \(g_L\le1\) reduces to
\[
\sqrt\kappa\le2+\sqrt5,
\]
which is equivalent to
\[
\kappa\le9+4\sqrt5.
\]

For dimension three, the interior curvature
\[
\lambda_*=1/\alpha
\]
has
\[
p_1(\lambda_*)=0,
\qquad
p_2(\lambda_*)=-\beta.
\]
If \(\alpha\lambda=1+\varepsilon\), then
\[
p_1=-\varepsilon,
\qquad
p_2=\varepsilon^2-\beta(1+\varepsilon),
\]
so the adjacent objective ratio diverges as \(\varepsilon\to0\).

The embedded `verify.py` checks the endpoint identities symbolically through polynomial cross-multiplication, verifies the threshold polynomial, and replays the exact \(\kappa=4\) examples with rational arithmetic. Finite computation is corroborative only and does not replace the all-\(\kappa\) proof.

The result does not address later iterates, arbitrary momentum initialization, nonquadratic objectives, or other parameter choices.
