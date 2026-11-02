---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For Sigma_d={x:||x||_1+||x||_infty<=1}, the exact support maximization over signed k-support vertices is H=max_{1<=k<=d} S_k/(k+1). Equivalently, F_d(H)=sum_i(|G_i|-H)_+-H=0, and the exposed support rank is N_d(H). The half-normal excess integrals yield t_d^2=2 log d-3 log log d-log(4 pi)+o(1), d p(t_d)/t_d^2->1, d E(Y-t_d)_+^2->2, and d E(Y-t_d)_+^2=d p(t_d)-t_d^2. A triangular-array CLT for the centered excess sum B and count A gives covariance [[2,1],[1,1]]; uniform local tail counts show t_d^2(H-t_d)=B+o_P(1), (K-t_d^2)/t_d=A-B+o_P(1), giving joint covariance [[2,-1],[-1,1]]. Radial G/||G|| normalization is o_P(1) on that scale; UI of H/t_d gives mean width equivalent. Reconstructed boundary d>=2 and asymptotic only; independent quadrature checked exact moment identity at d=1000,10000,100000. Finite checks do not prove asymptotic convergence.

## originality

PASS

Qualified PASS for the joint Euclidean random width/exposed support-rank fluctuation theorem and its negative covariance, not the signed-support vertex enumeration or deterministic mixed-norm support formula. Explicitly compared Gaussian threshold aliases and stronger geometry; primary Black–De Loera 2021 proves the vertex realization but not the joint stochastic asymptotic in the examined sections. A previous canonical-signohedron radial-shell finding fixes vertex radii, not their normal-cone probabilities. Could be independently implicit in classical Gaussian trimmed-order-statistic/empirical-threshold theory; that bibliographic risk remains.

## value

PASS

The exact metric law answers a natural question not addressed by the 3^d-1 combinatorial vertex count: a Haar support direction typically exposes only about 2 log d coordinates, with a nontrivial covariance between width and face support rank. Its explicit centering and negative correlation are plausible future benchmarks for random optimization on mixed-norm polars; more than a normalization check or face-count recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
