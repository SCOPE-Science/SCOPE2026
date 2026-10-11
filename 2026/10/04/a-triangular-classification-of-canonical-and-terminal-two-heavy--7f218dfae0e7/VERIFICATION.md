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

The unit-weight charts are smooth and the two heavy charts are cyclic quotients \(1/a(1^r,b)\) and \(1/b(1^r,a)\). For the \(b\)-chart, the age numerator \(rk+[-kd]_b\) is controlled exactly by \(d\le r\) (strictly \(d<r\)); for the \(a\)-chart, \(rk+[kd]_a\) is controlled exactly by \(a\le r+d\) (strictly \(a<r+d\)), with the equal-heavy case handled separately. These arguments cover every nontrivial group element. Summing the resulting triangular parameter region gives the stated exact counts. Independent direct age checks over a broad finite box agreed with the symbolic classification but are not used for the infinite proof.

## originality

PASS

The strongest inspected prior source gives general fractional-part criteria and finite-dimensional classifications. It does not state the all-dimensional two-heavy triangular region or the exact count formulas. The audited proof materially specializes and collapses the full Reid–Tai family of inequalities rather than merely renaming a known classification.

## value

PASS

The two-heavy family is a natural infinite slice of weighted projective spaces. Replacing many Reid–Tai/fractional-part checks by two sharp inequalities gives a complete all-dimensional classification, exact enumeration, and the full canonical/non-terminal boundary; this is a useful structural benchmark for broader algorithms and downstream invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
