---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. For the unit-rate continuous-time walk on depth-two regular T_{b,k}, b,k≥2, unique tree-edge flows give exact W1=ell1 edge norm; e^{-tBB^T}B=B e^{-tB^TB} reduces the operator norm to maximal abs edge-column sum. The edge Laplacian splits into b(k−1) contrasts eigenvalue 1 and two symmetric 2×2 blocks S,G. Counting branch/orbit entries gives the stated I_{b,k},O_{b,k} all-time formulas exactly. Along b=k=N, entrywise Metzler comparison implies 0≤G≤S; spectral slow/fast mode yields I≤4−10/N+O(N^-2); at t=3log N/N, I meets this to O(log N/N²). Uniform O≤3+2/sqrt N excludes domination at large N. Strictly positive finite-chain transition kernels prevent attaining diameter four. Independent complete edge matrix exponentials agreed with block formulas to <2e-14 for four parameter triples; finite test is supplemental.

## originality

PASS

PASS best-of-knowledge. Standard Ollivier coarse Ricci and Münch–Wojciechowski heat Lipschitz contraction theory provides abstract framework. The inspected sources do not present the exact two-orbit 2×2 expression or 4−10/N extremal asymptotic for two-level homogeneous trees; related one-level stars and complete bipartite graphs have different geometry. Some relevant Cheng–Li–Wu detailed full text was not obtained, leaving a historical risk.

## value

PASS

PASS. A natural finite diffusion family has an explicit exact all-time transport operator norm with computation independent of growing vertex dimension; its peak approaches the sharp diameter-four bound on a vanishing timescale, with a nontrivial exact 10/N deficit. This is a meaningful structural and asymptotic benchmark beyond generic curvature estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
