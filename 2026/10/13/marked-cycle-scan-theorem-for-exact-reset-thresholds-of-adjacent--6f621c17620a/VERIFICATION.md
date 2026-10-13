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

# Mathematical verification

## Symbolic proof checks
The inverse of the rotation shifts the left endpoint of every cyclic interval one state backward without changing size. An inverse marked unitary letter increases size by one precisely when its target is the current left endpoint, and the new left endpoint is the predecessor; otherwise it preserves/shrinks size without moving the left endpoint, or produces the empty set. Each enlargement is thus tied to a marked site in a consecutive backward cyclic scan. This proves the lower bound by the number of necessary enlargements; the explicit scan gives equality.

For two marks, the even case needs an odd count of visits, achieved after full turns and one additional marked step; the odd case needs an even count, achieved after full turns and a shortest marked-to-marked directed gap plus one step. In both cases the formula remains meaningful for the smallest allowed state counts.

## Executed reproducibility check
Run `python3 artifacts/verify.py` (Python standard library only). Executed output:

`VERIFY_OK automata=793 interval_cases=6083 complete_subfamilies=n2..8 random_and_two_pin=n9..11 one_pin=(n-1)^2 two_pin_parity_gap=checked forward_BFS=independent backward_witness=replayed`

The checker tests all nonempty marked subsets for state sizes 2 through 8, selected two-mark and deterministic sample cases through 11, 6083 inverse-interval cases through size 12, and verifies each constructed reset word forward from the entire state set. Finite tests are consistency checks, not infinite certificates.

## Limits
No independent audit has been performed. General automata and nonadjacent mergers lie outside the result; an inaccessible full text and possible unindexed equivalent calculations are originality risks.
