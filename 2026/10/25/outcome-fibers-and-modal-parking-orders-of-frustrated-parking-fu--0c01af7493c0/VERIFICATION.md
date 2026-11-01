---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For a prescribed final arrival-order permutation pi, before arrival i the vacant set is exactly {pi_i,...,pi_n}. If pi_i is not its maximum then the sole valid request is pi_i; if it is maximum, requests are pi_i plus each earlier occupied lower spot, counted by 1+(pi_i-1)-(n-i)=pi_i-n+i. The allowed preferences vary independently within the fixed vacant-state sequence, yielding the product over right-to-left maxima. If k positions are not right-to-left maxima, a record factor counts at most k earlier occupied smaller nonrecords, so product <=(k+1)^(n-k). Equality at every record requires all k small entries to occur first, with decreasing large suffix; this also establishes precisely k! outcomes for each maximizing k (including possible ties), and the overall maximum follows by finite integer maximization. The known total (2n-1)!! normalizes the probabilities. Independent literal simulation enumerated 50,069 candidate words n<=6 and exactly compared all 873 resulting permutations with formulas and modal counts; universality comes from the predecessor argument.

## originality

PASS

Previously published fixed-order fibers under first-vacant-forward parking differ in the rule and use inverse outcome permutations; their consecutive-small-block statistics are not the right-to-left maxima formula for farthest-free frustrated cars. The exact fixed-outcome formula and complete modes do not follow from the published double-factorial total or refinements by lucky sets.

## value

PASS

The full permutation-fiber distribution and its uniquely characterized modes refine the recently introduced frustrated parking model beyond its previously known total count. The prescribed-outcome statistic is natural in parking enumerations, gives exact probabilities for all n! outputs, and the extremal classification is nontrivial even when the total count is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
