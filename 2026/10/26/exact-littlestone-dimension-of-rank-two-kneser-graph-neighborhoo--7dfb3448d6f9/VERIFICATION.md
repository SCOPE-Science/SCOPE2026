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

# Verification record

The package contains explicit nested query trees in `witness_trees.json`. Run `python3 verify.py` alongside that file using a standard Python 3 installation. It checks the permitted labels, pair format, complete tree depth, all individual root-to-leaf path constraints, and the \(2+4+8+16=30\) terminal witnesses. It also tests all \(5985\) four-vertex samples for ordinary VC shattering in the seven-label graph, which is a separate finite diagnostic.

The theorem's uniform all-order upper bound is a mathematical argument, not an enumeration or a timed solver inference. It uses a four-error learning strategy and a direct contradiction with depth-five shattering. The finite certificate provides lower bounds for \(n\le7\); monotone embedding supplies all larger \(n\). Neither an exhaustive literature search nor independent mathematical certification has been claimed.
