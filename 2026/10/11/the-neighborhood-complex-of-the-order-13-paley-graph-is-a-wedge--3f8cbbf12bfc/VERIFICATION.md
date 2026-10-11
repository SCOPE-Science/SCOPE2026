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
The verifier reconstructs the graph, all 598 nonempty neighborhood-complex faces, every matching pair, and the full oriented Hasse diagram. It checks 2,067 covers and proves acyclicity by exhaustive topological sorting. It also recomputes boundary ranks over three finite fields.

Run `python verify.py` in the same directory as `CERTIFICATE.json`. The expected terminal line is:

`PASS: 598 faces; 2067 Hasse covers; 286 acyclic pairs; critical vector (1,0,25,0,0,0); mod-2/3/5 Betti vector (1,0,25,0,0,0).`

The computation is exhaustive for the stated finite complex. It does not prove any theorem for larger Paley graphs.
