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

It enumerates all
\[
6^6=46656
\]
set maps
\[
B:S_3\to S_3
\]
and tests
\[
B(g)B(h)
=
B\!\left(gB(g)hB(g)^{-1}\right)
\]
for all \(36\) ordered pairs \((g,h)\).

Exactly eight maps pass.

Their kernel-image size distribution is
\[
(6,1):1,\qquad
(3,2):3,\qquad
(2,3):3,\qquad
(1,6):1.
\]

The checker computes the action of every inner automorphism and obtains four operator orbits of sizes
\[
1,\quad1,\quad3,\quad3.
\]

It computes the standard involution
\[
\widetilde B(g)=g^{-1}B(g^{-1})
\]
and verifies that it swaps the two elementary orbits and the two non-elementary orbits.

For every non-elementary operator the descendant multiplication
\[
g\circ h=gB(g)hB(g)^{-1}
\]
has element-order multiset
\[
\{1,2,3,3,6,6\},
\]
so the descendant group is cyclic of order \(6\).

The checker also constructs the two displayed representative splitting maps directly from
\[
S_3=A_3\langle s\rangle
\]
and
\[
S_3=\langle s\rangle A_3
\]
and verifies the exact formulas.

The checker returns `VERIFY_OK`.

The exhaustive enumeration is an independent replay check; the mathematical exhaustion is proved structurally in `RESULT.md`.
