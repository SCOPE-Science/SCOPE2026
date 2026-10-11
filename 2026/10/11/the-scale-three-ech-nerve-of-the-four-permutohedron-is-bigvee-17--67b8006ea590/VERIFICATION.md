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

# Reproduction and boundaries

Run `python3 verify.py certificate.json`. The Python 3 standard-library checker reconstructs the Cayley graph of adjacent-position swaps in \(S_4\), the thirty-six generating edge-neighborhood unions, every simplex, the complete acyclic matching, the free-collapse prefix, and both mod-two homology calculations. The certificate is an explicit list of all \(606\) matched codimension-one incidences and the \(18\) critical face masks; it is not a trace from an inaccessible computation.

Expected checks are \(24\) graph vertices, \(36\) edges and Čech facets, \(1230\) Čech simplices, \(4344\) directed Hasse incidences, \(502\) elementary collapses, \(104\) further matches, one critical vertex and seventeen critical two-simplices. The independently reconstructed reduced integral homotopy type follows from the acyclic discrete-Morse matching; the secondary mod-two ranks check both Čech and Rips face enumerations but are not substituted for an integral homotopy proof.

Limitations: finite order-four permutohedron only; radius \(3/2\) in the geometric graph for Čech and threshold \(3\) in the graph vertex metric for Rips. No other scales, other graph families, or complete Rips integral homotopy types are claimed.
