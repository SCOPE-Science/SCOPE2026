---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Both force generators take u to -gu, and the stated stationary laws give E[U²]=v²/2. Stationary harmonic convolution preserves equality of all force, position and mixed two-time covariances. Applying the stationary joint generator to xu and x² gives E[XU]=v²/[2(k+g)] and k E[X²]=E[XU], yielding the common mean work rate. For run-and-rest, the generator sends Q=u² to gv²-2gQ and P=xu to Q-(k+g)P. Therefore Phi=aQ+bP with a=1/[2(k+g)] and b=-k/(k+g) has L Phi=mu-(Q-kP). Both run-to-rest and rest-to-run holding rates are g; the squared-jump bracket has a²v⁴ and b²v² E[X²] from the two jump types collectively, and the mixed 2abv² E[XU] term comes only from the running states because the rest-to-run sign is symmetric. The two b-dependent contributions cancel by k E[X²]=E[XU], giving the proposed V3. For the telegraph process Q is constant and Phi=bP; the squared difference from flips is 4 b²X²U² at rate g/2, giving V2. The stationary joint process is an ergodic factor of the stationary irreducible force path, and the coordinate is bounded by v/k. Martingale bracket averaging and the bounded jump sizes give the CLT; the bounded endpoint corrector changes variance per unit time by o(1) via Cauchy–Schwarz. The ratio and derivatives give the crossing at g=k and unique parameter maxima at g=k and g=k/2, respectively. The result matches second-order moments, not full one-time or path distributions.

## originality

PASS

No independent originality is credited to the stationary run-and-rest model, the telegraph comparator alone, or the martingale method. The supported finding is the evaluated run-and-rest work variance and its exact reversal against a second-order-matched telegraph comparator across the trap/switching rate equality. The strongest inspected same-model literature concerns stationary position laws. The strongest matching reversal and work records change the observable, model or both. None yields this pair of rates or the ordering by specialization.

## value

PASS

This is a quantitative counterexample to inferring work-noise ordering from matched second-order propulsion or position data, even when the mean work also matches. The reversal at a physically interpretable rate equality, rather than only a pointwise difference, supplies a test of models with identical covariance diagnostics. The explicitly evaluated jump-bracket cancellation explains why the difference survives the matching.

The dated certificate retains the supplied scientific assessment, sources and limitations.
