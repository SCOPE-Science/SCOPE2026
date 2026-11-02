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

For the original unrelaxed zero-linear-operator SAV recurrence on f(x)=x²/2, set t=1/h and A=x²+2C. The updates rationalize to r_{k+1}=r_k tA/(x²+tA), x_{k+1}=x_k−2r_k sqrt(A/2)x/(x²+tA). The exact first step yields x1=a(t(a²+2C)−2C)/(a²+t(a²+2C)) and r1=O(t); the second yields r2=O(t²) and x2=−2C/a+[(a²+2C)²/a³](1+|a|/sqrt(2C))t+O(t²). For b=−2C/a≠0 an invariant compact interval around b bounds all subsequent shrink factors r_{k+1}/r_k≤tR; the entire infinite x-tail from step2 is O(t²), hence x∞≠0 and r_k→0. The exact a=C=1,h=20 rational/square-root witness traps all subsequent steps. Independently evaluated the recurrence at steps h=50..5000: h(x∞+2) converges numerically toward 9(1+1/sqrt2), corroborating—not proving—the expansion. The source paper's Theorem1 certifies r² decay, not stationarity if r∞=0.

## originality

PASS

Best-of-knowledge PASS for exact nonstationary limit and reciprocal correction in the unrelaxed SAV quadratic recurrence; 2023 source covers energy decay and falsely infers stationarity without ruling out r*=0, but does not establish this explicit counterexample.

## value

PASS

The nonstationary ghost limit on the most elementary strongly convex objective exposes an important gap between unconditionally decreasing auxiliary energy and actual optimizer correctness. The reciprocal leading location, sharp first correction and rigorous fixed-step witness provide substantive diagnostic information for numerical integrators, beyond a qualitative slow-convergence warning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
