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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.10 or newer and no third-party dependencies. The deterministic expected output is in `verification_output.txt`. The checker constructs every neighborhood and comparison complex from its facet sets rather than trusting quoted face vectors, calculates binary boundary ranks using bitwise Gaussian elimination, and verifies equality of the nerves of the two indicated contractible covers. It also checks the free-pair condition before each of the \(4k\) proposed collapses, compares the resulting graph's mod-two Betti vector with the original neighborhood complex and the intermediate comparison complex, and verifies the exact component and first-homology rank formulas.

It runs an exhaustive finite test over all labeled connected graphs on \(4,5,6\) vertices having exactly one simple four-cycle: \(9+240+6480=6729\) labeled inputs. Nine additional explicit inputs include two or three four-cycles meeting at a vertex or joined by a bridge, with and without an additional odd cycle, and graphs of maximum degree up to eight. The all-parameter conclusion is supplied by the proof in `RESULT.md`; these finite tests do not certify infinitely many graphs.

Review status: same-model review only; independent audit not performed. The checked data do not claim peer review, exhaustive literature coverage, or independent validation.
