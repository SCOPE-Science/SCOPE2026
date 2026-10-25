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

The proof checks the restriction-property quantifiers for every nonnegative-integer count vector and uses the strictly positive Poisson probabilities to pass from almost sure to pointwise. The classification is a complete induction, not a numerical extrapolation. Its pointwise realization uses one atom added at each integer exploration time; an observed-count stopping time picks the first positive increment or the final query.

The attached `verify_atomic_stopping.py` has been executed with Python and completed without assertion failures. It enumerates stopping maps by exact cylinder covers, independently enumerates partial-permutation prefix maps, compares the two sets, and prints the following counts: for binary alphabets and atom counts \(n=0,1,2,3,4\), respectively \(1,2,5,16,65\); for ternary alphabets and \(n=1,2,3\), respectively \(2,5,16\). These are complete finite enumerations only for the stated truncated state spaces. They do not certify the unbounded-count theorem, which is proved separately.

Source review compared the finite-atomic, at-most-one-occupied-**location**, pointwise statement with the diffuse at-most-one-**point** theorem in arXiv:2610.22011v1, and with the general stopping-set framework and nonattainability example in arXiv:2101.07180v3. A general classical equivalent hidden in other finite sequential search literature has not been ruled out. No independent scientific validation has been performed.
