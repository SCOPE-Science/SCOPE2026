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

The accompanying `verify.py` is standalone except for SymPy. Running `python verify.py` completed 144 exact assertions: four symbolic determinant identities, 112 exact-rational full-matrix comparisons over graph orders three through eighteen, sixteen exact ranks at the uniform edge weight, and twelve signed-boundary nullity checks. The computational checks cover only these finite instances, whereas the proof's reflection/resultant factorization works for all integer orders at least three and all real or complex exceptional weights.

The Krylov determinant is formed from the positive Laplacian. For the continuous-time dynamics with negative Laplacian, controllability ranks are unchanged. No full-infinite-parameter numerical certification or independent audit is claimed.
