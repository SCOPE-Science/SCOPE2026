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

# Verification

The standalone `verify.py` (Python 3, standard library only) independently tests 2-binomial equivalence by enumerating scattered subsequences for all binary words of length at most 10, and checks the substitution image property for source words through length 8.

It constructs a Thue–Morse prefix of 32768 symbols using binary digit sums rather than substitution; uses exact integer prefix sums and weighted sums to check all possible starting positions and root lengths 1 through 256 for 2-binomial cubes. It additionally checks direct scattered subsequence counts for four consecutive blocks through root 48 and exponents 3, 4, 5, and 7 through root 100 where divisible by four. Odd-root abelian-cube absence is separately tested for odd roots through 257.

Execute `python3 verify.py`. Expected success is six lines ending `VERIFY_OK`. The finite experiments cannot establish the unrestricted absence or existence for all parameters; the symbolic proof in `RESULT.md` does so. The review is a self-review only, with no independent audit.
