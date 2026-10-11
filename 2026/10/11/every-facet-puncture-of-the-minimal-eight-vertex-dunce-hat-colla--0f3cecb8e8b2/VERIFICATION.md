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

The standalone verifier reads the exact `collapse_certificate.json` shipped with this package.

It first reconstructs the \((8,24,17)\) face vector and checks the full-complex edge-to-triangle incidence profile \(2^{\times 21},3^{\times 3}\). Hence there is no free edge in the unpunctured complex.

For each of all \(17\) facets, the verifier deletes only that triangle and replays the recorded elementary collapses. Before each triangle-edge removal it recomputes all current triangle incidences and requires the recorded edge to lie in exactly one current triangle. Before each graph collapse it recomputes all vertex degrees and requires the recorded vertex to have degree one. It then requires the terminal graph to be connected and two-regular.

The exact replay output is:

`VERIFY_OK f=8,24,17 full_free_edges=0 punctures=17 all_collapse_to_cycle=yes certificate_core_lengths=3:12,4:5`

The displayed terminal-length histogram belongs to the deterministic lexicographic certificate. The scientific claim uses only the verified existence of a collapse to a simple cycle for every facet; it does not claim uniqueness of terminal cycle or collapse order.
