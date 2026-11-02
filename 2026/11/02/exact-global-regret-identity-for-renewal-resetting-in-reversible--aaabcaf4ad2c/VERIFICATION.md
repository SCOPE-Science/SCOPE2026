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

The derivation in `RESULT.md` is analytic. In order, reconstruct the renewal mean identity; verify that the stopped-time numerator solves the mixed-boundary elliptic problem; derive the symmetric Green representation; symmetrize the two identical Green integrals; and check the equality and logarithmic lower bound. This chain does not rely on numerical computation or a finite-state approximation.

Run the included standalone artifact with `python CHECK.py` in an environment with Python 3, SymPy, NumPy and SciPy. Its replay passed 479 deterministic assertions, including exactly rational reversible birth-death Green matrices and regret equalities, constant-drift reflecting interval quadrature, and the symbolic Poisson half-line comparison. The checker does not certify every allowed potential or clock; the infinite-domain/all-protocol claim is the analytic statement in `RESULT.md`.

The numerical quadrature benchmark in the result uses the 801-node grid and parameters documented there. The source public date is based on arXiv:2410.01941v1, not the later journal or revised manuscript date. The strongest accessible primary overlap was directly compared by conclusion: functional extremality versus global positive regret. A complete independent scientific and priority audit is not part of this verification.
