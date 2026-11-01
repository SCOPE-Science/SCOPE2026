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

Directly reconstructed the sign-preservation lemma: writing q=sum w_j u_(j-1), next score q' differs by w1*sigma + sum_(j=1)^(L-1)(w_(j+1)-w_j)u_(j-1)-wL*u_(L-1). For sigma=+ the lower bound q'-q>=w1-sum(w_j-w_(j+1))-wL=0, and for - the reverse bound, so tie-breaking by the NEW current symbol preserves sigma. Induction gives constant emission; after t steps state has t new signs followed by the original prefix, yielding exact settling time. Global negation swaps equal-size basins. The sharp maximum follows from whether some initial sign can disagree with weighted-majority sign. Uniform count fixes first disagreeing index and counts remaining positive bits by binomial tails with even-length tie adjustment. Independent exhaustive iterates and counts for 329 nonincreasing weight vectors checked, not relied upon for general result.

## originality

PASS

España, Funez and Ugalde derive this same clover delay recurrence and analyze strict one-coordinate domination, which covers some easy regimes but not the full nonincreasing-weight cone with comparable weights (including all ones). New result: persistence under monotone lags, all basin and exact settling-time structure, and the full uniform histogram.

## value

PASS

A full phase-space classification, basin sizes and exact settling-time histogram of a nontrivial infinite family of deterministic memory majority dynamics is a natural exact dynamical invariant; the monotonicity condition sharply excludes a simple cycling example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
