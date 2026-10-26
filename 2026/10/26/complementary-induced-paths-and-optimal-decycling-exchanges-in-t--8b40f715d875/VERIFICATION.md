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

# Verification procedure

The package contains two **independently constructed** exact graph models and executable, Python 3 standard-library finite checkers. They were executed from their actual embedded file paths in this package. The ring model and the coordinate model each enumerate all six-vertex deletion candidates, check optimality, construct the exchange graph, test every edge for the token-slide restriction, and run breadth-first search from every optimum configuration.

Run `python3 verify_icosahedron_rings.py` and `python3 verify_icosahedron_coordinates.py` in the directory of the embedded files. Compare their outputs with `output_icosahedron_rings.txt` and `output_icosahedron_coordinates.txt` respectively. Each terminates with a `CERTIFICATE_VERIFIED` marker after all assertions complete (one names its marker `INDEPENDENT_CERTIFICATE_VERIFIED`).

Critical checks: \(2^{12}=4096\) total subset masks by the first program; complete \(\binom{12}{6}=924\) six-subset census in both programs; no smaller deletion sets; sixty optima; both halves are \(P_6\); 120 undirected exchange edges and 4 regularity; all jumps correspond to host-graph slides; one connected bipartite component; all 60 eccentricities equal 6; full 3,600 ordered-pair distance/overlap table. Reproducibility assumes ordinary Python 3 execution and exact integer arithmetic. Finite enumeration does not prove any extension to other graphs. External audit has not been performed.
