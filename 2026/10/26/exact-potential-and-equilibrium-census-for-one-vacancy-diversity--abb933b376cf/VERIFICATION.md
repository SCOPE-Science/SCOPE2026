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

# Reproducible checks and limits

Run `python3 check_potential.py` from the directory containing this file and that script. The checker requires Python 3 standard-library modules only. It iterates over each position of the sole vacancy on \(K_{a,b}\), every coloring for \(2\le a,b\le4\) and two or three possible types, and every resulting individual legal jump. It recomputes both old and new utilities using neighbor lists independently of the potential's occupancy-count expression, and uses exact rational arithmetic to verify that \(\Psi_{\mathrm{after}}-\Psi_{\mathrm{before}}=u_{\mathrm{after}}-u_{\mathrm{before}}\). It separately enumerates all two-type equilibria and compares each coefficient of the closed generating polynomial.

The checker returned `PASS` for \(35{,}682\) profiles, \(225{,}302\) legal jumps and 18 parameter combinations, including \(88\) stable profiles of \(K_{3,4}\). These are **finite tests**. The all-size and all-type proof is algebraic and supplied under `## Proof` in RESULT.md. The code does not certify anything about arbitrary bipartite graphs, two or more vacancies, convergence rates tighter than the derived coarse polynomial bound, or the originality of the statement. Independent audit or validation has not been performed.
