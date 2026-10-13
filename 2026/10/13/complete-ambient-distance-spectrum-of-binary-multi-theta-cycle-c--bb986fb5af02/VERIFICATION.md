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

Run `python3 verify.py` with Python 3.8+ and the standard library. The script prints `VERIFY_OK` only if every assertion succeeds. It first builds the edge set of an actual equal-path multi-theta graph and computes its incidence-kernel binary words from vertex parity, then compares them with the repeated parity-check construction. For each of five small-to-moderate parameter pairs it evaluates every ambient word's minimum distance to the entire code independently of the closed-form polynomial and compares the observed distributions. It checks each deep hole's count of nearest codewords, as well as the covering radius and exact number of deep holes.

Successful test instances include four paths of length two, three, four, and five, and six paths of length two; five larger instances check algebraic mass, codeword count, top degree and top coefficient without exhaustive enumeration. The independently enumerated parameter pairs yield (radius, deep-hole count, nearest codewords per deep hole): `(4,2)`: `(4,16,8)`; `(6,2)`: `(6,64,32)`; `(4,3)`: `(5,648,4)`; `(4,4)`: `(8,1296,8)`; `(4,5)`: `(9,80000,4)`.

The verification code is finite-case evidence only; the proof in `RESULT.md` establishes the universal parameter statement. The checks do not certify novelty, literature priority, independent auditing, or claims about unrelated graph families.
