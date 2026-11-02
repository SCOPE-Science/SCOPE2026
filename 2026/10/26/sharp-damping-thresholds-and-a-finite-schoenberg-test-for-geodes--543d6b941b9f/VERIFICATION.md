---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For a>0, omega>=0 on the geodesic unit S^3, the normalized Schoenberg coefficients are b_n=4(n+1)^2/pi*Re(beta_e/((z^2+n^2)(z^2+(n+2)^2))) where z=a-i*omega, beta_e=z(1-e*exp(-pi*z)), e=(-1)^n. Multiplication by the positive squared denominator gives exact sign quadratic P_e(X), X=(n+1)^2; minimum over each parity-square grid is at first square or the two squares bracketing the quadratic vertex, so at most four values plus leading/slope checks decide every degree. beta_e!=0 ensures eventually positive coefficients of both parities whenever admitted and hence strict PD. At integer omega=m, polynomial factors as positive scalar times (X+r-1)^2+4r(1-m^2) (r=a^2+m^2), strictly increasing X>=1; PSD iff a^2+4>=3m^2. At equality m>=2 only n=0 coefficient vanishes, and below it all initially below Xc negative. Independently symbolic-compared integer factor for m=0,...,5; source quadrature/checker formulas inspected. Float checks do not certify exact boundary comparisons.

## originality

PASS

Best-of-knowledge PASS: Gneiting’s general sphere coefficient criterion is a necessary framework but lacks this evaluated exponential-cosine two-parameter finite sign test, integer-frequency cone and exact negative-mode block; Jeong–Jun supports cos(theta) special case, explicitly acknowledged. Finite test follows from new explicit rational coefficient reduction, not merely numerical truncation.

## value

PASS

Exact computable global positive-definiteness test for a natural damped oscillatory geodesic covariance kernel on S^3, with sharp integer-frequency transition and strictness at boundaries. This resolves infinitely many harmonic sign inequalities using finite exact inequalities, a motivated covariance-model design fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
