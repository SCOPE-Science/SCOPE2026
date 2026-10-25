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

# Verification details

Exact symbolic diagnostics: running `python check_chazy_discontinuous.py` produced `PASS: 18 exact algebraic identity checks`. Both half-space formulas and both crossing orientations were checked by SymPy. These finite algebraic assertions do not prove global recurrence, uniqueness or the validity of the prior existence theorem; those require the explicit disk/annulus coarea-flux proof and the published Theorem 1.

Critical proof conditions: on \(H=-h<0\), \(x=0\) entails \(y^2=2h>0\); hence all switches are transverse and there is no sliding. Both saltation shears have determinant one and preserve the energy covector, permitting the surface-divergence theorem across a cut along the switching set. Strict contraction is conditional on an existing periodic orbit, existence being provided by the 2023 source.

This is a self-review, not an independent mathematical validation. Full text of one relevant 2024 article could not be inspected. Reproduce with Python and `sympy` as declared by `requirements.txt`.
