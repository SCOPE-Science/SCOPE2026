---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The annihilator identities can be checked without expanding minors. A signed shift supported on rows S with shift q and sign mask p has BᵀP_(x,y) supported on entries (t⊕q,t⊕x), with sign (−1)^(t·(p⊕y)). Transposing pairs t with t⊕q⊕x; skewness follows if S is preserved and (q⊕x)·(p⊕y)=1. For B₁,B₃ the masks are q=3,p=5, with S the two halves defined by bit mask 2. For the three x values, q⊕x is 1,5,4, all preserving the two halves; the dot product is one for each of the six specified pairs. For B₂ the masks are q=5,p=6, with all rows allowed; q⊕x is 7,3,2 and again every listed pair has odd dot product. The three B_j g thus bilinearly annihilate the six shifted columns over C, and their displayed first-three-row minor at the all-ones window is 2. Rank at most five holds on the open set where that minor is nonzero and extends to all windows by polynomial vanishing of the maximal minors. For the lower bound, independently produced exact Gauss–Jordan elimination gives rank five for all 595665 normalized sets at p=1000003, checked prime by trial division, with zero defects. Left composition by the inverse of any selected shift adds its label to all others over F₂, up to signs, so enumeration of the sets containing zero covers every five-set. A nonzero residue minor lifts to a nonzero integer minor. The explicit window witnesses the nonempty Zariski-open rank-five conditions for every five-set. On this open set the six-column relation has all six coefficients nonzero, giving two three-atom representations, while subtraction rules out distinct representations each of size at most two.

## originality

PASS

The exact spark-six threshold and integer-window certificate on the order-eight elementary abelian group are distinct from prior full-spark obstructions. The skew-symmetry ingredient already occurs in earlier work; the mathematical distinction is the simultaneous three-annihilator construction with six shared columns, and the matching all-five independence certificate.

## value

PASS

For the full time–frequency orbit on the first order-eight Boolean cube, the spark is the precise obstruction to sparse synthesis. The result determines the six-column boundary, gives an all-window mechanism and an exact witness for the lower bound, and distinguishes two- from three-atom synthesis in a way the known non-full-spark theorem does not.

The dated certificate retains the supplied scientific assessment, sources and limitations.
