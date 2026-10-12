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

Run `python3 verify.py` beside `certificate.json` using Python 3 standard library.

The verifier independently evaluates base-\(b\) digit sums for \(96\) combinations with \(2\le b\le9\) and \(1\le m\le12\). For every pair it reconstructs the predicted full two-letter language from allowed carries, checks the exact size and reversal-orbit count, and constructs an actual integer realizing each advertised pair. In the palindromic branch it constructs both length-three palindrome orientations for every alphabet residue by separating their high digits.

For \(63\) combinations it independently computes a finite digit-sum prefix of length \(36000\) and tests all occurring factors of lengths \(1\) through \(6\). It checks the absence of reflected pairs in the appropriate cases and the condition that every reversible length-three factor is palindromic. The prefix may miss factors requiring very long carries; therefore it is not used to prove any factor set is complete. A separate finite symbolic shape enumeration checks the binary-base difference-pattern obstruction for moduli \(3\) through \(29\).

The infinite theorem follows from the carry identity, additive-shift lemma, complete local-pattern proof and explicit witnesses in `RESULT.md`, not from extrapolating experimental enumeration. No independent audit has been performed.
