# Independent Audit — 2026/09/18/rare-bernoulli-tv-sign-cancellation--adcb7befe3ff

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `2fc29d3cd8c19652d5ff9f9458402fd041bbca2b`
- Disposition: **PASSED**

## Correctness

**PASS** — The rare-event expansion is correct. Decomposing total variation by Hamming weight, the zero slice differs from |A-B| by at most (A^2+B^2)/2, the singleton slice differs from sum_i|p_i-q_i| by at most A^2+B^2, and all weights at least two contribute at most (A^2+B^2)/2; division by two yields the displayed error bound. For Smirnov's proxy, singleton disagreement events contribute at least L-Lambda^2 and at most L, while two-or-more disagreement events have probability at most Lambda^2/2, proving the proxy expansion. In the signed family, lambda_i and a_i are exactly sign-blind while |A-B| retains the sign imbalance, so the asymptotic factor-two separation and the sqrt(2)/1/3 estimator lower bounds follow. A fresh exhaustive numerical stress test on 500 random product pairs of dimension up to seven found no violation of the finite inequality.

## Originality

**PASS** — Smirnov introduces the sign-blind (lambda_i,a_i) representation and a constant-factor proxy, while Avital--Kontorovich--Salafatinos analyze tiny/small Bernoulli parameters up to constants. The audited statement adds an additive second-order expansion with the explicit signed intensity term |sum_i(p_i-q_i)| and shows exact information loss of the full Smirnov proxy data. Searches for that signed first-order formula and factor-two same-proxy obstruction did not locate a prior result. The novelty is thus in the sharp rare-event decomposition and proxy-information statement, not in standard Poisson/rare-event heuristics.

## Scientific value

**PASS** — The theorem explains a concrete limitation of a newly proposed computable proxy: even the full proxy input and induced G-law can erase a first-order signed statistic that changes true TV by a factor two. The additive expansion is also stronger than a constant-factor comparison in the rare-event regime and supplies explicit lower limits on any estimator using only the sign-blind data. These conclusions are directly relevant to approximation guarantees for heterogeneous Bernoulli products.

## Sources

- TV between Bernoulli products, up to constants (Gleb Smirnov): https://arxiv.org/abs/2609.19222 — Introduces the recent efficiently computable proxy framework for Bernoulli-product TV.
- TV over Bernoulli products: the small parameter regime (Ariel Avital; Aryeh Kontorovich; George Salafatinos): https://arxiv.org/abs/2602.21828 — Gives constant-factor behavior in tiny and small parameter regimes.
- On the tensorization of the variational distance (Aryeh Kontorovich): https://doi.org/10.1214/25-ECP680 — Prior product-TV information-loss context from marginal TV data.

## Limitations

- The additive approximation is first-order only when A+B is small and can be dominated by its O((A+B)^2) remainder if L is exceptionally tiny.
- The factor-two obstruction applies to estimators restricted to the sign-blind (lambda_i,a_i) data, not algorithms that use the full p and q vectors.
- The record does not prove that 1/2 is a universal lower comparison constant for Smirnov's proxy.

## Independent check

```json
{
  "implementation": "fresh exact state enumeration for Bernoulli products",
  "random_cases": 500,
  "max_dimension": 7,
  "finite_bound_violations": 0,
  "all_ok": true
}
```

The assignment snapshot and source-tree-check commit were compared read-only and no file under this record changed. The dated independent-audit files were verified absent and the current `VERIFICATION.md` blob guard was checked. Open-access/preprint sources were checked first; no decisive comparison required Oxford Download. GitHub was not modified.
