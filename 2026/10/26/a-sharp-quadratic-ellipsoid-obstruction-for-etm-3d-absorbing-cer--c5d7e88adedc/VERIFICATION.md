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

In RESULT.md lines 25–63, coefficients of the distinct cubics x²y, x²z and xy² eliminate the three off-diagonal entries of W; the remaining xyz coefficient is a−2b+c. After translation, the even part of the boundary drift is the quadratic with diagonals (−2a,−b,−5c) and mixed coefficients b−aρ−cm_z, (b+c)ρ−am_x, and 2bm_y. Adding antipodal inequalities and rescaling every direction shows this form is negative semidefinite. The 2×2 minors bound the mixed coefficients by constants depending only on W, so m_x=(b+c)ρ/a+O_W(1), m_z=−aρ/c+O_W(1), m_y=O_W(1). Consequently f_y(m)=((2(b+c)−a)/c)ρ²+O_W(ρ)=3ρ²+O_W(ρ). At the positive y-boundary of the ellipsoid the exact drift is bt(f_y(m)−t), t=r/√b>0, giving the liminf. At the stated Euclidean center the completed-square drift is C−2(q_x+ρ)²−(q_y−h)²−5(q_z+(1−ρ)/2)². The shift has norm d; triangle inequality gives inward drift on the stated sphere and outside. Equality on the sphere would require both radial alignment with the shift and vanishing x,z coordinates after the shift; that is impossible since the shift has a nonzero x or z component for every ρ and C>0. Thus the sphere is forward invariant and entered in finite time from outside, by compactness of the intervening energy band. Rationalizing d−h and √C−h gives 5/12 and 13/12, respectively. The source's R(ρ) is the energy sublevel, not the radius. A bounded independent symbolic check of the antipodal and completed-square drift identities is replayable with `python /workspace/independent_reproduction.py`; no frozen code was executed.

## originality

PASS

The specific class-wide high-ρ lower bound is distinct on the inspected evidence. The published ETM construction gives an upper certificate; the closest same-flow theorem both overlaps the metric classification and resolves a different, small-ρ centered stability question. The fixed-metric necessity argument, including optimization over unrestricted centers, is the supported addition, not the ball or the cancellation definition.

## value

PASS

The source's conservative-looking radius raises a concrete certificate-design question: can the leading scale be reduced just by translating or reweighting the quadratic energy? The exact obstruction says no throughout a natural class and distinguishes certificate size from actual attractor size. This is stronger than constructing another sufficient ball.

The dated certificate retains the supplied scientific assessment, sources and limitations.
