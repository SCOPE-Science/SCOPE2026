---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The distance algebra gives PA=A_2 and A²=5I+2A+2A_2. On the even antipodal subspace the adjacency is that of K_6 (each vertex has one neighbour in each other antipodal pair); on the odd subspace A²=5I, with equal multiplicities by the trace. The weights at a vertex are therefore 1/12, 5/12, 1/4 and 1/4 by transitivity, with the last two phases reversed at the antipode. The weighted phase-variance identity yields both stated pair bounds. For infidelity ε≤1/256 they force √5x within π√ε of πn and x within πL√ε/2 of πp with opposite parity (L=π+√(48/5), x=Jt). Hence |√5p−n|<9√ε and 0<√5p+n≤2(1+x); the nonzero integer norm gives ε≥1/[324(1+x)²], with the larger-ε range automatic. This excludes all finite PST, and the bound transfers to a maximum on the compact time interval. At x=πp_k, the alternating norms ±1 and opposite parity reduce the fidelity to cos⁴(π/[2(n_k+√5p_k)]). Since p_1=1 and p_{k+1}=n_k+2p_k<5p_k, for every horizon X=JT≥π the last admissible Pell time has p_k>X/(5π). Its infidelity is at most π²/(10p_k²), giving the stated upper bound. Taylor expansion and n_k/p_k→√5 give π⁴/40 on that subsequence only. All six pairs are conjugate by symmetry. The packaged checker and finite output were inspected, not executed; neither finite matrix exponentials nor sampled times prove the all-time inequality.

## originality

PASS

The distinct contribution is the two-sided finite-horizon waiting-time theorem for the ordinary icosahedral adjacency, especially the obstruction that holds for every real readout time. The indexed five-Platonic-graph result has exact overlap on the qualitative behavior and the Pell fidelity formula, and mathematically implies the subsequence constant and the quadratic witness-side scale. Those are not independent originality grounds. Its indexed date is later than the frozen path date; no ordering inference is needed to credit that overlap. The closest exact and quantitative sources did not supply a horizon-uniform lower bound or two-sided law for this Hamiltonian.

## value

PASS

For a natural symmetric unweighted graph, near-perfect transfer existing is weaker than a schedule guaranteeing it by a deadline. The lower bound rules out improving the exponent by choosing arbitrary continuous times, while the upper provides explicit admissible schedules. Together they establish that the time budget needed for small infidelity scales like J^−1 times the inverse square root of the tolerance, without asserting an optimal constant or optimal individual witness times.

The dated certificate retains the supplied scientific assessment, sources and limitations.
