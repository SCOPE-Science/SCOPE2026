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

Run:

```text
python3 verify.py
```

The script uses only the Python standard library. It constructs the generalized Petersen graph \(G(8,3)\) directly from its defining outer, spoke, and inner-star edges; computes all shortest-path distances; and exhaustively tests every nonempty subset of the \(16\) vertices at the relevant scales.

The expected exact checks are:

- graph size \((16,24)\) and diameter \(4\);
- scale \(1\) face vector \((16,24)\), hence cycle rank \(9\);
- scale \(2\) face vector \((16,72,112,48)\) and \(248\) nonempty faces;
- \(118\) matched face-coface pairs under the fixed toggle order, leaving critical-cell counts \((1,0,9,2)\) in dimensions \(0,1,2,3\);
- complete acyclicity of the oriented Hasse diagram;
- exact Morse boundary from the two critical \(3\)-cells to the nine critical \(2\)-cells equal to zero;
- scale \(3\) distance-\(4\) graph equal to eight disjoint pairs, with face vector \((16,112,448,1120,1792,1792,1024,256)\), the boundary of the \(8\)-cross-polytope;
- scale \(4\) complete simplex.

`verification_output.json` is the captured deterministic output from the packaged verifier.

Limits: the script certifies this labeled graph and this exact claim only. It does not verify a family theorem, a literature novelty claim, or any independent audit status.
