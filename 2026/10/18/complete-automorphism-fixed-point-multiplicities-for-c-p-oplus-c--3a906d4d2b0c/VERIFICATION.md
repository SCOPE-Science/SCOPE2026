---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For every prime p and m>=4, independently reconstructed the automorphism parametrization a unit modulo p^m, d unit modulo p, b,c in F_p and the fixed-point congruences. The valuation k=min(v_p(a-1),m) gives the lower layers, and the rank-zero/one/two residue-field matrices at k=m-1,m give the two exceptional tails. The six disjoint formula cases (j=0, j=1, 2<=j<=m-2, j=m-1, j=m, j=m+1) sum to p^(m+1)(p-1)^2 including p=2. Direct independent enumeration of literal fixed-element congruences, not the source verifier, agreed for (p,m)=(2,4),(2,5),(3,4),(5,4); for (3,4) multiplicities are (243,405,216,84,23,1). Burnside gives ordered s-tuple orbit counts but is prior methodology; no claim of novelty for s=2. Exhaustive finite samples corroborate the uniform valuation proof, not conversely.

## originality

PASS

Best-of-knowledge PASS for complete all-layer m>=4 theta vector, not for earlier p^0/p^1/p^2 layers or the classical Burnside relation. The closest published results have full low-exponent tables m=2,3, one fixed-point-free all-exponent formula, and isolated low layers; a fixed subgroup existence/Reidemeister spectrum and pair-orbit polynomial do not recover counts at every j. We read the accessible 2018 primary article and 2019 adjacent-exponent primary text, plus complete published single-layer Resultary theorem; the same-object 2016 m=3 article was located online but its full PDF could not be fetched (502), and authorized institutional attempt returned vpn_disconnected. This is retained as material priority uncertainty and not asserted to be whole-document NOT_COVERING.

## value

PASS

The number of automorphisms with exactly p^j fixed points is a natural intrinsic distribution and a previously posed counting problem for finite abelian groups. A single closed formula supplies arbitrarily many intermediate layers and the two stationary upper tails for every prime and exponent m>=4; isolated previously known values j<=2 do not supply that classification. Characteristic-two vanishing low layers and fixed-subgroup structure are mathematically explanatory rather than arbitrary finite-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
