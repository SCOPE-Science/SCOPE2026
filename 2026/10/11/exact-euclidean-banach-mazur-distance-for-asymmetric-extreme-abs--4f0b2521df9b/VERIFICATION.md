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

The mathematical verification is analytic. Sign averaging proves that diagonal Euclidean forms suffice. Weighted Cauchy--Schwarz gives the exact inner-ellipse constraints, and convexity of the quadratic form reduces the outer factor to the polygon vertices. The non-disk problem is then a one-dimensional active-constraint minimax with a unique crossing; derivative signs establish global optimality at the crossing or the appropriate coordinate endpoint.

Checked identities include
\[
1-A^2-B^2=
\frac{(a-1)(c-1)(a+c+ac-1)}{(1-ac)^2},
\]
\[
u_*\ge1\iff a(c+2)\le1,
\qquad
v_*\ge1\iff c(a+2)\le1,
\]
and the endpoint substitutions
\[
L_2(u_c)=\frac{2(1-ac)}{2-c-ac},
\qquad
L_1(1)=\frac{2(1-ac)}{2-a-ac}.
\]
Finite numerical minimization was used only to search for counterexamples before the symbolic proof; it does not certify the theorem. The theorem does not cover complex scalars, higher dimensions, pairwise distances inside the family, or the already-covered symmetric and boundary subfamilies.
