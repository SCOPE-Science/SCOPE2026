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
The polytope input is
\[
\operatorname{Vol}(\Pi_n)=(n+1)^{n-1}
\]
in the convention where a fundamental parallelepiped of the type-\(A_n\) lattice has volume \(1\).

The toric projective degree is
\[
D_n=n!(n+1)^{n-1}.
\]

The braid fan has
\[
(n+1)!
\]
maximal cones, so the smooth complete toric variety has Euler characteristic
\[
E_n=(n+1)!.
\]

Thus
\[
D_n/E_n=(n+1)^{n-2}.
\]

The bundled checker uses exact integers for
\[
1\le n\le200
\]
and verifies the identity after cross multiplication together with the unique equality at \(n=2\).

Finite checks are regression evidence only.
