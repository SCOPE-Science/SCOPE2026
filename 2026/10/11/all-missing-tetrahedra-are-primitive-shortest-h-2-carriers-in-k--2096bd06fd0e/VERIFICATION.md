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

The standalone `verify.py` contains the complete standard 36-facet presentation of Kühnel's nine-vertex triangulation.

It reconstructs the face vector \((9,36,84,90,36)\), verifies three-neighborliness, and enumerates all \(\binom94=126\) four-sets. The \(90\) present tetrahedra have zero tetrahedral-boundary class; the \(36\) missing tetrahedra all give the unique nonzero class in \(H_2(-;\mathbf F_2)\).

An explicit integral two-cocycle is then checked on every oriented tetrahedron. It evaluates \(+1\) on \(18\) missing tetrahedral spheres and \(-1\) on the other \(18\), proving every one is a primitive integral class once the published identification \(H_2(K;\mathbb Z)\cong\mathbb Z\) is used.

Finally, all \(9!\) vertex permutations are tested. Exactly \(54\) preserve the facet set. Their carrier support orbits have sizes \(9\) and \(27\). Pushing forward a fixed primitive carrier and re-evaluating the cocycle gives \(27\) automorphisms acting by \(+1\) on \(H_2\) and \(27\) acting by \(-1\), with kernel of order \(27\).

Exact successful output:

`VERIFY_OK f=9,36,84,90,36 H2_F2_dim=1 missing4=36 present4=90 missing4_mod2_nonzero=36 cocycle_nonzero=19 missing4_integral_evals=+1:18,-1:18 aut=54 carrier_orbits=9,27 H2_action=+1:27,-1:27 kernel=27`

All finite claims are exhaustive. No sampled computation is used as an infinite proof.
