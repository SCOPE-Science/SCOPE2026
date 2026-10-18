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

Run `python3 verify.py` using Python 3 without third-party dependencies. The program exhaustively evaluates 65,536 local incoming/outgoing switch assignments on the 16 vertices of the binary order-four de Bruijn graph. It proves the single-cycle acceptance criterion by the Euler-tour correspondence and counts 2,048 accepted circuits. In an independently implemented depth-first generation, it reconstructs 2,048 distinct cyclic 32-bit words with every five-bit factor unique, compares the length-six Abelian-square counts, and validates the 528 reversal-complement orbits.

Observed execution output:

`ABELIAN_DEBRUIJN5_PASS pairing_assignments=65536 cyclic_tours=2048 direct_cycles=2048 orbit_classes=528`

All arithmetic and comparisons are integer-exact. Completeness follows from the two local bijections at each of 16 vertices and full enumeration of all 65,536 choices; a subset or a timeout would not establish the theorem. This verification concerns only binary order-five cycles and length-six Abelian squares. Independent mathematical validation has not been performed.
