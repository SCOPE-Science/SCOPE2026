---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Directly generated all 3^7 point assignments and allowable line choices using Fano difference set (0,1,3); independently constructed the 2106-state recolouring graph, exactly 6804 edges, 126 degree-zero states and the full degree polynomial 126t^4+420t^5+504t^6+588t^8+252t^9+84t^11+6t^14. All-root BFS, one root for each of 1980 mobile states, returned eccentricity 21 for every vertex. Flag bijection derives from sum_i binom(n_i,2)=7 and pair uniqueness; 3-point-colour extension forces the 126 flag states, whereas at most two point colours permit integral heights. The exact monotone height-transform lemma of Cereceda–van den Heuvel–Johnson (2007 preprint Lemma 5) supplies connectedness and the geodesic upper bound; exhaustive BFS supplies sharp metric independent of that lemma.

## originality

PASS

Qualified best-of-knowledge comparison of actual statements with primary literature and published mathematical results; not a claim of exhaustive historical-priority verification.

## value

PASS

A complete natural finite reconfiguration classification for the smallest cubic symmetric cage: exact geometric characterization of all 126 ergodicity obstructions and a sharp 21-move metric for the sole mobile sector. It can benchmark finite-state reconfiguration and colouring dynamics, not merely count proper colourings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
