---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite reproducibility and proof limits

Run `python3 verify_ejr1.py` with Python 3.10 or newer and no third-party libraries. The program independently evaluates the strict EJR-1 quantifiers using all affordable commonly approved project subsets, all voter coalitions, all feasible funded outcomes, and hypothetical project additions (which need not be budget-feasible). It compares those evaluations against the two exact conditions from the theorem, checks the cost-fair binomial count, the simultaneous-fairness threshold and the minimum singleton shortfall.

The recorded execution passed all 13 tested parameter pairs: `k=2,h=1..5`; `k=3,h=1..4`; `k=4,h=1..3`; `k=5,h=1`. This totals 63,191 feasible funded outcomes. As a diagnostic, the `(2,5)` instance has 2,301 feasible outcomes, 1,275 cost-EJR-1 outcomes, one cardinality-EJR-1 outcome and zero simultaneous outcomes.

These checks are finite and cannot establish universal quantifiers; the general proof is in `RESULT.md`. They do not establish originality, publication priority, independent validation or a stronger fairness notion. The results concern integer parameters, a fixed approval pattern and EJR-1 only.
