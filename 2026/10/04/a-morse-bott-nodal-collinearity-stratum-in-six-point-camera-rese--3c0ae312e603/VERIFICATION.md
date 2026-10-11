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

The relation space of the six world points has dimension two. For any collinear image sextuple, two independent relation vectors give two independent left-kernel vectors of the focal matrix, hence matrix rank at most \(16\); the determinant and all first derivatives therefore vanish. Fresh exact symbolic reconstruction at \(p_i=[1:i:0]\) reproduced focal-matrix rank \(16\), zero gradient, Hessian rank \(4\), an \(8\)-dimensional collinearity tangent space contained in the Hessian kernel, and normal minor determinant \(484\). Equality of tangent space and Hessian kernel plus the implicit-function/Morse-Bott argument gives the stated local node and generic-open persistence.

## originality

PASS

Best-of-knowledge originality passes. The primary resectioning paper supplies the focal generators and universal Gröbner-basis theorem under the no-four-coplanar hypothesis, but its full-text statement/proof inspected here contains no collinearity singular-stratum or Hessian/Morse-Bott local-type theorem. The Resultary search returned the assigned finding as the only exact match; nearby camera-singularity findings concern different varieties.

## value

PASS

The collinearity locus is an intrinsic, high-dimensional degeneracy in the minimal six-point resectioning hypersurface. Identifying its generic transverse node gives natural local geometry relevant to singularity analysis and conditioning, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
