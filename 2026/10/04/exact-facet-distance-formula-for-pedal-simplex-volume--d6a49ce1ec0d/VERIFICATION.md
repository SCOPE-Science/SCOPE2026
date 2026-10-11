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

The barycentric gradients give sum_i S_i u_i=0 and identify the unique cofactor vector of the normal matrix. Expanding the augmented determinant of the translated projected feet yields a homogeneous degree-n polynomial in signed distances with cofactors proportional to S_i. The determinant of the remaining barycentric gradients fixes the proportionality constant exactly, producing the displayed volume factor. At A_k, the n other signed distances are independent affine coordinates, d_k is a nonzero altitude, and the first nonzero homogeneous part has degree n-1 with positive nonzero coefficients, proving exact multiplicity. The deterministic verifier independently checks dimensions 2 through 6 and the planar Euler specialization.

## originality

PASS

Grace's primary 1927 extract explicitly records the tetrahedral coplanarity locus as a cubic surface with nodes at the vertices, so that qualitative n=3 fact is prior. Yang's full open 2004 paper treats pedal simplices through inequalities, not the exact signed facet-distance determinant identity. Resultary found the audited all-dimensional formula as the direct exact match.

## value

PASS

The formula unifies the classical Simson/circumcircle and tetrahedral pedal-surface degeneracies with an exact all-dimensional normalization and singularity multiplicity. That is a natural geometric structural identity rather than a numerical exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
