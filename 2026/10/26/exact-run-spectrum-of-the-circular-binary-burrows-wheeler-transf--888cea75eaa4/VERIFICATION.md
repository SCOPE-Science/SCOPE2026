---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every length n>=4 binary word with exactly four ones, cyclic rotation to the distinguished one gives ordered gap vector g in N^4, sum g=n-4. There are n choices of marked position per ordered gap tuple and 4 choices of marked one per word, proving 4N_r(n)=n h_r(n-4). Sorting all rotations by decreasing zero-prefix gap level and successor-gap lexicographic comparisons yields each BWT bit exactly; ties have identical preceding bits. Every gap vector lies uniquely in a weak rank-pattern cell with gap rank jumps 1 or >=2, plus free minimal gap. The run count is invariant under these latter shifts for nonconstant patterns. The 365 finite pattern/jump cells exhaust all g, and each has a rational geometric enumerator; the exact finite polynomial identity yields H_1=1, H_2=(4z+2z^2+4z^3+z^4)/(1-z^4), the displayed H_4,H_6,H_8 and sum (1-z)^(-4). Independent direct rotation-sorting for every 4-one word n=4..13 matched the coefficients of all five rational generating functions (including n=9 counts 9,63,36,18). This test is finite; the 365-cell classification and polynomial identity prove all lengths. Independent reimplementation of the 365 rank-and-gap cells formed the exact common-denominator polynomial separately for each run class; all five symbolic numerator identities and the total (1-z)^(-4) were verified as polynomial identities over integers, not merely by truncated series.

## originality

PASS

The full 2017 small-content paper treats BWT fixed points, not the run distribution on all inputs; the 2023 full morphism paper characterizes changes under morphisms and r=2 balancedness, but does not state the complete fixed-weight-four distribution. No equivalent published indexed run generating function was identified. The result is a constrained, natural complete classification, not an invented general higher-weight law.

## value

PASS

The first natural nontrivial sparse binary stratum beyond small fixed content admits an exhaustive all-length run spectrum. Five explicit rational generating functions give exact frequencies and the sharp onset of eight runs at length nine, useful for fine-grained analysis of BWT repetitiveness. The 365-cell proof is a nontrivial self-contained symbolic classification rather than an arbitrary isolated length table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
