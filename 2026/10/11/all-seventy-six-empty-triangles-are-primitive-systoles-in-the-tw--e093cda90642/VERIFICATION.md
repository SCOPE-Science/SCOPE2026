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

`verify.py` embeds all \(60\) facets and uses only the Python standard library.

It reconstructs
\[
f=(12,66,144,150,60).
\]
After contracting an eleven-edge spanning tree, the graph cycle lattice has rank \(55\). Integral unimodular reduction of the \(144\) triangular-face relations produces \(54\) unit diagonal entries and a zero residual block, proving
\[
H_1(K;\mathbb Z)\cong\mathbb Z.
\]

The explicit cocycle in the verifier annihilates every facial relation and evaluates to a unit on a triangular cycle. It therefore gives exact integral generator coordinates. Exhaustion of all \(220\) three-vertex subsets finds \(144\) facial triangles and \(76\) empty triangles. Every empty triangle evaluates to \(+1\) or \(-1\), hence is primitive.

The automorphism backtracking considers every vertex permutation compatible with triangular-face membership and verifies the complete facet set at its leaves. It finds exactly \(96\) automorphisms. Their carrier-set orbits have sizes \(12,48,16\), and their induced actions on an oriented primitive generator split \(48\) by \(+1\) and \(48\) by \(-1\).

Exact successful output:

`VERIFY_OK f=12,66,144,150,60 H1_Z=Z all_triangles=220 facial3=144 empty3=76 all_empty3_primitive=yes oriented_pairings=+1:30,-1:46 aut=96 carrier_orbits=12,48,16 reps=123|126|148 H1_action=+1:48,-1:48`
