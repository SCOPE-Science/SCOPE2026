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

Detailed balance for D_x↔S_xy uses rates 2a and a+1; separated moves have rate a both ways. The resulting collision probability is (a+1)/(na+1), yielding the displayed variance. The centered reversible Poisson formula gives the covariance integral and the 2T normalization. With z=ah and one double-state coordinate pinned, the Dirichlet conductances on double-to-edge transitions diverge like 2/(na), and separated conductances converge to 2/n. The pinned energy is uniformly coercive because the entire configuration graph is connected and its conductances are uniformly bounded below for 0<a≤1. Bounded maximizers collapse to zero on the connected double-and-edge subgraph. Dropping the nonnegative fast-edge energy gives the upper limit along any convergent subsequence; the zero extension of an arbitrary nonedge test vector gives the lower bound. The linear term there tends to −(2/n)1ᵀz and the energy is (2/n)zᵀ(−K_G)z. Holding one walker fixed along a finite path of possible moves of the other proves accessibility of killing from each nonedge, so the finite killed operator is invertible and its inverse on 1 gives the strictly positive mean killing times. For example, P_3 has one nonedge with killing rate 2 and coefficient 1/3. For complete graphs the two-state relaxation rate is 2(na+1). On cycles the proposed hitting-time quadratic solves the interior second-difference equation and both endpoint equations, including n=3; the centered Poisson solution obeys u(r)−u(0)=−ρ_0 t_r by stopping at collision. Summing gives the stated rational covariance. Direct differentiation gives the displayed polynomial; its constant term is positive for n≥4 and at n=3 the sole positive derivative zero gives the claimed maximum. The analytical proof does not rely on rerunning the frozen finite checks.

## originality

PASS

The killed nonedge walk is already used in finite-graph SIP spectral-gap work and is not new here. The distinct result is the collision observable's exact Green quadratic form and its consequences, including the exact finite cycle response. The examined stronger-looking work gives a different observable, operator statistic, setting, or process; none of the examined claims determines this formula as a corollary.

## value

PASS

Collision time is a basic stationary observable for two attracting particles. Its instantaneous variance vanishes on every graph, so the separation between a positive long-time noise limit on noncomplete graphs and a vanishing one on complete graphs cannot be read from statics. The exact coefficient identifies how each nonedge contributes and distinguishes observable persistence from spectral-gap control. The cycle formula makes that distinction quantitative and locates the triangle exception.

The dated certificate retains the supplied scientific assessment, sources and limitations.
