---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For every finite set of integer frequencies and each sign, lift its arcs to finitely many rational-center intervals of halfwidth r/a; a common intersection component has normalized length [min_a(u c_a+1/a)-max_a(u c_a-1/a)]_+ at u=1/r. This bracket is concave in u and globally maximized at u=0 by the shortest interval length, hence decreases in u and P_r(A)/r increases in r. Piecewise-affine rationality follows from finite rational center tuples. The powers-of-three family has precisely one central positive interval and its antipodal negative, giving equality 4r/3^(n-1). For r=1/5, exact two-frequency Bernoulli Fourier formula with finite b<=14 table and Lipschitz bounds for b>=15 proves inf P=4/15; scale monotonicity yields inf P_r=4r/3 on [1/5,1/4]. Independent rational interval partition checked examples [1,3], [1,2], [1,5], [2,5], [1,3,9], [1,3,9,27] and [2,3,7] at 1/5 and 1/4; all agreed, including P_1/5({1,3})=4/15 and P_1/4({1,3})=1/3. Exact proof, not finite testing, supplies unbounded frequency cardinality.

## originality

PASS

The 2019 sign-correlation literature studies radius 1/4, while Giannitsi–Madrid 2026 treats threshold correlations broadly and gives asymptotic n-frequency bounds. The inspected abstract has no explicit universal sharp P_r/r comparison or continuous two-frequency interval, but full text was inaccessible, so it remains a material priority risk. The reciprocal radius 1/5 pair minimum is credited as prior coverage; new assessed assertions are the sharp all-cardinality radius law and its continuum consequence.

## value

PASS

The radius law controls threshold correlation over every frequency family simultaneously and transfers exact reciprocal-radius extremal data to a genuinely continuous interval. Exact sharpness at every cardinality and an explicit nonreciprocal two-frequency optimum address meaningful harmonic-analysis questions rather than a numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
