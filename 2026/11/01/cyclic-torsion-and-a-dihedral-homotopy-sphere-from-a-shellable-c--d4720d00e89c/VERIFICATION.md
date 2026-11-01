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

Run `python verify_quotients.py` with Python 3 and SymPy. No other file inputs are required. Compare the printed output with `verification_output.txt`. The code enumerates every independent vertex subset, checks a complete list of 80 facets and an explicit shelling sequence, constructs every barycentric face flag, and uses the specified cyclic/dihedral actions to compute integral quotient-chain boundary matrices. Boundary compositions and Smith factor patterns are checked by assertions.

The two quotient cell vectors are `(20,134,234,120)` and `(16,73,117,60)`; the nonzero Smith factors are, by degree, `{1:19}`, `{1:114,16:1}`, `{1:119}` and `{1:15}`, `{1:58}`, `{1:59}`. Exact integer Smith forms are used, not estimates from field ranks. Reflection-fixed witnesses are the vertex `(0,)` and the edge `(2,15)` under parity-opposite reflections. The rotation freeness proof, orbit-space fundamental-group theorem and sphere recognition are explained independently of the numerical script in `RESULT.md`.

**Scope.** This verification is not a proof of a homeomorphism with a particular lens space; the first orbit space is identified only through its displayed homology and fundamental group. The finite computations can be checked mechanically, but independent mathematical audit is not performed.
