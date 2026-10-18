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

# Verification of the graph edge-averaging generating-radius formula

The universal argument is in `RESULT.md`: (i) convex coefficients force norm-attainment on same-sign edge faces; (ii) extreme points of those faces are the allowed signings; (iii) the dual support function follows by a cheapest sign flip; (iv) the lower support inequality and a proper-coloring witness establish the optimal radius. These steps cover every finite simple graph, including isolates and disconnected components. The support-function equality handles dual zero coefficients.

Execute `python checks/check_graph_averaging.py` using Python 3 and the standard library. In the reviewed run, the script printed:

```
n=2: all nonempty labeled simple graphs checked
n=3: all nonempty labeled simple graphs checked
n=4: all nonempty labeled simple graphs checked
n=5: all nonempty labeled simple graphs checked
PASS: 1094 graphs, 157849 exact support inequalities, and all bipartite sharp witnesses
```

The script exhausts graph labels through five vertices, not all real dual vectors and not all graph orders. Thus the proof's all-dimensional quantifiers come from the symbolic argument, not the finite test. The test does not address complex scalars, endpoint edge weights, or multiple-edge/hyperedge variants. Independent external validation has not been performed.
