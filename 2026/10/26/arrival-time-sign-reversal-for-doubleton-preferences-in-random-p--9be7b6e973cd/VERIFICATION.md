---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Pollak rotation on N=n+1 circular sites bijects shift-orbit representatives to uniform classical parking functions and preserves lucky indicators and preference-count profiles. Conditioning on preceding preferences, exactly N−i+1 free labels are absent from all earlier preference draws. An independent insertion of draw i changes frequency-r count by binomial difference h_m(r)=b_m(r−1)−b_m(r); conditional covariance gives (N−i+1)/N [h_{n−i}(r)−h_{n−1}(r)]. The first lucky indicator has zero covariance. Binomial second differences show h_m(1) strictly decreases; for r>=3 it increases over a nontrivial range; and h_m(2) increases then decreases, giving a unique positive-to-negative arrival change exactly for n>=5. Poisson limit yields the unique critical lambda in (0,2−sqrt(2)), alpha*=1−lambda≈0.714556. Independently enumerated every classical parking function for n=2,...,6 with exact rational covariance, checking the full formula. Exact Fraction sign computations checked n=2,3,4,5,6,7,10,25,50,100,200 including at most one zero; finite checks do not prove all n.

## originality

PASS

Best-of-knowledge: the circular parking law, lucky-count generating functions, and preference species occupancy distribution are prior work. The materially inspected source papers treat their marginal distributions and prescribed lucky subsets, not the mixed arrival-specific covariance of one lucky indicator with each multiplicity class. The conditional insertion formula and doubleton sign reversal are substantive additions and not entailed merely by multiplying marginal generating functions.

## value

PASS

The exact cross-covariance between arrival luckiness and the occupancy multiplicity spectrum is a natural joint parking-function statistic not determined by either well-known marginal. A unique doubleton sign reversal and critical macroscopic arrival fraction give substantive structural information useful for probabilistic parking and linear-probing analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
