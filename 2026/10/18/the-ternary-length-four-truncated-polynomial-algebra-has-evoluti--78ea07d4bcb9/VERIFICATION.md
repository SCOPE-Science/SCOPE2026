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

Multiplication modulo t⁴ gives the four stated independent formal quadrics. Expanding the eight displayed squares gives all four targets, and distinct cross terms followed by pure squares show the eight are independent. Formal polynomial equality is appropriate; no monomial has a variable degree reaching 3, so evaluation also separates the polynomials. Nonzero linear forms give 40 projective squares. If seven squares span a space containing S, their quotient images have dimension at most three; extending to a three-plane forces the span of all squares lying over it to meet S in dimension four. My exact replay computed the full 33,880-three-plane intersection histogram (31,905, 1,830, 145, 0 for dimensions 1–4), ruling this out. An eight-dimensional support containing S is the whole inverse image of its four-plane W, and is square-generated iff its squares have rank eight. For an independent census I generated only W spanned by four independent quotient images of squares (6,654 distinct flats), since every eligible W must have a basis of such images. The rank-eight cases were 243 with 10 squares and 9 with 16, totaling 252 without repetitions. The unital, characteristic-not-two result of Costoya–Fernández Ouaridi–Viruel identifies the verified rank with evolution dimension. By polarization it is also the symmetric bilinear rank of multiplication, not necessarily the unrestricted bilinear rank.

## originality

PASS

The complete 252-space incidence census is the supported distinct contribution. The lower bound greater than seven is already in Costoya–Fernández Ouaridi–Viruel, and the exact rank eight has direct overlap with a later Resultary entry. The scalar rank alone is not the basis of the originality decision.

## value

PASS

This is the explicit small-field exception in the motivating interpolation theorem, not a chosen numerical slice without context. Beyond the short upper-bound decomposition, the complete incidence split describes every possible optimal support for a natural local algebra and exposes two different numbers of available projective squares within those supports. It can inform the separate classification of optimal decompositions without pretending that the subspaces are inequivalent envelopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
