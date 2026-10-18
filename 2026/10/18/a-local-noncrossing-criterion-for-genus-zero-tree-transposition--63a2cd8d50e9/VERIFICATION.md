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

The theorem was checked independently in finite instances by running `python3 artifacts/verify.py` using only the Python standard library. The recorded stdout is `artifacts/verification_output.txt` and terminates in `VERIFY_OK`.

Exhaustive verification covered 688,147 distinct multiset words across 13 explicitly described trees, including all six unlabeled six-vertex tree shapes, and compared each product in a permutation representation with an independently implemented crossing test. It also checked the respective identity counts against the motivating paper's tabulated values. The verifier directly evaluated every contiguous factor of 347 selected valid words, checking Lemma 2 vertex by vertex. An additional 30,000 pseudorandom cases on paths and stars with six, seven and eight edges checked the equivalence outside that exhaustive range.

Finite checks neither establish the infinite theorem nor prove originality. The general conclusion depends on Lemma 1 (a bridge cannot appear once), Lemma 2 (cancellation normal form and fixed-point characterization for every contiguous subword of a locally noncrossing word), and the two-direction leaf induction in `RESULT.md`. Computation does not replace inspection of those arguments. External independent validation has not been performed.
