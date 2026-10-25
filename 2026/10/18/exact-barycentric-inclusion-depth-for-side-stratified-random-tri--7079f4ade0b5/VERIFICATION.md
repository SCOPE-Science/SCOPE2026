---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Affine arclength fractions remain uniform on each side. Almost surely the three corner triangles and sampled central triangle partition the host. A corner has probability F(x,y)=1-x-y-xy log[(1-x)(1-y)/(xy)]; exact integration from x/(1-y) to 1 and summing three corners gives the stated Σt(1-t)log((1-t)/t). The sign and monotonicity of φ' show strict pairwise equalization (Schur concavity) even across t=1/2; centroid maximum 2log2/3, zero host boundary, fixed-direction vertex expansion εH(q)+O_q(ε²log(1/ε)), and spatial mean 1/4 follow analytically. Independent SymPy integral and three direct simulated inclusion rates with 100,000 trials each corroborate; finite checks are not the proof.

## originality

PASS

The exact fixed-point inclusion profile and strict Schur extremum are not covered by the full closely matched Maesumi area-distribution paper, nor by differently sampled circle/boundary results inspected. This is a best-of-knowledge, qualified conclusion; an unindexed elementary barycentric derivation remains possible.

## value

PASS

Pointwise probability of a random inscribed triangle covering a given point is a natural geometric depth invariant. The full shape-independent profile and strict maximizer extend far beyond the known average area and quantify sharp entropy boundary decay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
