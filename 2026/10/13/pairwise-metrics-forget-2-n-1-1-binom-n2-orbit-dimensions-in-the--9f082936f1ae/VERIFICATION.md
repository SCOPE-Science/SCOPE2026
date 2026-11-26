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

Every nonnegative weighted sum of unordered cuts is realized by a weighted Boolean-coordinate embedding in L1; injectivity is exactly positive separation of each pair. Finite universality gives realization of every admissible vector, and ultrahomogeneity extends the label-wise diversity isomorphism exactly when the vectors agree, using uniqueness of the diversity cut decomposition. The rows of the pair-cut map are independent: twice each edge coordinate is the sum of its two endpoint singleton columns minus the column of the two-point cut (using the complementary representative if needed), with n=1 and n=2 immediate. Thus the fiber near a strictly positive vector is open relative to its translate of the kernel. The image of the positive orthant is nonempty and open by full row rank, and positive nullity at n=4 persists thereafter since successive differences are 2^(n−1)−n. The four-point perturbation adds one weight to each singleton cut and subtracts one from each two-plus-two cut; each pair sees net zero and the full-set value sees net one.

## originality

PASS

Cut-coordinate uniqueness, classical metric cut geometry, the universal ultrahomogeneous diversity, and the existence of some loss of information under pairwise restriction are prior. The supported distinction is the sharp quantitative orbit-fiber result on an open set, including the exact first arity and a four-point witness, not the bare observation of nontrivial fibers.

## value

PASS

The result supplies a sharp observability threshold for a canonical homogeneous structure: labeled pair data suffice through three points but leave an explicit positive-dimensional continuum of inequivalent full configurations on an open set from four points onward. The exact arity dependence and the four-point perturbation are usable in distinguishing what the reduct does and does not retain; qualitative nonhomogeneity alone would not give these facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
