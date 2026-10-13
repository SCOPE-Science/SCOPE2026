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

The proof uses Stewart–Sierpiński, repeated Bertrand bounds, and the prime number theorem for fixed reduced arithmetic progressions. These unrestricted ingredients are mathematical arguments, not inferred from the tests.

Standalone exact-arithmetic checker: `squarefree_practical_verify.py`. Its output is stored in `verification_output.txt`. Ten greedy steps were checked for all eligible moduli below \(5005\), together with residue-witness tests and the coprime obstruction below \(100000\). A finite check neither proves global minimality nor establishes infinitely many representatives; these follow from the proof.
