---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The unrestricted incidence-cover formulation is exact: deleting any one of five positions, with duplicates ignored, is equivalent to obtaining the target by one insertion. I rebuilt the 243 target rows from insertions into the 81 possible centers, independently checked that the displayed 31 distinct words meet every row, and excluded all covers of size at most 30 with a separate exact integer-arithmetic proof replay. Every branch fixes one selection bit to 0 or 1. Unit rows force their one remaining bit; duplicate rows and rows containing another residual row are redundant. At each bound leaf, nonnegative integer multipliers y_i applied to the residual covering rows give a scaled lower bound D times the number already selected, plus sum_i y_i, plus sum_j min(0,D − sum_{i containing j} y_i), where D=1000000. The last term minimizes each residual coefficient times a 0–1 selection bit. Every bound leaf's integer score is strictly above 30D. The standalone replay checks both children of all 357 splits and all 358 bound leaves: the result does not rely on the numerical LP that suggested the multipliers, or on reported HiGHS MIP optimality.

## originality

PASS

No checked earlier result establishes the exact unrestricted 4-to-5 ternary optimum. There is demonstrable exact coverage and a matching witness in the later-catalogued November 8 Resultary record; the November 2 record also prints the witness. These are not mathematically distinct statements of the unrestricted value or construction, and the shared witness does not establish independent discovery. Neither of those records is evidenced here to predate the frozen work. The pass is a bounded judgment at the frozen record, not a claim of global priority.

## value

PASS

The length-four center case is the natural next ternary single-insertion covering invariant after the exact length-three case. The precise minimum 31 with an explicit cover is an independently useful finite benchmark: the elementary volume count is only ceil(243/11)=23, which does not answer whether a candidate construction of size 30 is possible. The unrestricted minimum also provides the natural baseline for quantifying a symmetry or additional channel constraint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
