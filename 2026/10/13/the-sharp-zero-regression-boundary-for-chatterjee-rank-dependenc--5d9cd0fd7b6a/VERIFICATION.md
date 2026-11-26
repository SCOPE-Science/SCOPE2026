---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the conditional CDF F_u(t), E[|V−V′| | U=u]=2∫F_u(t)(1−F_u(t))dt. Since E F_U(t)=t, this yields E|V−V′|=1/3−2∫Var(F_U(t))dt, confirming both normalizations of xi and xi≥0. The hypothesis makes E[V′|U,V]=1/2 by conditional independence. Conditional Jensen gives E|V−V′|≥E|V−1/2|=1/4, hence xi≤1/4. With at most two support points and V fixed at one, V−V′ has a fixed weak sign. With three or more support points one can choose three separated ordered positive-mass intervals; for V in the middle, V−V′ has both signs with positive probability, giving strict Jensen inequality. The integrated nonnegative gap is zero exactly when almost every conditional law has at most two support points. The known reflected singular example attains it. Absolute continuity gives conditional densities a.e. and hence nonattainment. In the proposed step family each row and paired column set has length 1/m, so both margins are uniform; reflection makes each row mean 1/2. For two independent row draws the same and opposite component events have probability 1/2 each, with respective distances in expectation 1/(6m) and 1−(2j+1)/(2m). Averaging gives E|V−V′|=1/4+1/(12m), verifying the exact approach xi=(1−1/m)/4, including m=1. The frozen arithmetic checker was inspected, not executed.

## originality

PASS

The supported distinct claim is the universal optimality of the zero-ratio bound and its full conditional-support equality characterization, with strict nonattainment and explicit sharp approach in the absolutely continuous class. The value 1/4 as an attained point was already known, and capacity 1/4 is covered in the reflected subclass. Those statements do not imply the universal conclusion.

## value

PASS

This identifies an exact boundary of the joint population-dependence region, rather than adding an isolated example. In particular, it quantifies how much rank dependence is compatible with no rank mean regression, characterizes all ways to attain the bound, and distinguishes singular attainment from a sharp supremum under a density. The Jensen proof's brevity does not eliminate the prior gap in this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
