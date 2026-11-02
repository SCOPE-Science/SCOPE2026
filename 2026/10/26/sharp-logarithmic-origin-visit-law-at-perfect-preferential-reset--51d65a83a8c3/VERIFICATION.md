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

Under perfect off-origin relocation, an indicator of being at the origin next step has exact conditional probability q_n=C_n/(n+1)(1-pJ_n), p=1-xi_0. Hence a_n=C_n/(n+1) is a bounded nonnegative supermartingale with drift -p a_nJ_n/(n+2). Summability plus a hypothetical a_infty>0 contradicts harmonic divergence, giving a_n→0. The log C increment has predictable drift (1-pJ_n)/(n+1)+O(1/[(n+1)C_n]); its martingale controls first polynomial C_n growth, then C_n=n^(1-o(1)) a.s., yielding eventually C_n>=n^(3/4). Exact drift of Q_n=(n+1)/C_n is pJ_n/C_n+r_n with r_n <=C_n^(-2); conditional variance <=4(n+1)/C_n³. Both summable, so Q_n -p Σ_(k<n)J_k/C_k converges a.s. The harmonic identity Σ_(k<n)J_k/C_k=H_(C_n)-J_n/C_n yields Q_n-p log C_n→L and inversion gives -p loglog n correction and C_n log n/n→1/p. Independent exact rational derivation checked 4680 (t,c,J,p) drift configurations. Requires xi_0 in (0,1), off-origin relocation exactly one and origin start; no claim on L law or nondegeneracy.

## originality

PASS

Armfield–Mailler study this exact impurity walk and prove localization for off-origin relocation xi in an open interval (Xi,1), explicitly excluding xi=1, without a sharp pathwise local-time law. Boyer et al. analyze qualitative stationary mass near the strong-memory boundary, not almost-sure Q_n-p log C_n convergence and loglog correction at the singular endpoint. Homogeneous monkey-walk scaling theories have different site-independent relocation hypotheses. This exact pathwise endpoint expansion is best-of-knowledge original, with reinforced-urn priority risk.

## value

PASS

At the singular perfect-reset boundary, the walk has a nontrivial logarithmic local-time regime. The pathwise sharp coefficient, universal dimension independence and negative loglog correction refine qualitative stationary predictions and resolve a motivated endpoint asymptotic rather than a mere finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
