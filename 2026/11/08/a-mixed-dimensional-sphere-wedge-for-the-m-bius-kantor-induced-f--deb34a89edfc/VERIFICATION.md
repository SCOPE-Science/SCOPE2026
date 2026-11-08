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
# Reproducibility and verification

Run `python3 verify.py` (Python 3 standard library, no external dependencies). The program starts from an explicit graph \(\operatorname{GP}(8,3)\) with sixteen labeled vertices and 24 edges. It tests every possible vertex subset for induced acyclicity by both union–find and independently traversed connected components, then enumerates 50,996 nonempty faces. It constructs the deterministic 25,475-pair Morse matching and verifies complete acyclicity over 375,040 directed Hasse covering relations, with 50,996 visits in a topological sort. The critical-cell counts are \((c_0,c_8,c_9,c_{10})=(1,8,33,4)\).

The signed recursive gradient projection produces a \(8\times33\) integer boundary matrix in degree nine and an all-zero \(33\times4\) boundary in degree ten. Zero-based columns 21, 3, 2, 1, 5, 10, 12, 18 of the former have determinant \(-1\), giving integral surjectivity. A nonzero differential with torsion or an unexamined higher attaching map could not be ignored: here the CW model has no cells in positive degrees below eight, so the integral degree groups classify the nine- and ten-cell attaching maps after cellular cancellation. Consequently the result is a full integral homotopy equivalence.

`verification_output.txt` records every critical bitmask and the full \(8\times33\) matrix, allowing an exact replay comparison. The calculations prove only this finite sixteen-vertex graph. The verification is reproducible research evidence, not an independent audit or proof of publication priority.
