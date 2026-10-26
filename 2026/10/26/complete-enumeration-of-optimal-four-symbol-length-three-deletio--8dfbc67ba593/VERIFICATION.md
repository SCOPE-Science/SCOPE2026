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

# Reproduction

With Python 3.10+ in this directory, run `python verify_cover.py`. The script is standalone, imports only standard-library modules, and exhaustively checks the finite domain of 64 three-symbol words and all unordered six-word subsets. It first computes every six-subset union using an exact integer subset DP; it then separately reconstructs every covering sextuple by lexicographic enumeration with a justified remaining-capacity pruning rule. It enumerates all 48 relabeling/reversal actions on each cover and counts the orbit and overlap profiles. The expected output is in `verify_output.txt` and ends `VERIFY_OK`.

The script asserts that all 74,974,368 six-subsets are represented by the DP, exactly 644 have full deletion-shadow union, exactly 120 of these have pairwise-disjoint shadows, and the orbit sizes sum to 644. These are complete finite calculations, not a test of an asymptotic statement. They do not independently establish scientific novelty; the prior-work comparisons and the identified residual risk are recorded separately. No external independent audit has been carried out.
