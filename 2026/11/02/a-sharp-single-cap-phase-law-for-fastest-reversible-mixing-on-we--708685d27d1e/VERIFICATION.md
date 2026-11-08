---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For n≥3 strictly positive masses, edge prices, budget and one cap U, centered path coordinates give S_i(d)>0 and V(d)=Σ d_i S_i(d). The uncapped Rayleigh dual test x(sqrt(c)) yields λ0=B/V(q), w_i^0=λ0S_i(q)/q_i and threshold U0=w_k^0. Active cap U<U0 has exactly one positive root z>q_k of UA z²+(UD−CE)z−AE=0 with A=S_k(d^c),D=V(d^c),C=ML MR/Mtot,E=B−c_kU. Flux choices satisfy eigenvector and budget identities, and Sturm oscillation identifies λ2. The Rayleigh test at x(d(z)) bounds every unrestricted allocation, including the extra positive penalty (z²−c_k)w_k, proving optimality and uniqueness via equality in flux equations. Expanding the quadratic at U→0 gives λ*=U/C−A²U²/(C³B)+O(U³). Independent exact/numeric small-path reconstruction agrees, including the 4-vertex radical example; finite sampling is supplementary, not the universal proof.

## originality

PASS

Sun–Boyd–Xiao–Diaconis 2006 already give the uncapped uniform-mass priced-path optimum and a general reversible SDP; no novelty is attributed to them. This theorem introduces a single binding link upper cap, general positive masses/prices, explicit two-regime quadratic, uniqueness against all conductance allocations and bottleneck correction. No directly subsuming published theorem was located; specialist constrained spectral network design remains a residual risk.

## value

PASS

A single capacity-limited bridge in a reversible birth–death chain/consensus path is a natural physical and optimization constraint. Exact cap threshold, globally optimal all-edge conductances and the severe-bottleneck two-term response provide a reusable sharp benchmark, not an arbitrary low-dimensional numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
