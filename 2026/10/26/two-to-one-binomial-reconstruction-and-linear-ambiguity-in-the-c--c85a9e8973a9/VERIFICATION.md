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

Run `python checker.py` with Python 3 in the same directory. The code enumerates the finite morphic words, checks direct factor coverage by the two families, verifies one-to-one family signatures, tests the constructed partner identities and non-identity, and confirms that all enumerated binomial fibers have size at most two at scales \(3^k\) for \(1\le k\le7\).

Expected final line: `PASS: all finite construction, covering, injectivity, and ambiguity checks`. The proof of the theorem is the all-integer argument in `RESULT.md`; enumeration covers only those seven finite scales and cannot verify the statement for every \(k\ge3\). The claim makes no general assertion about the exact total number of ambiguous classes beyond the constructed lower bound. Independent mathematical review has not been performed.
