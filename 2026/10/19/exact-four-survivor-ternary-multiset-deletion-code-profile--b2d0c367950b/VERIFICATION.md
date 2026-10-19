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

# Verification

The source file `check.py` and output file `check_output.txt` reproduce all computational checks with the Python standard library. Run `python3 check.py` in this directory. The program calculates multiset intersections directly using exact integers, validates the explicit size-five incompatible-triple cover and size-six receiver certificates, checks every witness, and independently rules out larger compatibility cliques for every \(5\le n\le10\). Additional finite structural checks at lengths \(11,12,17,32\) are diagnostic only.

The finite search does not certify any unbounded statement. The infinite range follows from the written heavy-coordinate injection and the elementary bound \(x_0+x_1+x_2\le9\) for all-light vectors. The review is internal self-review only; independent audit and independent validation have not been performed.
