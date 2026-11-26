---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Two vertices on the same shore have a common neighbor (b_n or a_1); an opposite-shore nonadjacent pair has distance three via a_1,b_n. Thus a geodesic with three selected edges must have length three, and orienting from B to A gives b_j−a_ell−b_k−a_i with ell≤j<i≤k. The map a_i b_j ↦ {i,j+1} is a bijection. Every sorted triangle p<q<r lifts to b_(q−1)−a_p−b_(r−1)−a_q with nonadjacent endpoints, so the image of a feasible set is triangle-free and Mantel gives the upper bound. For a cut, three crossing pairs along the displayed geodesic would require alternating colors at ell,j+1,i,k+1; if j+1=i it is impossible, otherwise these are four distinct increasing positions. Conversely any alternating four positions p<q<r<s give the forbidden crossing pairs {p,q},{p,s},{r,s}, lifting to a geodesic. This is equivalent to at least four runs. A balanced two-run cut therefore attains the bound, and Mantel equality forces every maximum to be such a balanced cut with at most three runs. Connectivity of the complete bipartite image determines the partition up to reversal of colors. With positive counts x,y there are 2+(x−1)+(y−1)=n+1 labeled strings, with complementation dividing by two only when the color counts are equal. The proof covers n=2 and uses twin-free half-graph adjacency, not general chain graphs. The frozen code was inspected, not executed. Independent BFS predecessor recovery and branching over feasible edge subsets (`python3 -I /workspace/checks/4.py`) recovered all optimizer sets through n=6, equal to the predicted cut images, with respective counts 3,2,5,3,7; see /workspace/checks/4.log. The finite check is corroborative.

## originality

PASS

The supported distinct content is the sharp half-graph value together with the exact cut/run characterization of all optimizers and its count. The inspected prior results use different graph families or position parameters, or give general methods without this equality case. This is a best-of-knowledge verdict subject to the specific unavailable full texts below.

## value

PASS

On the canonical twin-free chain graph, the result goes beyond evaluating the invariant: it reduces geodesic avoidance to an ordered extremal condition, identifies every optimum and gives an exact optimizer census. The alternating pattern explains the extra constraint not captured by the Mantel bound alone and makes the complete classification usable directly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
