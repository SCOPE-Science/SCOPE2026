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

# Verification and reproducibility

Execute `python verify_prism.py` from the directory containing that file. It uses Python 3 and standard-library modules only. The executable reconstructs the graph-neighbour criterion separately from the run-count formula and raises an exception on the first disagreement.

Observed results in this package: all \(14\) exhaustive palette/size cases passed, covering \(2{,}065{,}492\) named vertex assignments; every accepted assignment satisfied one of the two disjoint constructive classes. The independent Lucas/periodic formula agreed with the run formula on \(147\) integer cases. Coefficientwise rational generating-function checks passed for palette values \(0,1,\ldots,8\), in powers through \(30\) (the zero-palette test is algebraic only).

The critical unrestricted steps are the forced propagation from one disagreeing rung, the cycle boundary-count divisor \(r\), and the formal logarithm factorization. The finite checks do not replace those proofs or establish bibliographic novelty. The stated result is not a theorem about convergence of stochastic dynamics. Independent audit has not been performed.
