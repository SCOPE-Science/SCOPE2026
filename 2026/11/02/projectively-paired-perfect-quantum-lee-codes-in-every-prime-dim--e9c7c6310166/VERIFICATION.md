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

The elementary syndromes are ±x_i and ±z_i. The consecutive pairing uses each antipodal class on each projective line exactly once. Every wedge x_i∧z_i vanishes and the columns span, giving an isotropic rank-r stabilizer. Every nonzero joint-Lee error of weight at most two is a difference of distinct radius-one errors, so none lies in the centralizer. The coordinate with pair (1,2) supplies X_i Z_i² of weight three and syndrome zero. Removing that coordinate leaves at least all other projective lines, which outnumber the lines in a hyperplane by p^(r−1)−1>0, so no stabilizer is supported there. Conversely, in a perfect nonempty coordinatewise-collinear code every syndrome is nonzero except the identity's, and each coordinate uses exactly two antipodal classes on a unique line. Thus (p−1)/2 must be even. This counts within the stipulated frame and does not give an obstruction for noncollinear checks.

## originality

PASS

Only the all-rank collinear stabilizer construction and the matching obstruction in that restricted class receive credit. Classical perfect Lee syndrome transversals and the six-qudit joint-Lee parameters are prior. The closest matching quantum example has rank-two column pairs; the complementary catalogue construction uses noncollinearity for the other prime congruence class. Classical Mannheim codes provide an even closer syndrome analogue, but the examined statements do not give this quantum family and necessity result.

## value

PASS

The useful result is a restricted-class classification in a fixed joint-Lee frame: it gives a uniform nondegenerate construction saturating the packing bound and a necessary constraint for designs with locally proportional checks. This is useful beyond merely evaluating the bound or reprinting the first parameter example, and the simple termwise commutativity makes the distinction from noncollinear global-cancellation designs precise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
