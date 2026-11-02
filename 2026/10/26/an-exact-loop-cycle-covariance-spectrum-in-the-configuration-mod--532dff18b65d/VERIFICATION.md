---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For each specified stub cycle, probability is 1/P_r(Q). It uses exactly two stubs at each participating vertex; therefore allowable leftover loop pairs decrease by sum_gamma(2d_v-3). Conditional residual matching gives E[LC_r]=(AB_r-S_r)/P_{r+1}(Q) when Q>=2r+2; E[L]=A/(Q-1), E[C_r]=B_r/P_r(Q). Subtraction gives displayed cov (2r A B_r/(Q-1)-S_r)/P_{r+1}. When Q=2r, the cycle exhausts all stubs, making mixed moment zero. Counting undirected vertex cycles (n)_r/(2r) and substituting regular degree d yields sign factor nd(2-d)+2d-3; fixed-r asymptotic coefficients follow dominant powers. Independent pairing enumeration by actual labeled half-edge matchings checked small graphs exactly. The model is not the uniform simple graph and r>=3 is essential.

## originality

PASS

The simple regular graph short-cycle results cannot determine covariances with loops, because loops are forbidden. The inspected configuration multigraph literature treats loops and double edges and their Poisson asymptotics, not the exact all-length r>=3 covariance and spanning exception. A prior r=2 pairing covariance is acknowledged. Thus the exact mixed-moment spectrum is not inferred from those results without the cycle-specific pair count.

## value

PASS

Finite-size dependence between loop defects and cycles is intrinsic to configuration models. The exact arbitrary-degree law gives a useful sign test, the d=2 versus d>=3 transition and spanning exception, not recoverable from limiting independent Poisson marginals alone; it is a natural complete mixed-moment classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
