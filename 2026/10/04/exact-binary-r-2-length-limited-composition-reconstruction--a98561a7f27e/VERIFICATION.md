---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a word with z zeros, o ones, and zero/one run counts r0,r1, the length-two composition counts are a=z-r0, b=o-r1, and mixed count t=r0+r1-1 for nonconstant words, so the observation is equivalent to (z,r0,r1). Feasible pairs satisfy |r0-r1|<=1; counting symbol totals over balanced and one-heavy run-count pairs yields the two closed forms. Positive compositions of z and o into run lengths give the stated class sizes and singleton criterion. An independent brute-force reconstruction for every binary word through n=12 reproduced the observation partition, closed forms, class sizes, and singleton sets exactly; the package verifier extends corroborative brute force to n=16 and arithmetic checks to n=500.

## originality

PASS

Ye--Elishco introduce the r-length-limited composition-multiset model and explicitly leave constant r and its capacity behavior as a further question. Their construction treats a regime where r scales with n and does not give the exact r=2 quotient, class-size formulas, or singleton classification. The older full-composition problem observes all substring lengths and therefore does not imply the much coarser r=2 ambiguity classes. Targeted Resultary searches found no covering exact formula.

## value

PASS

This resolves the first nontrivial constant-r case explicitly singled out by the defining paper as an open direction, and it does so completely: not only the asymptotic capacity but the exact all-n number of observations, every ambiguity-class size, and all individually reconstructible words. That is a natural structural base case likely to be useful in any study of fixed r.

The dated certificate retains the supplied scientific assessment, sources and limitations.
