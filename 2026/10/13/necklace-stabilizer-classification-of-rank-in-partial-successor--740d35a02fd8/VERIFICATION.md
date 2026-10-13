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

# Reproducibility and verification

Run `python3 verify.py` with a standard Python 3 interpreter. The script has no third-party imports and deterministically reports:

`VERIFY_OK exhaustive_pairs=1020 counted_masks=65532 weighted_cases=449 constructive_samples=1320 stride_cases=394 max_n=42`

The tests independently build image-subset reachability graphs for every \(n\in\{2,\ldots,9\}\) and every active mask, comparing the exact BFS minimum image size with the translation-stabilizer prediction. For sizes \(2\le n\le15\), they exhaustively count all active masks by stabilizer size and by active-set weight and compare with unweighted and fixed-weight Möbius formulas. They also construct a quotient pair-merging word for selected small masks, 1320 pseudorandom masks with \(10\le n\le42\), and structured equally-spaced masks, then replay each word on the original automaton. They assert the stated constructive length bound.

Full-state BFS is exponential in \(n\) and is only performed through \(n=9\). The enumerations through \(n=15\) and word tests through \(n=42\) are finite checks; they do not prove the all-size theorem. The symbolic proof is in RESULT.md. Unindexed earlier literature may still contain equivalent results. Independent external audit: not performed.
