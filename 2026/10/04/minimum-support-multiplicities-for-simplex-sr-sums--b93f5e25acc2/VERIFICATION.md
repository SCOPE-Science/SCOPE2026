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
`artifacts/verify.py` uses only the Python standard library.

It constructs the projective point set
\[
\operatorname{PG}(V_1\oplus V_2)
\setminus
\left(\operatorname{PG}(V_1)\cup\operatorname{PG}(V_2)\right)
\]
and assigns every point multiplicity \(q-1\).

For
\[
(q,k_1,k_2)=(2,2,3)
\]
and
\[
(q,k_1,k_2)=(3,2,3),
\]
the script enumerates every \(r\)-dimensional message subspace in reduced row-echelon form for every
\[
1\le r\le5.
\]
For each subspace it computes the support directly from the projective columns and records the exact minimum and its multiplicity.

The replay verifies the binary hierarchy
\[
(10,15,18,20,21)
\]
with minimizer counts
\[
(21,42,42,21,1),
\]
and the ternary hierarchy
\[
(138,184,200,206,208)
\]
with minimizer counts
\[
(104,624,624,104,1).
\]

It independently evaluates the closed formula
\[
M_r=
\left[{k_1\atop a_r}\right]_q
\left[{k_2\atop b_r}\right]_q
\left[{k_1-a_r\atop c_r}\right]_q
\left[{k_2-b_r\atop c_r}\right]_q
|\mathrm{GL}(c_r,q)|
\]
and checks equality in every case.

The finite replay verifies the implementation and representative instances; the all-\(q\), all-dimension theorem is proved symbolically in `RESULT.md`.

Successful replay prints `VERIFY_OK`.
