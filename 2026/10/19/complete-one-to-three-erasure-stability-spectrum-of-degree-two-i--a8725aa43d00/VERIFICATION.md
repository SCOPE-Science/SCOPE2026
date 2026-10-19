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

# Reproduction and limits

Execute `python icosa_erasure_check.py` with Python 3 and SymPy. The file constructs all twelve exact algebraic vertices, checks normalized moments through degree five, verifies the addition-theorem projection and complementary projection, evaluates every one-, two-, and three-row deleted principal minor with exact arithmetic, and verifies the 60/80/80 orbit partition. It prints `all exact checks passed` on success; all symbolic assertions are exact. The analytical proof in `RESULT.md` establishes the universal statement over the specific twelve-vertex set and its complete finite mask family. This is not an independent audit and does not verify novelty beyond cited literature comparisons.
