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

# Verification of the finite collision/exclusion classification

The self-contained analytic verification is the five-step proof in RESULT.md. The decisive identity is \(L_{\mathrm{kill}}=L_{\mathrm{ex}}-\operatorname{diag}(\kappa)\), with \(\kappa(S)=\sum_{i<j\in S}(q_{ij}+q_{ji})\). Under positive rates, irreducibility and positivity of the Perron eigenfunction show that equality of the Doob transform and exclusion is equivalent to constancy of \(\kappa\). Replacing one element of each occupied subset proves uniform edge weights for \(k\le n-2\); complements of singleton vacancies prove weighted-degree regularity for \(k=n-1\). Marked competing hazards verify the independence of the exponential clock and the stated configuration-dependent collision-pair kernel.

## Actual finite checks

The packaged `verify.py` was executed under Python 3 with NumPy, SciPy, and SymPy. It returned `PASS 45 exact rank/degree and generator checks`, including exact rational incidence-matrix rank computations for \(3\le n\le8\), strictly positive nonuniform weighted-degree examples, independent construction of exclusion and killed generators, positive Perron eigenvectors, Doob transformations, and killed-semigroup factorization at time \(0.37\). The two equal-generator discrepancy maxima were approximately \(1.6\times10^{-14}\) and \(1.3\times10^{-13}\); the two unequal examples had discrepancies greater than \(0.25\). These are diagnostic tests, not an infinite proof.

Run: `python verify.py`. The program neither fetches data nor requires access to other files.

## Scientific and validation limits

The statements use finite, fully positive directed rates and the infinite-horizon conditioned-process limit. No claim is made for sparse graphs, infinitely many sites, or nonexplosive unbounded-rate models. The explicit conditioning limit is derived from finite-state Perron–Frobenius theory, not simulated. This document records a self-review; an independent audit has not been performed.
