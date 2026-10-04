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

The theorem was checked by a standalone standard-library program, `verify_roman_chain.py`.

For every positive canonical twin-class profile of a connected chain graph with total order at most \(9\), the program constructs the graph from the nested-neighborhood definition, exhaustively enumerates all \(3^N\) labelings by \(\{0,1,2\}\), tests the Roman domination condition directly, and compares the complete brute-force weight polynomial coefficient-by-coefficient with the class-product formula in RESULT.md.

Observed replay output:

`VERIFY_OK profiles=255 labelings=3023307 coefficient_checks=4351 max_order=9`

The complete-bipartite one-pair boundary case was also compared conceptually with the published theorem in DOI 10.7251/BIMVI2102355G.

The exhaustive computation is finite and does not certify arbitrary graph order. The unrestricted theorem is justified by the extremal-index proof in RESULT.md. No independent audit has been performed.
