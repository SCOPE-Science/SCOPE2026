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

The two cheap nearest-neighbor edges replace any use of the pivot's expensive bypass; a simple geodesic between pivots therefore stays between them. Regeneration at j follows by splitting edges into the left and right closed half-lines and the single bypass B_{j−1}. The pivot conditions factor over these three disjoint groups. A previous candidate i≤j−2 is tested on the left; i=j−1 is automatically ruled out by B_{j−1}>2a. Thus locating the first/next pivot at j does not further condition the right side beyond A_j,B_j<a. Successive distance/reward pairs are iid with the same law as the block to the right of a pivot at 0. The spaced trials give an exponential gap bound. For its block length P≤m=ceil(K log x), take light edges of weight at most x/m. If Q>x they cannot connect the ends; the two cheap edges at each end put both parity chains and the nearest-neighbor chain across the light component boundary. A cut with just one nearest-neighbor transition is a unit cut; any other cut contains at least (2 short,2 long) or (1 short,3 long) heavy edges. Ignoring the pivot conditioning costs at most a fixed factor; a union bound on these fixed-size witnesses in [0,m] is a polynomial in m times (x/m)^{−2−min(γ1,γ2)}, hence o(x^−2). If the component cut is a unit cut but one of its three edges has weight ≤(1−ε)x, use that edge as the sole crossing and nearest-neighbor paths on its two sides. Q>x forces a fourth edge above εx/m, again an o(x^−2) witness. Large blocks have exponentially small probability. For any threshold t>a the expected number of all-high cuts C_u between successive pivots under the pivot-at-0 law is t^−2/p, where p=P(0 pivot): expand the sum over u, shift u to 0 and partition by the last pivot at or before 0. The same identity with the constant mark gives E P=1/p. Every cut with all weights above x forces Q>x; pair overlaps have exponent >2 (adjacent cuts share just one long edge; others are independent), and the expected count discarded for P>m is o(x^−2). The lower and (1−ε)x upper bounds yield P(Q>x)~μ_P x^−2. Centering by vP leaves that tail and an exponentially bounded left tail; the truncated second moment is asymptotic to 2μ_P log x. This gives the iid normal normalization sqrt(m μ_P log m). The dependent renewal index is valid: on a deterministic window of ηn terms around n/μ_P, truncate at b=sqrt(n log n), center and use the maximal variance bound O(ηn log n)/b²; the probability of a removed term and the normalized truncation drift tend to zero. Then let η decrease to zero and use the renewal law. Both end residuals are tight by the stationary exponential gap bound and a nearest-neighbor route in a deterministic finite window with high probability. This yields the claimed variance one with no simulation assumption.

## originality

PASS

Credit Dey–Kim for regeneration and the exact block-tail coefficient with a common edge law. That result and the standard normal-domain-of-attraction argument already imply the isotropic Pareto critical point γ1=γ2=2/3, even though their stated CLT and stable regimes exclude equality. The supported distinct contribution is the variance-one limit along the unequal-exponent critical curve: the separate weighted separator argument is needed and no inspected common-law theorem implies it.

## value

PASS

Determines both the borderline scaling and its exact coefficient for a continuum of genuinely unequal edge-tail laws. The law involves the balance of one short and two long edges rather than a single representative exponent, and the unit-cut intensity cancels the artificial pivot density. It fills a distinct critical regime beyond merely obtaining a CLT from an iid finite-variance case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
