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

Use Python 3 without third-party packages. From the directory containing these files, run:

```
python3 verify_cover.py > reproduced_cover.json
python3 verify_eertree.py > reproduced_eertree.json
```

Compare the outputs against `verify_cover_output.json` and `verify_eertree_output.json`. All scripts and data are standalone. The first script derives the six-word finite cover from the Tribonacci and return-word morphisms, checks all relevant palindromic factors through length 11 and the exact 24/25-letter prefix transition. The symbolic fact that every length-at-most-11 factor occurs in this cover, together with absence of length-10 and length-11 palindromes, is the proof of universal absence at longer lengths. The second script independently checks the morphic coding and uses an online palindrome tree for a 100,000-symbol prefix; its finite extent is not a proof of absence at all lengths.

The morphic identification of the original Kimberling sequence with the Tribonacci coding is a cited prior theorem, not independently reproved here. An independent scientific review has not been performed.
