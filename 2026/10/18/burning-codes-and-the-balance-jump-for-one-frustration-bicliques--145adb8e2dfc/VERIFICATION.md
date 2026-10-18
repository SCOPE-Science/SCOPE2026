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

# Reproduction

Run `python verify.py` with Python 3.10 or later. The standard-library-only program independently implements the signed-burning spread/ignition semantics and enumerates all reachable terminal states. It verifies the theorem's code formula, Hamming distances for all switching masks in the tested family, the radius and the exact word-weight counts.

The checked profiles are all \(3\le a,b\le6\) plus \((3,7),(7,3),(4,7),(7,4)\), totaling twenty graph families and \(20{,}544\) distance evaluations. The script also enumerates full burning processes on all \(192\) switched signatures of two small graphs. The final output is `PASS 20 full graph-state families; 20544 distance comparisons; 192 entire switching-class enumerations`.

The infinite theorem is supported by the three-step process classification and the covering-radius proof in `RESULT.md`; enumeration does not prove unbounded cases. No independent audit has been performed.
