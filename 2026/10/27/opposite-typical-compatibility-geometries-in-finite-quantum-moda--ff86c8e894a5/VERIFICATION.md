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

A compatibility edge forces equal successor rows in its two directions; thus an unrestricted graph with c components admits (2^n)^c modal relations. For equivalence accessibility, row equality is class membership, so each partition allows exactly the graphs with edges inside blocks. The weighted labelled-set formula is formal and distinguishing the block of world 1 gives the recurrence. For A_n a spanning forest of rank k=n-c has at most nk/2 within-component edges available, so the nonidentity relative mass is at most (1+2^{-n/2})^{binom(n,2)}-1. For B_n, a largest block of n-k>n/2 loses at least nk/2 available edges and there are at most n^{2k} such partitions; if all blocks are at most n/2, loss is at least n^2/4 against at most n^n partitions. All bounds vanish. The approximating law in each case is precisely the original law conditioned on its dominant event, so TV is the discarded probability; in the equivalence case a cut union bound yields connectivity for the conditional G(n,1/2). Independent replay (python3 -B /workspace/branches/independent_replay.py 1) counted unrestricted pairs by injectively naming row classes and equivalence pairs by recurrence through n=6, and separately enumerated row assignments through n=3; it matched all listed values. The finite checks are not the asymptotic proof. The operative measure is unambiguously the uniform admissible ordered pair, equivalently conditioning a uniform independent pair on admissibility; the first sentence on sampling in the scope note is awkward but the finding and its next sentence specify that same measure.

## originality

PASS

Credit the quantitative comparison of the two finite labelled-pair measures and their opposite total-variation limits. The forcing framework, component-row lemma and general partition-function constructions are prior or standard. A later indexed finding substantially overlaps and strengthens the defect analysis; it is not evidence of earlier coverage on the dates available. No absolute priority claim is made.

## value

PASS

The two measures differ by a natural accessibility axiom, yet that change reverses the typical compatibility geometry from the completely disconnected graph to a dense, high-probability connected random graph. The TV result describes the joint relation pair, not just a scalar count or a connectivity probability, and identifies actual sampling laws for a concrete finite-frame question. The value rests on this contrast, not on the standard exponential formula alone or on a claim about physical realizability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
