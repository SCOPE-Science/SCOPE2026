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

The theorem concerns one-attempt, opposite-species-only exclusion on the integer line, with independent uniform arrival times and independent \(A/B\) proposal labels. Its proof uses the half-line linear differential system, independent exterior conditioning for the all-\(A\) interval event, and inclusion-exclusion for maximal cluster intensities. The closed-form function \(H_p(t)\) agrees with the independent finite-half-line polynomial recursion within the proven factorial truncation bound.

Run the self-contained Python standard-library program `verify_runs.py`. It enumerates every active-site subset, priority ordering and attempted-color assignment for finite paths of lengths three through seven, with three rational biases and two observation times, and checks 270 independently enumerated all-\(A\) interval probabilities in exact rational arithmetic. Further assertions test boundary approximations and the geometric intensity sums. The replay in this package is expected to produce 360 passed assertions, 1,146,639 exhaustive histories and 270 joint-event comparisons; finite checks provide reproducibility but are not a substitute for the infinite-volume proof.

The finite-path checker samples no unpublished data, uses no external libraries, and requires no remote assets. All hypotheses, normalization, unproved extensions and prior-work distinctions appear in `RESULT.md`. Independent audit remains unperformed.
