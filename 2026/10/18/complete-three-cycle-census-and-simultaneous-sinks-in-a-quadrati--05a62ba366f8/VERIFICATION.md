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

The scalar recurrence retains all periodic states because the first coordinate of the three-dimensional state is forced by the preceding pair. Equal coordinates give only the fixed point or the cyclic form (nu,s,s) with a(s−nu)(s+nu)^2=1; its level-set count changes at k=27/32. For distinct A,B,C, subtracting the recurrence equations and dividing by the actual nonzero differences forces (S−t)(Q−3t^2)=−1/a at each of the three roots. Coefficient comparison gives P=−S^2, Q=3S^2 and R=−S^3−1/(3a). Newton sums give the squared-difference sum −4S/a and hence S=3nu/5. Conversely these relations make all three recurrence residuals equal with zero sum, for each ordering. The cubic discriminant is −3(96a nu^3+125)/(125a^2); strict positivity gives precisely two cyclic classes, with no distinct branch at equality. On the repeated-coordinate branch the planar trace is 16s^2/(s+nu)^2 and determinant zero, giving the claimed strict stability interval for the middle root only. Direct rational perturbation propagation at a=6331625/4572288, nu=−1 reproduces both orientation-specific trace/determinant pairs and the strict Schur tests. The three-dimensional derivative has a zero extra multiplier; simple roots and strict Schur inequalities persist on an open parameter neighborhood.

## originality

PASS

The normal form, one constructed three-cycle and analysis of its multiplier have direct primary precedent. Two distinct hyperbolic period-three sinks with all-distinct heights at one quadratic parameter, together with the all-distinct-branch exhaustion and exact onset, are supported as the distinct contribution relative to verified earlier material. Later indexed findings exactly overlap the count after rescaling; the strongest retrieved one does not assert attraction. No claim of historical uniqueness is made.

## value

PASS

The census answers a natural uniqueness question for the simplest quadratic defining polynomial in a studied family. The second threshold reveals two previously unaccounted cyclic orientations, and the exact witness proves stable coexistence, persisting under perturbation despite the strong nilpotence restriction in the original coordinates. Counting only the repeated-coordinate branch would miss both phenomena.

The dated certificate retains the supplied scientific assessment, sources and limitations.
