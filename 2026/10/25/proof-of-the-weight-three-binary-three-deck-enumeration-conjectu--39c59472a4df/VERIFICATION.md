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

# Reproducible verification

Execute `python3 verify_three_deck.py` using Python 3 and only its standard library. The expected terminal line is `VERIFY_OK`.

The script computes complete length-three scattered-subsequence multiplicity vectors directly by dynamic programming for every binary word with exactly three ones and length from 3 through 24. At every length it checks fiber sizes, the explicit involution, the number of ambiguous pairs, and the rational-generating-function coefficient. An independent non-deck enumeration of gap vectors confirms the ambiguity count at lengths 3 through 100. Example outputs: at length 7 the number of words is 35, ambiguous pairs 1, distinct decks 34; at length 24 these values are 2024, 190, and 1834.

These finite tests do not certify the universal statement independently. The symbolic proof in `RESULT.md` establishes the exact criterion and count for every length. No outside software, precomputed database or hidden file is needed.
