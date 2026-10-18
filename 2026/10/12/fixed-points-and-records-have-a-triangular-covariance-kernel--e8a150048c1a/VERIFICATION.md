---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Under I_i=1, prefix record probability is 1/(j-1) for i<j (other j-1 prefix positions are exchangeable and their maximum necessarily exceeds i), 1/C(n-1,j-1) for i=j, and 1/j for i>j. Subtract P(I_i)P(R_j)=1/(nj) to obtain the triangular kernel. The j-1 earlier positions contribute 1/(nj), canceling the diagonal -1/(nj), leaving 1/[n*C(n-1,j-1)]. Summation and known fixed-point Var=1 and independent-record Var=H_n-H_n^(2) give the claimed correlation. Independently enumerated all permutations n=2 through 7 with Fraction exact arithmetic, checking every i,j covariance and total. Finite checks are supplementary to the all-n conditional counting proof.

## originality

PASS

Best-of-knowledge acceptance follows the actual statement-versus-implication comparisons above; the strongest inspected primary sources establish a general framework, different problem, or strictly narrower subcase, not this final full claim. The explicitly listed plausible full-text access/implicit-coverage risks remain open; lack of search hits alone is not novelty evidence.

## value

PASS

The exact positional kernel disentangles the global fixed-point (cycle) and upper-record (order) statistics, identifies a nontrivial negative local-diagonal versus positive aggregate cancellation, and gives a quantitative finite-n and asymptotic dependence law. These are natural invariants of uniform permutations, not arbitrary refinements of a trivial count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
