---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

From a standard one-dimensional Brownian hitting density f(s)=e^{-1/(4s)}/(2√πs^(3/2)), independent exponential mortality and Poisson recruitment give exact P(τ>t0s)=(1−F_m(s))e^(−ρmJ_m(s)) with m=x logρ. A reciprocal-endpoint substitution w=1/(4s) gives F_m~e^(−w−m/(4w))/√(πw), J_m~e^(−w−m/(4w))/(4√π w^(5/2)) uniformly w=L+O(logL), x bounded away from zero and infinity. With centering C_L=L−1.5logL+log(x/(4√π))−x/4, ρmJ_m→e^(−z), producing standard Gumbel. Analytical tail bounds at w≈L/2 and dominated kernels control all fixed integer moments, permit E[1/(4(C_L+G_L))] expansion and the displayed second-order mean term; x/4−log x has unique fixed-positive-x minimum at x=4. Independently checked the endpoint intensity at L=50 and L=150 for x=1,4,8 and z=−1,0,1; errors decrease but finite convergence is slow. No finite-ρ global minimizer claimed.

## originality

PASS

The survival and mean integral identities are explicitly prior art (Gutiérrez et al, Linn–Kumar, Mercado-Vásquez–Boyer). Tung–Lawley proves fast-immigration Gumbel for a fixed single-searcher law, unlike this triangular array with mortality changing as logρ. The explicit moving-centering and second-order fixed-coefficient design have not been located in primary sources read, with caveat of incomplete latest Gutiérrez full text.

## value

PASS

Natural independently-recruited mortal Brownian search provides a sharp rare-fast-arrival Gumbel limit in a joint changing-parameter regime, including second-order optimal mortality coefficient within a stated asymptotic design class. This goes beyond mean-only fixed-ratio optimization and is directly interpretable for search process design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
