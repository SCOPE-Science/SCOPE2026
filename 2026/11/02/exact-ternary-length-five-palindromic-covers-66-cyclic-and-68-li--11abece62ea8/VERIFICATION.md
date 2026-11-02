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

# Exact certificate verification

Run `python3 verify.py` with `certificates.json` alongside it, under Python 3. The verifier enumerates the 27 ternary ordinary palindromes of length five and reconstructs the pairwise directed overlap costs. It validates each entry of the cyclic (27 vertices) and linear (28 vertices, including one dummy vertex) certificates, including vertex potentials, the positive weights of every nonempty proper directed cut, all distinct-vertex arc inequalities, and the exact sums of the dual objectives (66 and 68). It then constructs both witnesses directly from the permutation and overlap distances, checks that all 27 required substrings are present, and confirms the resulting lengths.

The expected terminal result is `VERIFICATION_OK`, with 702 cyclic arc comparisons and 756 linear arc comparisons. The arithmetic certificate supplies a proof of minimality for all possible covers via the degree-and-cut inequality, not an exhaustive search through potential source words. The code validates the provided finite certificate only; it does not prove that no separate mathematically equivalent statement appears in other literature. Independent scientific audit has not been performed.
