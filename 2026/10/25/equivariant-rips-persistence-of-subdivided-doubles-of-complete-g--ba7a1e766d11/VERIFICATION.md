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

Execute `python3 verify.py` from the containing directory. The script requires the Python standard library and reconstructs the graph from first principles. It computes the entire \(20\)-vertex distance matrix and the exact scale-two clique complex, performs a complete directed Hasse-graph acyclicity test, and verifies the full symmetry-character formulas for every one of the \(3840\) natural graph automorphisms. Its exact captured output is in `verification_output.txt`.

Expected finite check: \(1413\) nonempty scale-two faces, \(701\) matched pairs, one critical zero-cell, ten critical two-cells, \(6390\) codimension-one incidences, graph cycle rank \(21\), and threshold-three conicality. The full \(n\)-parameter result follows from the symbolic proof in `RESULT.md`, not from extrapolating the finite case. Neither independent external validation nor an equivariant homotopy classification is claimed.
