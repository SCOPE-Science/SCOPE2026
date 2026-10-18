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

# Reproducibility and checks

The proof in `RESULT.md` is self-contained. Execute `python3 verify.py` using Python 3 and the standard library. The exact expected console output is embedded as `verification_output.txt`.

The verifier enumerates every one of the 21,147 set partitions of the labeled \(3\)-by-\(3\) array and tests independence, domination, and each block's independent-coalition partner from scratch. Exactly 54 valid partitions occur, all of cardinality six; their three omission-pattern multiplicities are 12, 36 and 6. For each \(4\le n\le8\), it enumerates all partitions obtained from zero through three disjoint nonattacking cell pairs and leaves the other cells singleton. It rules out all candidates with fewer than three pairs and confirms that precisely the two families proved in `RESULT.md` attain the optimum. Counts are 36, 80, 150, 252 and 392.

The standalone exhaustive tests neither assume that no other larger-block partitions exist nor establish the unrestricted theorem; those statements follow from the independent-dominating-set lemma and the general proof. Computation is used only to check finite instances and the exceptional finite count independently. No formal proof assistant or independent audit was used. The risk of unlocated equivalent literature remains.
