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

The analytic argument establishes the exact eigenvalues by monomial-kernel projection, handles exceptional angles directly, and derives ordered singular-value asymptotics from two-singularity Darboux expansion plus periodic/equidistributed phase counting. Exact quantifiers, kernel normalizations and all nonexceptional parameter restrictions appear in `RESULT.md`.

The supplied `checker.py` uses only the Python standard library. The current package's file was executed using `python3 checker.py`; it passed 1,446 finite assertions, including comparisons against independently assembled symmetric monomial rows, exact integer-coefficient formulas and the Hardy sine identity. Separate numerical ranks were also compared with the predicted constants at rational and irrational angles. Finite checking is not an infinite proof.

No external validation or independent audit is asserted. The fixed-angle Darboux bound is not uniform as the two singularities coalesce at either exceptional angle. Source coverage is based on identified sections and comparisons, with historical-priority risk stated in the review.
