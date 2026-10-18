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

# Verification and reproduction

Run `python verify.py` with standard Python 3. No third-party packages or datasets are required. The script evaluates heat-evolved edge differences on the original graphs by convergent Poisson uniformization of the random-walk matrix, which is numerically independent from the analytic reduced-mode formula.

Observed result: `PASS: 542 finite deterministic assertions (no external dependencies)`.

For each integer multiplicity between 2 and 12, seven nonnegative times were checked for the exact bridge \(\ell^1\)-norm, its half-tree sign pattern, zero total signed mass, and the pendant-edge upper bound. Further direct formula evaluations check spectral identities, mode positivity, elementary amplitude bounds and large-multiplicity scaling. The checks use absolute tolerances at most \(2\cdot10^{-11}\) for computed heat vectors and spectral formulas.

These finite computations do not certify asymptotics or infinitely many cases. Their proof is given in RESULT.md, including the invariant-subspace equations, mode coefficients, the uniform pendant-edge bound, and global maximizing-time localization. There is no independent audit or external mathematical certification.
