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
# Computational verification

The program `verify_graph.py` constructs all twenty-seven incidence edges, uses ordinary graph breadth-first search to obtain all eighteen vertex-distance functions, exhaustively tests every subset of cardinality \(0\) through \(4\) for edge resolving, and generates each legal one-landmark replacement. It measures every connected-component distance by BFS. It compares its complete lexicographically ordered bases and exchange edges against `state_transition_certificate.json`.

The independent program `verify_geometry.py` does not use graph BFS: it evaluates all edge distances using finite-field incidence identities. Its second complete enumeration verifies the geometric criterion on all \(3060\) four-subsets. It builds exchanges through common-triple incidence, and measures every eccentricity using bit-parallel BFS, independently reproducing the certificate bytes at the structural JSON level. Both programs were executed and reproduced the exact recorded output files. Run each with `python script_name.py state_transition_certificate.json`.

The checks support precisely the eighteen-vertex Pappus incidence graph; experiments over a single finite object are not a proof of a uniform statement for larger biaffine planes. The token-sliding obstruction is also established symbolically by parity and does not depend on BFS. Comparison to an unknown unindexed publication cannot be automated into a uniqueness guarantee.
