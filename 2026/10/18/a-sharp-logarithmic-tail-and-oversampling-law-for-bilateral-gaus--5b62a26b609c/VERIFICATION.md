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

For the fixed Gaussian coupling, the Gram determinant gives sigma_1 sigma_2 = epsilon sqrt(det(G^T G) det(H^T H)), while sigma_1^2 tends to the squared norm of the leading outer product. Each orthogonal residual norm has a conditional chi law independent of the first column norm, and the two sketches are independent. Gamma integration gives the stated ratio density and the moments, with divergence at p=d as well as beyond. For unequal indices, x^s P(T_s>x/T_t | T_t) is dominated by a constant times T_t^s. In the equal-index case the conditional integral over 1<=u<=x/K contains u^d f_d(u)~d c_d/u; the remaining ranges contribute O_K(x^-d), and the relative tail approximation error on the middle range vanishes as K increases. This verifies the logarithmic coefficient. Independent special-case arithmetic gives c_2=1/2, M_3(2)=2, coefficients 1/2 and 1 for (2,2) and (2,3), and second moment 4 for (3,3). Fatou gives the asserted moment blowup along every sequence of positive gaps tending to zero; at a fixed gap the ratio is bounded.

## originality

PASS

Best-of-knowledge pass for the exact bilateral observed-gap limit and its sharp tails at fixed real sketch dimensions. Neither the closest same-day one-sided angle result nor the inspected two-sided sketching and matrix-product statements covers this statistic and limit. The F distribution, gamma moments and product-tail methods are not new.

## value

PASS

Rank-revealing bilateral sketches motivate the observed gap, and this minimal benchmark identifies separate roles for the two sketch dimensions: adding a row to one side can remove the balanced logarithm without making the limiting second moment finite; both sides must clear the cutoff. The sharp constants quantify the difference, beyond bounds on singular-value order. This is not a practical optimal oversampling rule for arbitrary spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
