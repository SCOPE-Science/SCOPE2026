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

## Reproduce the finite classifications

Using Python 3 with SymPy 1.14 (or a compatible exact Gröbner implementation) and a C++17 compiler, run these commands in the directory of the extracted files:

```sh
python3 verify_pencils.py
python3 verify_transversality.py
g++ -O2 -std=c++17 -o base_spectra verify_base_spectra.cpp
./base_spectra < representatives.txt > observed_base_spectra.txt
cmp observed_base_spectra.txt expected_base_spectra.txt
```

The first command must report `SMOOTH 144 PENCILS 804`, `ORBITS 13`, group orbit sizes ten 72, two 36, one 12. The second must finish with `ALL 13 REPRESENTATIVE PAIRS GEOMETRICALLY TRANSVERSE`, after checking every one of their 52 affine charts by Jacobian ideal. The third produces the base-point counts over \(\mathbf F_{2^r}\) for every \(1\le r\le8\); byte-for-byte comparison with the included expected output is required. All four automated reproducibility steps above passed against the attached source files.

The source code uses only exact arithmetic. Over each affine chart, smoothness is the condition that the ideal of the equation and its two partial derivatives is the unit ideal in characteristic two. Geometric base transversality is verified by adjoining the pairwise Jacobian determinant to the ideal of the two defining sections. Degree-eight Bézout bounds guarantee extension-degree completeness once eight distinct geometric base points have been found. No field extension beyond degree eight is inferred by finite testing alone.

## Limitations

The tested scope is precisely the 511 nonzero binary sections of \(\mathcal O(2,2)\) on the split quadric, and the 804 qualifying two-dimensional subspaces. The computations do not address pencils over larger base fields, all geometric fibers of the pencils, or abstract isomorphism classes of genus-one curves. The mathematical result has been reviewed in this package, but no independent audit has been performed.
