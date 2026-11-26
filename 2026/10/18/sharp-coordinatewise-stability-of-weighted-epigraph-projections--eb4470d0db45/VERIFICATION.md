---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For output height θ≥0, the spatial minimizers are coordinate clips, and the remaining scalar objective is strictly convex. On a strict clipped support S the active height-spatial derivative block is the rank-one orthogonal projector in direction (1,(σ_i a_i)_{i∈S}); the unclipped block is identity. The specified input at θ=1 realizes every S in an open chart, so segment integration and small row-sign perturbations give equality in the global formula. At an optimal subset for R, every unforced included a is ≤1/R and every excluded a is ≥1/R, by deletion and insertion, respectively. Ties can be ordered as a prefix. This proves the candidate count both with no forced coordinate and with one forced. Singletons give strict expansion at any non-unit reciprocal weight. For k active coordinates, a rank-one orthogonal projector in dimension k+1 has maximum row sum bounded by (1+√(k+1))/2: writing q for its diagonal entry, Cauchy–Schwarz bounds the row by q+√(kq(1−q)). Equality at the ambient ceiling forces full support and a distinguished coordinate larger in magnitude than every other coordinate by √(n+1)+1, the other magnitudes being equal. Normalizing the height coordinate gives exactly the n+1 listed positive designs; strict chart realization attains the bound. For the positive dual at unit weights, the active block is the complementary hyperplane projector with row sum 2k/(k+1); full support is feasible and gives the claimed constant. The negative polar has the same modulus by reflection. The frozen script was inspected, not executed.

## originality

PASS

Pass for the exact unconstrained design maximum for the weighted maximum-norm epigraph together with the exhaustive classification of its attaining weight vectors. Credit the earlier projection and derivative theory; the exact subset modulus is also a direct Moreau-complement consequence of the matching indexed weighted ℓ1 chart matrices, and the unweighted dual comparison is already covered. The generic matrix ceiling, taken alone, is not a distinct result. None of the inspected sources optimizes across reciprocal-weight designs for the maximum-norm epigraph or identifies which weights realize the ceiling; that requires the full-support and equality optimization, not just a numeric ceiling or duality of the cones. The unresolved complete-text comparison with Liu et al. limits this judgment. No priority conclusion is made from catalogue dates.

## value

PASS

The coordinatewise perturbation question is natural because Euclidean nonexpansivity does not control the largest coordinate error sharply. Beyond the generic ceiling, the design theorem says whether it is realized by this specific family and gives every calibrating weight vector that realizes it, distinguishing height and spatial failure modes. These exact equality cases are useful for choosing or ruling out worst-case anisotropic calibrations. The covered polar example is not counted separately.

The dated certificate retains the supplied scientific assessment, sources and limitations.
