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

# Verification protocol

Run `python3 verify.py` with standard-library Python 3. This checks: the full four-palette state/transition inventory (84 states and 84 transitions); the permutation cycle profile (six 2-cycles, six 4-cycles and eight 6-cycles); every representative cycle; cyclic admissibility of all three five-color template words; concatenated five-color constructions for odd lengths through 99; exact five-palette traces for circumferences 3, 5, 7, 9 and 11; and independent direct vertex-level backtracking comparisons at (palette size, circumference) (4,3), (4,4), (5,3), (5,5) and (5,7).

These are complete finite checks for the explicitly defined four-palette transition system and template words, plus bounded corroborating experiments for five-palette counts. The proof of the infinite conclusion uses color-permutation equivariance for the representative transition classification, the explicit concatenation construction, and transfer-matrix walk counting; it does not infer an infinite statement merely from the finite test range. Neither a separate expert review nor an independent mathematical audit has been performed.
