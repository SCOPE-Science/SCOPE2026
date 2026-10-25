---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

From conditional depth martingale innovations ξ_j and their exact recurrence v_{j+1}=(1-p_j²)v_j+p_j(1-p_j), var(T_n)=sum_{j<=n}[1+(n-j)p_j]^2 v_j. Summation yields v_j~c j^(1-β)/(1-β), with sum_j p_j² v_j having exponent 1-3β. Riemann-beta integration for β<2/3 gives coeff 2c³/[(1-β)(2-3β)(3-3β)(4-3β)], critical harmonic sum gives 3c³ n²log n; for β>2/3 orthogonal martingale series converges a.s. and L², Kronecker controls centered remainder. The finite exact enumeration checker over sizes 3..7 validates recurrence for sample weights; independent recurrence numerics at n=20k for β=.6,2/3,.8 show expected scaling trend, not asymptotic proof. Nonzero ξ_3 variance implies σ²>0.

## originality

PASS

Compared exact hypotheses, invariants, reductions, implicit prior implications, and relevant primary theorem/proof sections. None of the inspected cited primary results implies this final precise statement under its hypotheses; originality is best-of-knowledge only, with named residual risks.

## value

PASS

A sharp phase transition for a natural stretched-exponential cumulative-weight family lying outside the previously treated p_n=O(1/n) regime; identifies when normalized total depth has nontrivial L² martingale limit and separates power, logarithmic, and quadratic variance growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
