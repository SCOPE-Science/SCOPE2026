---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The non-Dirichlet Bloch determinant has cos(2t) coefficient 2/sin(kh)^2, so it cannot vanish on a positive-measure set of t. For sin(kh)=0, at generic Bloch phases both vertex values vanish and free rail-sine amplitudes solve the two Kirchhoff conditions if and only if some rung is Dirichlet. When rails are not Dirichlet, two Dirichlet rungs with unequal cos signs have a nonsingular 2x2 endpoint-derivative constraint; equal cos signs provide an opposite-rung compact eigenstate. With exactly one Dirichlet rung d, elimination of its free derivative gives 2(cos t cos A-cos kh)/sin kh-cot(ke)+cos(kd)csc(ke)=0, constant in t iff cos A=0. At k=0 a covariantly constant nonzero Bloch eigenstate can occur only at isolated compatible phases, not a flat band. Exact flux-only example h=3/4,r=1,s=2atan(1/2)/pi,A=pi/2,k=pi satisfies -2+3/4+5/4=0; symbolic verifier checks these edge cases.

## originality

PASS

Statement/implication comparison, not mere title search. Closest inspected antecedents give related machinery or narrower/scalar/qualitative statements, but not the full asserted theorem; coverage and inaccessible-source limitations are explicit.

## value

PASS

A complete if-and-only-if classification of positive flat energies in a natural unequal-length extension of a studied periodic tubular quantum graph, exposing a half-flux flat band supported by only one Dirichlet rung. The new branch is not a relabeling of equal-length Dirichlet levels and can inform spectral engineering and spectral localization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
