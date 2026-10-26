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

# Reproducibility and proof checkpoints

Run `python3 verify.py` with Python 3.10 or later; no external packages are used. Successful execution ends with `VERIFY_OK two-local classifications, exact binary enumeration, ternary pair-witness tests`.

The script enumerates all ordinary derivations (64) and ordinary automorphisms (24) of the three-dimensional Heisenberg Lie algebra over \(\mathbb F_2\), then checks all pairs of the eight algebra elements for each of all \(8192\) maps specified by the derivation classification and all \(48\) maps specified by the automorphism classification. It independently counts which classified maps are additive (128 and 24) and ordinary (64 and 24). For \(\mathbb F_3\), it enumerates all 729 ordinary derivation and all 432 ordinary automorphism witnesses and checks every element pair of each of 150 deterministically sampled classified maps per family. It also checks the displayed finite-field cardinalities arithmetically.

The infinite-family classification is justified by three separate mathematical steps: (1) classify all genuine linear witnesses from the Lie bracket; (2) derive homogeneity and, for automorphisms, projective and vertical-injectivity constraints from the pairwise condition; (3) explicitly interpolate arbitrary pairs using two-dimensional matrices with prescribed trace or nonzero determinant. Homogeneous-map and projective-permutation counts then produce the formulas. Checks over small fields cannot rule out untested exceptions or establish the all-field theorem without this argument.
