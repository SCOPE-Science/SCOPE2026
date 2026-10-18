---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For symmetric iid {-1,0,1} law with endpoint mass t, nested minimum and maximum event indicators yield rho_n(t)=[((1-t)^n+t^n)^2-(1-2t)^n] / [(1-t)^n+3t^n-((1-t)^n+t^n)^2]. The numerator >0 and variance >0 on 0<t<=1/2. For t=c/n, local uniform expansions give n rho_n→H(c)=c²/(e^c-1). The global finite-n bound using variance >=ell(1-ell) excludes both nt→0 and nt→infinity for maximizing sequences, so all optimizers localize at unique c*∈(1,2) solving (2-c*)e^c=2. Thus nR_n→c*(2-c*)≈.647610238, nt_n→c*≈1.59362426. Independent rational moment checks recovered n2 t=1/3 rho8/19 and n3 t=3/10 rho81/319; own finite optimization found n16,64,256 convergence. Endpoint t=0 excluded but limit 0 guarantees attained interior maximum for each fixed n. Numerical grid only corroborative.

## originality

PASS

Prior Papadatos 2022/2023 characterizes n=2 for a discrete-uniform 3-point law, quotes general Corr(min,max)<=1/n and asks about nonuniform masses; this bound does not identify the optimal rare-endpoint constant or all optimizers. Related published records establish n=3 counterexamples and the nonoptimal uniform point at n>=3, but these local finite-n results do not imply the n→infinity sharp maximizer-scale theorem. López-Blázquez/Salamanca-Miño maximize transformed-variable correlation, a different optimization. The primary inaccessible portions of that source remain an explicit risk.

## value

PASS

The extreme-statistic dependence optimization is a natural longstanding question, and the nonuniform symmetric three-atom family exhibits a nontrivial rare-event transition. The rate c*/n and sharp coefficient plus localization of every maximizer are asymptotic optimization facts requiring a global escape-exclusion argument; finite-n counterexamples and universal 1/n bounds do not settle them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
