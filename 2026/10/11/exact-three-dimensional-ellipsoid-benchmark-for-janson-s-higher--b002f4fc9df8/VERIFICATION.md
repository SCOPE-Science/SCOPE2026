---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For p=2, n=3 and (j0,j1,j2)=(1,1,1), six-dimensional mixed volume equals 4^6/6! times a six-vector determinant expectation. Multilinear determinant is exactly a scalar triple product of pairwise cross products, exhaustively checked on 3^6=729 basis tuples. Uniform spherical cross magnitudes give (pi/4)^3, angular sine another pi/4, and absolute cosine 1/2, yielding pi^4/90 for the unit ball. Block-diagonal affine scaling by T direct-sum T yields W=(pi^2/160)|E|^2 for every full ellipsoid. Universal Janson bound 3/10 leads to ratio pi^2/48. No sampling is used to establish the angular integrals.

## originality

PASS

Fryš–Kotrbatý 2026 identifies W_{2,K}(1,1,1), gives Janson upper bound and general special-case inequalities; no exact ball/ellipsoid coefficient appears in inspected pages 1-13, but the remaining pages were not all read and are a residual risk. The newer Fryš–Kotrbatý–Mouamine–Wang arXiv:2610.06806v2 proves the higher-order inequality and simplex-only equality, not a numerical ellipsoid mixed-volume evaluation. Breiding–Bürgisser–Lerario–Mathis zonoid-algebra formula supplies a general determinant representation, not the special block expectation.

## value

PASS

The ellipsoid class is the canonical affine comparison for mixed-volume extremal coefficients, and (1,1,1) is the sole nontrivial dimension-three higher-order index. The exact normalized value remains a useful calibration now that the general inequality and simplex equality have been proved; the record’s obsolete 2026 claim of an unresolved equality problem must not be disseminated unchanged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
