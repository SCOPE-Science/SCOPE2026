---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The local variation equals |y_i-y_{i-1}|+2dist(m_i,[ell_i,u_i]); compact convex LP duality gives max_{p_i in [-1,1]} sum_i[p_i a_i-u_i p_i^+ +ell_i p_i^-]-lambda d sum_i|p_{i+1}-p_i|. For each real p coordinate, ternary threshold layers over h in (0,1) satisfy exact coarea |p_i-p_{i+1}|=int |s_i(h)-s_{i+1}(h)|dh, so max attained on ternary labels and solved by 3 fixed starting labels with 3-state cyclic DP in O(n). The constant labels force total average A in [L,U] for zero extra variation. For nonconstant ternary labels, splitting positive and negative indicator runs into proper cyclic intervals gives exactly two cut edges per interval; maximizing interval deficits yields d_*=max(0,max_I sum_I(ell_i-a_i),max_I sum_I(a_i-u_i))/(2lambda). The arbitrary-budget formula follows by taking maximum of (R_s-t)_+/(lambda C_s) among labels with nonzero boundary; unbounded fluxes realize all corrected mean vectors with total A, giving dist(A,[L,U]). A new independent checker compared the ternary dual with a primal LP in 110 deterministic bounded cases n=2..6. These numerical checks support, not prove, the universal coarea/minimax theorem.

## originality

PASS

PASS (qualified): Barsukow 2026 defines precisely this Active Flux variation and proves Harten-type sufficient TVD conditions for physically parametrized flux updates; its PDF does not present the same unconstrained signed-correction minimization, global necessary-and-sufficient cap or three-state cyclic exact value formula in the inspected sections. Lu–Hochbaum 2021/2022 solve general one-dimensional convex fidelity/difference-penalty denoising but have a path and approximation-oriented methods, not the explicit endpoint-conditioned Active Flux feasibility identity. Classical LP duality, graph cuts and coarea supply essential prior ingredients, explicitly credited. Whether a generic graph-cut theorem has previously stated this specific 3-label interval-distance dual as a corollary remains a priority risk.

## value

PASS

PASS: The least globally reachable variation subject to a conservative uniform flux cap is a natural feasibility quantity for frozen scalar Active Flux endpoint data. Its exact linear-time characterization and the sharp proper-cyclic-interval obstruction (which can exceed every local cell obstruction linearly in n) are substantive precise results, while explicit scope disclaims physical flux realizability and multistep TVD.

The dated certificate retains the supplied scientific assessment, sources and limitations.
