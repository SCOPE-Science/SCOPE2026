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

From actual RESULT.md at the verified frozen Git tree, the projection onto a_i^T e=0 maps any nonzero current error to alpha n_i. The next residual magnitudes are |alpha|s_ij; for p>0 the repeated row has exactly zero probability. Thus index transition P_ij=s_ij^p/d_i and stationary detailed balance d_i/(2Zp) are exact. Multipliers are c_ij, so the irreducible finite-chain additive strong law gives the a.s. exponent ell(p). Differentiating is covariance of log s with the strictly decreasing log sqrt(1-s²), proving strict monotonicity except constant angles. Pairwise edge weights concentrate at maximal s as p grows. At p=0 independently uniform sampling DOES allow repeats; stationarity produces 2/m² sum log c, while p->0+ produces 2/[m(m-1)] sum log c. Check m=2 periodicity allowed, nonzero error from generic e0, no orthogonal rows. Independent exact geometry and numerical exponent checks at 6 p values match, including factor 3/2 for m=3. Finite checks corroborate; full a.s. quantifier rests on Markov ergodic theorem.

## originality

PASS

Original residual-power algorithm, expected error bounds and the zero residual observation are known. However, the source results compare expected squared/Bregman error or per-step selection, whereas the assessed theorem computes the exact almost-sure planar logarithmic contraction via reversible pairwise Markov edge measure and proves the noncommuting long-time/p->0 limit. Search did not find an explicit stronger theorem; qualification remains for unindexed specialized Markov/Kaczmarz work.

## value

PASS

Exact a.s. Lyapunov exponent and strict all-power ordering solve a natural algorithm-selection problem for consistent planar Kaczmarz, identifying a genuine singular contrast between arbitrarily small positive residual power and iid uniform sampling. The m/(m-1) jump matters to long-run pathwise convergence, not just finite-step implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
