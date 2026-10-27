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

# Verification of the characteristic-three plane-sextic classification

The included `verify.py` is standalone Python 3 code using only the standard library. Execute `python3 verify.py` in the directory containing this file and the program. It checks polynomial identities exactly in a sparse coefficient ring modulo three; it also checks the ten incidence points of the conic and four lines and all 24 rational projective symmetries preserving the defining sextic.

A complete enumeration of the finite projective planes over the finite fields of orders 3, 9, and 27 produces respective sextic rational-point counts 10, 40, and 130, agreeing with the formula \(5q-5\). The finite-field implementations use the irreducible polynomials `t`, `t^2+1` and `t^3-t+1` over \(\mathbf F_3\), and each projective point is enumerated with a unique normalized representative.

All computations are exact. The symbolic factorization, incidence proof, and projective group argument in `RESULT.md` establish the geometric and infinite-extension statements; the finite enumeration is corroboration, not proof of infinitely many cases. The program does not verify stable reduction, alternative integral models, or possible unindexed prior literature. Independent audit and validation were not performed.
