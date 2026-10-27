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

# Reproduction and verification

Run `python3 VERIFY.py` using the standard Python 3 library. The verifier directly enumerates all binary roots consistent with each tested host length, constructs their concatenated powers, and checks scattered-subsequence membership letter by letter. It never uses the transfer-matrix embedding threshold to decide membership.

Its tested ranges are \(2\le q\le8\), \(0\le k\le18\) (133 parameter pairs), plus rational-recurrence coefficient tests over the same range; Lucas and Fibonacci jump checks for \(1\le m\le7\); and the root-length bivariate spectrum for \(2\le q\le6\), \(0\le k\le12\), and \(1\le|u|\le9\) where length permits. The expected successful completion message begins `VERIFY_OK 133`.

Proof verification relies on the exact greedy-pair lemma, the edge-weight formula for a concatenated power, the formal transfer-matrix trace identity, algebraic inversion, and standard Fibonacci generating functions. The finite tests do not prove the universal quantifiers. A fully independent mathematical audit has not been performed.
