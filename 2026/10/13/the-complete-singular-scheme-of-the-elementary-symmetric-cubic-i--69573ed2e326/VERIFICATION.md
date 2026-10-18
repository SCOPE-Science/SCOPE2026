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

For char2 and n>=5 with n mod4 not 2, each partial derivative of e3 equals xi²+s1 xi+s2. All coordinate values therefore lie among the roots of one quadratic. Comparing coordinate multiplicity parities excludes two different nonzero values, while single nonzero value has admissible support cardinality |S|=1 mod4. At each indicator p_S the quadratic tangent form splits into e2 on the r−1 active and n−r inactive coordinates. For odd n both polar blocks have even size and full rank. If 4 divides n, the outside block has odd size 3 mod4 and its unique polar radical evaluates to Q=1, so the projective tangent quadric is still smooth. Odd n Jacobian local tangent=0 thus reduced. If 4|n, ∑ partials=0, exactly n−1 quadrics generate height n−1 zero-dimensional complete intersection of degree 2^{n−1}; support has 2^{n−2} points and tangent dimension 1 each, forcing every local Artin length 2 and local ring K[epsilon]/epsilon². Independently enumerated every F4 projective point for n=5,7,8 and obtained precisely 6,28,64 points; the universal algebraic argument, not samples, proves every admissible n.

## originality

PASS

Ying Xie arXiv:2610.00259v1 studies general elementary-symmetric derivative/multiplicity schemes, dimensions and coordinate components and explicitly points to open global primary-decomposition/reducedness cases in Section 7. This theorem gives a complete geometric support and local multiplicity classification for the char2 cubic e3, including reduced/curvilinear-double dichotomy and smooth quadratic tangent cones. Orzel’s general derivative bounds and Cafure–Matera–Privitelli partition framework do not yield the exact projective local rings in the inspected statements. Semantic Resultary query returned unrelated singular-scheme records; absence alone not proof of novelty.

## value

PASS

A full singular-scheme classification for a canonical symmetric cubic across an infinite characteristic-two family fills a recognized positive-characteristic gap. The distinction between ordinary quadratic tangent cone and nonreduced Jacobian local scheme is mathematically instructive and determines exact zero-dimensional lengths and local structure; not arbitrary tiny-case enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
