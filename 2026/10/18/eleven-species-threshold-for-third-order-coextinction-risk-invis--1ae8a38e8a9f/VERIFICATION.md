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

Execute `python3 verify_coextinction.py` with any Python 3 runtime supporting `int.bit_count()` (Python 3.8 users can replace it with `bin(x).count('1')`). The checker needs only Python's standard library, with no external data or libraries.

Its exhaustive enumeration uses the exact combinatorial bijection between pollinator neighborhoods and multisets of three-element plant subsets. It checks all totals from four to ten vertices, including connectedness and all one-/two-plant risk-signature collisions. This establishes the finite minimum only within the stated graph and failure model; it does not assert general uniqueness of the network pair or any infinite classification.

It also constructs the explicit eleven-species graphs, checks each pollinator degree and the labeled pair signatures, computes all twenty plant-triple neighborhood unions, and independently enumerates all thirty-two failure outcomes at failure probability \(1/2\). The counts are \((13,12,0,6,0,0,1)\) and \((14,9,3,5,0,0,1)\), for loss counts zero through six. Exact rational moments give shared mean \(9/8\), variance \(123/64\), and third central moments \(1095/256\) versus \(1047/256\).

The unrestricted failure-probability identity follows from symbolic counting by union size, not from numerical interpolation. There is no proof here for correlated failures, unequal pollinator risks, forbidding identical pollinator neighborhoods, or arbitrary pollinator degrees.
