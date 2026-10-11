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

# Reproducibility and proof dependencies

Run `python3 verify_pappus_cech.py` in a directory containing `certificates/pappus_cech3.json`. Both files are included. Only Python 3 standard-library modules are used. Success prints `VERIFY_OK` and the independent face-count, collapse, spanning-tree, van Kampen and mod-two-boundary checks.

The certificate uses integer vertex-subset bitmasks in the fixed 18-vertex LCF graph. The script generates the graph and all 27 facets from first principles, enumerates all 1107 nonempty faces, independently constructs boundary matrices over \(\mathbb F_2\), and checks that every one of the 422 indicated pairs is a legal elementary free-face collapse *at the step where it is deleted*. The residual 18-vertex, 109-edge, 136-triangle complex is checked for downward closure. A supplied 17-edge spanning tree is certified by union-find, and each of 92 successive triangle relations is verified to have exactly one previously untrivialized side, until all 109 core edges are accounted for. This establishes trivial fundamental group, not merely vanishing of mod-two first homology.

The final integral homotopy deduction invokes Euler characteristic 45, free integral second homology of a two-complex, integral Hurewicz and homological Whitehead. Finite arithmetic checks alone do not establish originality. No persistent-homology barcode or all-graph classification is claimed, and independent external audit remains unperformed.
