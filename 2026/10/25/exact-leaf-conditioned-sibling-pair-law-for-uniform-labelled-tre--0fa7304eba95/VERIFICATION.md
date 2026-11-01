---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Removing all ell original leaves yields an m=n-ell vertex labelled core tree; every core leaf requires >=1 attached original leaf, and every other core vertex may have >=0. Prufer degree enumeration gives the exact coefficient [u^(m-2) z^ell] (exp(u)H(z,y)-1)^m times the label factorials, with H=sum(z^a/a!)*y^choose(a,2). Expanding by the binomial theorem yields the alternating j^(m-2) expression. Differentiating at y=1 and using Stirling sums gives both factorial-moment ratios. A path with any two prescribed positive-leaf core endpoints realizes each allowed occupancy vector, proving complete support and balanced-minimum and (ell-1,1)-maximum bounds. The star case ell=n-1 and n=3 are explicit. Independently enumerated all 280,391 labelled Prufer trees of orders 3..8 and 45 exact conditional normalizations/moment checks; finite enumeration corroborates rather than proves all n.

## originality

PASS

Best-of-knowledge PASS. Isaev–Southwell–Zhukovskii (arXiv:1912.09838) studies asymptotic normality of local-pattern counts for uniform fully labelled trees, not this exact finite bivariate polynomial at fixed leaf count. Choi–Thompson–Wu (2020) gives cherry/pitchfork distribution in binary phylogenetic trees, where only leaves are labelled and all nonleaves have degree three, a distinct sample space and different cherry statistic when internal degrees exceed three. Choi–Kaur–Wu (2021) studies asymptotic PDA/YHK laws, also different. Resultary Cayley-tree endpoint-degree record is a different conditional statistic; no covering exact law identified.

## value

PASS

PASS: quantifies a genuinely natural local clustering feature conditional on the total number of leaves for every finite Cayley-tree size. Full conditional support, exact mean and variance and all coefficients provide usable finite-sample null distributions beyond degree counts. It is a complete natural classification, not an arbitrary tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
