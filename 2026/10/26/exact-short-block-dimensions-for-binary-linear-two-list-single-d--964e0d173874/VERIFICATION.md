---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Each k-subspace has a unique reduced-row-echelon generator. For each pivot pattern all free nonpivot bits are enumerated and every codeword and its distinct deletion outputs checked. For k+1 excluded at each n, no larger subspace can pass because list-size-two is inherited by subcodes. Independently compiled C++ gave 10,795 tested n=8,k=6, 788,035 tested n=9,k=6 and 6,347,715 tested n=10,k=7, zero admissible in all; the source RREF exhaustion counts and witness dimensions for n<=9 are inspected. At n=10 the explicit rank-six matrix has deletion parent histogram exactly (220,232,60), and direct independent check verified this. Exhaustion is only for declared n,k, not all lengths.

## originality

PASS

Verma–Hollanti–Tajeddine generalized half-Singleton treatment singles out binary complications; its stated asymptotic and generalized bounds do not determine this exact finite binary linear deletion-only table. Liu–Tjuawinata–Xing studies list decoding of insertion/deletion through general constructions. Resultary nearby codes differ in linearity, deletion number, output channel or question. Earlier unindexed exhaustive dimension tables remain possible.

## value

PASS

The first ten exact dimensions and minimal length for transmitting six linearly encoded information bits with two-list one-deletion reception are a natural sharp short-block synchronization-coding threshold, not an arbitrary slice; it is useful for baseline coding constructions and bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
