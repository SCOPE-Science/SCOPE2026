---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For fixed h,P,v and homogeneous epidemiology, set s=P^T h, r=v/s, q=P r, M=sum hq^2. For Perron eigenvector y of K_D=(mu I-D)^(-1)L set z=y/v. Balanced stationary flows F_ij=d_ij v_j and x-1>=log x give E=sum_i(Dy)_i/z_i>=0, strict unless y proportional to v. Groupwise Cauchy–Schwarz gives sum_i(Ly)_i/z_i>=sum_k h_kq_k^2=M, hence mu rho(K_D)>=M. If equality, E=0 and Lv=Mv; weighted inner product forces all q_k=M=1. Conversely q all=1 gives column sums of K_D=1/mu. Fast complete-generator D_k=k(v1^T-I) proves sharp infimum M by rank-one resolvent limit. Independent rational stationary-distribution and spectral example checks succeeded, including heterogeneous exposure strictness; no finite bound extrapolation.

## originality

PASS

Gao–Yuan 2024 already contains intermediate groupwise Cauchy lower bound and homogeneous baseline; neither is claimed novel. Its Remark 4.8 opens equality issue, and inspected theorem does not optimize over all generators at fixed stationary v, show nonattainment at finite rates, or prove group-exposure iff criterion. 2019 Gao–van den Driessche–Cosner all-Eulerian equality is a different host migration model. Gao–Cao 2024 all-Lagrangian full text inaccessible remains residual risk.

## value

PASS

Settles a natural exact variational question and equality criterion raised by the source: a quantified irreducible heterogeneous-exposure variance floor, strict finite-rate nonattainment, and constructive fast-mixing sharpness, useful for separating movement rates from stationary composition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
