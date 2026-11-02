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

# Reproducibility and limits
Execute `python3 verify.py` with an ordinary Python 3 interpreter. The checker constructs the incidence-algebra multiplication table from a poset's covers, enumerates idempotent elements and ordered tuples, computes the unital algebra's word span, and independently compares with the proposed Hamming-cover sum. It returns `VERIFY_OK: 11 exhaustive configurations`. It includes both positive and zero generator counts and checks an antichain, chains, a fork, and a diamond over prime fields \(\mathbb F_2\) and \(\mathbb F_3\).

The checker is finite verification only; it does not validate all prime powers, all posets or the independent priority status. The unrestricted formula is established through the written orbit-stabilizer and Longstaff–Rosenthal generation-criterion proof. The complete text of Kolegov's 2024 article was unavailable for inspection; novelty remains subject to external historical verification.
