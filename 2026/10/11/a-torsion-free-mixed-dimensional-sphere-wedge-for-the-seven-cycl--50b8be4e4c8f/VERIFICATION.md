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

# Finite exact verification

The standalone file `c7k4_verifier.py` requires only Python 3 and regenerates all structures from the graph adjacency rule, not a stored output log. Run:

`python3 c7k4_verifier.py`

Expected terminal success line after all checks:

`VERIFY_OK faces=36068 pairs=18023 critical=1x0+9x3+12x4 incidences=218008 integer_smith=1x6+0 mod2_b3=3 mod2_b4=6`

The exact critical three-cell masks, sorted as integers, are:

`0x30030 0x30050 0x30090 0x50030 0x50050 0x50090 0x90030 0x90050 0x90090`

The exact critical four-cell masks are:

`0x1110220 0x1110440 0x1110880 0x2220110 0x2220440 0x2220880 0x4440110 0x4440220 0x4440880 0x8880110 0x8880220 0x8880440`

With these respective row and column orders, the **complete oriented integral Morse differential** (nine rows, twelve columns) is:

```
-1,0,0,-1,-1,-1,0,-1,0,0,-1,0
0,0,0,0,1,0,0,1,0,0,0,0
0,0,0,0,0,1,0,0,0,0,1,0
0,0,0,0,1,0,0,1,0,0,0,0
0,-1,0,0,-1,0,-1,-1,-1,0,0,-1
0,0,0,0,0,0,0,0,1,0,0,1
0,0,0,0,0,1,0,0,0,0,1,0
0,0,0,0,0,0,0,0,1,0,0,1
0,0,-1,0,0,-1,0,0,-1,-1,-1,-1
```

The vertex labeling, orientations, pairing, directed incidence orientation, signed gradient-path recurrence and integer-only row/column reduction are specified in `RESULT.md` and implemented in the verifier. Six unit pivots and no nonunit pivot are encountered. The complete mod-two boundary-matrix check yields Betti numbers \(b_0=1\), \(b_3=3\), \(b_4=6\), with all other values zero. Crucially, the mod-two check alone would not rule out integral torsion; that conclusion uses the *integer* Morse differential and its verified unit diagonalization. No incomplete enumeration, random sampling, analytic extrapolation or external certification is used.
