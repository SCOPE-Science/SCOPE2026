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

# Reproducible finite verification

Execute `python3 verify_cube.py` using Python 3 and its standard library. The program constructs the 24 arcs by binary XOR and checks a complete 6,497-face enumeration by two different methods. It checks the acyclic face matching on all 29,160 cover incidences, the 99 exact integer Morse boundaries, and direct binary simplicial boundary ranks. The accepted output marker is `VERIFIED_Q3_BIDIRECTED_MULTIPATH_INTEGRAL_HOMOLOGY`.

The face hash uses sorted integer masks, serialized as three little-endian bytes each, and is `9115bf451a1470e640cb1d07f243f5c9f16cf7e1276d1c5a9034acc5e9a6a102`. The matching has 3,199 pairs and 99 critical augmented cells. Acyclicity follows from a complete topological ordering, not merely a sample of gradient paths. The integer Morse differential vanishes in every degree. This is a full finite proof for the stated graph, not an extrapolation to other parameters.

Separate mod-two chain ranks are `1,23,193,735,1275,840,132` in degrees zero through six. These are a consistency check and do not by themselves exclude odd-order torsion. The integer cancellation does exclude all torsion. The 2-connectivity conclusion follows from the resulting nonaugmented CW Morse model; higher homotopy attaching maps were not verified. Independent mathematical validation has not been performed.
