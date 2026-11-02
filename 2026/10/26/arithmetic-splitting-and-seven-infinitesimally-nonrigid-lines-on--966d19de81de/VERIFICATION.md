---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The quartic is exactly the one in Veniani Example 5.4. An independent finite-field implementation enumerated all 9^4+9^3+2·9^2+9+1=7462 RREF 2-subspaces of F9^4, tested all five coefficients of the quartic restriction and obtained exactly 48 distinct F9 lines; pivot charts contain 33,11,0,2,1,1 candidates. Veniani independently establishes there are exactly 48 *geometric* lines, so the F9 list exhausts algebraic closure. Frobenius (x→x^3) partitions these 48 as 6 fixed +21 pairs. On each RREF Grassmannian chart, independent dual-number differentiation of all five restricted quartic equations gives tangent dimension 1 at exactly seven supports (one fixed + three pairs) and 0 at 41. Since geometric support is finite, tangent≠0 implies nonreduced local Artin ring, whereas tangent0 implies residue field by Nakayama; reduced part is finite étale over perfect F3. This yields N_n=6 (odd),48 (even) and zeta (1-T)^(-6)(1-T^2)^(-21). The local *lengths* of the seven thickened points are not determined.

## originality

PASS

Veniani's actual Example 5.4 supplies exact singular model and geometric 48-line count and the eight A1 nodes; both are credited as prior. The inspected source does not determine the F3/F9 Frobenius orbit profile or which line-scheme supports are infinitesimally nonrigid. This is a new arithmetic and infinitesimal classification of the original model to best knowledge; there may be other algebraic-geometry computation sources giving equivalent or stronger scheme data.

## value

PASS

Fields of definition and nonreduced tangent support are natural arithmetic and scheme-theoretic invariants of an extremal line-rich singular quartic; they cannot be recovered just from the known 48 geometric lines. The seven marked nonreduced supports identify a genuine infinitesimal deformation phenomenon, while the exact reduced zeta counts all finite extensions. The result is a complete natural classification at the support/tangent level, not a restatement of a known line count or arbitrary coordinate slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
