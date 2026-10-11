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
The theorem is proved symbolically in `RESULT.md`; finite enumeration is corroborative only.

Critical checks:
- each source vertex has coordinate sum \(1\) and squared norm \(3\);
- the proposed center has every coordinate \(1/D\) and squared norm \(1/D\);
- hence every source vertex has squared center distance \(3-1/D\);
- the three degree-dependent weights attached to each graph edge are positive;
- their total mass is \(1\);
- each edge coordinate of their barycenter is \(1/D\);
- each graph-vertex coordinate is \(1/D\) after summing \(d_v\) equal contributions \(1/(Dd_v)\);
- the weighted variance identity proves every displaced center needs strictly larger radius.

`verify.py` exhaustively checks every connected labeled simple graph on two through six vertices with exact rational arithmetic. It verifies the weight sum, every barycenter coordinate, and the common squared-radius identity. It does not replace the arbitrary-graph proof and does not assess originality.
