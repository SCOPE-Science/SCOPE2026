---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The common-edge-label root decomposition T_n(p)=1+sum_i 1[U_i<p] T_{n,i}(U_i) yields E T=e^{np} and an exact second-moment ODE, solved as f=(2-2/n)e^{2np}+(2p-1+2/n)e^{np}. For p<=q, the additional root-label bins are disjoint, so Cov(T(p),T(q))=Var T(p)-(e^{np}-1)(e^{nq}-e^{np})/n. Factoring gives the one-zero bracket n-1+2np/(e^{np}-1)-e^{n(q-p)}, establishing q_*, sign classification, (log n)/n crossover and correlation limits. With fixed distinct p_j, disjoint-bin Laplace transform (1-sum a_{n,j})^n and the published one-threshold Exp(1) limit yield independent limiting exponentials; the ignored smaller-bin contribution vanishes in L1. Independent evaluation n=2,p=.4 gives q*=.817658752284986 and negative covariance at q=.9. This is an analytic proof; packaged finite-depth simulations are not used as infinite certification.

## originality

PASS

The exact same n-ary temporal-tree one-threshold distribution was published in 2025; its marginal Exp(1) limit alone does not determine the negative common-coupling covariance or sign crossing. Hu–Wu–Dong 2022 covers accessible counts and joint depth cutoffs on vertex-label accessibility, a mathematically related but distinct two-time observable. Full 2022 paper access was interrupted after the first screenshot, a residual risk rather than an automatic failure. The exact all-n formula and sign transition survived the best-of-knowledge implication comparison.

## value

PASS

The exact sign reversal in covariance of NESTED random sets is a substantive structural phenomenon rather than a routine single-time moment. The sharp (log n)/n gap and independent finite-dimensional exponential limit quantify how temporal thresholds decorrelate, with an explicit finite-n crossing useful for accessibility research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
