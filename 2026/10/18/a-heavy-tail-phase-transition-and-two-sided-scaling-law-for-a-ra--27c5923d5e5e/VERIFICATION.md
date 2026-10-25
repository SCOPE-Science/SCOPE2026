---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Let W_P(t)=P+2cos t and theta=arccos(1/4). Its three-frequency recurrence gives F(Phi_P(t))=Phi_P(t+theta). The projective triple map is invertible, except antipodal quotient at P=0; theta/pi irrational because 2cos theta=1/2 is a nonintegral rational algebraic integer contradiction, yielding unique Haar pushforward on each punctured rotation carrier. For P<2, D_P has two simple zeros with derivative absolute 2sqrt(1-P²/4) and nonzero numerator V±, giving precise r^-1 tails. For P=2 the double zero has D≈(t−pi)² and numerator norm sqrt261/4, giving r^-1/2 constant sqrt(a)/pi. For P>2 the positive denominator lower bound gives compact support. Layer cake proves exact moment cutoffs; approximating divergent R^q below by capped observables continuous at poles proves divergence along every complete orbit. Setting t=pi+sqrtδ z gives denominator δ(z²±1), yielding the two limiting arcs lengths. Independently checked 12 conjugacy evaluations and twelve deterministic root-isolation threshold profiles at δ=1e−3 and 2e−4, including zero-plus-side cases. Finite diagnostics do not prove all-orbit limit/unique ergodicity, which follow from the irrational rotation argument.

## originality

PASS

Best-of-knowledge originality is assigned to the exact strengthened/specialized claim, not to previously published premises: Known conic geometry plus irrational rotation implies the invariant measure on a specified carrier; the sharp r^-1 vs r^-1/2 vs bounded tail trichotomy and exact two-sided scaling profiles are new computations not stated in Theorem 4.4. Be cautious that these are elementary consequences of singularity order, not a general new ergodic principle. Targeted Resultary searches and primary-paper comparisons were performed; unsuccessful searches are not priority proof. The original map paper treats general complex-root families and orbit conics, covering the conjugacy and invariant-carrier construction, but does not imply explicit radial moment constants without specialize-and-analyze singular observables. General ergodic theory proves existence and recurrence but not the two-sided crossover for this rational observable.

## value

PASS

The studied rational map has a natural projective-conic invariant family with an actual singular geometric transition at P=2. Tail exponents, sharp moment cutoffs and both crossover profiles are physically and mathematically interpretable orbit-sampling invariants not specified by the known existence of conics. The result is narrow but resolves a motivated distributional transition exactly and provides all-orbit divergence beyond almost-sure ergodic statements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
