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
# Reproducibility and verification

Run `python3 verify.py` using the standard Python library. The script uses `fractions.Fraction` throughout and checks 8,528 rational assertions on exact polynomial integrations, orthogonal and Lagrange quadratic Gram matrices, vertex and interior reproducing kernels, nonuniform rational edge masses, and finite hypercube Hamming-shell bounds. It reconstructs the local nodal/bubble basis and verifies exact inverses before comparing evaluations. The all-finite-graph ceiling, strictness, infinite hypercube limit, and universal positivity excursion are proven in `RESULT.md`; a finite checker does not establish those quantified statements on its own.

The original proof does not require a numerical tolerance, probabilistic estimate, or inaccessible external artifact. No expert or independent audit is represented as performed.
