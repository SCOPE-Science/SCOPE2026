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
# Reproducibility and limitations

The exact finite result follows from the exhaustive augmentation-and-isomorphism algorithm in `census_stdlib.py`; the independent `census_networkx.py` reproduces it from NetworkX graph-atlas seed types. Execute `python3 census_stdlib.py` and `python3 census_networkx.py` from a directory containing the scripts. The first requires only Python 3; the second was tested against NetworkX 3.6.1. Check parsed JSON outputs against `census_stdlib_output.json` and `census_networkx_output.json`. Both independently report 188 unlabeled connected cactus graphs of order eight and two refinement-orbit failures with 9 and 10 edges. For orders 1 to 7, the dependency-free program confirms zero failures over 1,1,2,4,9,23,63 graph types.

The programs enumerate only graphs of order at most eight. All automorphism membership tests are exact bijection searches; no probabilistic graph-isomorphism oracle or approximate floating-point calculation is used. The two implementations are evidence of reproducibility, not independent mathematical peer review. No claim of completeness beyond eight vertices is made.
