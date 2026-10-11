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

# Reproducibility checks
Run `python3 verify_cuboctahedron_cech.py`. The script has no third-party dependencies.

It builds the 12 edge labels of the three-cube from bit differences, constructs the cuboctahedral line graph, verifies degree four and the one-antipode distance profile, forms all even/odd intrinsic Čech facet sets, and checks complete nonempty-face enumerations for integer scales zero through five. It constructs the two explicit vertex-stage discrete-Morse matchings and checks complete Hasse directed acyclicity, obtaining 120 and 547 matched pairs with critical vectors \((1,0,7)\) and \((1,0,0,5)\). The checks cover 732 and 4,644 Hasse incidences, respectively. An independently implemented mod-two boundary elimination yields scale-two ranks \((11,49,48,12)\) and scale-three ranks \((11,55,157,192,108,24)\). The final high-scale checks verify the boundary of the 11-simplex and the full 11-simplex by exact face equality.

These are exhaustive finite computations for the specified graph. Their interpretation as integral homotopy types uses Forman's discrete-Morse CW-complex theorem, including the fact that only one zero-cell and cells of a single dimension at least two remain. They are not a computation of equivariant homotopy groups or a universal classification for all graphs. The literature originality judgment is limited to inspected sources; no independent audit has been performed.
