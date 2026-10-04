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

Run `python verify_grid_4x4_k10.py` with a standard Python 3 interpreter. A successful replay ends with `VERIFY_OK`.

The verifier performs the following exact finite checks from definitions:

1. It rebuilds the \(4\times4\) grid and confirms that it has \(16\) vertices and \(24\) edges.
2. It enumerates all \(\binom{16}{10}=8008\) ten-vertex subsets and classifies induced connectivity, obtaining \(2286\) connected and \(5722\) disconnected subsets.
3. It forms the \(5722\) six-vertex facets as complements of the disconnected ten-subsets.
4. It constructs the complete face set twice: by downward closure of the facets and by a direct complement criterion. Exact equality of the two face sets is required.
5. It checks the face vector \((16,120,560,1820,4344,5722)\).
6. It builds each simplicial boundary over \(\mathbb F_2\), computes each rank independently from columns and from an explicitly constructed transpose row space, and requires the two ranks to agree.
7. It checks \(\partial^2=0\) on every basis simplex and verifies the Betti vector \((1,0,0,0,4,2747)\).
8. It checks that the Euler characteristic obtained from faces and from homology is \(-2742\).

These checks prove the finite mod-\(2\) homology calculation used in the claim. They do not compute integral homology, torsion, a homotopy type, or minimality of the counterexample. Independent audit has not been performed.
