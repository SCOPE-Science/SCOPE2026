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

# Reproducibility

With Python 3, execute `python verify.py` in the folder containing `verify.py`. The program constructs all six-ranking anonymous ballot vectors for each electorate from one through ten, computes their position matrices and head-to-head winners directly, and compares every such profile to the integer-fiber theorem. It checks that all matrices have at most two distinct possible Condorcet winners, that none have two before five voters, and that the five-voter ambiguity consists exactly of three labeled matrices with the stated multiplicities. It separately enumerates all ten-voter fibers and certifies the first even-parity boundary, including its three matrices and conditional weights. It also checks strictly log-concave multinomial counts on every fiber with three or more members.

The finite enumeration is exhaustive over the explicitly reported finite layers because it recursively iterates every weak composition of the electorate size into six ballot counts. It is not a proof for arbitrary electorate sizes; those statements follow from the closed linear parametrization, cyclic-triple argument, and exact weight-ratio calculation in RESULT.md. The computation uses integer arithmetic throughout. No external data or inaccessible artifact is needed.
