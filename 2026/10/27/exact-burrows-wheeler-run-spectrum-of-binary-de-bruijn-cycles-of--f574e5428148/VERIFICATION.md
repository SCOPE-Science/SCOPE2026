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

Distinct k-prefixes order the rotations. Rows u0 and u1 cannot have the same predecessor, or the k-factor bu would repeat; their last-column letters are complementary. The displayed LF formulas rank each predecessor extension bu exactly once. A transitive LF orbit thus reconstructs one cycle with each prefix, and a de Bruijn cycle gives one such orbit, with one representation per rotation class. The internal boundaries contribute m=2^(k−1); each across-block boundary contributes one exactly for equal adjacent orientations. The end orientations are both 1, since the predecessors of the unique all-zero and all-one factors are respectively 1 and 0. With m even at least one adjacency is equal, giving m+2; differing end letters also make the linear run count even and equal to the circular count. I independently enumerated Hamilton cycles of the directed shift graph on k-bit words: start at word 0, extend by unused overlapping k-words, and retain full paths with an arc back to 0. The BWT letter at each destination rank is the high bit of its predecessor. This confirmed the spectra (4:1), (6:2), (10:4,12:4,14:8) and (20:38,22:426,24:840,26:608,28:130,30:6) at orders 2–5 and all six lexicographically first witnesses in TABLE.csv. The unique 0^k root makes this exhaustive without identifying reversals or complements. Frozen replay: verify.py, with both LF orientation and rooted Euler routines, and TABLE.csv; the uploaded code was inspected, not run. The count is exact at these orders, not extrapolated.

## originality

PASS

Pass for the exact order-five run distribution and the first strict nonattainment, not for the block or feedback characterization or the all-orders lower bound, which were known. There is an exact distinct later catalogue duplicate and a later stronger forward/reverse joint table; both are direct coverage of the statistic in those records, not evidence that they preceded the frozen result. The available earlier feedback census concerns a different statistic and does not give the adjacent-transition distribution. A relationship note should credit the previously published run bound explicitly.

## value

PASS

Run count measures residual BWT compressibility of a highly factor-diverse object. Order five is not an arbitrary cutoff: it is the first that misses the general lower bound, and the spectrum identifies both the true minimum and its exact multiplicity. The older bound and earlier different weighted count leave those quantities undetermined without a separate computation. This finite exact invariant is useful without claiming a formula or gap for all larger orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
