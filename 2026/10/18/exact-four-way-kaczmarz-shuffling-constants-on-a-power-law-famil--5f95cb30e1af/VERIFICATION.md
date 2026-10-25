---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Pinned RESULT.md, verify_pair_shuffling.py inspected. Each 2D row pair has residual rank-one projectors whose Frobenius product squared is c_j^(2 w) with w equal to number of row-label switches. SS has 2t−1 switches; FF t; RR t plus t−1 independent Bernoulli(1/2) switches, yielding h_j^(t−1). For IID the pair count K~Binomial(2Nt,1/N), with conditional E[c^(2w)|K≥1]=h^(K−1), K=0 gives 2, giving a_j,b_j finite formula. Jensen and c²≤h, h≥c prove finite inequalities. Monotone Riemann-sum error O(1/N), Laplace v=tλ scaling and exponential domination produce Γ(β+1)/(2(k t)^β) with t^β/N→0. Independent exact rational binomial pair calculation checked five (N,t,c) settings. These finite checks do not imply all-β limits; analytic domination does.

## originality

PASS

2026 Ahle–Bulatov–De Sa–Ré v2 is closest full text, deriving Gaussian-design spectral-edge β=1/2 error constants (SS/FF/IID) and a qualitative shuffling gap conjecture; its quantitative √2 in that model is neither asserted universal nor refuted. The audited coherent 2-row full-rank family has exact finite formulas including RR for any β>0, and gives exponent-indexed ratio 2^β. Two-factor rearrangement work of Yun–Sra–Jadbabaie and broad Liu RR convergence bounds do not imply these four traces and powerlaw constants.

## value

PASS

The row-normalized fully consistent paired block family disentangles spectral-edge exponent from row-coherence geometry while giving exact finite constants for four widely used sampling policies; it quantifies a genuine dependence of the IID/SS advantage on β, an interpretable shuffling-performance benchmark rather than a textbook inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
