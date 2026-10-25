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

# Reproduction and limits

Run the included `verify_cograph.py` using Python 3.8 or later: `python3 verify_cograph.py`. Expected stdout: `VERIFY_OK direct=91 finite_state=216 witness=456`.

The first enumerator directly forms all induced four-vertex paths and checks every vertex subset for \(1\le k\le7\), \(1\le n\le13\). The independent finite-state computation checks optimal values and uniqueness for \(1\le k\le4\), \(1\le n\le54\) using only the previous \(3k\) choices. A third constructor validates the periodic sharpness witness for \(1\le k\le12\), \(1\le n\le38\). All comparisons use integer arithmetic.

The infinite assertion is proved in `RESULT.md` by a local \(2k+2\)-window induced-path obstruction, explicit constructions, and a backwards rigidity argument. Finite enumeration is not asserted to be proof for unbounded parameters. Independent audit has not been performed.
