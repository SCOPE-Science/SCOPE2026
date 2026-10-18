---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every derivation D(v+az)=Av+(φ(v)+ac)z obeys A²=A, c²=c, φA+cφ=φ, A†=cI-A. For c=0, A†=-A and A²=A imply 2A=0. Outside characteristic two this leaves zero; in characteristic two, self-adjoint idempotent A has orthogonal nondegenerate symplectic image/ker, so dim im(A)=2r. φ|ker A=0 and the full D rank is 2r. For c=1, im and ker of A are complementary Lagrangians of dimension m and φ|im A=0, so rank D=m+1. Central shears eliminate φ, symplectic automorphisms make each allowed projection class transitive, and c and r separate orbits. Counting nondegenerate 2r-subspaces by |Sp(2m,q)|/[|Sp(2r,q)||Sp(2m-2r,q)|], transversely paired Lagrangians by ∏(q^i+1)q^{m(m+1)/2}, and φ choices q^{2r},q^m yields the stated rank polynomial. Independent matrix enumeration confirmed H_1(F2)={0:1,2:16}, H_1(F3)={0:1,2:36}, H_2(F2)={0:1,2:80,3:480,4:16}. Finite tests corroborate but do not prove all fields/dimensions.

## originality

PASS

The complex conformal-symplectic derivation block is known, and symplectic counting formulas are classical; the simultaneous composition-idempotent conjugacy classification, characteristic-two extra branch, and explicit labeled q-rank polynomial are not among the inspected primary results. Best of knowledge, with stated equivalence risks.

## value

PASS

The Heisenberg family is the central model of nonabelian two-step nilpotent Lie algebras. The theorem resolves exact conjugacy and labeled idempotent-operator ranks for every field, with a genuine characteristic-two phase change from two to m+2 orbits. Both the orbit census and finite-q polynomial provide structural data not contained in the general derivation presentation; small m=2,q=2 already shows three nonzero full ranks 2,3,4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
