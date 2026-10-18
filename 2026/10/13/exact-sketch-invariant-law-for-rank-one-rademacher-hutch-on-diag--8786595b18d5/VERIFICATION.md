---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For every positive diagonal A=diag(lambda_i), one Rademacher sketch column s gives q=D_s p with p=lambda/sqrt(S2). Because D_s commutes with diagonal A, its deflated residual is D_s(I-ppT)A(I-ppT)D_s, and an independent Rademacher probe remains iid after multiplying by fixed D_s. Thus the entire conditional law is sketch-invariant, not merely moments. Rank-one expansion gives T_hat = sum(lambda)+mu - (2/(ell*S2))*sum(U_a V_a) + S3/(ell*S2^2)*sum(U_a^2). Rademacher quadratic variance 4 sum_i<j B_ij^2 divided by ell yields the exact positive expression; choosing max lambda_i shows nonvanishing for all n>=2 positive spectra. Flat lambda I specializes to lambda(n+1) - lambda/(n ell) sum W_a^2, variance 2lambda^2(n-1)/(n ell), and n2 ell1 gives lambda or 3lambda equally. For fixed ell independent sign CLT plus continuous mapping gives centered chi-square limit. Limits: Rademacher diagonal coordinates only, one sketch column, exact products.

## originality

PASS

Prior-work comparisons credit foundational techniques and potential broader theorems. No actually inspected source has a theorem that entails the complete claimed new invariant/formula at the assigned parameters; real full-text gaps are identified as residual risk. The exact mathematical implication comparison is given in four named checks.

## value

PASS

This is an exact full output law, not another generic trace estimator error bound. One-sign-column Hutch++ introduces positive error on diagonal matrices where classic Rademacher Hutchinson is deterministic, and the sketch-sign invariance and chi-square limit quantify precisely the low-budget regime. It motivates probe allocation and inference even though overall recommended Hutch++ high-query complexity and prior warnings about deflation are not challenged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
