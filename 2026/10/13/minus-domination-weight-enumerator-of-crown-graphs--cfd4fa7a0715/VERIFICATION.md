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

The proof reduces every closed-neighborhood inequality to one of two exact identities:
\[
f(N[a_i])=B+x_i-y_i,\qquad f(N[b_i])=A-(x_i-y_i).
\]
Taking the extreme pair differences proves the iff criterion without computational assumptions.

The enumerator is independently reconstructed from the nine possible labels on one matched pair. The five Laurent polynomials \(\Phi_d\) group pair states by the difference \(d=x_i-y_i\); inclusion-exclusion extracts exact minimum/maximum difference ranges, and coefficient truncation applies the feasibility inequalities.

A standalone exhaustive checker verifies every labeling for \(3\le n\le6\), compares the direct graph predicate with the structural criterion, compares every nonzero bivariate coefficient with the symbolic construction, compares every total-weight coefficient, and checks the complete minimum layer.

Replay output:

`VERIFY_OK n_range=3..6 labelings=597780 valid_functions=28559 criterion_checks=597780 bivariate_coefficients=94 weight_coefficients=32 minimum_checks=4 max_order=12`

The exhaustive range is finite and does not establish the theorem for larger \(n\); the symbolic proof supplies the general result. The boundary \(n=2\) is excluded from the theorem because its minimum-function classification is different.
