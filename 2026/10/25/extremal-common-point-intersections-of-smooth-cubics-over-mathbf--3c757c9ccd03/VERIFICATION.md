---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Every geometrically smooth plane cubic over F2 has at most floor(3+2sqrt2)=5 F2-points by Hasse–Weil. The group PGL3(F2) is transitive on the 21 five-element Fano-plane subsets; for one fixed S, five linear evaluation constraints leave exactly 32 ternary cubic forms, and the homogeneous Jacobian-quadratic rank-15 criterion (equivalent to no common geometric projective zero, by the three-quadrics regular-sequence Hilbert series (1+t)^3) leaves exactly smooth encodings 60 and 172. Their displayed gradients also have no common projective zero. Hence every five-set lies on one unordered smooth pair and there are exactly 21, one orbit with stabilizer size 8. The third pencil member f+g=xz(x+z) has three concurrent lines; line restrictions of f yield divisor 5p+p1+p2+p3+p4, exhausting Bézout length 9 and proving scheme support/multiplicities (5,1,1,1,1), with p the third point on the line through omitted rational points. Fresh independently constructed GF2 Jacobian-rank census over all 1023 nonzero coefficient vectors gave 336 smooth cubics and 56280 unordered pairs with intersection histogram (12740,22575,14448,5488,1008,21). The separate assigned Gröbner-chart and binomial-moment verification file was inspected; its complementary algorithm covers all finite masks. Reconstructed all nine Git blob entries and matched assigned tree SHA 0dd580acb9b8aacc337d39b751a91d2d75969d13.

## originality

PASS

Best-of-knowledge PASS for the F2 geometrically smooth cubic pair orbit and local fivefold contact, not for known smooth-cubic count 336. The nearest Kaplan–Matei theorem excludes q=2; Asgarli–Ghioca concerns all-smooth pencils whereas this pencil is not all-smooth. Earlier individual-cubic tables remain residual priority risks.

## value

PASS

The smallest-field sharp simultaneous-rational-point intersection problem for smooth genus-one plane curves is natural, and the unique projective orbit, forced fivefold scheme contact, and complete incidence histogram supply geometrically meaningful information beyond a Hasse upper bound or recomputation of the already known 336 smooth cubics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
