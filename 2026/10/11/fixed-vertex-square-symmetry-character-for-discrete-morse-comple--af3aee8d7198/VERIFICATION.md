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
# Verification

The accompanying \(`verify_cone_tree.py`\) uses only Python 3 standard-library modules. Execute `python verify_cone_tree.py` from the directory containing it. A successful run prints `VERIFY_OK trees=24 automorphisms=967 homology_cases=4`.

The finite checks enumerate unlabeled trees on two through seven vertices, **all** automorphisms of each representative and all g-invariant partial acyclic matching choices. Independently, for all tree types on two through four vertices they build the complete augmented simplicial chain complex and compute mod-two boundary ranks. These checks do not establish the theorem for arbitrary size or establish a canonical module basis.

The general proof depends on the published complete-source shellability theorem, the explicitly derived orbit-determinant identity and the tree matrix-tree theorem; each hypothesis and sign is given in RESULT.md. Originality remains conditional on the stated bibliographic risks. Independent audit has not been performed.
