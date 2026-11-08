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

The exact labelled update depends only on outside-shore counts: q_i maps to n,0,or retained q_i according to whether sum_{j != i}q_j is above, below,or equal to n. The classification by 0/1/2/3 tied shores yields all fixed states 2+1_{2|n}binom(n,n/2)^3, 3(2^n-2) distinct primitive two-cycles, and entry within two updates, sharp for n>=3. Unique strict-between tied shore gives B_n=3 sum_a binom(n,a)^2 sum_{b=min(a,n-a)+1}^{max(a,n-a)-1} binom(n,b). Hypergeometric/binomial conditional CLT and Gaussian orthant signs give rare oscillation 6 pi^-3/2 atan(1/sqrt2) n^-1/2 and persistent reversal 1-(3/pi)atan(sqrt2). Independent weighted count-state census for n=1..8 confirmed exact B_n [0,12,36,660,3180,38172,218904,2266164] and all fixed/periodic counts. Finite census is corroboration, not an infinite proof.

## originality

PASS

Prior Goles–Olivos general period-at-most-two theorem is strictly weaker than sharp entry-time, full labelled orbit/basin census and asymptotic reversal probability. Benjamini et al analyze unimodular and random graphs with distinct hypotheses, not balanced complete tripartite exact formulas. Direct Resultary query located parity-automaton multipartite work, not strict-majority. No implication from those sources to the displayed constants; best-of-knowledge PASS with residual equivalent-treatment risk.

## value

PASS

Sharp, complete dynamics of a canonical dense multipartite network, with surprising nonzero probability (~0.08774) that eventual consensus opposes the initial global majority despite vanishing oscillatory basin. Exact labelled basin size, 2-update cutoff and asymptotic constants may be needed in majority-network studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
