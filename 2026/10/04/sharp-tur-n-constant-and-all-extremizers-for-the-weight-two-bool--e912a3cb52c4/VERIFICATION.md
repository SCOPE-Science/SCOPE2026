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

The proof uses no numerical approximation. Positive definiteness is checked symbolically through the finite Fourier transform
\[
Q(s)=1+\sum_{i<j}a_{ij}s_i s_j.
\]
The upper bounds follow from exact slice averages, and equality classification follows from exact linear identities on the zero slices.

The accompanying `artifacts/verify.py` uses only exact rational arithmetic. For dimensions \(2\) through \(10\) it exhausts all sign characters for the radial extremizers, checks the equality-slice matrix ranks predicted by the proof, and checks explicit nonradial even-dimensional extremizers. Its expected output is:

`VERIFY_OK dimensions=2..10 radial_values=exact odd_unique_ranks=exact even_extremal_dimensions=exact nonradial_examples=exact`

The computation is a finite corroboration only. It does not certify the infinite family; the all-dimensional statement rests on the spanning lemmas and the algebraic identity \(Q(s)=ST\).
