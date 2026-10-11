---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

With standardized held-out and training fold means \(A_j,B_j\), the log e-value is \(A_jB_j/\sqrt{K-1}-B_j^2/[2(K-1)]\) with independent standard Gaussians. Conditioning on \(B_j\) gives an exponential-square integral with coefficient \(q(q-1)/[2(K-1)]\), hence \(\mathbb E E_j^q=(1-q(q-1)/(K-1))^{-1/2}\) exactly when \(q(q-1)<K-1\), with divergence at and beyond the boundary. For \(q\ge1\), convexity gives finiteness of the average from component finiteness, while positivity of one summand gives the converse; \(0\le q\le1\) follows from \(x^q\le1+x\). The integer thresholds and two-way unbalanced formula follow by solving the same quadratic condition in the fold-size ratio. The log-moment claim follows because each component log is a Gaussian quadratic polynomial and \(\log\bar E_K\) is trapped between component log extrema.

## originality

PASS

Tse and Davison already study the same Gaussian cross-fit and \(K\)-fold averaged likelihood ratios and derive their variance, so the variance subclaim is prior context rather than novel content. Their complete main article explicitly says the \(K\)-fold variance derivation is in supporting information. The 2023 discussion likewise emphasizes the known infinite cross-fit variance and suggests studying logarithms. Neither inspected main article nor current searches state the all-real-order moment spectrum, the exact integer-\(p\) threshold \(K\ge p(p-1)+2\), or the unbalanced two-way critical exponent and balanced golden-ratio optimum. Those claims follow from a fresh Gaussian quadratic-form calculation rather than from the published variance statement.

## value

PASS

Moment robustness is directly motivated by the published discovery of infinite variance for cross-fit universal likelihood ratios. The exact spectrum explains how many folds are needed for each moment, identifies the sharp variance boundary, and shows that balanced two-way splitting uniquely maximizes integrability. These are natural exact diagnostics for a current inference construction, not arbitrary Gaussian moment calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
