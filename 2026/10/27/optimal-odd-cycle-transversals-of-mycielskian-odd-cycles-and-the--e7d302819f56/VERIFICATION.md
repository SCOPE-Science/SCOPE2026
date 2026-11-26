---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Every transversal must delete an original. If the apex is deleted, a missing original can be replaced by its shadow in the odd cycle, and two nonadjacent missing originals can both be replaced. These obstructions leave exactly A_i and B_i among triples deleting the apex. For either retained original path, any remaining shadow with two original neighbors has neighbors of the same alternating color, proving sufficiency. If the apex is retained, all surviving shadows have the same color, forcing any original with a surviving shadow neighbor to share the apex color. Two deleted shadows can make at most one original flexible; with one deleted original the remaining path has at least four vertices, so one flexible vertex cannot meet all original edges. With two or three deleted originals there is at most one deleted shadow and hence no flexible original: the retained originals must be independent. The cycle independence bound excludes two original deletions and permits three only at n=5, where the five complementary independent pairs give exactly R_i and the forced coloring works. With at most two total deletions, the same replaced cycle or forced-color obstruction persists. Exchanges follow by intersecting triples. For n=2k+1>=7 each A has two B partners at every distance 1..k and one at k+1; distinct B's at cyclic separation t have exchange distance t+1 via their incident A edges. Together with the A-cycle this gives the stated shells of unordered pairs and common eccentricity. At n=5 the A,R Petersen core contributes 15 pairs at distance one and 30 at distance two; each B contributes (2,2,1) to distances to A and (0,2,3) to R. The ten B-B pairs split equally at distances two and three. This yields (25,55,25) and every vertex has a distance-three partner. Independent replay (python3 -B /workspace/branches/independent_replay.py 5) exhaustively enumerated deletions through size three and all exchange distances for odd n=5..19, confirming those cases and the exact distance histogram. The frozen verifier prints but does not assert that histogram, and its out-of-scope n=3 check stops at size two; neither limits the deductive result.

## originality

PASS

Pass for the complete family-wise minimum transversal classification and the exchange metrics, including the Petersen exception in the ordinary Mycielskian of C5. The construction, graph bipartization concept and related scalar OCT bounds are not credited as novel. Compared statements on the closest same-invariant and same-graph work do not establish the submitted classification or metric; the conclusion is bounded by inspected evidence.

## value

PASS

A scalar bipartization number does not tell how many minimum choices exist, whether one can move between them without increasing cost, or how far apart they can be. This classification answers those questions exactly for a standard family and identifies a real small-cycle change of shape: the larger odd cycles have an exchange cycle decorated by triangles, while C5 also admits apex-retaining minimizers forming a Petersen core with the A layer. The full distance distributions record that difference and provide concrete reconfiguration benchmarks, not just verification of a known count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
