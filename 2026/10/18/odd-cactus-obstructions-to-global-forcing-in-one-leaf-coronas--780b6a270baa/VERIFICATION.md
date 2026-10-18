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

The proof uses a bijection between core matchings and maximal matchings of the one-leaf corona; a nonempty alternating symmetric difference yields either a forbidden even cycle or a path with two omitted pendant endpoints. This establishes the necessity and sufficiency statements without exhaustive computation.

The standalone `verify.py` constructs all actual matching signatures and independently tests the graph obstruction characterization for all labeled graphs of order at most four, paths through order seven, cycles through order seven, and six additional named examples. It checks minimum cardinalities by direct comparison of every candidate observed-edge subset, then checks the graph-optimization formula. In finite path and cycle cases it also verifies the enumerative consequences. The script ends in `VERIFY_OK` when all assertions hold.

To reproduce: run `python3 verify.py` (Python standard library only). All arithmetic is exact integer arithmetic. Tests are finite and do not establish the universal theorem on their own; the argument in `RESULT.md` does. No formal independent audit has been performed.
