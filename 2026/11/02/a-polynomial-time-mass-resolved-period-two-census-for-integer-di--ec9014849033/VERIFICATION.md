---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The tree incidence matrix is injective on edge fluxes (successively remove leaves). Hence F²(x)=x is equivalent to exact reversal of every edge sign. For a parent-child sign t and fluxes q,q′ the gap is zero only if q=q′, or tk with 1≤k≤t(q−q′)−1. On a tree these gap choices integrate uniquely up to translation, and the coefficient extraction enforces q=s+sum(t). The weight z^(−m_w tk) records the child's subtree contribution to total modulo n. Each residue-matching gap configuration has one lift to a specified integer total S; F preserves S, and the only fixed configurations are constant. This gives the subtraction and division by two, including n=1. The scalar transfer costs at most O(nΔ³) exact operations (n=1 separately); width-n cyclic arrays and at most O(Δ) monomial shifts per edge-weight entry fit the stated O(n³Δ³) bound. Coefficient lengths are polynomial because each edge has O(Δ) gaps. The independent direct two-update replay matches both six-vertex vectors and totals. Up to five vertices, each feasible tree degree multiset specifies a unique shape (paths, stars and the unique five-vertex tree with degrees 1,1,1,2,3).

## originality

PASS

Credit prior edge-reversal dynamics, orientation/gap counting on paths, and exact mass-resolved restricted tree families. The supported distinct result is the polynomial-time fixed-total residue census for arbitrary labelled trees in sign-gradient diffusion, with an exact degree-twin obstruction. No equivalent arbitrary-tree result was evidenced in the examined comparisons.

## value

PASS

The finite residue vector replaces infinite enumeration with exact computation at every conserved total for every tree. The smallest structural degree-twin witness demonstrates that degree statistics cannot substitute for connectivity information in this census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
