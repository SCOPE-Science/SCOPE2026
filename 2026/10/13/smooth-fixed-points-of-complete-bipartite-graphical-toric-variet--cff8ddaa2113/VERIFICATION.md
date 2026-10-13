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

# Reproducibility and limits

Execute `python3 verify_graphical_zonotope.py` with the standard Python 3 library. The script iterates all \(2^{ab}\) orientations at \((a,b)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\), excludes directed cycles, computes the directed transitive reduction independently of its source-layer criterion, checks the covering graph, tests smoothness by tree edge count, and compares exact totals with the closed formula. A separate factorial calculation verifies the balanced specialization for \(2\le m\le14\). The results are contained in `verify_graphical_zonotope_output.txt` and can be reproduced directly from the embedded source.

Finite checking is not proof for all positive parameters. The general proof is contained in `RESULT.md`. The result states no external certificate or independently validated status. The full singular locus away from torus fixed points has not been computed.
