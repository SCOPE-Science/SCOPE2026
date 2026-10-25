---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The specified U columns are orthonormal and each row product-squared is 1/16; independent Bernoulli covariance ratios give every B_ab=(h+ell)/2. Orthogonal E+/E- reduction yields minus corrected eigenvalue beta-(h-ell)K_-/(2nu), K_-~Bin(2nu,1/2); exact failure is K_->=nu(kappa+1)/(kappa-1). It is absent for all samples exactly for 1<kappa<3, with singularity at equality. Raw PD is K_+>0,K_->0, yielding joint probability (1-4^-nu)q. Fusion minus eigenvalue scaled by ell is (kappa+1)+[theta-(kappa-1)]K_-/nu; extremal K_-=2nu gives iff theta>(kappa-3)/2. Frobenius variances (h^2+ell^2)/(2nu) and (h-ell)^2/(4nu), CLT threshold 2sqrt2/c and Cramer exponent follow from exact binomial. Independently enumerated all 16 one-sketch outcomes at h=7,l=1: 4 bad corrected, 3 bad corrected with good raw, 9 raw good.

## originality

PASS

Polydorides et al 2025 already give the optimal entrywise control variate and warn about loss of positive definiteness; no novelty claimed for that warning. The exact four-row all-sample coefficient contrast 3, binomial failures, fusion ridge, and sqrt(nu)-contrast transition are separately assessed, with substantial risk from unavailable full 2026 sketching preprint.

## value

PASS

The model is a transparent minimal leverage-balanced Galerkin example of a real algorithmic conflict: optimal entrywise variance reduction need not preserve SPD. Exact finite-sample tail and contrast-versus-sample phase transition expose when this happens and distinguish it from matrix inversion constraints; not a generic matrix counterexample alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
