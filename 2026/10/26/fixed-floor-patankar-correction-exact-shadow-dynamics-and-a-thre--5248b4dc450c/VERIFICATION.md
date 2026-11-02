---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Expand the two SDIRK stage resolvents as Y_j=y+O(h), giving scaling s_i=y_i/max(y_i,eps)+O(h) uniformly on the mass simplex. The exact corrected resolvent then has drift G phi_eps(y)+O(h); uniform Lipschitz stability and discrete Gronwall yield global O(h) shadow-flow convergence including nonnegative boundary data. For α>β, monotonicity of phi_eps and the strictly decreasing scalar drift yield one attracting equilibrium. Solving respectively both-below-floor, mixed and both-above-floor balances gives the square-root, quadratic and true-equilibrium branches with exact matching boundaries. At exact ydagger the stage predictors equal ydagger for every h; inversion gives delta=h{β z^2/max(z,eps)-α x^2/max(x,eps)}/{1+h[α x/max(x,eps)+β z/max(z,eps)]}, strictly positive iff eps>x, with exact α=4,β=1,m=1,eps=2,h=1 value x_new=1/3. Direct rational tests and 21 branch checks corroborate, but analytic stability establishes the infinite limit.

## originality

PASS

The 2026 Nurkhametova et al. preprint defines the final-stage correction with a denominator floor and analyzes positivity, conservation and ε-dependent error; it does not in the read sections state the exact fixed-floor shadow ODE, three-branch equilibrium, or all-positive-h displacement at exact equilibrium. The complete 2022 Torlo–Öffner–Ranocha study of different modified Patankar methods treats equilibrium preservation and near-zero effects but not this final-only floor-correction formula. Qualitative fixed-floor bias may be inferred from original consistency analysis, but not these exact identities as stated.

## value

PASS

A sharp method-design boundary shows unconditional positivity and conservation can coexist with systematic equilibrium bias under refinement. The three regimes quantify exactly when a minority component is biased, and the all-h explicit equilibrium displacement gives a useful well-balancing diagnostic for a natural two-state test problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
