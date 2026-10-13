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

The proof establishes a channel identity through commuting idempotent local replacements. For every sequence of selected sites the resulting channel depends only on the selected set; full coverage gives the full preparation channel. Conditional mixture gives the completely bounded upper bound, and the product of orthogonal local input states gives equality without an ancilla.

The weighted finite-time formula follows from inclusion–exclusion; the uniform profile follows by dominated convergence in the inclusion–exclusion series. The classical comparison follows from the Walsh-character chi-square upper bound and the magnetization lower bound. None of these conclusions relies on a finite numerical extrapolation.

Reproduce the finite-dimensional checks with `python verify.py` after installing dependencies from `requirements.txt`. The script contains seeded random state tests, direct Kraus channel propagation, exact subset-mask coupon probabilities, ancilla-reference tests, product witnesses, biased qubit–qutrit tests, and large finite occupancy tests. Expected success message: `VERIFY_OK 122 independent Kraus, reference, masks, inclusion-exclusion and Gumbel tests`.

Numerical checks are finite and approximate. They do not establish priority, mathematical independence of verification, or validity for dynamics outside the stated commuting pure-reset family.
