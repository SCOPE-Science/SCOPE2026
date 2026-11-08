---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The unique gap-necklace encoding (positive zero-gaps between successive ones) preserves rotations, including imprimitive necklaces. Window accounting gives A+4B+3G+2E=n and all eight constrained gram counts. Burnside rotations with repetition d, multinomial gap types and stars-and-bars excess distribute every feasible fiber. Singleton cases follow from changes in cyclic type orders or long-gap excess. Rational generating functions and their uncancelled cyclotomic poles imply least periods 12 and 6. Independent literal four-gram enumeration checked all admissible necklaces for every n<=14, including n<4 wraparound and first ambiguity at n=9.

## originality

PASS

Kiah–Puleo–Milenkovic 2015 proves quasipolynomial asymptotic profile counts for constrained de Bruijn systems, not this explicit fiberwise necklace Burnside formula or singleton classification. Chee et al 2024 study maximum length RLL de Bruijn sequences with distinct-window objectives, a different statistic.

## value

PASS

The exact zero-error read-multiset capacity and complete reconstructibility/ambiguity classification for a biologically motivated constrained four-gram channel quantify information loss beyond asymptotic Ehrhart estimates, including a sharp first failure length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
