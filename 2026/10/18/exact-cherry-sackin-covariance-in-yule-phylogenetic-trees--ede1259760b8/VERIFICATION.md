---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Under equal-rate uniform leaf splitting, designated root subtree size K is uniform on {1,...,n-1}; given K, independent Yule subtrees satisfy C_n=C_K+C_(n-K), S_n=S_K+S_(n-K)+n for n>=3, with C1=0,C2=1,S1=0,S2=2. Recurrences yield c_n=n/3 (n>=3) and s_n=2n(H_n-1). Setting delta_j=c_j-j/3 gives delta_1=-1/3, delta_2=+1/3, delta_j=0 for j>=3. Total covariance v_n=2/(n-1)sum_{j<n}v_j+F_n with F_n=2/[3(n-1)][s2+s_(n-2)-s1-s_(n-1)]=4(1-H_(n-2))/[3(n-1)] using s_(m+1)-s_m=2H_m; substitution and induction cancel harmonic terms exactly to v_n=-n/9+2/[3(n-1)]. This gives v3=0 and strict negativity n>=4, no all-n claim for n2. Independent rational root-moment recursion through n=50 reproduced n4=-2/9, n5=-7/18, n8=-50/63, n20=-374/171, n50=-2444/441. Total cherry variance recurrence plus n4=2/9,n5=2/9 gives w_n=2n/45 for n>=5. Thus slope v_n/w_n=-5/2+15/[n(n-1)]; substituting published Sackin variance 7n²−4n²H_n^(2)−2nH_n−n yields rho~−sqrt(45/[2(7−2pi²/3)])/9 /sqrt(n), approx −0.812994847/sqrt(n). Source checker separately enumerates leaf-splitting histories to n9, but these finite checks are not the proof of induction.

## originality

PASS

Best-of-knowledge PASS for evaluated cherry–Sackin finite covariance, negative sign and corresponding regression/correlation, not for standard Yule root splits, cherry marginals, or Sackin variance. Direct examination of Wu–Choi 2016 and Choi–Thompson–Wu 2020 accepted full PDFs shows their joint statistics are cherries with pitchforks (two- and three-leaf clades), not with Sackin depth; Cardona–Mir–Rosselló 2013 computes Sackin variance and correlations/covariance with other balance indices including total cophenetic, not cherry count (capital C there can mean Colless). Their general recursive shape-index method is known and could be specialized, but does not algebraically state or supply the evaluated cross-moment without a mixed recursion and harmonic cancellation. Current exact numerical and empirical tree metric papers are not equivalent finite formulas.

## value

PASS

Cherries are local clade structure while Sackin is global root-to-leaf imbalance. Exact dependence under the canonical Yule null model is a natural question for calibrating joint tree-shape statistics, not an arbitrary finite parameter slice. The covariance is negative linear in n, yet normalized Pearson correlation vanishes as n^-1/2 with explicit constant; the exact finite-size regression slope quantifies conditional predictive association. No claim of novel generation law or joint CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
