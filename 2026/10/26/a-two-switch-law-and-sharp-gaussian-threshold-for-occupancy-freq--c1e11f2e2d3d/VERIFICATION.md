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

For unequal loads the same-box product vanishes, giving the ordered-pair coefficient m(m-1) and the subtraction m²p_rp_s. The diagonal B is auxiliary only. On the feasible support the consecutive ratio is ((n-r-s)/(n-s))((m-1)/(m-2)), strictly decreasing for r>0 and constant above one for r=0. The zero forbidden tail preserves unimodality. An independent exact rational recalculation gave Q at s=6,7,11,12 respectively 14348907/17039360, 4782969/4259840, 4782969/3727360, 4782969/7454720 for (m,n,r)=(3,15,3), giving the stated two genuine reversals after deletion of s=3. For central r_n the consecutive ratio crosses one at n-(m-1)r_n, which is strictly inside the support for large n and gives standardized maximizing-load displacement x/rho, up to o(1), including an adjacent-integer tie. Thus the compact central local limit is used at the actual maximizer, not extrapolated to the tails. The Gaussian joint-to-marginal ratio completes to a_m exp(x²/2) times a Gaussian factor centered at x/rho. Here a_m<1 by the displayed polynomial inequality. Below the threshold the entire row is negative eventually; above it the maximum is positive and loads at suitable fixed displacements on each side give negatives. The maximizing loads are then distinct from r_n since x/rho!=x. No sign is claimed at equality.

## originality

PASS

The ordered-box covariance formula and Gaussian approximation are classical tools, not distinct claims. The supported distinction is the sign interval as the second frequency s varies at fixed m,n,r, and the sharp fixed-m central-load threshold obtained by locating the true global maximum. The strongest indexed sign-window results share the model and in one case the covariance itself, but vary a different coordinate or take a different limiting regime.

## value

PASS

The sign of dependence between exact occupancy frequencies is not settled by knowing that the loads of two specific boxes are negatively correlated. The result gives a complete finite restriction on where positive covariance can occur, proves that two reversals really occur, and identifies the exact centered-load threshold separating no positive pairs from positive pairs across the entire row. The global maximizer is essential to that distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
