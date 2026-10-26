---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

Run `python3 CHECK.py` with a stock Python 3 interpreter. The program has no external dependencies, enumerates \(12\) simple cubic bipartite circulant graphs with bipartition orders \(3\) through \(6\), and evaluates \(87,837\) candidate committees using four rational Thiele scores, for \(351,348\) exact evaluations. For each committee, it compares the score against the predicted bound and tests the perfect-matching criterion; an independent permutation enumeration determines the number of perfect matchings of each source graph.

The program completed successfully. In particular, the count for \(K_{3,3}\) is \(6\); the three other tested sizes give counts \(9\), \(13\), and \(17\) or \(20\), depending on the circulant edges. The exact-rational checks are finite tests, not a proof of the result for unbounded \(n\).

The proof for all finite cubic bipartite graphs is the elementary scoring inequality plus Hall's theorem. The counting-classification step invokes the independently established cubic-bipartite perfect-matching counting hardness of Dagum and Luby. Neither the finite program nor this package constitutes an independent audit of the complexity-theoretic source theorem or of historical priority.
