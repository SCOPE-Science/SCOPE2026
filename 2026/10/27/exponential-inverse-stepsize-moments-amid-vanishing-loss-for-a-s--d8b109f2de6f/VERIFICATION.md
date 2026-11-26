---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The population mean and second moment of the component gradient are x and 1+x², so the pre-sample oracle step gives the maps T±(x)=x(1±x)/(1+x²). For x∈(0,1), T₋(x) is positive and below x while x<T₊(x)<1, using 1−T₊(x)=(1−x)/(1+x²). The conditional second moment is x²/(1+x²). Thus x_n² is a bounded nonnegative supermartingale and Jensen gives 1/E[x_(n+1)²]≥1/E[x_n²]+1. The expected objective gap is half the second moment; dominated convergence then identifies the almost-sure limit as zero. On n−1 plus draws then one minus, with probability 2^(−n), the plus orbit y_k has deficits δ_k=1−y_k with δ_(k+1)=δ_k/(1+y_k²)≤δ_k/(1+x_0²). Hence Σδ_k<∞, and the factors 2/(1+y_k²) differ from one by at most 2δ_k. This proves 2^kδ_k→D(x_0)∈(0,∞). The last minus map gives 2^n x_n=2^n y_(n−1)δ_(n−1)/(1+y_(n−1)²)→D on those varying words. Restricting E[(1+x_n^(−2))^(p/2)] to the word proves exactly the stated scaled liminf for every fixed p>1. This is a lower moment bound, not an upper rate or a pathwise assertion about the rare words. The supplied finite rational tests are corroborative; the infinite claim is analytic.

## originality

PASS

The ideal rule and an O(1/n) expected objective bound are prior work; the supported distinct claim is the exponential inverse-moment lower bound coexisting with convergence in the specific true-moment oracle recursion. The closest inspected primary and indexed comparisons use different random variables or dynamics and do not imply that lower bound.

## value

PASS

The example gives a motivated counterexample to treating expected-loss convergence as evidence of stable inverse ideal gains. It works without moment-estimation noise in two strongly convex quadratic samples and gives a quantitative rare-history mechanism and a range of divergent moments. It does not claim practical safeguarded SGD instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
