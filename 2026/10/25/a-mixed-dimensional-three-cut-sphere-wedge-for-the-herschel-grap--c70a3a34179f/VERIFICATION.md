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

# Reproduction

With Python 3 and no third-party packages, run `python3 verify_herschel.py` in a directory containing the extracted files. The verifier recomputes the graph, the disconnected triples and all \(1930\) complex faces, the deterministic \(957\)-pair acyclic matching, the \(10238\) oriented Hasse incidences, and the exact integral gradient boundary row (all thirteen entries zero). It also independently evaluates ordinary simplicial boundary ranks modulo \(2\), \(3\), and \(5\). Check for final `VERIFY_OK` and compare with `verification_output.txt`.

The integer gradient calculation, not the modular calculations, establishes that all attaching degrees vanish. Discrete Morse theory converts the acyclic matching into a CW homotopy model; maps from each attaching six-sphere into the single six-sphere are classified by their integer degree. A separate published theorem (Bayer et al., Corollary 5.5) supplies the induced-subgraph-minimality conclusion once three-connectivity and nonshellability are verified.

The computation exhausts this specific eleven-vertex graph. There is no claimed proof of broader graph-family behavior and no independent external audit.
