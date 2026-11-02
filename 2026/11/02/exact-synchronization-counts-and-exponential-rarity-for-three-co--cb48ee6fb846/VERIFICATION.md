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

Run `python3 artifacts/verify_count.py` from the package root. Its output should match `artifacts/count_output.txt` and end in `ALL_COUNT_CHECKS_PASS`.

Compile `g++ -O2 -std=c++17 artifacts/verify_dynamics.cpp -o verify_dynamics` and then execute `./verify_dynamics` from the package root. Its output should match `artifacts/dynamics_output.txt` and end in `ALL_DYNAMIC_CHECKS_PASS`.

The counting program independently computes the symbolic inclusion–exclusion formula and a column-mask dynamic program for several finite rectangles. The transition-graph program visits all states of seven small rook graphs and calculates reverse-reachable synchronization basins from each of the three constant configurations. The combined independently analyzed finite state spaces contain exactly \(1,148,985\) labelled configurations; they do not prove the theorem for all dimensions. The infinite proof appears in `RESULT.md`, including the row-type upper bound which is not inferred from sample counts.

The manuscript's general synchronization criterion and diameter bound are established literature and are explicitly identified as such. No external independent review, infinite computation certificate, or expert verification has been performed.
