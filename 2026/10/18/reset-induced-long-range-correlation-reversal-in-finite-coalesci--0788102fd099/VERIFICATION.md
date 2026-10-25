---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: Global rate-r resets yield the finite-state resolvent r∫exp(-rt)P_t(full,.)dt and a unique stationary law. As r↓0, coalescence on a finite connected ring reaches one surviving symmetric walker, so the Abel-limit covariance of distinct occupancy sites is -1/N². For nonadjacent vacancies i,j, a single jump gives 2t+O(t²) per vacancy and precisely eight ordered two-event histories produce both vacancies, yielding joint vacancy probability 4t²+O(t³); exponential age mixing gives E(V_i V_j)=8/r²+O(r^-3) and Cov=4/r²+O(r^-3)>0 for large r. At N=4, independently assembled all 15 nonempty-state generator transitions and solved the exact stationary system symbolically without using the package code; the displayed near/opposite rational functions and unique positive opposite-covariance root 0.530754559719 agree exactly. Positive-root uniqueness follows from polynomial derivative positive for r>0; N>=4 universal only guarantees existence of a nonadjacent sign crossing, not its uniqueness.

## originality

PASS

PASS best-of-knowledge: Durang–Henkel–Park analyze reset coagulation density, contiguous empty intervals and interparticle distributions primarily for an infinite one-dimensional system; they do not state finite C_N nonadjacent occupancy covariance crossover or the exact N=4 rational near-versus-opposite threshold. The unreset two-time correlation paper changes dynamics, and general quantum reset correlation results change model entirely. Historical finite-ring multi-interval literature may still cover an implied identity; risk explicitly recorded.

## value

PASS

PASS: Coalescence produces local occupancy anticorrelation while shared reset age creates a far-pair positive covariance at high reset rates. The all-finite-ring sign-reversal theorem and explicit smallest-cycle coexistence of negative nearest-neighbor and positive opposite-site correlation are structural and experimentally checkable benchmarks, not arbitrary low-dimension numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
