---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Replacing |f| by f after positive translation does not change any interval maxima on nonnegative data; |.| cannot raise the input seminorm. Every interior-only interval always has ordinary arithmetic mean, endpoint-only intervals tend to their included endpoint sample, and full path tends to (a f1+b fn)/(a+b). Thus the limiting T0 has interior max{f1,fn,Uf(i)} and endpoint max{f1,mean}, max{fn,mean}. Extending one unweighted interval across one adjacent vertex bounds interior output edge differences by input-Lip/2. Left boundary edge is <=max{(n-1)/2,a(n-1)/(a+b)}, with reflected right bound max{(n-1)/2,b(n-1)/(a+b)}; the greater mass ratio is >=1/2, giving R=(n-1)*max(a,b)/(a+b). Opposite affine ramps attain each branch. For positive epsilon, interval average differs from endpoint-only limit by at most delta=(n-1)(n-2)epsilon/min(a,b) after Lip normalization; maximalization preserves sup error delta and edge differences change by <=2 delta. For fixed arbitrary positive w, every output >= strict whole-path average > input minimum, while <= max input; compact unit-Lip quotient sphere gives K<n-1, and concentrated endpoints approach n-1. Uniform extension gives K=1/2, endpoint spike attains. n=2 has no interior and zero epsilon error.

## originality

PASS

Inspected uncentered maximal Lipschitz results for Lebesgue intervals, discrete total variation for counting measure, and qualitative regularity with general measures. None of the relevant theorems implies endpoint-degenerate weighted finite-path Lipschitz sharp constants: both the norm and averaging measure differ. Specialist unindexed atomic regularity calculations remain possible.

## value

PASS

Sharp loss of the uniform-mass half-contraction under endpoint mass concentration is a natural regularity stability phenomenon for discrete maximal operators. The exact balance-dependent limiting amplification, quantitative epsilon control and unattained mass-uniform linear growth isolate a meaningful obstruction, not a random constant or pure unweighted restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
