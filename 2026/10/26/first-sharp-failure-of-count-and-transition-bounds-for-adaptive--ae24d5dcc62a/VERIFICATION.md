---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

One-turn selections cannot increase cyclic transitions: the arcs between consecutive selections partition the source cycle and each target change consumes a source change. The even alternating target of length t+2 and the constant targets above each symbol count give the bound. Independent integer-mask replay (python3 replay/1.py) enumerated every source rotation orbit for n=2 through 14 and marked target orbits from all increasing position subsets, stopping early only when none were left. It reproduced every census total; at n=14 the sole deficient orbit is 00000101111101 of size 14, covering all 14 six-letter necklaces and missing the seven-letter necklaces 0010011 and 0011011. Universality is downward closed by extending shorter targets. In the infinite family the two 00 blocks of 0010011 cannot both use the long zero run, since each path between target blocks includes a selected one. The block outside that run must use both singleton zeros, in the direction that skips the long one run and leaves only two eligible ones, not the required three. Each family member for a,b>=5 contains the length-14 exception as a one-turn selection and has B=7; composition of selections preserves one turn.

## originality

PASS

No inspected statement or table covers the exact adaptive-cut failure or persistent family. The strongest apparent overlap, a same-date Resultary distribution, explicitly excludes adaptive cuts. Priority is not inferred from the date.

## value

PASS

The count and transition bounds are dictated by unavoidable constraints on one-turn selections. Locating exactly the first failure of their sufficiency, with both an exhaustive cutoff and a structural obstruction stable under run inflation, gives a concrete test for stronger proposed characterizations of target-dependent coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
