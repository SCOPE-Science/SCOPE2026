---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The source rational MGF is F=[(P_J(t)-t²)/P_J(0)]/[Q(t)/Q(0)] with P_J=(mn-2t)((m-1)n-t)(m(n-1)-t) and Q=(mn-3t)((m-1)n-2t)(m(n-1)-2t)((m-2)n-t)((m-1)(n-1)-t)(m(n-2)-t). At R=mn/3, split logF=log J+log(1-h), h=t²/P_J. Coefficientwise 0<=h(Rz)<=h*(z)=z²/[36(1-2z/3)(1-z/2)²], with a_p=(2/3)^p-(p+3)/(3*2^p)>=0, p a_p<=1/3, sum a_p=1/3. From c_p=p[z^p](-log(1-h*)), c_p=p a_p+sum_(k=2)^(p-2) a_k c_(p-k), induction gives c_p<=1/2. Three J numerator poles-zero pairings contribute nonnegatively and the remaining simple pole at R contributes 1/p, thus p[z^p]logJ(Rz)>=1. Defect <=1/2, implying p[z^p]logF(Rz)>=1/2, hence full lower bound for ALL p,m,n. Independent exact rational coefficient tests for 5 size pairs and orders<=50 confirmed the bound; no finite experiment used to prove infinite claim.

## originality

PASS

Wastlund (2026) explicit three-edge MGF, Janson comparison and Conjecture 10 positive cumulants supply the exact analytic problem. Source Proposition15 zero-free disk is weaker than all-sign coefficient positivity; follow-up paper extends zero-free at k=4 but not all cumulant positivity. The source MGF is not claimed as original. Wastlund full primary manuscript could not be read this run because open-access text unavailable and authorized Oxford returned vpn_disconnected; original full statement coverage risk explicitly retained. Alm--Sorkin 2002 full paper inaccessible, possibly relevant to exact distributions. Best-of-knowledge O passes subject to these named gaps and the source excerpts actually read.

## value

PASS

A dimension-uniform all-orders inequality resolves an explicit open conjecture at the first nontrivial matching size three, not merely finite cumulant positivity. Strict quantitative bound can inform probabilistic shape and absolute-cumulant comparisons. Scope intentionally excludes larger matching size and optimality of lower constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
