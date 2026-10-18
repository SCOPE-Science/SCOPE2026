---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For uniform π∈S_n, each bounded rectangle in either of two opposite rescaled corners has n·area+o(n) eligible cells and only O(√n) cells in any fixed row or column. At fixed factorial order m, incompatible repeated rows/columns contribute O_m(n^(m−1/2)) of O(n^m) choices; compatible pinned cells have exact probability 1/(n)_m. Thus joint count factorial moments converge to independent unit PPPs. Under any m fixed compatible pins, the inversion statistic differs from inversions of the remaining uniform relative permutation by at most mn, while the means differ O(mn); after n^(3/2) normalization the shift is uniformly o(1). Independent Lehmer digits produce the CLT with Var limit 1/36, and mixed factorial/characteristic moments imply the corner processes and Gaussian are jointly independent. The identity relating max |π(i)−i| to minimum corner coordinate sum then yields survival exp(−t²), independent of G. Independent exact enumeration over n=2,…,7 verifies inversion means/variances and coordinate identity in finite cases; no claim that this proves PPP convergence.

## originality

PASS

Existing finite Chebyshev-distance permanent formula determines the marginal maximum displacement distribution but not spatial Poisson fields coupled to inversion fluctuations. The inversion/major-index joint Gaussian result concerns a different global statistic; general additive permutation CLTs alone do not establish sparse corner Poisson processes or their independence from nonlinear inversion counts. The three-way joint limit requires a uniform finite-pinning stability argument. Broad uninspected extreme-process literature might imply the claim, so priority is explicitly best of knowledge.

## value

PASS

Worst-case permutation displacement is a natural extremal ranking-error statistic and inversion count is the canonical aggregate Kendall-disorder statistic. Joint asymptotic independence gives simultaneous calibration on incompatible extreme/central scales and preserves both full two-corner spatial point processes, a strictly richer result than the scalar maximum law. Uniform finite-pinning stability provides a reusable proof mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
