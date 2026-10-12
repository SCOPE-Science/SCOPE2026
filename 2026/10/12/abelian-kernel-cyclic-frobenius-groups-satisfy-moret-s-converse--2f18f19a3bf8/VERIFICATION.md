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
The proof is symbolic and uses the Frobenius action on the dual of an abelian kernel.

The packaged checker `artifacts/verify.py` represents finite abelian kernels as products of cyclic groups and verifies six fixed-point-free cyclic actions:
\[
C_9\rtimes C_2,\quad
C_{15}\rtimes C_2,\quad
(C_3\times C_3)\rtimes C_4,
\]
\[
(C_5\times C_5)\rtimes C_3,\quad
(C_3\times C_9)\rtimes C_2,\quad
(C_5\times C_{25})\rtimes C_4.
\]

For every nonprincipal dual character it checks that the complement orbit has full length, forms
\[
N_\theta=\bigcap_h\ker(\theta^h),
\]
computes the predicted induced-character codegree
\[
|K:N_\theta|,
\]
and finds an element of \(K\) with exactly the same prime support in its order.

It also checks all linear complement-character codegrees and the degree-squared identity proving that the inflated and induced families have the correct total size.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.
