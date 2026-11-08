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

From this directory, run `python3 verify_hesse_nonincidence.py` and `python3 verify_binary_homology.py`. Both require only Python 3 standard libraries. The exact stdout from these checks is stored in `morse_output.txt` and `binary_output.txt` respectively. The first script enumerates all subsets on both sides and separately tests face membership, constructs greedy acyclic discrete-Morse matchings for both vertex orders, verifies the complete oriented Hasse diagrams by topological sorting, and reduces the signed critical four-cell boundary over the integers to zero. A zero degree vector proves a null attachment by the degree-three Hurewicz isomorphism for a wedge of three-spheres.

The second script independently constructs the affine-line relation, enumerates faces directly, and calculates reduced homology over \(\mathbf F_2\) from complete simplicial boundary matrices. Both sides have reduced mod-two ranks eleven in degree three and one in degree four. This independent check does not by itself prove the integral homotopy statement. The finite verification says nothing about larger affine planes, and no independent external scientific audit is represented.
