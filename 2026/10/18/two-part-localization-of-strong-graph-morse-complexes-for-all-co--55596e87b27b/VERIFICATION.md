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
# Reproduction and verification

Run `python3 verify_faces.py` and `python3 verify_collapses.py` from the directory containing both scripts. Compare their output to `verification_faces.txt` and `verification_collapses.txt`. Both scripts use only the Python 3 standard library; neither reads external research data or makes network requests.

`verify_faces.py` enumerates every vertex permutation for each listed finite graph, independently generates its strong matching, closes under faces, constructs the asserted bipartite star/flap generators, checks exact equality of simplicial face sets and computes all mod-two boundary ranks. `verify_collapses.py` starts from the proposed facet complex, applies each claimed elementary collapse step and explicitly checks that the removed lower face has only its prescribed upper coface. It checks the final graph's vertex and edge count and first Betti prediction on ten graph choices; no precomputed matching certificate is trusted.

The tested vectors include tripartite graphs with and without singleton parts, four-part graphs, the all-singleton boundary and representative bipartite cases. A finite verification is not an exhaustive proof over all part-size vectors; the general argument is in `RESULT.md`. The program does not independently assess bibliographic novelty or scientific importance. Independent audit: not performed.
