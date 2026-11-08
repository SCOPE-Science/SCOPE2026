---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Proved the leftmost greedy subsequence embedding criterion Phi(u)=|u|-number_of_even_candidate_runs+indicator(first_letter=1) <=r. Every minimal absent candidate has all odd runs, and if it starts with 0 then its first run has length at least three. Deletion effect and last-run exception yield Phi=r+1, or Phi=r+2 with final run long. Counting all-odd compositions via z/(1-z-z²) yields the three exact Fibonacci layers; r=1 gives {1,000}. An independent exhaustive subsequence algorithm enumerated all binary candidates for each r=1..7, matched exact lengths and counts; this is finite corroboration, with proof for all r from greedy/candidate-run arguments.

## originality

PASS

Kosche et al characterize generic absent subsequences and construct exponential MAS using larger alphabets, and Manea et al enumerate general MAS; this theorem evaluates the exact length spectrum for a restricted but canonical binary doubled-run input with a structural greedy certificate. The nearby Resultary Fibonacci extremal result counts shortest, not all minimal, absent subsequences of a different family.

## value

PASS

The exact length-resolved enumeration of minimal absent scattered subsequences on a simple periodic binary source is a natural word-combinatorics invariant, showing sharp localization into three adjacent length layers and Fibonacci growth; precise structural words can be needed for MAS automata and complexity benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
