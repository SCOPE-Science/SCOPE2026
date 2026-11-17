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

In the stated exactly-two-agent, two equally abundant chore-type model, r>1 crossed wrong-agent A and B chores permit a strict fractional Pareto improvement; absence of a cross is sufficient by strictly positive weighted-sum minimization. On either fPO branch, the binding EFX inequality is j≤t/2−(t−1)/(2r). The two branches contain binom(t,j) labeled allocations per j and overlap exactly once. At r=1, all allocations are fPO and EFX is exactly equal bundle cardinality. Integer floor crossing yields listed inclusive jump ratios; fixed r>1 binomial tail Stirling gives h2((r−1)/(2r)). Independently enumerated all 4^t labeled allocations for 1≤t≤5 at six exact rational r values, testing owner-by-owner EFX and crossed-case fPO, agreeing with formula in 30 parameter instances. Actual verify_chores.py read and checks more cases. Finite tests do not establish all real r or t.

## originality

PASS

Aziz, Lindsay, Ritossa and Suzuki arXiv:2211.00879 already establish the two-chore-type fPO structural principle and EFX existence but the inspected Lemma 4.1, Theorem 5.1 and surrounding algorithmic results do not specify this symmetric labeled allocation census, its jumps or its fixed-parameter entropy law. Related EFX/fPO existence and other binary zero-cost chores census results concern different domains. The exact joint counting/phase theorem survives best-of-knowledge.

## value

PASS

Counts the simultaneous fairness-and-fractional-efficiency feasible set rather than only its existence. The rational discontinuities, sharp r=1 collapse, and asymptotic probability exponent quantify a natural combinatorial economics statistic with distinct labeled chores.

The dated certificate retains the supplied scientific assessment, sources and limitations.
