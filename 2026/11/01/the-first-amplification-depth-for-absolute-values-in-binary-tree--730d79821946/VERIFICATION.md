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

The analytic reduction is stated in `RESULT.md`: each node oscillation is the maximum of finitely many linear forms, and, on each sign cell, each output root oscillation is another explicit linear form. Exact nonnegative rational dual weights in `certificate.json` bound every output form by the input seminorm. Tree automorphisms and global sign reversal reduce all possibilities to 910 cases; `verify.py` checks the orbit enumeration from first principles, rather than trusting a stated count.

Run `python3 verify.py certificate.json`. This exact-arithmetic check was executed against the two package files and yielded:

`EXACT_CERTIFICATE_OK cases=910 constraints=290 automorphisms=128 dual_terms=4739 max_bound=1 depth4_ratio=41/40`

The program checks uniqueness and total coverage of all canonical sign/subset cases, nonnegativity of every rational dual coefficient, the sum-of-weights bound, exact equality of all 8 coefficient coordinates in every case, and the two depth-four benchmark seminorms. It uses only standard-library `fractions.Fraction` arithmetic. The finite proof covers all real vectors through the sign-cell decomposition; it is not an experiment on a finite sample of vectors. The pre-existing two-/four-atom folding inequality is used to handle proper descendant nodes. Neither correctness nor originality has been independently audited.
