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

From the actual CPSR payment rule, for the target among three delegates with efforts a,b>=c>0 the state-G action advantage divided by Ba is (b+c)/(a+b+c)+(b-c)(J_b-J_c), where J_c=0, 1/[2(a+c)], or 1/(a+c) according to a+c<b, =b, or >b, and J_b=1/(a+b). Each region, including the tie boundary, is strictly positive. State symmetry and Bayes with neutral prior give conditional good-signal advantage 2Bx_iK_i. Independent exact-Fraction enumeration of all 16 opponent ballots for efforts (2/5,2/5,1/100,1/100,1/100) gives K=-616489/33459375 and 2x_iK=-2465956/167296875, no possible weighted tie because total effort 83/100. The all-parameter three-delegate statement is proved analytically, not by 5184 finite examples; no effort Nash equilibrium is asserted.

## originality

PASS

The source already proves symmetric-profile sincerity and supplies a nonneutral-prior asymmetric failure. The novel combined threshold requires universal heterogeneous three-delegate truthfulness at neutral prior and a fully signal-responsive five-delegate reversal. The reference incentive conditions have different quantifiers and no result inspected implies both statements.

## value

PASS

This sharp 3-versus-5 threshold determines when a published conditional coalition reward loses signal-following incentives even at a neutral prior. It adds both a robust exact violation and a universal small-committee protection, a substantive design boundary rather than a merely negative calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
