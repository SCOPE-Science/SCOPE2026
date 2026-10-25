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

# Reproducibility and verification

Run `python3 verify_rectangular_tori.py` using Python 3 and the standard library. The script constructs graph-metric adjacency independently of the predicted facet formula, enumerates every maximal clique, checks short-fiber intersections, computes exact simplicial boundary ranks over the two-element field, and separately verifies each claimed elementary free-face collapse of the baseline complex against every remaining coface.

The executed checks include \((m,n)=(5,5),(5,6),(6,6),(5,7),(6,7),(7,7),(5,8),(6,8),(7,8),(8,8),(5,9),(6,9),(7,9),(5,10),(6,10)\). For \((5,6)\), the verified face vector is \((30,180,340,210,36)\) and the reduced mod-two Betti vector is concentrated in degree two with rank fifteen. For \((5,7)\), the corresponding vector is \((35,210,385,245,42)\), with reduced Betti ranks one in degree one and seven in degree two. For \((6,7)\), they are \((42,252,434,252,42)\), with reduced ranks one and fourteen in those degrees. The script also verifies \(9mn\) individual collapses for eight separate parameter pairs including \((5,5)\) and \((6,6)\).

Outputs `VERIFY_OK` and `COLLAPSE_VERIFY_OK` were observed. Tests do not establish the infinite family; the proof uses the exact mixed-edge link and its parameter-independent classification, followed by uniform free-face and CW attachment arguments. The assertions concern ordinary integral homotopy type; finite-field calculations alone would be insufficient to establish it. No external or independent audit has been performed.
