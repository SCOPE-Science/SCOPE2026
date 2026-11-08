---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Encode every two-chain linear extension as a monotone gap vector and queries as rectangular-grid ideal membership. The standard antichain argument gives VC=min(a,b). Independent direct enumeration of all 35 (3,4) interleavings gave the smaller root-branch counts rows (15,10,4,1),(5,13,13,5),(1,4,10,15): each root has at most 15 concepts in one branch, preventing depth five (requires 16 each). A separate memoized Littlestone recursion over exact membership-mask splits computed all twelve unordered positive two-chain profiles through total size seven: (3,4) has Ldim=4, entropy bound=5; every other profile saturates the bound. This validates the witness lower bound and minimality without relying on saved verification_output.txt. No claim is made for all chain sizes.

## originality

PASS

The exact claim is not established as a corollary or table entry in the inspected relevant material; foundational objects, algorithms and covered subclaims are separately credited. This is a qualified best-of-knowledge comparison, not absolute priority certification.

## value

PASS

This identifies a sharp and mathematically motivated first entropy-cardinality obstruction for adaptive shattering of linear extensions, with explicit difference from the static grid width. It gives a canonical small counterexample to assuming that concept-count information always controls online comparison depth. An exact first obstruction is useful without an all-parameter recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
