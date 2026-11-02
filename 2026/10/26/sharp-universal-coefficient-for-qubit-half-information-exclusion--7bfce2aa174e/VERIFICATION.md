---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For g_c(v)=h(|v|)-h(x)-c h(z), the all-ensemble inequality equals Jensen concavity of g_c. The negative radial Hessian is R=A I+(B-A)u u^T with inverse R^-1=A^-1 I-(1-delta)vv^T. The Schur complement for x/z curvature gives Q_c with determinant delta*a*(Y+Z)*(1-Z)+delta² Y s-(1-2delta) XZ, a=1/c-1, delta=(1-A^-1)/s>=1/3. The largest required a at each radius is s(1-2delta)/delta, approached by Y=0,Z→0+,X=s-Z, yielding the exact global a*. This proves concavity for c=c*, violation for any larger c by local two-point ensembles, and pure-state extension by continuity; two oriented applications plus dephasing data processing yield the cross-information corollary. Independently verified determinant symbolically, a*=0.2647413168287692, c*=0.7906755213053483 numerically and a concrete Schur-negative witness for c>c*; decimal is diagnostic only.

## originality

PASS

Wang–Wang–Chen establish coefficient 1/2 for the same all-finite-label qubit ensemble domain and a two-qubit complementary correlation bound. The supplied refinement optimizes the one-sided coefficient with a matching local curvature violation, giving c*≈0.7906755. Available primary abstract and detailed secondary technical analysis do not state that optimized coefficient; full closest primary paper is inaccessible and is an explicit priority risk rather than an automatic O failure.

## value

PASS

The sharp universal tradeoff and explicit optimality witnesses are natural exact qubit-information invariants, strengthening an operationally relevant cross-basis lower bound by a non-negligible amount; it is not merely a numerical optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
