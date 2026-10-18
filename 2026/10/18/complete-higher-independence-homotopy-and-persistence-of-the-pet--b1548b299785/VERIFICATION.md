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
# Reproducible finite checks

The source `verify.py` and data `certificate.json` use only Python 3 standard-library modules. Run `python3 verify.py certificate.json` in the directory containing those files. The complete recorded stdout from an actual successful execution is `verifier_output.txt`.

The graph is regenerated as the ten two-subsets of five points, with adjacency iff disjoint. Its fifteen edges and degree-three vertices are checked. For each of the 1023 nonempty subsets the script computes the exact largest induced-component cardinality; this serves as its filtration parameter. Every stage from one through ten is therefore exhaustive. The per-stage certificate lists every removed pair and unmatched maximal cell; the verifier asserts that the list exhausts exactly the corresponding simplicial complex and verifies every free-face condition. The removal order proves absence of closed gradient paths. Critical dimensions and counts are tested against the reported homotopy types.

Separately from certificate matching, full simplicial chain matrices over \(\mathbb F_2\) are regenerated and reduced to derive each reduced Betti vector. Finally, the full 1023-face filtered boundary is reduced with a face-before-coface ordering to recover every nonzero-length persistence interval. All asserted checks pass. The finite certificate and these arithmetic checks do not by themselves prove an assertion about any other graph. Independent validation was not performed.
