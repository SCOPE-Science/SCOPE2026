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

# Reproducibility and verification

The mathematical proof is in RESULT.md. The two plain-Python scripts are self-contained and use only the standard library. Execute `python verify_structure.py` and `python verify_homology.py` in the extracted directory.

`verify_structure.py` enumerates all maximal cliques for \(1\le r\le12\), compares them with the cyclic windows and equilateral triples, and for \(2\le r\le6\) independently deletes explicit free-face pairs until the radius-\(r-1\) clique complex remains. It tests actual free-face uniqueness before each deletion.

`verify_homology.py` enumerates all faces for \(1\le r\le6\); exact binary elimination computes the augmented simplicial chain ranks. It verifies vanishing reduced mod-two Betti numbers except degree two with rank \(r-1\). For every dihedral element in these cases it computes a signed fixed-simplex trace, including the reduced augmentation correction, and compares with the integral character formula. These experiments are not exhaustive over all \(r\); the all-parameter integral result rests on the relative-pair proof and the cited collapse theorem.

The finite group action is checked on a triangulated simplicial complex, not assumed to be free. The rational quotient assertion uses averaging over finite groups after barycentric subdivision. It does not assert integral acyclicity or integral quotient torsion calculations.
