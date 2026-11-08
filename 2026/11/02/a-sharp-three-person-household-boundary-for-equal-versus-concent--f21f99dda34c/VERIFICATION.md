---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Exact finite directed Reed–Frost ancestor-set probabilities are P(K=1)=(1-p)^2, P(K=2)=2p(1-p)^2, and P(K=3)=p^2(3-2p). Substitution into F1,F2,F3 gives D3=pq(q-1)[2+6p-6p^2-q(9p-6p^2)], including q_c=(2+6p-6p^2)/(9p-6p^2) only for p>2/3. D2=-2pq(1-q)<0. For n>=3, the r=1-q coefficient in Dn is p(1-p)^(n-3)(np-2), leaving np=2 intentionally undecided. Independent exhaustive enumeration of all directed contact graphs and seed masks at (p,q)=(9/10,1/2),(9/10,9/10),(2/5,4/5) gave D3=-207/1000,3807/125000,-1328/15625 respectively. All quantifiers and endpoints are respected.

## originality

PASS

The exact two-dose, three-person Bernoulli-introduction expected-cases threshold is not an immediate corollary of household reproduction-threshold minimization; prior final-size susceptibility-set methods are acknowledged. The sharp phase boundary and general n high-introduction sign remain best-of-knowledge additions.

## value

PASS

Finite household policy allocation is a naturally motivated nonlinear objective, and the exact first concentration-favorable household size and crossover are nontrivial. The result separates expected case minimization from reproduction-number heuristics without claiming real-world vaccine policy applicability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
