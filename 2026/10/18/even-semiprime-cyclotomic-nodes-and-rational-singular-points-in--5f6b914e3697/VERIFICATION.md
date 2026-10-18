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

The mathematical proof uses the projective Jacobian criterion, the minimal polynomial of a primitive prime-order root of unity, the matrix determinant lemma, the explicit Galois action, and Burnside's lemma. No finite experiment is used to infer the all-parameter conclusion.

To reproduce finite samples, run `python verify_nodes.py` in the same directory. It compares exact multinomial summation with a separate exhaustive enumeration normalized to first coordinate one. It checks six parameter pairs and verifies exact arithmetic of all reported examples, rational-node counts, Galois-orbit divisibility and permutation orbits, printing `VERIFY_OK` on success.

The computations do not verify the infinite family or the complete search of published mathematics. The theorem is characteristic zero only, and the displayed finite etale scheme is not a model for extra singularities of characteristic-positive hypersurface reductions.
