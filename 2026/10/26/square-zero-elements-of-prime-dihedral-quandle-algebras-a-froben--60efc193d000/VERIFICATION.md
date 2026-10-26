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

# Reproducibility and checked limits

Run `python check_square_zero.py` with a Python 3 interpreter. The checker builds prime fields and the nonprime fields of orders four and eight using finite polynomial-quotient arithmetic, exhausts all coefficient vectors for fourteen \((p,q)\) configurations, and compares the actual quandle-algebra product \(u^2\) against the derived modular-order formula. Expected terminal line: `ALL_DIHEDRAL_SQUARE_ZERO_TESTS_PASSED 14`.

Direct enumeration includes \((p,q)=(5,4)\) with 31 solutions, \((5,11)\) with 241 solutions, and \((7,2)\) with 15. The verifier counts all elements including zero and applies no assumption of associativity. The proof gives an independent argument for all odd prime \(p\), all prime-power \(q\) coprime to \(p\), including fields not explicitly exhausted.

The general theorem is not formally or independently certified; finite tests neither establish its infinite quantifiers nor guarantee novelty. The scope explicitly excludes modular characteristic and composite quandle orders.
