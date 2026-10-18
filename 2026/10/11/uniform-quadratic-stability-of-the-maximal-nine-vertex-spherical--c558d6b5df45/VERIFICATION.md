---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Strict oriented-facet inequalities (84 tests across 14 triangles) guarantee a stable combinatorial chamber with exact cubic determinant volume. In tangent orthonormal bases the constrained 18x18 Hessian has off-diagonal ambient determinant derivatives and diagonal sphere-curvature corrections -lambda_i, with no same-vertex ambient second derivatives. Exact rotational invariance plus stationarity at the globally proved maximizer makes H W=0. The source certificate constructs the projector P=W diag(1/g,1/g,1/k) W^T with exact g=15/2-3r²,k=3+6r², encloses sqrt(3) and h=sqrt(2sqrt(3)-3) by integer outward intervals, then interval LDL^T proves every pivot of -H+P-(39/100)I positive (minimum lower endpoint >0.05575). The source code was inspected at exact frozen blob SHA; its near-zero numeric gradient is used as a sanity check only, not a substitute for published global stationarity. Independently rebuilt all 9 points, 14 facets, tangent frames, signed volume determinant and 18x18 Hessian: 3h=2.043750115899639, gradients <7e-17 in tangent coordinates, three eigenvalues numerically zero, first transverse gap ~0.39549>0.39, and rotation residual ~8.2e-16. Rigorous positivity is established by the rational interval proof, not this double-precision spectrum. Tubular coordinates normal to compact rotation orbit and uniform Taylor remainder imply the conservative 1/10 chord-distance deficit for some delta>0.

## originality

PASS

The same-object Hoehner-Ledford 2026 original global theorem proves the unique volume-maximizing nine-point shape and exact 3 sqrt(2sqrt(3)-3) volume; full manuscript sections 1,3,4 were inspected. Its Hessian test applies to an auxiliary concavity function of two angular parameters, not the full 18-dimensional constrained configuration volume Hessian. Global uniqueness alone does not imply nondegenerate Hessian or quadratic stability: a unique maximum could be quartically flat. Dedicated Resultary searches for the triaugmented prism, full transverse Hessian and stability yielded the target and unrelated Hessian results for different polytopes. The new complete transverse matrix certificate and local quadratic inequality therefore survive as best-of-knowledge additions; exact gap optimality or global stability is not claimed.

## value

PASS

A just-resolved canonical nine-vertex spherical volume maximizer now has a quantified, all-nonrotational-direction second-variation theorem. Identifying the exact symmetry kernel and a certified positive spectral margin supplies genuine local rigidity beyond a uniqueness statement, with meaningful geometric perturbation control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
