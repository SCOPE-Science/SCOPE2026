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

Factored each period of the scalar delayed recursion x_{k+1}=x_k-t x_{k-d_k} using T0=[[1-t,0],[1,0]]=ve1^T and T1=[[1,-t],[1,0]]. Each run of L delayed updates after a zero has rank-one matrix T1^L ve1^T, with nonzero eigenvalue p_L following p0=1-t,p1=1-2t,p_{L+2}=p_{L+1}-t p_L. Product of cyclic runs has determinant 0 and trace Π p_L; all initial pairs decay iff |Π p_L|<1; equality has a nondecaying modal trajectory and product 0 yields monodromy square zero by Cayley-Hamilton, so annihilation within two full periods. p_L=det(I-sqrt(t) A_path(L+2)) gives exact positive simple roots 1/[4cos²(jπ/(L+3))]; their largest grows quadratically with run length, giving arbitrarily large specially tuned finite-termination steps. The L=2 stability windows (0,1)∪(2,3) follow from -1<t²-3t+1<1. Independently checked symbolic monodromy traces/determinants for every cyclic delay word through length seven, path determinants through size eleven and period-three nilpotence. The all-length result is the rank-one/path proof, not finite enumeration.

## originality

PASS

The source-independent rank-one cyclic run product and path-spectrum factorization go beyond the known general Floquet/Schur stability criterion. Primary periodic linear-system work treats general monodromy without explicit binary-run factors; random staleness momentum literature uses probabilistic modeling and unrelated convergence objectives. No exact dominating same-recurrence all-pattern classification found in searched published records; unindexed specialized periodic delay literature remains a risk.

## value

PASS

Complete tractable Floquet classification of every deterministic periodic fresh/stale scalar-gradient schedule plus exact cancellation roots and reentrant stability regions reveals a meaningful stability boundary that generic asynchronous optimization bounds obscure. The unbounded stepsize existence is a fragile exact-tuning phenomenon, explicitly not a robust algorithm, but structurally important for discrete-delay systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
