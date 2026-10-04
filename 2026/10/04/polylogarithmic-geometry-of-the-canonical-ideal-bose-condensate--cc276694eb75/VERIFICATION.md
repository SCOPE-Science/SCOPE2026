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
The claim is analytic. The source right-tail exponent is rewritten with \(z=e^s\), the logarithmic Bose integral is evaluated term by term, and the source normalization \(b_c^\alpha=L\alpha\Gamma(\alpha)\zeta(\alpha)\) is used to obtain the closed form. Differentiating the unique saddle equation proves the first- and second-derivative identities. The endpoint and local regimes follow from \(z\downarrow0\) and the standard \(t\downarrow0\) expansions of \(\operatorname{Li}_\alpha(e^{-t})\), respectively.

The bundled `verify.py` uses high-precision arithmetic for \(r=2/5\) and representative \(\alpha=3/2,2,3\). It checks: (i) the fugacity equation; (ii) equality of the closed form with minus the source variational exponent at the saddle; (iii) the first- and second-derivative identities by finite differences; (iv) strict positivity of the second derivative; (v) approach to \(r\zeta(\alpha+1)/\zeta(\alpha)\) near the terminal threshold; and (vi) convergence of the three small-\(\eta\) asymptotic ratios to one.

The numerical replay is a consistency check, not an infinite proof. It does not verify the source theorem itself, does not establish the exact threshold probability, and does not establish a uniform moderate-deviation limit. Those are outside the claim.
