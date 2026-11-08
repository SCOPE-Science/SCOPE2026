---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For any selected pivots S, Sherman–Morrison gives residual D_{S^c}+(b^{-1}+sum_{i in S}d_i^{-1})^{-1}11^T. The exceptional index excluded/included fixes sum=k versus k-1+a^{-1}, hence exactly the event-based trace pair T0,T1. At j previous normal pivots, residual-diagonal sampling avoids exceptional with factor (n-1-j)(1+u_j)/[(n-1-j)(1+u_j)+a+u_j], u_j=(b^{-1}+j)^{-1}; multiplication is p0. Algebra yields T0-T1=(a-1)[1-(n-k)/((a x+1)(x+1))], x=b^{-1}+k-1. Greedy picks exception first and gives T1; expected random minus greedy=p0(T0-T1); the exact boundary is sharp and globally minimizes trace among two subset types. For n=t^3,a=t,b=t²,k=1: greedy~t^4, randomized~2t^3, ratio~t/2 while every correlation tends uniformly one and diagonal ratio tends one. Independently computed exact SymPy Schur complements for every k-subset with n=5,7 and two rational (a,b) pairs; all matched formulas. Finite checks are not proof of asymptotics.

## originality

PASS

Qualified best-of-knowledge originality: compared exact claim and possible implications with relevant primary literature and two actual semantic published-record searches; a failed search is not proof of novelty. Schur complement and greedy-failure existence are known premises. Their combination does not by itself imply the probability-product formula, exact finite k global optimum or correlations-tending-one counterfamily.

## value

PASS

The exact finite-step residual law, necessary-and-sufficient pivoting reversal and unbounded failure under near-perfect correlations expose limitations of a widely used numerical heuristic under strikingly benign-looking covariance structure. It is not a generic worst-case failure restatement because earlier block-diagonal constructions have vanishing cross-correlations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
