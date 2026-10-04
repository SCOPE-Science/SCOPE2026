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
The checker uses exact rational arithmetic only.

It implements depth-one Anderson acceleration in the affine-combination form
\[
x^{(k+1)}=(1-s_k)g(x^{(k-1)})+s_kg(x^{(k)}),
\]
with
\[
s_k=-\frac{f_{k-1}^{\mathsf T}(f_k-f_{k-1})}{\|f_k-f_{k-1}\|_2^2}.
\]

At \(\varepsilon=1/200\), it verifies strict positivity of the first five nonzero iterates and the exact negative sixth-coordinate fraction reported in RESULT.md.

It independently reconstructs the scaled limiting recurrence and checks the exact states through
\[
S_6^{(0)}=
\left(
\frac{2235098625}{2165688769},
-\frac{143897600}{2165688769}
\right).
\]
All limiting least-squares denominators used in the continuity argument are checked to be nonzero.

Finally, several rational scalar affine contractions are replayed to verify that depth-one Anderson lands exactly at the positive fixed point at its first accelerated step. The open-family statement itself is proved analytically by rational dependence and continuity, not by enumeration.
