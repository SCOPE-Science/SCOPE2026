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

The reproducibility artifact `verify_gluing.py` runs using Python 3 and its standard library only. Run `python3 verify_gluing.py` in the same directory as the extracted files.

The direct breadth-first distance reconstruction enumerates every convex subset and every Boolean support trace on each tested graph. It verifies both unrooted and rooted cycle polynomials for lengths 3 through 12; 1,089 ordered pairs from 33 representative rooted graphs of at most four vertices; and six further bouquets (including the triple-pentagon case). The exact final marker is `ALL_ARTICULATION_SHATTERING_CHECKS_PASS`.

The proof for all graphs and every cycle length is mathematical, not extrapolated from the finite checks. Neither independent audit nor exhaustive historical-priority verification has been performed.
