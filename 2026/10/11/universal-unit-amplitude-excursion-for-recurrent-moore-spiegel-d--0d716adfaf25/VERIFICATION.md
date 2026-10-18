---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

C: Prior balance-generating polynomials F,G have exact Lie derivatives y²−Tx² and z²+(R−T)y²−Rx²y²; independent symbolic expansion confirmed. Invariance of xy yields ∫xz=−∫y². Cauchy–Schwarz and ∫y²=T∫x² imply ∫z²≥T∫y² for T>0. Substitute in second balance and divide by R>0. Equality forces z=−Tx µ-a.e.; invariant support is flow invariant, and L(z+Tx)|_{z=−Tx}=R(1−x²)y. The only orbit trapped in z+Tx=(1−x²)y=0 is origin, giving strictness for any other µ. Positivity of weighted (x²−1)y² forces mass at |x|>1,y≠0. Compact support legitimizes all polynomial averaged derivatives; no claim of existence for each T,R.

## originality

PASS

O: Complete published same-ODE prior yields exact balances and only weaker parameter-dependent threshold for R>T. The additional xy stationarity covariance and equality rigidity are not part of its theorem; the strict universal barrier is not a consequence of its stated excursion conclusion. Bibliographic search left old full manuscript inaccessible.

## value

PASS

V: A universal and strict geometric threshold for all nontrivial compact recurrent statistical states, independent of both physical parameters, is a meaningful strengthening of the previously known damping-sign boundary and applies even where that earlier support argument cannot be used. This is a necessary recurrence obstruction, not a rebranding of an existing numerical observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
