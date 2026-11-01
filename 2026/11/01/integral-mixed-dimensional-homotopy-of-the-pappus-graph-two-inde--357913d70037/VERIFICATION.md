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
# Computational reproducibility

Run `python3 verify_pappus_ind2.py` using the Python standard library only. The included `verify_pappus_ind2.txt` gives the exact recorded output, ending in `ALL_CHECKS_PASS`.

Verified graph: 18 vertices, 27 edges, cubic, connected, bipartite, girth six; full nonempty face vector `(18,153,762,2394,4806,6027,4428,1728,308,27)` totaling 20,651. The recursive face generator agrees with the direct validity test over all 262,144 subsets. The finite matching contains 10,320 pairs, nine critical 5-cells, one critical 6-cell, one critical vertex; topological sorting checks all 20,651 nodes and all 120,222 directed face incidences. The integral 6-to-5 Morse cellular degree vector is exactly `(0,0,0,0,0,0,0,0,0)`; its memoized recursive expansion visits 933 faces. Independently, mod-two full simplicial boundary ranks are `(17,136,626,1768,3038,2980,1447,281,27)` for dimensions 1 through 9.

The discrete Morse matching and integer attaching-degree calculation, together with Hurewicz in degree five, prove the stated integral homotopy equivalence for this one finite complex. The mod-two ranks do not by themselves establish an integral homotopy type. No infinite census, unpublished independent inspection, or equivariant homotopy classification is asserted.
