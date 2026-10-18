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
# Verification

The infinite claim follows from the proof in `RESULT.md`: essential positions cover every minimal supersequence; the binary coloring argument excludes length equal to the sum of input lengths; the near-bound rigidity lemma uses both runs of each input having length at least two; the unique shared letter partitions all maximizers into two explicitly counted families. The binomial product is **not** invariant under arbitrary redistribution preserving cross-sums; it has the two pair-swap symmetries stated in the result.

Run the packaged standard-library Python checker using `python3 verify.py` in a directory containing these files. It independently enumerates all binary candidate supersequences of the extremal length for 80 qualifying four-run quadruples, checking both subsequence containments and every one-symbol deletion. It confirms the *full extremizer sets*, not only counts, and rejects length equal to the sum of input lengths for sixteen smaller parameter cases. It also verifies a singleton-run counterexample showing the scope restriction is necessary.

Observed output (reproduced in `verification_output.txt`): `VERIFY_OK cases=80 brute_words=274560 extremal_words=6888 upper_bound_cases=16 singleton_boundary=3`. This finite check does not independently certify the general theorem. The 1996 and 1995 specialized sources were not both accessible as full text, and possible unrecognized prior coverage remains a limitation. Independent scientific validation has not been performed.
