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

Run `python3 verify.py` with Python 3.9+ and no third-party packages. The script checks the exact rational three-node fixed-point equation, strict positive Perron sub-eigenvector inequalities on both endpoint linearizations, and complement symmetry for the Möbius declaration kernel. It uses `fractions.Fraction`; no tolerances or random sampling are involved.

The all-network uniqueness proof is analytical: odds-ratio domination, equality propagation on connected support, strict Jensen equality, and odd-cycle connectivity. Existence follows from Perron sub/supersolutions. The stochastic consequence additionally relies on the published almost-sure convergence-to-equilibria and avoidance-of-unstable-endpoints theorems of Tang et al. (arXiv:2308.09275, Theorems 3 and 4); those are cited rather than independently reproved. A computer check of one graph cannot establish the infinite graph family claim.

Independent scientific audit: not performed.
