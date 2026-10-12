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
The packaged checker `artifacts/verify.py` represents \(S_3\) as the six permutations of three letters.

It tests all
\[
6^6=46656
\]
set maps \(\mathcal A:S_3\to S_3\) against Das's defining identity
\[
\mathcal A(g)\mathcal A(h)\mathcal A(g)^{-1}
=
\mathcal A(\mathcal A(g)h\mathcal A(g)^{-1}).
\]

It independently tests the equivalent generated-image subgroup condition
\[
\mathcal A(khk^{-1})=k\mathcal A(h)k^{-1}
\qquad
(k\in\langle\mathcal A(S_3)\rangle).
\]

The exhaustive accepted-map counts are
\[
129
\]
overall and
\[
51
\]
pointed.

The generated-image subgroup counts are
\[
1,\quad45,\quad80,\quad3
\]
for subgroup orders
\[
1,\quad2,\quad3,\quad6,
\]
and
\[
1,\quad21,\quad26,\quad3
\]
in the pointed case.

The checker then computes conjugation by all automorphisms of \(S_3\). It obtains
\[
60
\]
orbits overall and
\[
25
\]
pointed orbits.

The full orbit-size distributions are
\[
6\times1,\quad39\times2,\quad15\times3
\]
and, for pointed maps,
\[
6\times1,\quad12\times2,\quad7\times3.
\]

The checker returns `VERIFY_OK`.

The finite search is exhaustive and serves as an independent replay of the conceptual proof.
