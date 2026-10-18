---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For P=A⊕B with antichain widths m,n≥2, every finite meet-preserving extensive idempotent j on Up(P) has a unique support S⊂P via K_x=intersection of opens U with x∈j(U); j_S(U) tests S∩↑x⊂U. Composition tests for x∈A yield the two implications on S_A\T_A and T_A\S_A regarding upper supports; top level B is automatic. For commuting nuclei their composite is exactly j_{S∩T}. Split lower-support choices into equal, strict-inclusion each orientation, incomparable; respective polynomials (1+x)^m, (2+x)^m−(1+x)^m, (3+x)^m−2(2+x)^m+(1+x)^m and corresponding upper choices (3+y)^n, (2+y)^n, (1+y)^n yield F_mn. Expanding is symmetric in (m,x)↔(n,y). A nucleus with intersected lower/upper supports a,b has image size #Up(S∩T)=2^a+2^b−1. Independent brute-force of all 16^2 ordered pairs for m=n=2 found 162 commuting pairs and full rank counts {1:35,2:68,3:28,4:18,5:12,7:1}, matching formula. The general combinatorial derivation is necessary; finite brute force is supporting evidence only.

## originality

PASS

Erné 2022 Nuclear ranges in implicative semilattices develops abstract nuclei and notes commutation/composition consequences, but its inspected Lemma 3.6 gives neither the height-two subset-support criterion nor generating polynomial or composite image census. No equivalent explicit formula surfaced in Resultary query. Standard finite distributive-lattice duality only underpins recovery of the underlying poset, not the rank-profile symmetry. An older relational/combinatorial equivalent remains plausible and disclosed.

## value

PASS

The exact count of commuting nuclei and their composite image sizes on a natural two-level distributive Heyting family is a meaningful complete classification. The rank distribution agrees after exchanging widths even though the Heyting algebras are not isomorphic when widths differ, a structural limitation of an intuitive invariant, not just an arbitrary tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
