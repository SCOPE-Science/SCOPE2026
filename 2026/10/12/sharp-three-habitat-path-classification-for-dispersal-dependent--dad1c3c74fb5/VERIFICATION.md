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

Pinned theorem treats 3-vertex path L=[[1,-1,0],[-1,2,-1],[0,-1,1]], h>m>ell>0, linear H_r=diag(r)-dL for every finite d>0; Perron max eigenvalue is simple, decreases strictly with d, lies strictly between the mean and h. Independently expanded tridiagonal F_{a,b,c}=det(zI-H) and verified F_{a,b,c}-F_{a,c,b}=d(z-a)(b-c) and F_{a,b,c}(a)=d[(a-b)(a-c)+d(2a-b-c)]. A tie between reflected placements requires eigenvalue equal the shared endpoint rate. Small-d first/second perturbations select medium-center as unique optimum; absence of admissible Perron ties proves its global superiority. The two nonoptimal layouts with common m endpoint meet only if 2m>h+ell and then at exact d*=(h-m)(m-ell)/(2m-h-ell), common principal eigenvalue m and opposite derivative signs; when 2m<=h+ell they never meet. Transversality verified by nonzero derivative of common characteristic determinant; n=1,2 or triangle permutation symmetry rules out smaller reversal. Independent exact characteristic calculation and spectral numerics for (h,m,ell)=(6,5,1) verified d*=4/3, and opposite orders d=1 vs 2. The parameter-uniform proof is analytic.

## originality

PASS

The primary ecological competition literature models diffusion, growth and asymptotic fitness, but the inspected Gourley–Kuang (2005) full paper builds a nonlinear two-species, primarily two-patch model and does not classify permutations of three rates on an unweighted path. General graph principal-eigenvalue rearrangement literature could conceivably dominate special placement comparisons; no directly implying published theorem emerged from targeted searches, a stated residual risk.

## value

PASS

Exactly classifying the three distinct-rate placements of a canonical minimal connected habitat path explains a sharply located dispersal-driven ranking reversal and rules out any smaller connected unweighted network. The crossing layouts are globally nonoptimal without further constraints, but under realistic fixed-endpoint placement they become the two relevant choices; this motivation is explicit and mathematically substantive despite the three-vertex setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
