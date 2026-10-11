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

Run `python3 verify.py`. The script uses only the Python standard library.

It regenerates all 15 duads and 15 synthemes, constructs their incidence graph, and verifies the graph has 30 vertices, 45 edges, and diameter 4. It checks every pairwise distance against the proof's three cases. It then reconstructs the two scale-3 join factors and verifies that each has face vector \((15,45,15)\), that every edge belongs to exactly one triangle, and that each 1-skeleton is connected.

The complete threshold-3 Rips complex is enumerated both from the join description and independently as all cliques of the actual threshold graph; the two face sets are required to agree. Its verified face vector is \((30,315,1380,2475,1350,225)\). Exact elimination over \(\mathbb F_2\) gives Betti vector \((1,0,0,256,0,0)\).

These finite checks validate the concrete combinatorics and provide an independent homology cross-check. The exact homotopy type additionally uses the proved elementary collapses of the two factors and the standard identity \(X*Y\simeq\Sigma(X\wedge Y)\). No result for other generalized quadrangles is inferred.
