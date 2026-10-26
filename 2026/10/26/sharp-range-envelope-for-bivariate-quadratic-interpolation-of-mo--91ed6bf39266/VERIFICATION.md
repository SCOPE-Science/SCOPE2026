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
# Reproducibility and scope

The proof in `RESULT.md` is a symbolic argument valid for every continuous evaluation point in the closed unit square and every real bounded coordinatewise monotone array. The critical bounds are elementary polynomial signs and the identity of a shared upper-right dominating sample. It does not rest on a solver or finite enumeration.

`python3 check_q2.py` uses standard-library exact fractions. It verifies all twenty extreme increasing \(3	imes3\) binary arrays at a \(17	imes17\) rational evaluation grid, checks both exact equality examples, and checks the tensor weights sum to one. The grid check is deliberately finite and cannot by itself establish a continuum theorem. The proof, full known source identity, and literature comparison are contained in the other files; independent audit is not performed.
