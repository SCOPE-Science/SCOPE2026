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
# Computational and mathematical verification

Run `python3 verify.py` from the same directory as this file. The standard-library test script constructs the graph and its edge relation independently of the proof exposition. It exhausts all vertex permutations for listed small blade-size tuples, compares the complete exact integer counts for every maximal independent set against rational probabilities, recomputes the total-variation distance, and checks the product-sum uniformity criterion. Cases include the isolated blade boundaries and exact-uniform/nonuniform mixed bouquets.

This replay is a finite cross-check. All unbounded claims rest on the set classification, vertex-order symmetry, and exact mass comparison in `RESULT.md`. No formal theorem prover or independent mathematical audit was used. No output from external code is represented as a proof of originality.
