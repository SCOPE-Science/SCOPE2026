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
# Computational verification

Both included programs use only Python 3 standard library and directly reconstruct their graphs. Execute `python3 verify_recursive.py` and `python3 verify_tabular.py` beside the embedded sources; each checks all expected starting scores and each possible legal second-move distance class for every starting vertex. Compare outputs byte-for-byte to `verify_recursive.out` and `verify_tabular.out`.

The first program performs memoized exact alternating minimax on 2,216 Heawood and 11,836 Pappus reachable \((\text{dominated mask},\text{next player})\) states. The second separately generates the incidence graphs and calculates the recurrence on all 16,384 and 262,144 dominated masks, respectively, for both turns. It asserts that all vertices have degree three and that all distance-class histograms and continuation scores agree with the declared theorem. The reference outputs end in `VERIFY_OK` and `INDEPENDENT_VERIFY_OK`.

Because each move enlarges the dominated set, backward induction on the finite mask partial order yields exact game values, not experimental estimates. Checks establish this finite theorem, not a general-family theorem or a global negative originality claim. No independently commissioned external audit was carried out.
