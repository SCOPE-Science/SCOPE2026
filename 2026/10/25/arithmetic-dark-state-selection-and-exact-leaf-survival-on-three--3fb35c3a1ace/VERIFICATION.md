---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility of the spider absorption formula

Execute `python verify_spider.py` in an environment with the dependencies in `requirements.txt`. The program builds all adjacency matrices from the hub-and-path definition, separately computes the exact gcd expression, and compares it with the full Hermitian eigenspace projection onto trap-invisible modes.

Observed checks: 492 full-adjacency comparisons for triples of positive arm lengths at most eight and total length at most twenty (maximum survival difference approximately \(1.443\times10^{-15}\)); 24 integer-arithmetic exact Krylov-rank comparisons; and 21 checks of non-Hermitian eigenvalue locations and nondecaying multiplicities at absorption strengths \(0.25\), \(1\), and \(3\). All passed. The example outputs included survival \(1/3\) for lengths \((1,2,3)\), zero first-leaf survival with five dark modes for \((4,5,11)\), and survival \(17/39\) for \((3,5,7)\).

The analytical proof requires the exact Dirichlet spectrum of an open path, the hub cancellation condition, the finite-dimensional contraction argument, and the identity \(\sum_{s=1}^{g-1}\sin^2(\pi s/g)=g/2\) for \(g\ge2\). None of the finite computations certifies these for all lengths. The norm limit is taken for fixed finite graph and fixed strictly positive absorption rate before varying graph size or absorption rate. Verification does not establish originality; relevant historical-priority limitations are reported separately.
