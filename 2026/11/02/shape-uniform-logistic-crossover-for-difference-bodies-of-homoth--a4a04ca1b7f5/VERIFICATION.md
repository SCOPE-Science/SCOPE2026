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

After shearing so the base contains zero, at fixed nonnegative height difference h both lateral scales decrease as the lower height increases. The nested Minkowski sums are largest at lower height zero. Integrating this section and its reflection gives (1), including the direct prism limit; the mixed-volume expansion gives the exact quotient. Its integrand relative to the denominator weight is vol(B−s^−1 B)/vol(B), strictly decreasing because the added body is full-dimensional. The lower bound and equality follow from Brunn–Minkowski; all upper weights are positive, so the verified Godbersen inequality and the arbitrary-body equality theorem force a simplex. These arguments also cover the prism and pyramid; in m=1 the bounds agree. Continuity along Minkowski interpolation fills the interval. For the crossover, reflection symmetry and Alexandrov–Fenchel make the mixed-volume reweighting of Binomial(m,1/2) decrease in distance from m/2. Opposite monotonicities give mean m/2 and variance at most m/4. Taylor expansion of (1−u/m)^J about J=m/2 gives error at most u²/(2m), and comparison to exp(−u/2) contributes at most as much. The denominator differs from exp(−u) by at most u²/m and its integral is bounded below by τ exp(−2T), giving a uniform O_T(1/m) ratio error including τ=0. The planar linear inverse follows by integrating 1+2cs+s². The standalone verify.py and check_polytope.py were inspected as finite diagnostics, not executed or used to prove the unlimited-dimension statement.

## originality

PASS

The exact symmetric-base profile and its logistic limit are already on record, as is the arbitrary-base pyramid endpoint. The distinct claim supported here is the uniform normalized crossover for arbitrary varying, possibly nonsymmetric bases, with a shape-independent compact-interval error bound, together with the all-taper arbitrary-base section formula. The prior symmetric formula removes base dependence before the limit; it does not give concentration for the full collection of mixed-volume profiles. Godbersen and its equality theorem are inputs, not original findings.

## value

PASS

The quotient is a standard affine invariant of a natural family. The complete taper profile interpolates two distinct sharp geometric regimes, and the uniform extension identifies a boundary layer even when the base changes arbitrarily with dimension. Reflection symmetry plus mixed-volume log-concavity giving a shape-independent variance estimate is the substantive reusable mechanism, beyond the known extremal-base calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
