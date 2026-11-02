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

PASS. Beatty complementarity partitions positive integers into lower and upper Wythoff sets; the upper-set indicator equals floor(delta(m+1))-floor(delta m). As floor(k phi²)<n iff 1<=k<=floor(delta n), the ordered count is exactly a bounded-rotation sum H_{y_n}({k phi}), where y_n={n delta}. The indicator H_y is a union of at most two intervals, and its interval integral is F(y)/delta: plateau F=delta for y<=1-2delta, descending branch F=1-delta-y for 1-2delta<=y<=1-delta, rising branch F=y-1+delta. The continued-fraction denominators of phi are Fibonacci numbers; every length-q block differs by O(1) from a translated grid with error uniformly in the starting phase. Zeckendorf decomposition into O(log n) such blocks gives discrepancy O(log n) uniformly in phase, not just asymptotic equidistribution. K_n=floor(delta n)=delta n+O(1) then proves r(n)-nF({n delta})=O(log n). The pushforward of circle-uniform phase by continuous F has plateau mass 1-2delta at delta and two branches mapping one-to-one to (0,delta) giving density 2. Combining pointwise normalized error sum O(log² X/X) with bounded-variation discrepancy O(log X/X) gives the claimed W1 bound. Independent direct convolution of both Beatty sequences for all n<=5000 gave maximum observed absolute profile error <1.869; the frozen verify.py uses different exact arithmetic and was directly read. Finite experiments do not prove the all-n discrepancy or convergence.

## originality

PASS

PASS, qualified: Shallit already has an exact Fibonacci-linear representation of the identical sequence, so novelty is solely the explicit phase profile, limit mixture, and W1 quantitative rate, not a new definition or ability to compute r(n).

## value

PASS

PASS. An explicit global linear-scale profile and an effective limiting law with a genuine point mass answer a natural quantitative question for a classical Beatty representation function. The distinct atomic and continuous components and explicit W1 rate are meaningful statistics not contained in an OEIS value list or exceptional small-count classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
