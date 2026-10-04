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

Run `python3 verify.py`. The script uses only the Python standard library.

For every binary word of lengths \(1\) through \(16\), it constructs the multiset of compositions of all contiguous substrings of lengths one and two directly. Independently, it constructs the signature from symbol counts and run counts. It then checks that the two signatures induce exactly the same partition of all words, verifies the claimed class-size formula for every observed class, and checks the complete singleton classification word-for-word.

The exhaustive range contains \(131070\) words and \(1020\) ambiguity classes. A separate direct feasible-run-profile count checks the two parity formulas and the first-difference identity through \(n=500\).

Successful replay ends with `VERIFY_OK words=131070 n=1..16 classes=1020 formulas_n<=500`.

The finite checks do not prove originality and are not used to extrapolate the all-length theorem; the infinite statement follows from the run decomposition and exact sums in `RESULT.md`.
