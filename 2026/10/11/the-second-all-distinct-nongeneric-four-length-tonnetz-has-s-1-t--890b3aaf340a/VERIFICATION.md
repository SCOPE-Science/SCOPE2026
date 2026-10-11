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

The bundled `verifier.py` reconstructs \(\mathrm{Tonn}^{11,4}(1,2,3,5)\) directly from the facet formula. It checks the face vector \((11,55,110,66)\), \(\partial^2=0\), exact rational boundary ranks \(10,44,65\), and explicit maximal-rank determinants \(1,-1,1\). The same ranks are recomputed modulo \(2,3,5,7,11,13\).

For the link of vertex \(0\), the verifier reconstructs face vector \((10,30,24)\) and checks a staged matching with \(30\) pairs. The directed Hasse graph of the matching is acyclic and the only critical cells are one vertex and three triangles, proving \(\operatorname{Link}_T(0)\simeq\bigvee^3S^2\). Cyclic translation is then exhaustively checked to preserve the complete facet set, so all vertex links are isomorphic.

The verification establishes only the stated finite homology and vertex-link claims. It does not compute the whole-complex homotopy type, fundamental group, or cohomology ring.
