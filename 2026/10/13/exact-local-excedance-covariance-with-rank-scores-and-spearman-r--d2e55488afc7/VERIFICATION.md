---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Uniform permutation Pi in S_n (n>=2). For E_i=1[Pi(i)>i], P(E_i)= (n-i)/n. Given E_i, Pi(i) mean (n+i+1)/2, a shift of i/2; others have mean shift -i/(2(n-1)) due to constant sum. For L_w=sum w_j Pi(j), Cov(E_i,L_w)= i(n-i)(nw_i-W)/(2n(n-1)). Taking weights j and D=2 sum j²-2 sum j Pi(j) yields local Cov(E_i,D)=i(n-i)(n+1-2i)/(2(n-1)); R=1-6D/[n(n²-1)] produces the given local Spearman covariance and conditional Spearman mean. Summing gives Cov(X,R)=-1/(2(n-1)); Eulerian excedance variance (n+1)/12 and random Spearman variance 1/(n-1) imply Corr(X,R)=-sqrt(3/(n²-1)). At n=2 the correlation -1 matches direct two-permutation analysis.

## originality

PASS

Primary Jiang study of Spearman-type metric dependencies does not study excedances; Hultman studies excedances and character-theoretic permutation statistics but not Spearman displacement. Their separate one-variable laws do not determine joint covariance. Resultary related papers on cycle/inversion and fixed-point/descent cross moments target different statistic pairs. Older Eulerian polynomial or excedance-set literature could hide this elementary mixed-moment law.

## value

PASS

The uniform identity is a reusable covariance functional for EVERY linear rank score, not merely a single Spearman number. It identifies a position-resolved exact sign change and explicit finite-n global correlation linking a canonical Eulerian statistic to a standard nonparametric rank metric. Motivated null calibration and joint-statistic interpretation beyond a table of small n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
