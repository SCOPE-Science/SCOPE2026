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

The proof was checked from the commutator coordinate identity through the Potts expansion and the random-cluster/Tutte conversion. `verify.py` independently enumerates all algebra elements and all ordered pairs for seven small field/quiver cases, computes commutation directly from the quotient multiplication law, and compares the result with the spanning-subgraph formula. It also checks the generalized-Kronecker specialization for multiple field sizes and arrow multiplicities.

The finite replay verifies examples only; it is not used as an infinite proof. The theorem is limited to split algebras of the form \(\mathbb F_qQ/J^2\) with finite loopless quiver. Prescribed nonzero commutator fibers are outside the claim.
