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

The standard-library checker `verify_icosidodecahedron.py` and explicit `collapse_certificate.json` are complete standalone dependencies. From their directory execute:

```sh
python3 verify_icosidodecahedron.py collapse_certificate.json
```

It reconstructs the graph from twelve original icosahedral vertices, confirms the rectification, all thirty shortest-path shell profiles, maximal distance five, twenty disjointly edged graph triangles, and all 15 antipodal pairs. It exhaustively enumerates every simplex at radii one, two, and three, checking their exact dimension-indexed face vectors.

At radius two, the dimension-indexed face vector is `(30,180,380,330,102)`; at radius three it is `(30,300,1340,3150,4374,3800,2100,720,140,12)`. It replays 7472 plus 426 certificate pairs. For each, it checks present faces, codimension one, a unique surviving immediate coface, maximality, and exact equality with the target at completion. The final surface has face vector `(30,84,56)`, all edges in exactly two triangles, connected vertex links, connected one-skeleton, and Euler characteristic two. Any false certificate entry raises an assertion. The recorded actual execution ends with `ICOSIDODECAHEDRON_RIPS_COLLAPSE_CERTIFICATE_VERIFIED`.

**Limits.** The graph-metric and inclusivity convention are necessary. No perturbation/general-family claim and no independent audit is included.
