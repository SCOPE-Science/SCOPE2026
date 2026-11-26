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

Independently verified the certificate with degree-set arithmetic and direct polynomial remainders of t^j r, not the supplied shift recurrence. P=f^3 divides t^28+1, so reduction is a surjective intertwiner, and the four independent quotient rows pull back to the four stated length-28 rows and preserve codimension four. All 22 least representatives, orbit lengths and first kernel witnesses matched; the size histogram is {1:1,7:1,14:4,28:16} and exhausts 512 states. Each quotient orbit hits K, so a shift of each original vector lies in the preimage U. The union bound for 28 shifts gives 2^c<=28<32, establishing sharpness.

## originality

PASS

Best-of-knowledge pass for the exact length-28 value and certificate. The direct binary table leaves a gap, and the strongest inspected nearby literature/indexed results do not give the missing lower bound. This is not a priority certification.

## value

PASS

Length 28 is an explicitly unresolved table entry of a standard covering invariant, not an arbitrary code slice. The equality resolves whether the counting upper bound is attainable at this length. A nine-dimensional orbit quotient gives a compact independently checkable witness for the full 28-dimensional covering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
