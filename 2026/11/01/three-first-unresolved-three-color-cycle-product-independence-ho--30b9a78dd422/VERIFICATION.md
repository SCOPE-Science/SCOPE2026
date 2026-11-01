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

# Exact finite verification

The standalone Python 3 checker `verify_cycle_products.py` requires only the standard library. Execute `python3 verify_cycle_products.py` from the package directory; `verification_output.txt` is the saved output of that same command. All checks are independently repeatable from source; no hidden dataset or other package is required.

For \(\operatorname{Ind}(C_7\times K_3)\), the checker finds 5,281 faces, 2,635 matched pairs, 25,221 directed Hasse incidences, and critical cells \((c_0,c_3,c_4)=(1,4,6)\). Its exact degree-four-to-degree-three Morse matrix is

```
[[-1, 0, -1, -1, 0, -1],
 [ 0, 0,  0,  1, 0,  1],
 [ 0, 0,  0,  1, 0,  1],
 [ 0,-1,  0, -1,-1, -1]]
```

It has rank three and a determinant-minus-one minor on zero-based rows and columns \((0,1,3)\).

For \(\operatorname{Ind}(C_8\times K_3)\), the checker finds 18,721 faces, 9,353 matched pairs, 104,568 Hasse incidences and \((c_0,c_4,c_5)=(1,6,8)\). Its degree-five-to-degree-four Morse matrix is

```
[[ 0,-1, 0, 0, 0,-1, 0, 0],
 [ 0, 0,-1, 0, 0, 0,-1, 0],
 [ 0,-1, 0,-1, 0, 0, 0, 0],
 [ 0, 0,-1,-1, 0, 0, 0, 0],
 [ 0, 0, 0, 0,-1, 0,-1, 0],
 [ 0, 0, 0, 0,-1,-1, 0, 0]]
```

It has rank five and a determinant-plus-one minor on rows \((0,1,2,3,4)\) and columns \((1,2,3,4,5)\).

For \(\operatorname{Ind}(C_{10}\times K_3)\), the checker finds 216,257 faces, 108,121 matched pairs, 1,502,070 Hasse incidences and \((c_0,c_5,c_6)=(1,8,6)\). Its degree-six-to-degree-five Morse matrix is

```
[[ 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 1],
 [ 0, 0, 1,-1, 0, 0],
 [ 1, 0,-1, 0, 0, 0],
 [ 0, 1, 0, 0,-1, 0],
 [ 0, 0, 0, 0, 1,-1],
 [ 0,-1, 0, 1, 0, 0],
 [ 0, 0, 0, 0, 0, 0]]
```

It has rank five and a determinant-plus-one minor on rows \((1,2,3,4,5)\) and columns \((0,1,2,3,4)\).

Independent mod-two reductions of the **full original** simplicial boundary complexes agree with the reduced homology dimensions in every degree. The theorem about the integral homotopy type follows from integral Morse-boundary matrices and the cellular attaching-map/Hurewicz argument, not from mod-two homology. The finite checker does not prove any all-length assertion. Independent external auditing has not been performed.
