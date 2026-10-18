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

For any positive-area measurable X, closed convexification preserves minimal width and can only increase area. Bounding rectangle in a minimizing width direction gives A(X)<=ω(X)D(Ω). A diameter chord pq and off-chord interior point r provide a triangular section of length D(1−s/h), so 0<t<h slices satisfy ω(X_t)/A(X_t)<=1/[D(1−t/2h)] ->1/D. Equality would force a positive-width D-by-ω rectangle within Ω, whose diagonal exceeds D(Ω), contradiction. Noncompact X is handled by closed hull.

## originality

PASS

Cañete explicitly proposes the replacement-functional Cheeger question with minimal width in Remark 11; Ftouhi–Masiello–Paoli keep the perimeter-based Cheeger constant, and their width inequalities do not optimize ω(X)/area over subsets. No equivalent reciprocal-diameter all-Ω result identified in targeted or published SCOPE search; older geometry formula remains possible.

## value

PASS

An exact universal solution to an explicitly proposed natural Cheeger-type functional, including nonattainment and a geometric minimizing construction; distinguishes degeneration from the ordinary perimeter Cheeger problem and is not an arbitrary test shape.

The dated certificate retains the supplied scientific assessment, sources and limitations.
