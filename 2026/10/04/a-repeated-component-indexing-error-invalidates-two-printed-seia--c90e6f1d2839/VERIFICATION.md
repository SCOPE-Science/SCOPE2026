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

The source's target equations and numerical component assignments were checked directly in the open-access article. The target model and Eq. (5.24) define \(F_3\), \(F_4\), and \(F_5\) as the infected, asymptomatic, and recovered fields. Eqs. (5.10)–(5.11) and (5.15)–(5.16) instead use \(F_3\) for \(A\) and \(F_4\) for \(R\); Eq. (5.21) also uses \(F_4\) in the \(R\)-predictor.

The bundled checker evaluates the rational witness
\[
\theta=\frac12,\quad \rho=2,\quad \gamma=\mu=\omega=\tau=1,
\quad E(0)=1,\quad I(0)=A(0)=R(0)=0
\]
and verifies
\[
F_3(0)=\frac12,\qquad F_4(0)=1,\qquad F_5(0)=0.
\]
It also verifies the two leading coefficient differences \(-1/2\) and \(+1\) that multiply \(t^\alpha/\Gamma(\alpha+1)\) in the printed-versus-target \(A\) and \(R\) equations.

The asymptotic step from field values to the leading fractional-integral term is analytic: for continuous \(g\),
\[
I^\alpha g(t)=\frac{g(0)}{\Gamma(\alpha+1)}t^\alpha+o(t^\alpha).
\]
No finite computation is used to infer convergence or nonconvergence. The result does not inspect unavailable source code and therefore does not certify whether the paper's plots used the printed or a repaired mapping.
