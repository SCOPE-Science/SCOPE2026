---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

All unital subalgebras of k1⊕V⊕kz arise uniquely from radical subspaces containing z, Z(U)=k1⊕U⊕kz, or graph subspaces avoiding z, I(U,f), whose multiplication closure is exactly B(U,U)=0; graph inclusions give the asserted complete partial order. Counting gives P_A(t)=sum_d([n choose d-1]_q+q^d I_d(B))t^d. Projecting isotropic spaces through radical s=n-r contributes [s choose a]_q q^{b(s-a)}I_b(nonsingular quotient). In odd characteristic, zero counts recover even-rank Witt type and rank, and maximum isotropic dimension distinguishes odd ranks, determining similarity. In characteristic two, nonalternating square-map zero hyperplane H has alternating B|H and ranks r=2h-1 and 2h induce the SAME isotropic-poset structure, whereas alternating forms are distinguishable by I_1; this yields exact rank-pair collision classification. Small n=2 diagonal forms diag(1,0), diag(1,1) are nonisomorphic by socle dimensions 2 vs1, but their subalgebra lattice polynomial is 1+(q+1)t+(q+1)t²+t³ for all q=2^e. Source verifier implemented direct RREF subspaces over q=2,3,4,5,7 and was inspected; its finite checks are not used to infer all ranks.

## originality

PASS

Best-of-knowledge PASS: finite-field symmetric bilinear form and polar-space isotropic counts are standard, but the inspected maximal-subalgebras and short Gorenstein classification works do not supply the exact full poset of ALL unital subalgebras, nor the characteristic-two 'two adjacent nonalternating ranks same lattice' iff classification. The small example is not the sole result: the full n and q family answers a natural algebra-invariant reconstruction question. A potentially equivalent lattice treatment in finite-ring literature remains a priority risk.

## value

PASS

PASS: The complete subalgebra lattice and exact reconstruction obstruction for split short local rings are mathematically natural structural invariants. The characteristic-two construction exhibits two nonisomorphic algebras with IDENTICAL full unital-subalgebra lattice but distinct Gorenstein property, across every even q and n with eligible ranks; this is independently useful invariant-theory information, not merely a small exact count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
