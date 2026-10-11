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

The included `verify.py` uses Python 3's standard library and reconstructs all graph, metric, simplicial and chain data from definitions; invoke with `python3 verify.py`.

Actual replay checks include 16 vertices and 24 edges, every vertex's distance profile, every antipodal scale-five facet, the 120 pairwise scale-four facet intersections, 1,090 independence faces, 542 matched incidences, acyclicity of 4,272 oriented Hasse incidences, exactly six critical faces, and all 542 exact integer unit pivots with vanishing remaining integral Morse differentials. A separately assembled mod-two boundary calculation obtains ranks 15, 81, 191, 181, 58, 14, and 2 in positive dimensions one through seven. The script prints `VERIFY_OK` after every assertion passes.

The infinite continuum of filtration scales is handled by the graph Čech even/odd neighborhood lemma and the proof's threshold identifications. The verifier is an exact finite certificate, not an independent mathematical audit or an assertion about the unspecified low-dimensional persistence groups.
