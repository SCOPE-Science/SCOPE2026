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

## Analytic checks

- The Gibbs law gives exact magnetization weights \(\binom{N}{N(1+m)/2}e^{Nm^2/2}\).
- The entropy expansion through \(m^6\), together with the Stirling prefactor, yields the first scaled correction \(g(x)=x^2/2-x^6/30\).
- The quartic reference density has moment recurrence \(\mu_{r+4}=3(r+1)\mu_r\); in particular \(\mu_4=3\), \(\mu_6=9a\), and \(\mu_8=45\).
- The normalized moment correction is \(\operatorname{Cov}(X^2,g(X))=-a^2/5\).
- The exchangeability identity \(c_N=(N\mathbb E[m_N^2]-1)/(N-1)\) produces the coefficient \(-(1+a^2/5)\).

## Reproducible finite-sum check

Run `python3 verify_curie_weiss.py` with the Python standard library. Output from the packaged script:

```text
a=1.170828656608
target coefficient=-1.274167949
N,c_N,N*(c_N-a/sqrt(N))
100,0.105536410299,-1.154645536
300,0.063589855846,-1.202390448
1000,0.035790998876,-1.233854171
3000,0.020959446880,-1.250585980
10000,0.011582172012,-1.261145541
```

The values show convergence toward the claimed coefficient but do not prove the asymptotic expansion.

## Limits

The claim is for zero field and exactly critical inverse temperature in the specified Curie–Weiss normalization. The full text of two older higher-order critical-limit references was not inspected, so exhaustive novelty is not asserted. Independent audit and external validation remain unperformed.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
