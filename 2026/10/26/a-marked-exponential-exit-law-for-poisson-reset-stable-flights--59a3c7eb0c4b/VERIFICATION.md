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

Reconstructed the full theorem for each fixed 0<alpha<2, sigma,r>0 and -1<Lambda<1, with the symmetric stable characteristic exponent sigma^alpha |k|^alpha, actual post-jump location and one rate-r independent Poisson reset clock. The Lévy density c|z|^{-1-alpha} integrates to lambda across the exterior of (-1,1) after shift Lambda. On each reset excursion, decompose jumps at delta L. Large jumps have rate O_delta(L^-alpha); two or more before independent Exp(r) time cost O_delta(L^-2alpha). The compensated symmetric small jumps have quadratic variation 2c(delta L)^{2-alpha}/(2-alpha), and stopped Doob yields an O(delta^{2-alpha} epsilon^-2 L^-alpha) probability of macroscopic displacement. After excluding the O(epsilon L^-alpha) boundary landing band and controlling tails, the marked single-excursion success measure converges at rate L^-alpha to (c/r)|y-Lambda|^-1-alpha dy. In particular p_L~lambda/(rL^alpha). The factor e^{-s tau_L/L^alpha} changes the successful measure by at most O(L^-alpha sqrt(p_L)) =o(L^-alpha) since tau_L<R and E R²=2/r². The exact geometric renewal transform q_L(s,g)/(1-E[e^{-sR/L^alpha}1_{R<tau_L}]) has denominator (s+lambda)/(rL^alpha)+o(L^-alpha), yielding Exp(lambda)×Pi for all s≥0 and bounded continuous g. Integrating the exterior power law gives the stated side bias and conditional Pareto overshoots. All limiting integrations are finite because Lambda strictly interior and alpha>0; alpha<2 is needed for the small-jump variance cutoff. Independent code repeated 243 bounded constant, normalizer, tail, Laplace and finite-renewal checks; these are not substitutes for the analytic infinite-L proof. Excluded alpha=2, varying parameters and convergence-rate assertions.

## originality

PASS

Qualified best-of-knowledge novelty of the full fixed-rate, two-sided continuous-time joint law (Exp waiting time independent of the complete scaled exit location), not of the mean, the one-big-jump heuristic, renewal calculus, nor stable overshoot tails in unrelated settings. The exact same mathematical model 2026 paper proves leading mean first passage time, not a joint marked limit. Primary preprints on discrete-time leapovers and unreset Levy bridges study different protocols and observables. Independently searched published mathematical findings and general heavy-tail escape theory; no inspected theorem was shown to imply this full statement, with residual risk of a more general marked regenerative rare-event result or a detailed appendix not located.

## value

PASS

The model, large-interval scale and mean exit-time problem are natural and already investigated. The complete two-coordinate weak limit gives the limiting exit sign, size of the terminal overshoot and independence of where a heavy-tailed search exits from how long it takes, quantities not implied by the previously published mean asymptotic. Exact asymmetric reset-point bias and conditional Pareto tail formulas are independently useful for stochastic search risk and first-exit mark questions. The value is a self-contained nontrivial marked rare-event refinement, without asserting a novel general regeneration method or a wider theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
