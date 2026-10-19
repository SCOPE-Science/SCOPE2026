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

# Reproduction and boundaries

The proof covers all integers \(m,n\ge2\). The accompanying `checker.py` is a standalone Python 3 script requiring SymPy. Run `python3 checker.py` in the same directory as this file. For all 16 ordered size pairs in \(\{2,3,4,5\}^2\), it independently enumerates the reachable labeled graph orbit by breadth-first search, compares those graphs to the symbolic six-family description, checks each vertex-choice transition and its reversibility, and verifies the full exact characteristic polynomial of \(N(I-P)\).

Symbolic validation also confirms the expansion of \(p_{m,n}(1-h)\) used in the proof. The checker has finite scope: no finite computation is offered as proof of the universal spectral claim. That claim is justified by the invariant-space factorization and positive-coefficient polynomial argument in RESULT.md. Neither the absolute spectral gap nor an exact total-variation mixing time is asserted. Independent audit has not been performed.
