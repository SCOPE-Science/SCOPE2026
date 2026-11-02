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

# Verification

The proof defines the full rooted-tree leaf flag separately from the retained-edge component. Conditional updates of the joint counts \(C_n,L_n\) yield the exact first and second moments. Weighted martingale convergence and Yule processes establish almost-sure limits; the random-variance Gaussian limit uses the stable martingale CLT with its predictable bracket, conditional Lindeberg, and bounded-increment conditions verified in the proof.

A standalone Python 3 program, `root_cluster_leaf_checker.py`, was executed from the same collection of files. It verified 313 exact assertions using two different finite calculations: a rational joint-state Markov recursion and direct enumeration of original-tree parent choices and retained-edge marks. Its seeded \(n=6000\), \(p=0.7\), 1000-trial diagnostic yielded a realized-component-normalized residual variance approximately 0.11819 against the theoretical 0.11662; simulation is neither proof nor exact validation of an infinite limit.

Run `python root_cluster_leaf_checker.py` with standard Python 3 and no third-party packages. The exact checks cover only the explicitly enumerated finite graphs and tested rational parameters. No formal proof assistant, external certification, or independent audit has been carried out.
