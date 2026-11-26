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

Under the stated strict test, additions need not be feasible. For cost, the grand coalition's full common bundle rules out c≤k−2 and c=k−1 with no private funding: even the best augmentation cannot exceed kh. At c=k−1 with positive private funding, the voter who has a funded private project witnesses every missing grand-coalition bundle, including proper subsets of the common bundle (the latter case is implicit in the written proof). Smaller nonsingleton coalitions have targets of cost at most (k−1)h, and singleton targets cost at most h. The c=k sufficiency case and the labeled binomial count then follow. For cardinality, singleton private bundles force z_i≥h; when a common project is missing, every g-person coalition can ask for a g-common-project bundle containing one such project. Its largest score must be at least g; the minimum of these maxima is z_(g). The same missing-approved-project witnesses prove sufficiency. Summing z_i≥h and using the budget gives c(h−k)≤0, so h>k forces the unique all-private outcome; h≤k admits the all-common outcome. For c=k−1 the optimal smallest x_i is floor(h/k), attained by an even allocation of all h private selections, and comparing with c=k gives the stated floor formula. For h=k+t, t≥1, it equals t−floor(t/k)>0. The phrase 'prior projects' in the Finding is a typo for 'private projects'; scope and proof are unambiguous.

## originality

PASS

The incompatibility phenomenon and its (2,5) example are known; the supported distinct contribution is the all-k symmetric-family characterization, including the cost count, sorted-score test, exact boundary and sharp deficit, not the original incompatibility witness. The closest indexed variant covers the two-voter diagonal rather than the full family.

## value

PASS

The family generalizes a standard incompatibility witness while keeping the source of the conflict controlled. The exact boundary distinguishes when a joint guarantee is possible, and the tight deficit separates bare impossibility from its quantitative severity. The spectrum and labeled count are useful benchmarks for comparing outcome rules in this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
