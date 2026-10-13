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

With Python 3 standard library installed, run `python3 verify.py` from this directory. It reads `representatives.csv` and verifies all 220 canonical codebooks, exhaustive admissibility at sizes 8 and 9, the double-syndrome construction, monotone-word statistics, and preservation of the deletion-confusability relation by all symmetry generators. The expected success line begins `VERIFY_OK rank_del_S5=8 labeled_optima=1568 classes=220`.

With a C++17 compiler, run `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`. This second implementation separately constructs the standardized-deletion bit masks and searches all index-increasing candidate sets of sizes 8 and 9. Its success line begins `INDEPENDENT_VERIFY_OK n=5 maximum=8 labeled_optimal_codes=1568`.

These programs constitute two ordinary finite proof replays, not external or infinite certification. Their search is exhaustive because any admissible subset has a unique increasing-index presentation and branch pruning occurs only when too few compatible candidates remain. The conclusions are exact for five-cell permutations but say nothing about larger blocklengths. No independent audit has been performed.
