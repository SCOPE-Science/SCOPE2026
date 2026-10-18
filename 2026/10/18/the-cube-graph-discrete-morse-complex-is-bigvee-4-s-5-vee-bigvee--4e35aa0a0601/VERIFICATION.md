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

Run `python3 verify_cube_homotopy.py` using Python 3 and only its standard library. The script reconstructs all arcs and faces of the cube Morse complex, checks face-set equality between all 4-to-the-8 tail assignments and all 3-to-the-12 edge states, computes the exact face vector and Laplacian check, constructs the deterministic matching, and topologically sorts the entire reversed-matched Hasse diagram. It then calculates the complete signed integral Morse differential with both a recursive gradient projection and a separately written forward propagation, tests entrywise equality, and carries out explicit invertible integral Smith cancellations. The verifier exits without `VERIFY_OK` if any assertion fails.

Observed completed run:

```
VERIFY_OK faces=23625 hasse_incidences=124200 matching_pairs=11698 critical5=47 critical6=182 morse_shape=47x182 morse_nonzero=334 unit_smith_factors=43 smith_zeros=4 H5_rank=4 H6_rank=139 matrix_sha256=c5d099140b205ee3bc820da7ae1a15884d4571827ae031d129773635bc82fdd2
```

The integral cancellation algorithm counts 43 unit pivots and asserts the entire remaining four-row by 139-column block is identically zero. Hence the calculation excludes undetected nonunit Smith factors at this matrix size; no claim is extrapolated to other hypercubes. Discrete-Morse acyclicity, cellular attachment degrees, and the homotopy passage from the degree matrix follow from the proof and stated standard theorems. This is a finite exact certificate, not an independent external audit.
