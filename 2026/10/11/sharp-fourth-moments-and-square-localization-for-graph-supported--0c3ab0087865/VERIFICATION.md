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

# Verification and limits
The fourth-moment identity is obtained by expanding \(F_a^4\) and using independence and parity of every vertex degree. The only four-distinct-edge contributing configurations are four-cycles. The global defect decomposition is exact because different four-cycles have disjoint edge sets. Two sharp AM--GM inequalities certify the local nonnegative brackets; normalization and elementary mass packing certify the quantitative concentration law.

Reproduction: `python3 verify.py` using Python 3 standard library gives `EDGE_DISJOINT_SQUARE_MOMENT_EXACT_OK 24`. The checker enumerates the sign cube for eight example graphs and 24 coefficient arrays and also verifies rational two-cycle sharpness identities. Such finite tests do not prove the theorem for arbitrary graphs and arbitrary real arrays; that part is analytic. Bibliographic comparisons are not proof of absolute historical novelty. Independent audit remains unperformed.
