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

The standalone `VERIFY.py` uses only the Python standard library and reconstructs all edges from their defining Hamming-weight condition. It has three distinct computational pathways: (i) an integer Bareiss determinant of the root-deleted outgoing graph Laplacian (directed matrix-tree theorem), (ii) exhaustive outgoing-selector maps with detection of functional cycles and direct checks of the high-index exclusion criterion, and (iii) enumeration of possible local outgoing-edge orders and direct recovery and validation of universal cycles.

Invocation: `python VERIFY.py`.

Observed output ends with:

`VERIFY_OK matrix_tree_k=3..10 functional_tree_k=3..10 direct_euler_k=3..8`

Checks are finite. The independent mathematical proof in `RESULT.md` supplies the quantifier \(k\ge3\). No external or independent scientific audit was performed.
