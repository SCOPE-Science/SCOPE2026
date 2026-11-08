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

For all m≥2, r_i>1,c_i>0, the scalar envelope H(N)=max_{z_i≥0,sum z_i=N}sum r_i z_i/(1+c_i z_i) is strictly increasing, strictly concave along rays and H(N)/N strictly decreasing. With A=sum(r_i+1)/c_i, B=sum sqrt(r_i)/c_i, C=sum 1/c_i, q+1/q=A/B, the vector y_i*=(sqrt(r_i)/q−1)/c_i is positive and has equal marginal derivatives q²; direct algebra gives H(K*)=K*, K*=B/q−C. For every history-dependent column-stochastic redistribution N_(t+1)≤H(N_t), yielding limsup≤K*. Rank-one D=p1^T, p=y*/K*, achieves K* from any nonzero state. Strict concavity proves K* equals sum isolated K_i iff all r_i are equal and gives quadratic rigidity of the allocation when N_t→K*. Independently evaluated exact two-patch r=(4,9), c=(1,1): q=(3−sqrt5)/2, K*=(11+5sqrt5)/2>11, equal marginal derivatives and exact growth balance. All-patch assertion is under unrestricted conservative complete redistribution only.

## originality

PASS

Best-of-knowledge PASS for explicit unrestricted adaptive all-policy ceiling, stationary attainment in arbitrary finite m, heterogeneity equality characterization and limiting allocation rigidity. The perfect-mixing mechanism and qualitative benefits of asymmetric dispersal are prior work; the major 2026 general-patch paper is a priority risk.

## value

PASS

An optimal-control-style extremal theorem for a natural heterogeneous patch ecology model, rather than just a sample equilibrium. The sharp all-policy bound and rigidity show what any dynamic dispersal strategy can or cannot improve; the exact K* and strict-gain condition are scientifically interpretable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
