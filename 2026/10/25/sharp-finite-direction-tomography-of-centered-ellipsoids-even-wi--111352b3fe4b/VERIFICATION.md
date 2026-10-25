---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification
The result is proved for every integer \(n\ge2\) by affine coarea, matrix polarization and a deterministic indefinite-kernel construction. The exact formula is valid at all real offsets by taking the positive part; strict monotonicity at the noncentral sample holds under \(Q\succ nt^2I\). The determinant crossing argument needs no genericity assumption on the normals, because an indefinite kernel matrix exists even when the normals do not span the ambient space.

Run `python verify.py` with SymPy installed to reproduce three symbolic consistency checks: (i) six exact central observations reconstruct a rational positive definite \(3\times3\) matrix; (ii) the matrices \(Q(z)=I+z\bigl(\begin{smallmatrix}0&1\\1&-2\end{smallmatrix}\bigr)\) at \(z=-1\pm\sqrt6/2\) have the same determinant \(1/2\) and quadratic samples in normals \(e_1\) and \((e_1+e_2)/\sqrt2\); (iii) the noncentral-response derivative identity. These are finite illustrations only, not exhaustive verification of all dimensions or of literature priority.

The validity of the central inversion rests on \(\det(Q/\det Q)=(\det Q)^{1-n}\), which requires \(n\ge2\). Sections at a single noncentral height can have nonmonotone dependence on directional support radius outside the stated thick class; no general one-height injectivity is claimed there.
