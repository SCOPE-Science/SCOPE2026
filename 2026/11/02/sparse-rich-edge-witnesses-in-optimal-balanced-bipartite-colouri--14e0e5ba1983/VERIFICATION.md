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

# Verification and scope

The result is proved for every integer \(n\ge2\) by elementary graph-colouring and palette arguments in `RESULT.md`. Every occurrence of "neighbor" in the claim uses adjacency of **distinct** edges. The reference value \(\chi'_{\mathrm{rn}}(K_{n,n})\) is also obtained from a rich-edge palette lower bound plus the explicit constructions (and a four-cycle exception).

The standalone file `verify.py` directly builds coloured edge matrices and tests properness and richness by scanning each adjacent-edge neighbourhood. It checks exactly \(83\) constructed cases covering balanced orders through \(11\), all possible large-order two-star splits in that range, and control examples. It additionally enumerates normalized proper five-colour matrices for \(K_{3,3}\), finding minimum four rich edges among valid colourings, and rejects a three-colour four-cycle test for violating open rich-neighbor domination. Output from the executed program:

```
DIRECT_EXHAUSTION_3x3 4 rich edges, 36 normalized witnesses
CONSTRUCTION_TESTS_OK 83
VERIFY_OK
```

The exhaustive five-colour test fixes the first row to distinct colours \(0,1,2\) by global colour renaming; this is complete under that normalization. The finite diagnostics do not certify historical priority and do not replace the all-order proof. The classifications of rich-edge graphs at all palette sizes, or of all optimal-palette colourings, are not asserted.
