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

# Reproduction and limits

Run `python3 verify.py` from the directory containing this document. Only Python's standard library is needed. The program checks the exact weighted pair-codegrees, all binary-state generator evaluations for the two seven-vertex examples, complete lumpability over all 126 nonabsorbing states, the rational quotient equations, and their exact absorption-time solutions. It also checks the unequal-codegree identity on all 16 states of a heterogeneous four-vertex example.

For the seven-vertex comparison, every Fano pair belongs to precisely one triple, exactly as every pair belongs to exactly one edge of the complete graph. The program confirms both have identical generator action \(\mathcal LH=-H\) on every binary configuration, while the two exact absorption-time solutions differ by \(13/210\). The universal characterization for arbitrary finite hypergraphs is proved separately by generator and cut identities; no finite test alone proves the quantified theorem.

Scientific limitations: independent audit has not been performed; the model uses fixed hyperedges, independent edge clocks, binary opinions, and simultaneous uniformly selected group opinion. Other update rules and published equivalent formulations are not exhaustively excluded.
