---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

An independent reconstruction from E and L reproduced 105x238 H_X,H_Z, row weight 8, exact CSS orthogonality, ranks 97/97 and k=44. Rebuilding the explicit support gave weight 6, zero H_Z syndrome, nonzero remainder modulo rowspace(H_X), and rank augmentation 97->98. Independent enumeration of the 16-dimensional kernel of the 21x35 base matrix gave minimum weight 6 with 21 such codewords. Exhaustive neighbourhood checks gave zero expansion failures at sizes 1,2,3 and exactly 84 at size 4. These facts directly falsify d>=9; no claim of exact quantum distance is needed.

## originality

PASS

Best-of-knowledge searches found the 2025 finite-length lifted-product distance/RCPC framework but no prior source giving this exact 3x5 lift-7 array instance, its ranks, expansion-failure count, or weight-6 logical support.

## value

PASS

A concrete low-weight logical operator in a structured QC lifted-product code is a useful finite-length design obstruction: it invalidates a hoped-for distance-above-stabilizer certificate on a natural type-I protograph instance and pinpoints the associated local expansion failure. This is more than a normalization check and can guide selection of exponent arrays in the finite-length LP-QLDPC program.

The dated certificate retains the supplied scientific assessment, sources and limitations.
