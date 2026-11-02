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

The proof in `RESULT.md` is an exact all-length argument using inverse preimages, an interval-growth lower bound, and a complete classification of the only allowable one-letter slack. No finite computation is used to infer an infinite statement.

Run `python3 verify.py` in the directory containing the files. The executable computes the full bit-mask subset automaton for all state counts from 2 through 11. It uses dynamic programming on nonreset subsets to count first-reset words, separately builds the explicit word list, checks candidate distinctness, checks first synchronizing position for each candidate, checks minimum reset length and unique minimum word, and checks both next-length counts. The exact output ends with `VERIFY_OK`.

Boundary cases \(n=2\) and \(n=3\) are included; the first-at-final-letter counts are \(1\) and \(2\), respectively. Subsequent values for \(n=4,5,6,7,8,9,10,11\) are \(5,10,17,26,37,50,65,82\).

Limitations: finite checks do not prove the universal theorem. Historical priority, which is not a computation, is assessed only from the cited and inspected literature. Independent audit has not been performed.
