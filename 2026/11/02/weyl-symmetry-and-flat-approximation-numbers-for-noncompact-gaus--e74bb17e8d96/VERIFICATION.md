---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The literal frozen equality of distance to every compact operator is false: take T=I (γ=1 with all other coefficients zero) and the rank-one negative projection K=-P onto the constants; ||T-K||=2. The delivered RESULT.md instead asserts the sharp lower bound against each compact K, attained at K=0, which is what the proof establishes. The Sang–Zhao classification applies to the exact five-parameter kernel at p=q=2, gives compactness when γ=0, and forces |α|,|β|<1/2 and boundary equality |γ|²/D+2|N|=1 in the noncompact case. An independent direct check gives the same degeneracy: integrating the coherent-state output norm squared leaves the input quadratic (|γ|²/D-1)|w|²+2 Re(N w²); a strictly negative form would make the integral of ||Tk_w||² finite and hence T Hilbert–Schmidt. Comparing coefficients of z and conjugate w in the two displaced coherent outputs gives precisely the two equations in the record. Equivalently, conjugate the second equation and solve for v to obtain v=(γ-bar*u+2α-bar*γ*u-bar)/D; substituting into the first leaves (1-|γ|²/D)u-2N-bar*u-bar=0. At the boundary there is a nonzero u, and |2β|<1 ensures v is nonzero. Norms force the constant phase to have modulus one. Weyl powers run weakly to zero on any fixed vector while preserving its T-output norm, so compact K vanishes on that sequence in norm and ||T-K||≥||T||. This yields the essential norm and all finite-rank infima, not equality for each K. Conversely, finite monomial projections converge uniformly on a compact output image. In the explicit nonunitary example direct Gaussian integration gives ||Tk_w||²=D^{-1/2} exp(-(Im w)^2), nonconstant on unit vectors. No frozen script was executed.

## originality

PASS

What survives is the implication from the five-parameter noncompact boundary to a nonzero Weyl intertwining pair in the real phase plane, including arbitrary admissible linear terms. The essential norm and all approximation numbers are then determined by a general weak-convergence argument, not by a new theory of compact approximation. Known convolution multipliers and canonical or weighted-composition subfamilies already give some nonunitary behavior, but the sources inspected do not cover the full real-pair implication.

## value

PASS

For the full bounded noncompact boundary, knowing only failure of compactness does not determine even the first nontrivial approximation numbers. The theorem identifies a nonzero nondamping phase-space direction and uses it to show that no compact perturbation, of any rank, can reduce the operator norm. This uniform structural explanation survives the quantifier correction and extends beyond the known convolution, weighted-composition and unitary examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
