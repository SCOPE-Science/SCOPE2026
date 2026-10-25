---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For G=E(F_q) with origin at a rational flex, distinct rational points are collinear iff they sum to zero; Bezout gives cov>=N/3=m. If |G[2]|=2, the sum of all group elements is the unique involution, so partitioning 3m points into m disjoint zero-sum trisecants is impossible; cov>=m+1. Because 3|G|, choose an epimorphism chi:G->Z/3 and H=ker chi with |H|=m. A partial transversal (h_i,k_i) in the Cayley sum table of H gives disjoint triples h_i, u+k_i, -u-h_i-k_i drawn from three different cosets, each summing to zero. The established Goddyn–Halasz near-transversal theorem yields m-1 triples, leaving exactly three points coverable by at most two rational lines: upper m+1. When |G[2]| is 1 or 4, H has trivial or noncyclic Sylow-two subgroup, so the Hall–Paige complete-mapping theorem yields m full triples (alternatively Cichacz 3-ZSP), achieving m. Explicit cyclic formula in RESULT.md checked arithmetically for m=1..200; finite examples are not a proof of the group transversal theorem.

## originality

PASS

Cichacz already proves the zero-defect zero-sum partition regime, and Goddyn–Halasz proves group near-transversals independently of geometry; these antecedents are credited. The contribution is the exact one-extra-line elliptic covering classification, derived by a specific index-three coset realization and group-sum obstruction. General Asgarli et al. discuss rational line covering and older N/3+O(1) bounds, not the precise all-finite-field unique-involution formula in sections inspected.

## value

PASS

The exact projective line covering number of all rational points on an elliptic plane cubic is a natural finite-field geometric invariant. The sharp one-involution obstruction completely determines the defect relative to Bezout for every allowed cardinality, and the algebraic and combinatorial correspondence gives a reusable explicit geometric covering mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
