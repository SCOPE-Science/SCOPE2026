---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: The proof for every n≥3 and nonnegative unimodal sequence uses a threshold t and centered-ball shifting: when i<j≤k and Mf(i)>t while f(j)≤t, a smaller ball centered at j reaches the same right endpoint and removes only nonpositive excess terms, so Mf(j)>t. Reflection proves the decreasing half; Mf(k)=f(k) because of the singleton ball. Therefore Var(Mf) telescopes to 2p−Mf(1)−Mf(n). The prefix/suffix balls at 1,n give the two deficit bounds. For zero-endpoint interior-peak data, Var(f)=2p and the nonnegative interior mass sums yield exact C=1−1/(2k)−1/(2(n−k+1)), with unique positive point-mass extremizer. Endpoint equality follows from monotone sequence prefix averages. Independent exact rational arithmetic sampled 1,147 unimodal sequences on n≤7 and confirmed the inequalities and peak preservation. Infinite claim is established by the ball argument, not by this finite test.

## originality

PASS

PASS (best of knowledge): The March 2026 González-Riquelme–Kovač–Madrid paper explicitly conjectures full-path sharp 1−1/n and presents small-n evidence; it does not prove all-n peak-preserving unimodal theorem. The published Resultary monotone-path result (full RESULT read) covers boundary peaks only, not interior nonmonotone humps, sharp k-dependent coefficient or stability remainder. Bilz–Weigt treats infinite line/lattice indicator functions under different geometry. There is real residual risk of an unindexed folklore peak-preservation observation, but the exact boundary-truncated all-n classification was not covered by inspected statements.

## value

PASS

PASS: The full finite-path variation conjecture is an identified mathematical problem. The theorem settles an infinite-size natural genuinely nonmonotone unimodal subclass, proves a structural shape-preservation lemma, gives a strictly better exact position-dependent factor, equality rigidity and quantitative remainder. This is an independently useful sharp subproblem, not a restatement of monotone endpoint estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
