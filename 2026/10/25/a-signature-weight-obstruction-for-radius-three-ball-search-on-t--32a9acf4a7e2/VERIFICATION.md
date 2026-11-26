---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Distinct answers require injective signatures. Seven or fewer bits cannot encode 256 vertices. At eight bits a bijection would require 128 ones in each column, but a closed radius-three ball contains 1+8+28+56=93 vertices. At nine bits the total weight is 837; the exactly 256 words of weight at most four have total weight 837 and form the unique minimizing set (the next available words have weight at least five). Thus all those signatures are forced, and any two columns have 1+7+21=29 simultaneous ones. For distinct centers c,d, translation by c⊕d pairs points of the intersection without fixed points, so it has even size; with identical centers the intersection has size 93, not 29. Independent direct XOR enumeration of all 32,640 pairs of distinct centers (`python -B /workspace/branches/replay_records_1_3_4_5.py`, section 3) confirms the frozen table 93,58,58,38,38,20,20,0,0 by increasing distance including the identical case. The proof is for nonadaptive, fixed closed radius-three balls and gives only a lower bound; it does not supply a ten-ball system or determine the exact optimum. The erroneous arXiv identifier in reference 2 is bibliographic, not an input to the proof.

## originality

PASS

In the checked evidence, the near-half-radius Q7 construction and general uniform-size separating bounds do not yield the two extra queries at Q8. Requiring both uniqueness and coverage changes the problem; no inspected same-parameter covered-code result implies this lower bound. The new step beyond the signature weight bound is an equality-case incompatibility with Hamming-ball intersections. This is a bounded best-of-knowledge decision, not a historical priority claim.

## value

PASS

Dimension eight at the same radius is the immediate neighbor of the information-theoretically sharp seven-query Q7 example. The bound rules out even a one-query overhead over the eight-bit capacity threshold; equal ball sizes alone do not rule out nine via the first moment. Rigidity of the extremal signature set and its incompatibility with Hamming-ball pair intersections give a substantive, checkable obstruction, without claiming the optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
