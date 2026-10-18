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

# Reproducible checks and boundaries

The result is a theorem for one exact natural parameter pair: ternary alphabet and cyclic window order three. Run `python3 check.py` with the files in this directory; compare standard output to `check.out`.

The checker constructs all 27 triples, identifies the three negated-reversal-fixed triples and twelve remaining orbit pairs, checks that fixed-vertex incidence signatures and invariant-cut crossing indicators agree for both members of every orbit, and computes their complete table. It confirms that the all-orbit incidence parity is `011` and all-orbit cut count is five; only the `121` orbit has the necessary signature `011`, and that orbit does not cross the cut.

Independently of the parity calculation, the checker explicitly tests every ternary cyclic word of lengths 10, 11, and 12 (767637 tested words). It obtains 320, 0, and 0 admissible labeled words, respectively. The period-ten word `0100112111` is directly checked against all ten cyclic windows and their negated reversals.

A finite brute-force computation does not establish an infinite nonexistence theorem. The actual proof is the twelve-orbit upper bound and the two closed-trail parity obstructions, which logically exclude every period greater than ten; the direct enumeration is an independent consistency check. No alternative alphabet, window size, maximizer uniqueness claim, or independent scientific review is claimed.
