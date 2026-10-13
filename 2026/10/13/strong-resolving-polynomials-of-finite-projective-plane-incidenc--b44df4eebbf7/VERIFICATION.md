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

# Reproduction and proof boundary

From the directory containing `verify.py`, run `python3 verify.py` with Python 3.8+ and no third-party dependencies.

The program constructs \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\) using normalized nonzero vectors and equation \(a\cdot b=0\) over prime fields; independently computes graph distances, enumerates mutually maximally distant pairs, confirms they agree exactly with the nonincidence relation, counts all independent complements by exhaustive subsets, and compares every coefficient with the closed form. It also checks inclusion-maximal independent sets.

Recorded output:

```text
VERIFY_OK PG(2,2) points=7 lines=7 MMD_edges=28 all_independent_sets=332 strong_bases=2
VERIFY_OK PG(2,2) independent_counts={0: 1, 1: 14, 2: 63, 3: 112, 4: 84, 5: 42, 6: 14, 7: 2}
VERIFY_OK PG(2,2) maximal_independent_sets={4: 14, 7: 2}
VERIFY_OK PG(2,2) exhaustive_strong_resolvers=16384 count=332 poly={7: 2, 8: 14, 9: 42, 10: 84, 11: 112, 12: 63, 13: 14, 14: 1}
VERIFY_OK PG(2,3) points=13 lines=13 MMD_edges=117 all_independent_sets=16721 strong_bases=2
VERIFY_OK PG(2,3) independent_counts={0: 1, 1: 26, 2: 208, 3: 728, 4: 1534, 5: 2600, 6: 3432, 7: 3432, 8: 2574, 9: 1430, 10: 572, 11: 156, 12: 26, 13: 2}
VERIFY_OK PG(2,3) maximal_independent_sets={5: 26, 13: 2}
VERIFY_FINISHED all invariants established
```

For \(q=2\), the direct test considers all unordered vertex pairs and all \(16384\) candidate landmark sets; it does not merely check an MMD-derived formula. For \(q=3\), all possible independent point/line subsets are enumerated and compared with the formula. Neither finite instance certifies the claim for arbitrary \(q\). The self-contained proof in `RESULT.md` establishes the general theorem from the axioms of a finite projective plane. No independent external mathematical audit has yet been performed.
