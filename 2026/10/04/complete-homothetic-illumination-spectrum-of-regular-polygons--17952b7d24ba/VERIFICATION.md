---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The completeness reduction follows from Horváth–Lángi's polygon theorem: a homothetic illumination body must arise from a \((k,l)\)-extension with \(k,l\ge1\), even \(k+l\), and \(k+l+1<m/2\). For a regular \(m\)-gon, rotational symmetry centers the homothety and sideline intersections with normal separation \(2q\alpha\), \(q=k+l+1\), give \(\mu=\cos\alpha/\cos(q\alpha)\). Choosing \(k=l=(q-1)/2\) realizes every admissible odd \(q\). The triangle-minus-polygon-cap area calculation reconstructs \(\delta=R^2(\cos^2\alpha\tan(q\alpha)-q\sin\alpha\cos\alpha)\). I independently checked the algebraic equivalence of the two area expressions and the count \(\lfloor(m-3)/4\rfloor\) for all \(3\le m\le60\); those finite checks are corroborative, while completeness for all \(m\) comes from the source theorem plus exact regular-polygon geometry.

## originality

PASS

Horváth–Lángi's full accessible article was inspected around the polygon characterization. Their theorem gives the structural \((k,l)\)-extension criterion for arbitrary convex polygons and identifies the extension as an illumination level curve, but it does not state the regular-polygon homothety ratios, area levels, or complete count of homothetic levels. Resultary search returns the audited spectrum and a separate equiangular-rigidity result; the latter concerns when homothety forces regularity, not the spectrum once regularity is assumed. No inspected primary or indexed result implies the explicit \(q\)-indexed spectrum.

## value

PASS

The source work explicitly motivates homothetic illumination bodies for polygons. For the fundamental regular family, the audited theorem completely resolves the discrete spectrum of possible homothetic illumination bodies, including exact ratios, area levels, onset, and count, and transfers the result affinely. This is a natural complete classification tied directly to the motivating structural problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
