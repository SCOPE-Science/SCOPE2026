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

The defect is bilinear, and choosing all four matrix-unit images independently enumerates every one of the 16^4 linear maps exactly once. I independently ran python3 /workspace/branches/record5_replay.py, which builds the product table from contracted matrix coordinates, checks the 16 basis pairs for every map at each weight and all 256 pairs for every accept, and uses incremental GF(2) elimination on matrix powers to find the first monic relation. It returned totals 28 and 110, degree distributions (1,21,6) and (2,84,24), and extremal polynomial masks 8 (six) and 10,12 (twelve each), i.e. X³, X³+X, X³+X². The replay independently constructs inner conjugations from inverse pairs of invertible matrices; Skolem–Noether applies to the central simple algebra M_2(F_2), and the scalar center of GL_2(F_2) is trivial, yielding all six. Transpose normalizes the conjugation action and R→R+id commutes with both actions; substituting the identity verifies it preserves the weight-one condition. Taking the direct orbit images gave sizes (3,3)→(6) at weight zero and (6,6,6,6)→(12,12)→(24) at weight one; these partitions verify the stated exchanges. Both prescribed canonical reductions were in the independently determined extremal sets. Only the independent program was executed. In the frozen documentation VERIFY_OK is said to be at the end, whereas the packaged output begins with it; all numerical lines agree and this does not affect the result.

## originality

PASS

The distinct supported result is the full finite-field census at the two weights and the refined rational extremal orbit partitions, including the degree bound achieved in characteristic two. Known integral canonical examples and the analogous characteristic-zero equivalence are not new. The broader rank-one result overlaps one subset of the weight-zero maps but neither determines the total nor reaches an extremal. No inspected source determines the whole result; this is a best-of-knowledge assessment.

## value

PASS

The smallest field excluded by the related characteristic hypotheses is a natural boundary for the stated rigidity question, not a randomly selected finite sample. The exhaustive result resolves that boundary for both possible weights and establishes the necessity of the individual symmetry generators in the finite-field setting: conjugation is not transitive, transpose alone still fails at weight one, and adding φ resolves the split. These precise counts and degree/orbit distributions give a useful reference and test case for attempts to extend the rigidity theorem to positive characteristic. No extension to other fields or sizes is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
