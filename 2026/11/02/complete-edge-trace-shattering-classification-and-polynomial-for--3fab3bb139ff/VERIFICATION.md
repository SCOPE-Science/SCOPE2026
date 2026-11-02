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

# Verification procedures

Run `python verify_support_classification.py` in a directory containing that program. It builds each undirected Hamiltonian-cycle edge mask using a fixed starting vertex and reversal quotient, checks the cardinality and uniqueness of concepts, enumerates **all** supports contained in at least one Hamiltonian cycle for orders three through seven, and computes the realized trace patterns for every support. An independent graph-component calculation implements the structural criterion. All computed cases agree. The actual program output is in `verification_output.txt`.

Representative two-path component supports at orders eight and nine are tested directly against all Hamiltonian-cycle hypotheses of those orders. The checker also counts the largest supports for orders five through seven and checks the exact factorial formula. No sampling was substituted for finite exhaustive enumeration through seven vertices.

The unrestricted classification is proved mathematically in RESULT.md. These finite checks cannot themselves prove an all-order statement, and the checker does not exhaust all subsets of all possible edges at orders eight and nine. The external independent scientific audit has not been performed.
