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

The executable `artifacts/verify.py` reconstructs the Petersen graph from the stated ten-vertex presentation and enumerates every one of the \(4^{10}\) possible tail choices. It retains exactly the assignments corresponding to acyclic vertex-edge matchings and checks simplicial closure.

The face count is then recomputed independently from the Petersen Laplacian: for each cardinality \(k\), the script sums all exact principal \(k\)-minors, using Bareiss elimination. By the matrix-forest theorem this equals the number of rooted forests and must match the Morse-face count.

The full reduced simplicial boundary complex over \(\mathbb F_2\) is constructed from the retained faces. Every boundary rank is computed twice with different column orders and opposite pivot conventions. The two rank vectors agree exactly and give reduced Betti ranks \(38\) in dimension \(7\), \(294\) in dimension \(8\), and zero elsewhere. The reduced Euler characteristic is checked both from faces and from homology.

Running

`python3 artifacts/verify.py`

must end with `PETERSEN_MORSE_VERIFY_OK`.

The verification is exhaustive for this finite complex but only over \(\mathbb F_2\). It does not certify integral homology, torsion, or a homotopy decomposition.
