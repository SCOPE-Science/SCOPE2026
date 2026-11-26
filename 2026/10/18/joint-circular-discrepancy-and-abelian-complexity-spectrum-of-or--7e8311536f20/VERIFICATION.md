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

A fresh exact census independently reproduced the eight joint cells, all symmetry orbit columns, both marginals, both means (839/128 and 445/64) and each lexicographically least CSV witness. For replay, run python3 /tmp/opencode/independent_order5_census.py: prescribe 00000 as the first departure from vertex 0000, then assign the order of outgoing edges independently at the 15 other four-bit vertices. Each rooted Euler tour uniquely determines these orders, and a walk consuming the next available prescribed edge is completely determined. Reject early stops; a 32-step walk uses every distinct edge and closes by conservation. The 32768 assignments yield exactly 2048 distinct normalized words, each checked to have all 32 cyclic factors of length five. Count ones with prefix differences on the doubled word for every start and length 1 through 32; then D is the largest |2k-length| and P the largest set size of k. Generate the four reversal/complement candidates and normalize each at its unique zero factor, counting distinct orbits only. This yields 32 size-two and 496 size-four orbits and no other size. Consecutive fixed-length counts differ by at most one, establishing the equivalent max-minus-min formula. The census is exhaustive for binary order five, not a higher-order theorem or an external attestation. The frozen verify.py and spectrum.csv were inspected, not executed as code.

## originality

PASS

The supported distinct contribution is the complete joint D versus peak circular Parikh-range classification, including how the nonextremal discrepancy layers split and how their symmetry orbits split. The full discrepancy marginal and the minimum-layer orbit counts are already in 2c8828a3eb45; even P=6 on that layer follows from 6<=P<=D+1. Those facts and the least minimum-discrepancy witness are not new. The closest same-day Abelian census counts different words within its superficially identical aggregate row. Inspected catalogue and literature do not cover the remaining joint classification; this is a bounded comparison, not a priority guarantee.

## value

PASS

The pair measures two independently motivated kinds of circular balance: largest absolute excess over all windows, and concentration of symbol counts among windows of the same length. Order five is a complete nontrivial benchmark beyond individual construction examples. In particular identical peak P=6 allows discrepancies 5, 6, and 7, and the D=7 population splits over three peak values. Quantifying these splits and their symmetry decomposition gives exact test data for proposed dependences and population models; the already-known marginal alone would not give this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
