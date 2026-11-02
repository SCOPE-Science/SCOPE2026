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

Fraïssé homogeneity reduces complete types to all finite labelled strict poset extensions of the fixed chain. Every new point has a unique pair 0<=ell_i<=u_i<=n of predecessor/successor cut positions. The necessary relation inequalities for comparable and incomparable tuple points are exactly the isotonicity arrows of Q_F. Conversely the proof checks all mixed triples and forces any x_i<a_t<x_j comparison to agree with F; no extra transitive closure constraints remain. Thus T_r(n)=sum_F Ω_QF(n+1). Surjective isotone images of sizes k=1..2r yield strictly positive integer c_r,k because any linear extension can be coalesced into k nonempty consecutive blocks, establishing degree precisely 2r. Independently direct full ternary-relation closure matches endpoint formula in 12 configurations. The closed r<=3 formulas have been checked against original verifier and structural constraints.

## originality

PASS

Earlier full Resultary paper on random-poset 1-types proves c(C_n)=binom(n+2,2) and an arbitrary-parameter #P-completeness theorem: this explicitly dominates the r=1 specialization and must be credited. The earlier empty-parameter orbit-profile paper counts p_r, not relative tuple types over varying named chains. Jochemko/Stanley prove order-polynomiality for fixed posets but do not construct the Q_F tuple-constraint family or identify the complete r-arity type spectrum; the published OEIS A071245 scalar r=2 polynomial is known. The new contribution is the all-r structured endpoint bijection and positive 2r binomial spectrum, with possible older combinatorial extension-enumeration priority risk.

## value

PASS

Parameter-dependent complete type spectra are natural invariants of the countable generic poset. The explicit arity-uniform endpoint representation, sharp degree 2r, strict positivity of all binomial-coefficient layers, and limiting 1/4:1/4:1/2 relation split are useful structural facts, not merely a finite sequence lookup. This contrasts polynomial growth over chain parameters with established exponential growth over antichains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
