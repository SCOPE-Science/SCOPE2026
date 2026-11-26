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

Independently recovered the rank-one bound without relying on the minimal-ideal reductions. Adjoin 0 and, for orbit notation, use S^1 allowing the identity. If there is a rank-one matrix A=u v, irreducibility makes span(S^1 u) the full plane, so some v s u≠0. The nonzero eigenvalue of As is then a rational root of unity by finiteness, hence ±1; (As)^2 is a rank-one idempotent e=u_0 v_0. The nonzero orbits U'=S^1 u_0 and V'=v_0 S^1 (omitting zero) span by irreducibility and its dual. All pairings v' u' are in {−1,0,1} since e t s e=(v' u')e is in S. Take one vector on each projective direction of each orbit. Two independent evaluations place the columns in at most four signed projective directions (coordinate axes and both diagonals); by duality the row count is also at most four. If either count is four, any covector on the other side has coordinates α,β with α,β,α+β,α−β in {−1,0,1}, so only two projective covectors are possible. Otherwise the product is at most 3·3. Any rank-one A sends a suitable u' to a nonzero column of U' and a suitable v' to a nonzero row of V', so its directions lie in these families. Writing A=λu_i v_j, pick v' and u' with v' u_i and v_j u' nonzero. The scalar v' A u' belongs to {−1,0,1} from e t A s e, so λ=±1. This upper-bounds all rank-one members, not only those in the minimal ideal, by 18. Invertible members form a finite group when present, conjugate over R into O(2) by averaging; rational rotational traces are integral and force orders 1,2,3,4,6. This gives at most 12 units and hence at most 31 including zero. For equality, checked the two signed orbits by applying R,F,−I directly (R cycles the three column and row directions up to sign). R has order 3, F conjugates it to R^−1 and det(F)=−1; adjoining the central −I doubles the group order to 12. The displayed pairing matrix gives closure of the 18 distinct signed outer products under multiplication or zero, and the four matrix units ensure rational irreducibility. The frozen scripts and recorded 961-product check were inspected without execution; the direct checks and all-semigroup argument above establish the conclusion.

## originality

PASS

The general bound, minimal-ideal method and finite rational subgroup constraint are prior work. The supported distinct result is the exact maximum of 31 in the irreducible dimension-two rational class, using a new rank-one count in the comparison and a joint equality example. Inspected stronger-looking general results do not supply that sharp count or example.

## value

PASS

This solves the first nontrivial dimension of the exact extremal size question posed alongside the general asymptotic theorem. The bound distinguishes the contributions of units and rank-one matrices and the example proves they can be jointly maximal. It is substantially sharper than 81 and identifies a concrete projective restriction relevant to future exact classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
