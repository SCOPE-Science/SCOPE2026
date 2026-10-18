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
# Finite and symbolic verification

The proof supplies the unrestricted validity claim. The standalone `check.py` computes scattered-\(01\) subsequences of all rotations, without using the height formula to compute these counts, and enumerates all words for \(5\le n\le15\) at coprime interior weights. It verifies the cyclic spread lower bound, the missing value \(n\), exactly \(n\) words in each of the first two classes, correct class representatives, and both exact sets of scattered-pair counts. The actual run produced:

`CYCLIC_2_BINOMIAL_SPREAD_PASS n_range=5..15 coprime_classes=44 full_words_checked=33122 rotations_checked=457898 extremal_necklaces_checked=88`

For a general \(n\), the residue classes of the prefix-height walk prove the possible first two spread strata. The two modified steps in the runner-up construction are explicitly checked, and the exact counts follow by summing heights. This finite program neither proves exhaustive coverage beyond length fifteen nor certifies originality. No external independent audit has been conducted.
