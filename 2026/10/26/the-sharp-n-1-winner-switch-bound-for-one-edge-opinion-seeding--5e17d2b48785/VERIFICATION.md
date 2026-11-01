---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

In an n-vertex nonnegative weighted directed unit-anchored FJ model, varying only edge a->b adds rank-one matrix t e_a(e_a-e_b)^T to I+L(0). Since the latter is a nonsingular M-matrix, H>=0 and x=H e_a has its unique positive maximum at a, implying d=x_a-x_b>0. Sherman-Morrison yields common increasing u=t/(1+dt) and each reduction score s_j sum_i [(I+L(t))^-1]_{ij}/n affine in u. Every strict winning affine score can win on at most one interval, bounding genuine strict switches by n-1. The constructed directed acyclic network with m=n-2 leaves has distinct, strictly increasing slopes and positive strictly ordered adjacent crossing abscissae T_0/2,T_0,...,T_{m-2},T_*; the adjacent crossing weighted-average property forces all n lines onto the upper envelope in turn. Delta, kappa and all opinions satisfy (0,1] rational bounds. Independently checked exact-rational arithmetic for all m=2..18 and direct matrix inverse at n=4,5; n=4 transitions 153/4,153/2,90156. Finite examples complement but do not prove the universal all-n assertion.

## originality

PASS

Qualified PASS for the sharp parametric switch count and explicit all-winner attaining family. Sun-Zhang Theorem 4.1 supplies the fixed-network column-sum seeding objective, which the claim openly uses; it does not bound changes under a continuously reweighted edge. Other edge-influence sources optimize a different set of agents/objectives. Generic upper-envelope facts are prior and not novelty by themselves; the exact FJ reduction and attaining construction supply the meaningful increment.

## value

PASS

The exact number of optimum intervention reversals is a natural parameter-sensitivity invariant for network opinion optimization. The nonreturn property is universal and its sharpness is realized by an explicit valid nonnegative network of every size n>=4 with all vertices winning in sequence. This is more informative than a generic line-envelope observation or a fixed-network calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
