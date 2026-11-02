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

The proof of the infinite assertion is the parameter-uniform case analysis in RESULT.md, not the finite experiments. The latter are useful reproducibility and regression checks of both point/line sorts, the generalized-quadrangle axioms, and exact first-order signatures.

With Python 3 and a C++17 compiler, run from the package directory:

```
python3 generate.py
c++ -O3 -std=c++17 verify.cpp -o verify_gq
./verify_gq w2.txt w3.txt qminus2.txt qminus2dual.txt
```

The exact captured standard output is in `verification_output.txt`. The generated text input files are deliberately not embedded because `generate.py` constructs them deterministically and completely. The C++ source computes all atomic diagrams of four selected vertices and recursively interns their extension-type sets at the preceding tuple levels. The four models have point/line orders \((2,2),(3,3),(2,4),(4,2)\); the verifier checks their full incidence axioms. The code does not purport to certify all finite generalized quadrangles, and it does not compute full rank-five equivalence classes. The rank-five witnesses are explicit degree-threshold sentences proved in RESULT.md.
