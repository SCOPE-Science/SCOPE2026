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

## Reproduction

Execute `python3 verify_morse.py` for the combinatorial face enumeration, explicit 6,934 pairs, 70,536 oriented Hasse incidences, full DAG sort and four zero signed integral boundary coefficients. Execute `python3 verify_chains.py` for an independent construction of the graph from Euclidean coordinates and exact mod-two boundary ranks.

The two programs have been run successfully on the embedded versions. `verify_morse.py` reports critical bitmasks `8388608`, `2163272`, `99426`, `807456`, `2183304`, `3146889`, in dimensions \(0,4,5,5,5,5\). `verify_chains.py` reports rank sequence `23,205,899,2041,2326,1206,234` and reduced mod-two Betti vector `0,0,0,0,1,4,0,0`.

## Scope of verification

The integer attaching-map conclusion comes from the signed Morse boundary calculation. Mod-two ranks independently support the homology pattern but are not a substitute for integral homotopy verification. The calculation is finite and exhaustive on the stated 24-vertex graph; it makes no claim for other graphs or a complete literature census. Independent scientific validation is not recorded.
