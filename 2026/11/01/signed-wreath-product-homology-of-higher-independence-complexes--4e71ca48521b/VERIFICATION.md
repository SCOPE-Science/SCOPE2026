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
# Reproducibility
Run `python3 verify.py` with Python 3; no external packages are required. The executable reconstructs the complete finite complexes directly from the induced-component definition and checks all oriented link incidences for acyclicity, separate mod-two simplicial boundary ranks, and signed simplicial Lefschetz characters against the wreath-product character formula. The checks include \((r,m,s)=(3,3,3)\) (all \(1296\) group elements), \((3,3,4)\) (\(26\) selected elements), and the nonuniform leaf sizes \((3,3,4)\). Exact outputs are produced by the script itself, not hardcoded certificates.

The infinite-parameter theorem is established by the root-link patchwork matching, the homotopy-pushout description of star factors, integral chain identification with leaf augmentation exterior powers, and graded join functoriality. Finite experiments verify only their sampled instances. There is no independent audit or independent validation.
