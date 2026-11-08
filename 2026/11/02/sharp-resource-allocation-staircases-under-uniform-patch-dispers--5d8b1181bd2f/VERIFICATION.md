---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For P_{ii}=1-theta and P_{ij}=theta/(n-1), D=diag(c_i h_i), PD and S=D^{1/2}PD^{1/2} have the same characteristic polynomial. S=aD+beta vv^T with a=1-n theta/(n-1). For theta<theta_c=(n-1)/n PSD trace bound forces single best patch, and at equality S has rank one and permits every allocation on tied maximal efficiencies. When theta>theta_c, the unique positive Perron eigenvalue obeys F_h(lambda)=beta sum_i c_i h_i/(lambda+s c_i h_i)=1. For each lambda>0 F_h is strictly concave on the budget simplex; its KKT unique maximizer has square-root truncated form. Solving sum_i(1-z/sqrt(c_i))_+=delta=n-(n-1)/theta yields the unique global h and exact monotone activation thresholds; zero-root allocations at theta=1 cannot beat a positive candidate. Exact four-patch c=(16,9,4,1), theta=1: h/B=(21,20,6,0)/47 and rho/B=96/47. Distinctions between spectral radius and nonlinear persistence are explicit.

## originality

PASS

Closest Delmas–Dronnier–Zitt 2023 Theorem 4.2 solves rank-one homogeneous mixing with a capped/unweighted mass constraint, and yields horizontal allocation for disassortative kernels. Our uncapped heterogeneous cost sum_i x_i/c_i=B after x_i=c_i h_i has a different feasible geometry, changing the optimal shape to square-root cutoff. Kirkland et al optimize dispersal with fixed fecundities; Haight–Travis target stochastic habitat survival. Generic secular equations, matrix inertia and KKT are prior methods, not claimed novel. Possible broader weighted matrix-allocation theorem remains a priority risk.

## value

PASS

The qualitative switch from concentration to diversification, exactly ordered site-entry thresholds, and permanently uninvested low-efficiency sites answer a natural heterogeneous budget-planning question across every patch count. The sharp support phase diagram, not merely a routine numerical maximizer, is useful even in this deliberately simplified linear system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
