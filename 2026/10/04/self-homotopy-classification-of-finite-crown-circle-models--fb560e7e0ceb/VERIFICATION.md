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

The general proof is symbolic and does not depend on finite enumeration. `verify_crown.py` reconstructs the crown order from its defining cover relations and enumerates all monotone self-maps for \(n=2,3,4,5\). For every map it computes winding from the cyclic edge walk, checks that every nonzero-winding map is an order automorphism, and checks that every winding-zero image omits at least one target point.

For \(n=2,3,4\), the script also constructs the pointwise-comparability graph on the full self-map set. Connected components of this graph are finite-space homotopy classes, and the computed counts are \(5,7,9\), equal to \(2n+1\). The \(n=5\) component graph is not exhaustively built; only the theorem-critical degree and image checks are replayed there.

Replay command: `python3 verify_crown.py`. The captured output in `verification_output.txt` ends with `VERIFY_OK`.
