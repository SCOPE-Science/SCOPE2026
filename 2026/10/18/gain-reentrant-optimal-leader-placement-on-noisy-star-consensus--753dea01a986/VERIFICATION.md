---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Connectivity with at least one pin gives positive definiteness and the Lyapunov solution is A⁻¹/2. The hub indicator c determines the entire placement orbit, with r=q−c pinned leaves. Set t=κ/(1+κ) and u=1−(1+κ)⁻². Eliminating the diagonal leaf block gives trace n−1−rt+(n−ru)/(cκ+rt). Subtracting the two cases gives the stated rational gap after dividing by two. Its sign is the sign of 2q−n+q(q−1)κ/(1+κ)². For q=1 the gap is the negative constant (2−n)/2. Otherwise the final gain function is strictly positive, increases to 1/4 at one and decreases thereafter by reciprocal symmetry, proving the strict regimes, the tangent tie, and the two reciprocal roots in the intermediate case. For q=2 the intermediate interval contains no integer n; for q≥4 it requires n≥9. For q=3 the first and only such order is seven, where the gap numerator is −κ²+4κ−1, the roots are 2±√3, and at κ=1 the variances are 31/8 and 23/6. The ‘smallest’ example is scoped to the stated unit-star family.

## originality

PASS

The distinct result is the all-budget comparison for a single unweighted star with equal finite gains and the resulting exact reciprocal reentrance threshold. The arbitrary-graph formulation and effective-resistance identity are prior. So are general one- and two-noisy-leader criteria. A related same-day reentrance theorem is acknowledged rather than treated as irrelevant from its date, but its two-hub topology and competing leader classes are different.

## value

PASS

The result identifies a natural counterexample to a gain-independent or monotone rule for whether the central hub belongs to an optimal leader set, on the simplest family with a unique hub. It gives all exact ties and the smallest star witness rather than a numerical example or an isolated gain comparison. This supplies a benchmark for finite-feedback placement methods beyond perfect pinning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
