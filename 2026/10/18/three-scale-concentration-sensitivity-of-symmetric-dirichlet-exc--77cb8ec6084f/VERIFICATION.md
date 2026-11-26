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

The frozen decimal with equality and ellipsis was inaccurate in its trailing digits: independent 60-digit quadrature of the defining gamma-score integral and bisection on [1,2] gave 1.3714020181783566482956564..., rather than 1.3714020181783595.... The complete corrected RESULT.md uses the correctly rounded approximation 1.3714020181784 and spells out dominated differentiation at small shape. The repaired claim was checked as follows. Centering the symmetric Dirichlet score gives L−EL, and exchangeability yields the beta-tail derivative. The beta score has derivative (1−mx)/(x(1−x)), negative endpoint limits and mean zero; the two score roots force a unique strict positive-to-negative crossing of its upper integral. Subtracting x^(alpha−1) from the incomplete-beta integrand leaves an integrable differentiable remainder even at alpha=0, with finite part log(t/(1−t)); multiplication by the inverse beta normalization gives the claimed small-shape covariance limit and traps its zero near 1/2. At large shape the limiting score has its sole maximum zero at 1/m; monotonicity and negativity at the two fixed bracketing points bring both score roots, hence the covariance root, to 1/m. At fixed alpha, the rescaled marginal and score converge locally to the stated gamma density and score. Trigamma cancellation bounds the beta-score second moment uniformly in dimension; Cauchy–Schwarz and tightness (EY_m=1) control the omitted upper tails. The analogous unimodal centered gamma score gives a unique strict crossing, and two fixed points flanking it trap the scaled beta zero. Integration by parts gives the E_1 expression, and the independent numerical quadrature verifies the repaired approximation but does not certify all digits or prove uniqueness. Only RESULT.md required correction; the unexecuted supplied script and verification notes already use finite tolerance and the same rounded output. No formal verification or expert attestation is claimed.

## originality

PASS

The repair does not change the mathematical scope. Fixed-mean beta concentration crossing and score differentiation are established ingredients, and catalogue results give analogous covariance thresholds for other statistics. The supported distinct claim is the quantitative three-scale sensitivity of the log-product covariance, in particular its small-shape amplitude and the fixed-shape gamma score profile and moving cutoff.

## value

PASS

The score covariance is a natural sensitivity for threshold occupancy in a symmetric Dirichlet model. A mere positive/negative crossing would overlap significantly with established concentration comparisons. The quantified sparse response and distinct fixed-shape gamma cutoff give usable scale-dependent predictions, notably distinguishing the high-dimensional cutoff from the mean-coordinate rule; the numerical repair leaves that contribution intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
