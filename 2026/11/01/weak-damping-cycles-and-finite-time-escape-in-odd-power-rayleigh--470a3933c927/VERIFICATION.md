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

For xdot=y, ydot=-x+eps*(1-x²)*y^m with m positive odd fixed, E=(x²+y²)/2 satisfies Edot=eps*(1-x²)*y^{m+1}. Harmonic averaging yields Delta E=eps*A_m*r^{m+1}*(1-r²/(m+3))+O(eps²), A_m=2*pi*binom(m+1,(m+1)/2)/2^{m+1}; the simple root r0=sqrt(m+3) and C1 implicit-function expansion give a cycle with multiplier 1-2*eps*A_m*r0^{m-1}+O(eps²)<1. Global at-most-one cycle relies explicitly on Chen–Xiao–Zhang Theorem 1: g(x)=x, f(x)=eps*(x²-1), sign changes at ±1, x*g(x)>0 and potential G(±1)=1/2 satisfy its hypotheses; uniqueness is not a new theorem. At m=1, Edot≤2eps E implies forward global existence by Gronwall for any eps>0. For odd m≥3 and arbitrary eps>0, on the explicit open set |x0|<1/8, y0>Y large with eps Y^m≥1 and 2/((m-2)eps Y^{m-2})<1/8, ydot≥(eps/2)y^m and x remains in (-1/8,1/4); finite-time forward velocity escape follows by comparison. Since w=y^{-(m-1)} has derivative tending -(m-1)eps*(1-x_inf²), the exact terminal velocity law and integrated (m-2)/(m-1) position law follow. No whole-plane basin classification is claimed.

## originality

PASS

Best-of-knowledge conclusion from actual source-tree proof reconstruction, current Resultary published-finding search and material inspected from primary literature: These new mathematical steps are not already implied by the prior at-most-one-cycle theorem, despite using it as a key lemma. A closer historical blowup theorem remains a documented priority risk. Source access and possible historical equivalents remain listed as residual risks.

## value

PASS

Natural global/local dynamics counterpoint: a unique hyperbolic attracting limit cycle can coexist with an open set of finite-time blowup trajectories for superlinear odd velocity forcing, whereas linear forcing has global forward solutions. The sharp degree transition plus explicit amplitude, multiplier and blowup exponents make a reusable concrete example, not merely a reparametrized linear oscillator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
