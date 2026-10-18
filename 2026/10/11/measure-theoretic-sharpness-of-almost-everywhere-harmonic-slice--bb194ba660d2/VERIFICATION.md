---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Both 0 and log|z_1|+a are plurisubharmonic, with the latter allowed -infinity only before the bounded maximum; local boundedness plus finite max ensures continuous finite psh phi_a. The first-coordinate disk restriction equals 0 until radius exp(-a), then log|w|+a; its radial derivative jumps, so nonharmonic. For direction xi, the ridge lies inside |w|<1 exactly when |xi_1|>exp(-a); boundary equality has identically-zero open-disk slice. For Haar-uniform xi on complex unit sphere, |xi_1|² has Beta(1,n-1) law, giving tail (1-exp(-2a))^(n-1); choosing a below the stated logarithmic epsilon threshold yields the assertion. Includes n=2 and epsilon endpoint restrictions. This is an exact construction, not experimental extrapolation.

## originality

PASS

Best-of-knowledge quantitative counterexample to a recently proved a.e.-direction threshold. A positively measured arbitrarily small exceptional set defeats any positive tolerance; direct source theorem controls only null sets. Original primary material inspected; generic absence of index hits is not treated as proof of global novelty.

## value

PASS

The exact limiting boundary of a newly formulated almost-everywhere rigidity theorem is mathematically natural: zero measure is best possible even among bounded continuous finite psh functions, and the bad-direction fraction is explicit in every dimension. This gives a useful sharp obstruction to proposed positive-tolerance stability generalizations; it is not merely a recasting of the null-set theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
