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

# Reproducibility and scientific limits

Run `python3 verify.py` in this directory with Python 3 standard library. The checker enumerates every ternary relation on the one- and two-element chains, filters to the two published frame monotonicity axioms, and compares all persistent valuation triples' actual nested modal truth sets against the order-closure criterion. There are respectively 2 and 67 admitted frames, with exact agreement throughout. On the three-element chain it independently generates all 19,683 binary operations, keeps the 95 whose graph relations satisfy both frame conditions, and compares the two procedures. Explicit positive and negative controls are included.

The code checks finite examples only. The theorem for every nonempty partial order, including infinite partial orders, is proved by the two principal-upset separation arguments in RESULT.md. The complexity bound assumes explicitly represented finite relations and order. No computation proves novelty, strong completeness, a finite-model property for the entire logic, or independent validation.
