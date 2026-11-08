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

The event of nonnegative weights integrating (1,x,x²) with target (1,0,q), q∈(0,1), is convex hull membership (0,q) in parabola points (X_i,X_i²). With opposite signs, the feasible vertical segment is from nearest-sign product uv to extreme-sign product ab because the curve is strictly convex and every opposite-sign chord hits height rs at zero. Thus E_n iff uv≤q≤ab, and strict interior yields all node weights strictly positive by epsilon redistribution for n≥3; for n=2 event measure zero. Joint unconditional extreme density n(n−1)(a+b)^{n−2}/2^n and near-zero density n(n−1)(2−u−v)^{n−2}/2^n, integrated over ab≥q, give displayed exact double integral, n3=3q/2(log(1/q)−1+q) and n4=2P3. Failures ab<q and uv>q are disjoint. Constraints ab≤q ⇒ a+b≤1+q and uv≥q ⇒ u+v≥2sqrt(q) yield sharp root upper bounds; events all nodes in [-q,1] and all outside [-s,s] with both signs yield matching root lower bounds. Therefore lim(1−P_n)^(1/n)=max{(1+q)/2,1−sqrt(q)}, crossover q=3−2sqrt2. Independent adaptive double integration at q=.12,1/3,.7 checked n3/n4 closed forms; direct sample computations are not an all-n proof.

## originality

PASS

Best-of-knowledge original scientific contribution confined to the exact theorem beyond explicitly acknowledged prior partial coverage. Meaningful searched aliases, broader-result implications, primary source materials, and access limits are documented below.

## value

PASS

Exact positive-weight feasibility probabilities for the first nonlinear moment system (quadratic integration) quantify a natural numerical quadrature design constraint across every n and q. The two independent geometric failure mechanisms and crossover at 3−2sqrt2 give a nontrivial sharp sample-complexity diagnostic beyond sufficient high-probability bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
