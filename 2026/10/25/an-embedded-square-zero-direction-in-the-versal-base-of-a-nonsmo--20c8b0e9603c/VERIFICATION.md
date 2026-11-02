---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For Q with vertices (0,0),(-2,-1),(-3,-2),(-2,-3),(-1,-2), primitive cyclic edge vectors d0..d4 as displayed, Altmann miniversal Minkowski equations G_k=sum d_j t_j^k after translation apply to this isolated toric Gorenstein cone. Solving G1 gives t=(u,v,0,3u+v,-u). Independent symbolic expansion verifies G2=(8u^2+6uv,10u^2+6uv), generating ideal exactly (u^2,uv) in characteristic zero. For every k>=2 modulo that ideal, u^k=(-u)^k=0 and (v+3u)^k=v^k, so only d1v^k+d3v^k=0; hence all higher equations are redundant, not merely the checked degrees through 20. Completion gives C[[u,v]]/(u^2,uv). u is a nonzero square-zero element killed by maximal ideal (u,v), so its support is an embedded associated point while the generic reduced line is smooth. The result depends on Altmann’s isolated-versal theorem, not a direct global Calabi-Yau deformation computation.

## originality

PASS

Wuebben identifies this exact area-seven pentagon and the reduced one-dimensional versus two-dimensional tangent properties but does not state the completed scheme or its nilpotent support. Altmann already exhibits the abstract ring C[[u,v]]/(u^2,uv) for a different area-five pentagon; originality is limited to precise assignment to the explicitly motivated Wuebben singularity, not invention of this ring type or a new versality theorem. Best-of-knowledge PASS.

## value

PASS

A scheme-theoretic distinction left open by reduced-base and tangent-dimension data: the nilpotent is supported only at the special fiber, not along the entire deformation line. Computing the exact local miniversal base of a canonical recently studied nonsmoothable Calabi-Yau local model is a specific useful obstruction invariant despite being a short Altmann-algebra calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
