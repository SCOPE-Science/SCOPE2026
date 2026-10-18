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

# Reproducibility and limitations

Place `verify_king25.py` and `morse_certificate.json` beside one another and execute `python3 verify_king25.py` (Python standard library only). The code regenerates the vertex adjacencies and complete face list, checks all matching and unmatched-face entries against the graph, verifies acyclicity on the *complete* directed Hasse diagram, and computes \(\mathbf F_2\) boundary ranks independently. The critical dimensions are one \(0\)-cell and 141 \(3\)-cells; the complete graph has 4,550 face-poset cover edges.

The verifier also classifies the ten independent five-sets, computes exact signed action of every translation, and checks all six order-five subgroup rational Betti numbers plus full translation-group invariants. `verification_output.txt` is a transcript of an actual successful execution with the supplied current certificate. It is corroboration, not an alternative to the source code and data.

The proof for all translated copies of the fixed finite graph is exact; nothing here asserts a formula for all toroidal board sizes. Quotient transfer is rational and does not certify integral quotient homology. Independent scientific review has not been performed.
