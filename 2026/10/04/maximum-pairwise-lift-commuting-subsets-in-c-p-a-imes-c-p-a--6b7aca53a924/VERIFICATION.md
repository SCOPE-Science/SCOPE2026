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
The theorem has three independently checkable stages.

First, the published Schur-cover commutator relation for finite abelian \(p\)-groups specializes to
\[
[\widetilde x,\widetilde y]
=
z^{x_1y_2-x_2y_1},
\qquad
o(z)=p^a,
\]
so adjacency is exactly determinant zero modulo \(p^a\).

Second, Smith normal form over
\[
R=\mathbb Z/p^a\mathbb Z
\]
writes every subgroup as an invertible image of
\[
p^iRe_1\oplus p^jRe_2.
\]
The determinant of its two Smith generators is a unit times \(p^{i+j}\). Hence the subgroup is isotropic exactly when \(i+j\ge a\), and its order is then at most \(p^a\). Equality occurs exactly for order-\(p^a\) subgroups.

Third, the \(\operatorname{GL}_2(R)\)-orbit of
\[
p^kRe_1\oplus p^{a-k}Re_2
\]
has size \(p^{a-2k-1}(p+1)\) for \(k<a/2\), because the stabilizer condition is divisibility of the lower-left matrix entry by \(p^{a-2k}\). When \(a\) is even, the middle subgroup \(p^{a/2}A\) is unique.

The packaged checker `artifacts/verify.py` constructs the determinant-adjacency graph, enumerates all maximal cliques by an exact bit-set Bron--Kerbosch search, and verifies the maximum size, subgroup property, total count, and invariant-factor distribution for
\[
(p,a)=(2,1),(2,2),(2,3),(3,1),(3,2).
\]
It returns `VERIFY_OK`.

The finite replay is not used as the proof of the universal theorem.
