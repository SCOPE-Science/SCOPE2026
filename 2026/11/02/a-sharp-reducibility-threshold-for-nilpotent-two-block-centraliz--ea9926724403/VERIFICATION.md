---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For N=J_(n−2)⊕J_2, n≥5, over arbitrary fields the nilpotent fixed-centralizer matrices have module-coefficient form with a0=d0=0. Coordinate reduction extracts x,b,c,B,C∈k^m subject to rank([x;b;c])≤1 and b∧C+B∧c=0, with (n−3)m free affine factors. The closed L={b=c=0} has dimension 3m; the complementary U has common line ℓ∈P^(m−1), parameters ν,λ,μ with (λ,μ)≠0 and m−1 independent constraints on (B,C), hence irreducible dimension 2m+3. Rank(x,B,C)≤2 on closure(U) but L contains rank 3 for m≥3, proving exactly 2 components with dimensions nm,(n−1)m+3. Explicit degenerations yield L⊂closure(U) for m≤2, hence irreducible (m0 trivial). Over F_q, b=c=0 contributes q^(3m), and nonzero proportional b,c contribute (q+1)(q^m−1)·q·q^(m+1), yielding q^(nm)+q²(q+1)(q^((n−1)m)−q^((n−2)m)) after free factors; m0 gives one empty tuple. Independent complete enumeration of five-coordinate two-vector constraints gave q2:208 and q3:3321, matching source; inspected actual matrix-multiplication checker code, which supplements algebraic proof.

## originality

PASS

Qualified PASS for exact all-arity reducibility threshold at m=3, both component dimensions and entire q-point formula in fixed centralizer of Jordan partition (n−2,2). Existing two-regular centralizer literature proves irreducibility for commuting PAIRS (m=2); unrestricted nilpotent commuting tuple reducibility and commuting similarity type classifications do not impose the same fixed partition or provide the all-m count.

## value

PASS

Sharp m=3 onset of a second component and exact arithmetic point counts for every characteristic give a complete natural geometric/arithmetic invariant of a canonical minimal unequal two-block centralizer, explaining how adding the third commuting nilpotent changes geometry. Not simply a known one-matrix nilpotency count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
