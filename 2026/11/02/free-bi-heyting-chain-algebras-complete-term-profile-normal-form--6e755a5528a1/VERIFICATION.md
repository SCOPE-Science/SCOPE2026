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

# Verification notes

The all-arity proof is constructive: each term function selects one variable/end value per endpoint-marked comparison type; the crisp test \(D(a,b)=1\setminus(a\to b)\) gives the converse selector construction. Surjectivity and injectivity of the product map are proved in the accompanying RESULT.md. The Stirling multiplicity count follows from choosing interior variables, assigning the remainder to endpoints, and ordering the nonempty interior equality blocks.

Run \(\texttt{python3 checker.py}\) with Python 3 and only the standard library. The program exhausts small finite comparison patterns and reports \(\texttt{ALL\_CHECKS\_OK}\). It also checks unary term-closure sizes, the exact two-variable selector count, and the smallest chain detecting the strict-order witness through three variables. The all-rank result does not rest on finite enumeration. No independent audit, automated theorem-prover certification, or evaluation on arbitrary branching bi-Heyting frames is asserted.
