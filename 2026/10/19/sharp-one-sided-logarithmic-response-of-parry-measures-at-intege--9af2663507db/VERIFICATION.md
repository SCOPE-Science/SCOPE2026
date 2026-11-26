---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Parry series normalized by its integral is invariant: applying the transfer operator to each initial interval and telescoping the digits recovers the series, including when the orbit terminates. Subtracting its nonnegative defect vβ from Sβ=β/(β−1) gives the signed density (dβ−vβ)/(Sβ−dβ), where dβ=∫vβ. To check the exact digit cutoff, let Dₙ=ε(βⁿ−1)/(β−1) be the candidate endpoint defect. Given aₙ₋₁=1−Dₙ₋₁ on the maximal-digit block, βaₙ₋₁=b−Dₙ. Thus the digit at the preceding step n−1 is b−1 exactly when Dₙ≤1 (Dₙ>0); equality yields aₙ=0 and is correctly included. Equivalently Dₙ₋₁≤(1−ε)/β, so there is no index discrepancy. The maximal block has length floor(logβ(1+(β−1)/ε)); β^(−m)=O_b(ε), and its contribution to dβ is ε/(β−1) times ∑ₙ₌₁ᵐ(1−β^(−n)), with all later contributions O_b(ε). Hence dβ~ε log(1/ε)/[(b−1)log b]. On any [0,1−η] the terms present have Dₙ≥η or lie in the tail, giving vβ=O_{b,η}(ε) there. Nonnegativity and the mass asymptotic imply a concentrated endpoint measure in the scaling limit, and Sβ−dβ→b/(b−1). Probability TV is the positive-part integral of the signed density, bounded above by dβ/(Sβ−dβ); its lower bound over [0,1−η] is asymptotically at least 1−η times that upper bound. Let η tend to zero. Testing the weak limit with x gives the stated mean coefficient and sign.

## originality

PASS

The invariant-density formula and general logarithmic stability or failure of linear response are prior knowledge. The supported distinct claim is the explicit signed leading coefficient for every integer approached from below, with the matching sharp probability-TV asymptotic. The closest Resultary statement has the same structural response and proof device for a different double-base map and path; it does not specialize to the single-slope greedy β family here.

## value

PASS

The one-sided perturbation of a classical greedy expanding map at a full-branch integer base is a natural response problem. The sharp scale, signed endpoint term, and explicit coefficient determine which observables have nonzero leading response and how strongly the invariant law moves in probability TV. This is useful information beyond an order bound or a failure of differentiability for one observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
