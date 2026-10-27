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

# Exact finite factor-language check

Run `python3 verify.py` from this directory. The script requires only Python 3 and has no external dependencies or network use. It explicitly derives the six-letter coding from the original two-letter morphism using ten decorated-position states, checks all ten commuting identities, and certifies the stable eight-pair language of the six-letter uniform fixed point.

The key exhaustive identity uses the eight 50-character words `tau(g^2(xy))` for the eight permitted adjacent state pairs `xy`. Their length-24 and length-25 factor sets contain 78 and 81 distinct binary words respectively, none palindromic. The exhaustive 25-entry palindrome-complexity vector sums to 37, with exactly two length-23 palindromes. The parity-center argument excludes all larger lengths.

For every six-letter source state the script checks that its second iterate contains all eight allowed pairs and its fourth iterate contains all 37 palindromes after coding. A block-alignment argument then proves the result for **all** length-1249-or-more factors, without an infinite computational search. Separately, the script generates a long word directly from the original binary morphism and compares all its factors through length 25 with the certified pair-block language; this is corroboration, not the infinite proof.

Limitations: the sufficient cutoff 1249 is not proved optimal; a finite verifier cannot establish novelty, and this verification is not independent mathematical audit.
