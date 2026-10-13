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

## Checks performed

The included pure-Python program `verify.py` builds the forbidden-edge graph and determines exact independent-set maxima by graph decomposition and dynamic programming, separately from the Legendre-symbol/projective-order formula. It checks every nonzero target for every prime between 5 and 199. For primes through 13, an additional independent brute-force search enumerates all subsets and tests the original two avoidance conditions directly.

The program passed 4,178 prime-target comparisons, including 671 instances of the exceptional one-unit loss, and reproduced three stated examples. Recorded output is provided as `verification_output.txt`. Reproduce with `python3 verify.py` in the same directory; only Python's standard library is needed.

## Limits

No finite test is used as a proof for infinitely many primes or targets. The deductive proof relies on alternating-color component structure and diagonalizable projective dynamics. No independent audit is claimed.
