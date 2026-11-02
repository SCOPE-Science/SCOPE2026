---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Under the height<=2 assumption every strict comparable pair is a cover, so off-diagonal incidence-algebra multiplication has no intermediate summand. For E,F idempotent with diagonal bits a_x,b_x, the edge coordinates X,Y are independently permitted exactly when a_x != a_y and b_x != b_y. The off-diagonal EF entry is a_x Y+X b_y and an additional rank-one linear equation applies if diagonal products agree; enumerating the 16 ordered bit-state cases yields precisely the non-symmetric 4x4 D matrix. Thus independent q^(D) edge factors and rank monomials follow from an exhaustive local linear-space calculation. Idempotent matrices have rank equal to number of diagonal ones even in char2. For the star center, three row sums of q^D equal (1+q)^2 and the fourth 1+3q, giving N=3(1+q)^(2m)+(1+3q)^m. Total individual idempotents 2(1+q)^m, hence probability=3/4+1/4[(1+3q)/(1+q)^2]^m and limit 3/4 for every fixed finite q>=2. Empty poset and isolates handled by empty products; no height>=3 claim.

## originality

PASS

Can-Casimiro-Malheiro analyze incidence-monoid idempotent varieties and products within prescribed antichain submonoids; their Theorem 4.9 calculates product of selected idempotent components, not all ordered pairs in full I(P,F_q) with (EF)^2=EF and not a joint triple-rank polynomial. Gargate-Gargate compute single potent/idempotent element counts using diagonal roots, not the mixed condition on EF. The four-state weighted partition function is an independent exact whole-algebra counting invariant; standard local equation solving is credited as the method, not claimed as intrinsically new.

## value

PASS

The exact triple-rank polynomial for ordered idempotent pairs supplies a natural all-ranks algebraic invariant of every height-two poset; the universal 3/4 limit for growing stars quantifies a nontrivial failure of closure under multiplication, contrasted with known orthodox submonoid structures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
