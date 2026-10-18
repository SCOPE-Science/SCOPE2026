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

# Reproducible verification

The bundled Python checker constructs the labeled hypercube graphs from binary-coordinate adjacency, enumerates perfect matchings by two independently structured complete recursions, cross-checks square-flip adjacencies by faces and by endpoint reconnections, and computes the full four-dimensional connectivity graph and its all-source eccentricities. It verifies the orbit of the eight frozen configurations under every coordinate permutation and bit translation. It also checks the four explicitly listed frozen seeds, their cross-disjointness, and all four parity-slice combinations at dimension five.

To replay, run `python3 verify_hypercube_flips.py` in a directory containing the extracted source. The output should match `verify_output.txt` exactly and end in `VERIFY_OK`. Source and output bytes are included within the same package; no downloaded numerical tables are needed. The proof of the infinite-family lower bound is a symbolic argument by square-coordinate types, not an attempted exhaustive computation in arbitrary dimension.

Scope limitations: no enumeration of higher-dimensional components or an exact total frozen count is claimed, and a successful program execution is not an independent audit.
